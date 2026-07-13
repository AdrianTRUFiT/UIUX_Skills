"""Evidence Intake Workstation — FastAPI application.

Serves the API and, when built, the React frontend. Runs locally for a
single operator. Evidence lives under the data root on the local
filesystem; the registry and review state live in SQLite. Live mode never
seeds or fabricates records.
"""
from __future__ import annotations

import csv
import datetime as dt
import io
import json
import urllib.parse
from pathlib import Path

from fastapi import FastAPI, Form, HTTPException, Query, UploadFile
from fastapi.responses import FileResponse, JSONResponse, Response
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel

from . import config, db, importer, preservation, search as search_mod

def _model_data(model) -> dict:
    # pydantic v2 (model_dump) and v1 (dict) are both supported.
    return model.model_dump() if hasattr(model, "model_dump") else model.dict()


CLASSIFIABLE_FIELDS = (
    "repository", "doc_type", "source_collection", "detected_people",
    "detected_date", "topic", "review_status", "operator_notes",
)
FTS_FIELDS = {"detected_people", "topic", "operator_notes"}


def _now() -> str:
    return dt.datetime.now(dt.timezone.utc).isoformat(timespec="seconds")


def create_app() -> FastAPI:
    config.ensure_dirs()
    app = FastAPI(title=config.APP_NAME, version=config.VERSION)
    conn = db.connect()
    db.init_db(conn)
    app.state.conn = conn

    @app.on_event("shutdown")
    def _close() -> None:
        app.state.conn.close()

    # ------------------------------------------------------------- status
    @app.get("/api/status")
    def status() -> dict:
        c = app.state.conn
        counts = {
            "proof_objects": c.execute("SELECT COUNT(*) n FROM proof_objects").fetchone()["n"],
            "pending_review": c.execute(
                "SELECT COUNT(*) n FROM proof_objects WHERE review_status = ?",
                (config.REVIEW_PENDING,),
            ).fetchone()["n"],
            "duplicates": c.execute("SELECT COUNT(*) n FROM duplicate_occurrences").fetchone()["n"],
            "errors": c.execute("SELECT COUNT(*) n FROM processing_errors").fetchone()["n"],
        }
        return {
            "app": config.APP_NAME,
            "version": config.VERSION,
            "mode": config.MODE,
            "data_root": str(config.data_root()),
            "repositories": config.REPOSITORIES,
            "counts": counts,
        }

    # ------------------------------------------------------------- import
    @app.post("/api/import")
    async def do_import(
        files: list[UploadFile],
        repository: str = Form("Unassigned"),
        source_collection: str = Form(""),
        source_label: str = Form(""),
    ) -> dict:
        if repository not in config.REPOSITORIES:
            raise HTTPException(400, f"unknown repository '{repository}'")
        items = []
        for f in files:
            data = await f.read()
            name = f.filename or "unnamed"
            items.append(importer.ImportItem(name, data, source_path=name))
        batch = importer.run_import(
            app.state.conn, items, repository,
            source_collection or None, source_label or None,
        )
        return batch.manifest()

    @app.get("/api/batches/{batch_id}/manifest")
    def batch_manifest(batch_id: int) -> dict:
        row = app.state.conn.execute(
            "SELECT manifest_json FROM import_batches WHERE id = ?", (batch_id,)
        ).fetchone()
        if not row or not row["manifest_json"]:
            raise HTTPException(404, "batch not found")
        return json.loads(row["manifest_json"])

    # ------------------------------------------------------ proof objects
    @app.get("/api/proof-objects")
    def list_proof_objects(
        repository: str | None = None,
        review_status: str | None = None,
        limit: int = Query(200, le=1000),
    ) -> list[dict]:
        where, params = [], []
        if repository:
            where.append("repository = ?")
            params.append(repository)
        if review_status:
            where.append("review_status = ?")
            params.append(review_status)
        sql = f"SELECT {search_mod.PO_COLUMNS} FROM proof_objects p"
        if where:
            sql += " WHERE " + " AND ".join(where)
        sql += " ORDER BY imported_at DESC, po_id DESC LIMIT ?"
        params.append(limit)
        return [dict(r) for r in app.state.conn.execute(sql, params).fetchall()]

    @app.get("/api/proof-objects/{po_id}")
    def get_proof_object(po_id: str) -> dict:
        row = app.state.conn.execute(
            f"SELECT {search_mod.PO_COLUMNS}, sha256, metadata_json FROM proof_objects p WHERE po_id = ?",
            (po_id,),
        ).fetchone()
        if not row:
            raise HTTPException(404, "proof object not found")
        item = dict(row)
        item["duplicate_occurrences"] = [
            dict(r) for r in app.state.conn.execute(
                "SELECT original_filename, source_path, occurred_at FROM duplicate_occurrences WHERE po_id = ?",
                (po_id,),
            ).fetchall()
        ]
        item["classification_history"] = [
            dict(r) for r in app.state.conn.execute(
                "SELECT field, old_value, new_value, changed_at FROM classification_history"
                " WHERE po_id = ? ORDER BY changed_at",
                (po_id,),
            ).fetchall()
        ]
        return item

    class Classification(BaseModel):
        repository: str | None = None
        doc_type: str | None = None
        source_collection: str | None = None
        detected_people: str | None = None
        detected_date: str | None = None
        topic: str | None = None
        review_status: str | None = None
        operator_notes: str | None = None

    def _apply_classification(po_id: str, fields: dict) -> None:
        c = app.state.conn
        row = c.execute(
            "SELECT * FROM proof_objects WHERE po_id = ?", (po_id,)
        ).fetchone()
        if not row:
            raise HTTPException(404, f"proof object {po_id} not found")
        touched_fts = False
        for field, value in fields.items():
            if field not in CLASSIFIABLE_FIELDS or value is None:
                continue
            if field == "repository" and value not in config.REPOSITORIES:
                raise HTTPException(400, f"unknown repository '{value}'")
            if field == "review_status" and value not in (
                config.REVIEW_PENDING, config.REVIEW_REVIEWED,
            ):
                raise HTTPException(400, f"unknown review status '{value}'")
            old = row[field]
            if old == value:
                continue
            c.execute(
                f"UPDATE proof_objects SET {field} = ? WHERE po_id = ?", (value, po_id)
            )
            c.execute(
                "INSERT INTO classification_history (po_id, field, old_value, new_value, changed_at)"
                " VALUES (?, ?, ?, ?, ?)",
                (po_id, field, old, value, _now()),
            )
            if field in FTS_FIELDS:
                touched_fts = True
        if touched_fts:
            db.fts_upsert(c, po_id)

    @app.patch("/api/proof-objects/{po_id}")
    def classify(po_id: str, body: Classification) -> dict:
        _apply_classification(po_id, _model_data(body))
        app.state.conn.commit()
        return get_proof_object(po_id)

    class BulkClassification(BaseModel):
        po_ids: list[str]
        fields: Classification

    @app.post("/api/proof-objects/bulk-classify")
    def bulk_classify(body: BulkClassification) -> dict:
        for po_id in body.po_ids:
            _apply_classification(po_id, _model_data(body.fields))
        app.state.conn.commit()
        return {"updated": len(body.po_ids)}

    # --------------------------------------------------- original sources
    @app.get("/api/proof-objects/{po_id}/original")
    def open_original(po_id: str):
        row = app.state.conn.execute(
            "SELECT preserved_path, original_filename, mime_type FROM proof_objects WHERE po_id = ?",
            (po_id,),
        ).fetchone()
        if not row:
            raise HTTPException(404, "proof object not found")
        try:
            path = preservation.open_preserved(row["preserved_path"])
        except FileNotFoundError:
            raise HTTPException(410, "preserved original missing from data root")
        quoted = urllib.parse.quote(row["original_filename"])
        return FileResponse(
            path,
            media_type=row["mime_type"] or "application/octet-stream",
            headers={"Content-Disposition": f"inline; filename*=UTF-8''{quoted}"},
        )

    # -------------------------------------------------------------- search
    @app.get("/api/search")
    def do_search(
        q: str | None = None,
        person: str | None = None,
        date_from: str | None = None,
        date_to: str | None = None,
        filename: str | None = None,
        repository: str | None = None,
        file_ext: str | None = None,
        limit: int = Query(100, le=500),
    ) -> list[dict]:
        return search_mod.search(
            app.state.conn, phrase=q, person=person, date_from=date_from,
            date_to=date_to, filename=filename, repository=repository,
            file_ext=file_ext, limit=limit,
        )

    # -------------------------------------------------------------- errors
    @app.get("/api/errors")
    def error_report() -> list[dict]:
        return [
            dict(r) for r in app.state.conn.execute(
                "SELECT batch_id, po_id, filename, source_path, stage, message, occurred_at"
                " FROM processing_errors ORDER BY occurred_at DESC LIMIT 500"
            ).fetchall()
        ]

    # -------------------------------------------------------------- export
    @app.get("/api/export/registry.{fmt}")
    def export_registry(fmt: str):
        if fmt not in ("csv", "json"):
            raise HTTPException(400, "format must be csv or json")
        rows = [
            dict(r) for r in app.state.conn.execute(
                "SELECT po_id, sha256, original_filename, source_path, source_collection,"
                " repository, size_bytes, mime_type, file_ext, doc_type, imported_at,"
                " preserved_path, extraction_status, extraction_error, detected_people,"
                " detected_date, topic, review_status, operator_notes"
                " FROM proof_objects ORDER BY po_id"
            ).fetchall()
        ]
        stamp = dt.datetime.now(dt.timezone.utc).strftime("%Y%m%d-%H%M%S")
        if fmt == "json":
            return JSONResponse(
                rows,
                headers={"Content-Disposition": f"attachment; filename=registry-{stamp}.json"},
            )
        buf = io.StringIO()
        writer = csv.DictWriter(buf, fieldnames=list(rows[0].keys()) if rows else ["po_id"])
        writer.writeheader()
        writer.writerows(rows)
        return Response(
            buf.getvalue(),
            media_type="text/csv",
            headers={"Content-Disposition": f"attachment; filename=registry-{stamp}.csv"},
        )

    # ----------------------------------------------------------- frontend
    dist = Path(__file__).resolve().parents[2] / "frontend" / "dist"
    if dist.is_dir():
        app.mount("/", StaticFiles(directory=dist, html=True), name="frontend")

    return app
