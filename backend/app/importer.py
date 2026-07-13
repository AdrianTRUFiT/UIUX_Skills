"""The governed import pipeline.

Order of operations for every incoming item:
preserve bytes → SHA-256 → duplicate check → extraction → Proof Object
registration → Review Queue. Failures are recorded in the error report and
never delete or reject a preserved source. ZIP archives are preserved as
their own Proof Object and their members are imported individually with the
archive recorded in each member's source path.
"""
from __future__ import annotations

import datetime as dt
import io
import json
import mimetypes
import sqlite3
import zipfile
from dataclasses import dataclass, field
from pathlib import Path

from . import config, db, extraction, preservation


def _now() -> str:
    return dt.datetime.now(dt.timezone.utc).isoformat(timespec="seconds")


@dataclass
class ImportItem:
    filename: str
    data: bytes
    source_path: str


@dataclass
class BatchResult:
    batch_id: int = 0
    total_items: int = 0
    imported: list[dict] = field(default_factory=list)
    duplicates: list[dict] = field(default_factory=list)
    errors: list[dict] = field(default_factory=list)
    unsupported: list[dict] = field(default_factory=list)

    def manifest(self) -> dict:
        return {
            "batch_id": self.batch_id,
            "total_items": self.total_items,
            "imported_count": len(self.imported),
            "duplicate_count": len(self.duplicates),
            "error_count": len(self.errors),
            "unsupported_count": len(self.unsupported),
            "imported": self.imported,
            "duplicates": self.duplicates,
            "errors": self.errors,
            "unsupported": self.unsupported,
        }


def _next_po_id(conn: sqlite3.Connection, sha: str) -> str:
    row = conn.execute("SELECT COUNT(*) AS n FROM proof_objects").fetchone()
    return f"PO-{row['n'] + 1:06d}-{sha[:8]}"


def _register(
    conn: sqlite3.Connection,
    item: ImportItem,
    repository: str,
    collection: str | None,
    batch: BatchResult,
) -> None:
    batch.total_items += 1
    ext = Path(item.filename).suffix.lower()
    try:
        sha, preserved_path = preservation.preserve(item.data, item.filename)
    except Exception as exc:
        batch.errors.append(
            {"filename": item.filename, "source_path": item.source_path,
             "stage": "preservation", "message": f"{type(exc).__name__}: {exc}"}
        )
        return

    existing = conn.execute(
        "SELECT po_id FROM proof_objects WHERE sha256 = ?", (sha,)
    ).fetchone()
    if existing:
        conn.execute(
            "INSERT INTO duplicate_occurrences (po_id, original_filename, source_path, batch_id, occurred_at)"
            " VALUES (?, ?, ?, ?, ?)",
            (existing["po_id"], item.filename, item.source_path, batch.batch_id, _now()),
        )
        batch.duplicates.append(
            {"filename": item.filename, "source_path": item.source_path,
             "duplicate_of": existing["po_id"], "sha256": sha}
        )
        return

    result = extraction.extract(item.data, ext)
    po_id = _next_po_id(conn, sha)
    mime = mimetypes.guess_type(item.filename)[0]
    conn.execute(
        """
        INSERT INTO proof_objects (
            po_id, sha256, original_filename, source_path, source_collection,
            repository, size_bytes, mime_type, file_ext, doc_type, imported_at,
            import_batch_id, preserved_path, extraction_status, extraction_error,
            extracted_text, detected_people, detected_date, file_modified,
            review_status, metadata_json
        ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        """,
        (
            po_id, sha, item.filename, item.source_path, collection,
            repository, len(item.data), mime, ext, result.doc_type, _now(),
            batch.batch_id, preserved_path, result.status, result.error,
            result.text or None, result.detected_people, result.detected_date,
            None, config.REVIEW_PENDING, extraction.metadata_to_json(result),
        ),
    )
    db.fts_upsert(conn, po_id)

    record = {"po_id": po_id, "filename": item.filename, "sha256": sha,
              "extraction_status": result.status, "repository": repository}
    batch.imported.append(record)
    if result.status in (extraction.STATUS_UNSUPPORTED, extraction.STATUS_FAILED):
        batch.unsupported.append(record)
        conn.execute(
            "INSERT INTO processing_errors (batch_id, po_id, filename, source_path, stage, message, occurred_at)"
            " VALUES (?, ?, ?, ?, ?, ?, ?)",
            (batch.batch_id, po_id, item.filename, item.source_path,
             "extraction", result.error or result.status, _now()),
        )


def _expand_zip(
    conn: sqlite3.Connection,
    item: ImportItem,
    repository: str,
    collection: str | None,
    batch: BatchResult,
    depth: int,
) -> None:
    # The archive itself is preserved and registered first, then its members.
    _register(conn, item, repository, collection, batch)
    if depth > config.MAX_ZIP_DEPTH:
        batch.errors.append(
            {"filename": item.filename, "source_path": item.source_path,
             "stage": "zip", "message": "nested ZIP depth limit reached; members not expanded"}
        )
        return
    try:
        archive = zipfile.ZipFile(io.BytesIO(item.data))
    except Exception as exc:
        batch.errors.append(
            {"filename": item.filename, "source_path": item.source_path,
             "stage": "zip", "message": f"{type(exc).__name__}: {exc}"}
        )
        return
    for info in archive.infolist():
        if info.is_dir():
            continue
        member_source = f"{item.source_path}!/{info.filename}"
        try:
            data = archive.read(info)
        except Exception as exc:
            batch.errors.append(
                {"filename": info.filename, "source_path": member_source,
                 "stage": "zip-member", "message": f"{type(exc).__name__}: {exc}"}
            )
            continue
        member = ImportItem(Path(info.filename).name, data, member_source)
        if Path(info.filename).suffix.lower() in config.ARCHIVE_EXTENSIONS:
            _expand_zip(conn, member, repository, collection, batch, depth + 1)
        else:
            _register(conn, member, repository, collection, batch)


def run_import(
    conn: sqlite3.Connection,
    items: list[ImportItem],
    repository: str,
    collection: str | None,
    source_label: str | None,
) -> BatchResult:
    if repository not in config.REPOSITORIES:
        raise ValueError(f"unknown repository '{repository}'")
    batch = BatchResult()
    cur = conn.execute(
        "INSERT INTO import_batches (started_at, source_label) VALUES (?, ?)",
        (_now(), source_label),
    )
    batch.batch_id = cur.lastrowid
    for item in items:
        if Path(item.filename).suffix.lower() in config.ARCHIVE_EXTENSIONS:
            _expand_zip(conn, item, repository, collection, batch, depth=1)
        else:
            _register(conn, item, repository, collection, batch)
    conn.execute(
        "UPDATE import_batches SET total_items=?, imported=?, duplicates=?, errors_count=?,"
        " unsupported=?, manifest_json=? WHERE id=?",
        (
            batch.total_items, len(batch.imported), len(batch.duplicates),
            len(batch.errors), len(batch.unsupported),
            json.dumps(batch.manifest(), ensure_ascii=False), batch.batch_id,
        ),
    )
    conn.commit()
    return batch
