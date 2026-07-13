"""Core-pipeline verification (stdlib only — no FastAPI required).

Verifies the framework-independent heart of the workstation: preservation,
SHA-256 checkpoints, mixed-file and ZIP import, duplicate detection, Proof
Object registration, Review Queue placement, search (phrase / person /
date / filename), original-source retrieval, restart persistence, and
error capture. The API layer and operator classification endpoints are
covered by the full acceptance suite (run_acceptance.py), which requires
FastAPI.

Usage: python3 -m backend.tests.run_core_verification
Writes evidence to $EIW_EVIDENCE_OUT (or a temp dir).
"""
from __future__ import annotations

import hashlib
import json
import os
import sys
import tempfile
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[2]))


def main() -> int:
    evidence: dict[str, object] = {"checks": []}

    def check(name: str, ok: bool, detail: str = "") -> None:
        line = f"{'PASS' if ok else 'FAIL'} — {name}" + (f" ({detail})" if detail else "")
        print(line)
        evidence["checks"].append(line)
        if not ok:
            raise AssertionError(line)

    with tempfile.TemporaryDirectory(prefix="eiw-core-") as tmp:
        data_dir = Path(tmp) / "eiw-data"
        os.environ["EIW_DATA_DIR"] = str(data_dir)
        os.environ.pop("EIW_MODE", None)

        from backend.app import config, db, importer, preservation, search
        from backend.tests.conftest import make_pdf, make_zip, synthetic_corpus

        config.ensure_dirs()
        conn = db.connect()
        db.init_db(conn)

        n0 = conn.execute("SELECT COUNT(*) n FROM proof_objects").fetchone()["n"]
        check("fresh live-mode registry starts empty", n0 == 0)

        corpus = synthetic_corpus()
        check("synthetic corpus holds at least 25 mixed files", len(corpus) >= 25, f"{len(corpus)} files")

        items = [importer.ImportItem(n, d, n) for n, d in corpus.items()]
        batch = importer.run_import(conn, items, "Unassigned", None, "core-batch-1")
        m = batch.manifest()
        evidence["import_manifest"] = m
        check("all items imported in one governed batch", m["imported_count"] == len(corpus), f"{m['imported_count']}")

        zip_bytes = make_zip({
            "production/zip-doc-01.pdf": make_pdf("SYNTHETIC-TEST-DATA zipped filing about the saffron docket."),
            "production/zip-note-01.txt": b"SYNTHETIC-TEST-DATA zipped note on the saffron docket.\n",
            "production/duplicate-of-letter-01.pdf": corpus["synthetic-letter-01.pdf"],
        })
        zb = importer.run_import(
            conn, [importer.ImportItem("synthetic-production-01.zip", zip_bytes, "synthetic-production-01.zip")],
            "Opposing", None, "core-zip",
        )
        zm = zb.manifest()
        evidence["zip_manifest"] = zm
        check("ZIP preserved and expanded (archive + 2 new members)", zm["imported_count"] == 3)
        check("duplicate ZIP member attached to existing Proof Object", zm["duplicate_count"] == 1)

        rows = conn.execute(
            "SELECT po_id, sha256, preserved_path, original_filename, extraction_status,"
            " review_status, import_batch_id FROM proof_objects"
        ).fetchall()
        mismatches = 0
        for row in rows:
            preserved = data_dir / row["preserved_path"]
            if not preserved.is_file():
                mismatches += 1
                continue
            if hashlib.sha256(preserved.read_bytes()).hexdigest() != row["sha256"]:
                mismatches += 1
        check("every original preserved on disk with matching SHA-256", mismatches == 0, f"{len(rows)} records")

        shas = [r["sha256"] for r in rows]
        check("one durable Proof Object per unique source", len(shas) == len(set(shas)))
        check("all records placed in the Review Queue", all(r["review_status"] == "Pending Review" for r in rows))
        check("every record traces to an operator import batch", all(r["import_batch_id"] for r in rows))

        dup = importer.run_import(
            conn, [importer.ImportItem("synthetic-letter-01.pdf", corpus["synthetic-letter-01.pdf"], "reimport")],
            "Unassigned", None, "core-dup",
        )
        check("re-import detected as duplicate, no new record", dup.manifest()["duplicate_count"] == 1
              and dup.manifest()["imported_count"] == 0)
        occ = conn.execute("SELECT COUNT(*) n FROM duplicate_occurrences").fetchone()["n"]
        evidence["duplicate_occurrences"] = occ

        hits = search.search(conn, phrase="mulberry appraisal")
        check("phrase search over extracted content", len(hits) == 3, "3 email hits")
        evidence["search_phrase"] = [h["original_filename"] for h in hits]
        hits = search.search(conn, person="Casey Sample")
        check("person search", len(hits) > 0, f"{len(hits)} hits")
        hits = search.search(conn, date_from="2023-06-01", date_to="2023-06-30")
        check("date-range search on detected dates", any(h["detected_date"] == "2023-06-06" for h in hits))
        hits = search.search(conn, filename="ledger-02")
        check("filename search isolates the record", len(hits) == 1)

        hit = search.search(conn, phrase="saffron docket")[0]
        row = conn.execute(
            "SELECT preserved_path, sha256 FROM proof_objects WHERE po_id = ?", (hit["po_id"],)
        ).fetchone()
        reopened = preservation.open_preserved(row["preserved_path"])
        check("search result reopens its preserved original, bytes intact",
              hashlib.sha256(reopened.read_bytes()).hexdigest() == row["sha256"])
        evidence["retrieval"] = {"query": "saffron docket", "po_id": hit["po_id"], "path": str(reopened.name)}

        errors = conn.execute("SELECT filename, stage, message FROM processing_errors").fetchall()
        check("processing-error report lists the unsupported file",
              any(e["filename"] == "synthetic-unknown-01.xyz" for e in errors))
        unknown = conn.execute(
            "SELECT preserved_path FROM proof_objects WHERE original_filename = 'synthetic-unknown-01.xyz'"
        ).fetchone()
        check("unsupported file preserved, never lost", (data_dir / unknown["preserved_path"]).is_file())
        evidence["error_report"] = [dict(e) for e in errors]

        expected = conn.execute("SELECT COUNT(*) n FROM proof_objects").fetchone()["n"]
        statuses = {
            r["extraction_status"]: r["n"] for r in conn.execute(
                "SELECT extraction_status, COUNT(*) n FROM proof_objects GROUP BY 1"
            )
        }
        evidence["extraction_statuses"] = statuses
        conn.close()

        conn2 = db.connect()
        after = conn2.execute("SELECT COUNT(*) n FROM proof_objects").fetchone()["n"]
        check("restart persistence: registry intact on reconnect", after == expected, f"{after} records")
        hits = search.search(conn2, phrase="mulberry appraisal")
        check("restart persistence: search index intact", len(hits) == 3)
        conn2.close()

        out_dir = Path(os.environ.get("EIW_EVIDENCE_OUT", tmp))
        out_dir.mkdir(parents=True, exist_ok=True)
        (out_dir / "core_verification_evidence.json").write_text(
            json.dumps(evidence, indent=2, ensure_ascii=False)
        )
        print(f"CORE VERIFICATION: ALL {len(evidence['checks'])} CHECKS PASSED")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
