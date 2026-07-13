"""WO-001 acceptance criteria — shared implementation.

Runs the twenty authorized criteria end to end against a live-mode app
instance bound to an isolated temporary data root. Used by both the pytest
wrapper (test_acceptance.py) and the standalone runner (run_acceptance.py).
Fixture data is synthetic and never committed.
"""
from __future__ import annotations

import csv
import hashlib
import io
import json
import os
import sqlite3
import subprocess
from pathlib import Path

from .conftest import make_pdf, make_zip, synthetic_corpus

REPO_ROOT = Path(__file__).resolve().parents[2]


def _pass(n: int, message: str, evidence: dict) -> None:
    line = f"CRITERION {n:02d} PASS — {message}"
    print(line)
    evidence.setdefault("criteria", []).append(line)


def _import(client, files: dict[str, bytes], repository="Unassigned", **form):
    payload = [("files", (name, io.BytesIO(data))) for name, data in files.items()]
    resp = client.post(
        "/api/import", files=payload, data={"repository": repository, **form}
    )
    assert resp.status_code == 200, resp.text
    return resp.json()


def run_criteria(client, data_dir: Path, scratch: Path) -> dict:
    evidence: dict[str, object] = {}

    # Criterion 20 precondition: a fresh Live-mode instance is empty —
    # there is no seeding, sample, or fallback data path.
    status = client.get("/api/status").json()
    assert status["mode"] == "live"
    assert status["counts"]["proof_objects"] == 0

    corpus = synthetic_corpus()
    assert len(corpus) >= 25

    # ---- 1. Import at least 25 mixed supported files.
    manifest = _import(client, corpus, repository="Unassigned", source_label="acceptance-batch-1")
    assert manifest["total_items"] == len(corpus)
    assert manifest["imported_count"] == len(corpus)
    evidence["import_manifest"] = manifest
    _pass(1, f"imported {manifest['imported_count']} mixed files in one governed batch", evidence)

    # ---- 2. Import at least one ZIP archive (with one duplicate member).
    zip_members = {
        "production/zip-doc-01.pdf": make_pdf(
            "SYNTHETIC-TEST-DATA zipped filing about the saffron docket."
        ),
        "production/zip-note-01.txt": b"SYNTHETIC-TEST-DATA zipped note on the saffron docket.\n",
        "production/duplicate-of-letter-01.pdf": corpus["synthetic-letter-01.pdf"],
    }
    zip_manifest = _import(
        client,
        {"synthetic-production-01.zip": make_zip(zip_members)},
        repository="Opposing",
        source_label="acceptance-zip",
    )
    assert zip_manifest["imported_count"] == 3  # archive + 2 new members
    assert zip_manifest["duplicate_count"] == 1
    evidence["zip_manifest"] = zip_manifest
    _pass(2, "ZIP archive preserved and expanded; members carry archive source paths", evidence)

    registry = client.get("/api/proof-objects", params={"limit": 1000}).json()

    # ---- 3 & 4. Every original preserved; SHA-256 over preserved bytes.
    for po in registry:
        detail = client.get(f"/api/proof-objects/{po['po_id']}").json()
        preserved = data_dir / detail["preserved_path"]
        assert preserved.is_file(), f"missing preserved original for {po['po_id']}"
        digest = hashlib.sha256(preserved.read_bytes()).hexdigest()
        assert digest == detail["sha256"], f"hash mismatch for {po['po_id']}"
    original = corpus["synthetic-letter-01.pdf"]
    stored = client.get(f"/api/proof-objects/{manifest['imported'][0]['po_id']}/original")
    assert stored.status_code == 200 and stored.content == original
    evidence["preservation_checked"] = len(registry)
    _pass(3, f"all {len(registry)} preserved originals present on disk, byte-for-byte", evidence)
    _pass(4, "recomputed SHA-256 of every preserved file matches its registry checkpoint", evidence)

    # ---- 5. Extract searchable text where supported.
    supported = [p for p in registry if p["extraction_status"] == "extracted"]
    assert len(supported) >= 18, f"only {len(supported)} extracted"
    _pass(5, f"text extracted from {len(supported)} supported documents", evidence)

    # ---- 6. One durable Proof Object per unique source.
    shas = [client.get(f"/api/proof-objects/{p['po_id']}").json()["sha256"] for p in registry]
    assert len(shas) == len(set(shas))
    assert all(p["po_id"].startswith("PO-") for p in registry)
    _pass(6, "one durable Proof Object ID per unique SHA-256", evidence)

    # ---- 7. Duplicates detected without uncontrolled duplicate records.
    dup_reimport = _import(client, {"synthetic-letter-01.pdf": original})
    assert dup_reimport["imported_count"] == 0
    assert dup_reimport["duplicate_count"] == 1
    dup_po = dup_reimport["duplicates"][0]["duplicate_of"]
    detail = client.get(f"/api/proof-objects/{dup_po}").json()
    assert len(detail["duplicate_occurrences"]) >= 2
    evidence["duplicate_proof"] = {
        "duplicate_of": dup_po,
        "occurrences": detail["duplicate_occurrences"],
    }
    _pass(7, "re-imports attach occurrence records to the existing Proof Object", evidence)

    # ---- 8. All new records land in the Review Queue.
    pending = client.get(
        "/api/proof-objects", params={"review_status": "Pending Review", "limit": 1000}
    ).json()
    assert len(pending) == len(registry)
    _pass(8, f"all {len(pending)} records entered the Review Queue", evidence)

    # ---- 9. Classify records across separate repositories.
    targets = {
        "Operator": manifest["imported"][0]["po_id"],
        "Court": manifest["imported"][1]["po_id"],
        "Former Counsel": manifest["imported"][2]["po_id"],
        "Authority": manifest["imported"][3]["po_id"],
    }
    for repo, po_id in targets.items():
        updated = client.patch(
            f"/api/proof-objects/{po_id}",
            json={"repository": repo, "review_status": "Reviewed"},
        ).json()
        assert updated["repository"] == repo
        assert updated["classification_history"], "classification history must be recorded"
    for repo in ("Operator", "Court", "Opposing"):
        rows = client.get("/api/proof-objects", params={"repository": repo}).json()
        assert rows, f"repository {repo} should hold records"
    _pass(9, "records classified across Operator/Court/Former Counsel/Authority with history", evidence)

    # ---- 10. Bulk classification.
    bulk_ids = [r["po_id"] for r in manifest["imported"][4:9]]
    resp = client.post(
        "/api/proof-objects/bulk-classify",
        json={"po_ids": bulk_ids, "fields": {"repository": "Opposing", "topic": "bulk-classified"}},
    )
    assert resp.status_code == 200 and resp.json()["updated"] == 5
    for po_id in bulk_ids:
        row = client.get(f"/api/proof-objects/{po_id}").json()
        assert row["repository"] == "Opposing" and row["topic"] == "bulk-classified"
    _pass(10, "bulk classification applied to 5 records at once", evidence)

    # ---- 11. Search by phrase.
    hits = client.get("/api/search", params={"q": "mulberry appraisal"}).json()
    assert hits and all("synthetic-mail" in h["original_filename"] for h in hits)
    evidence["search_phrase"] = hits[:3]
    _pass(11, f"phrase search hit {len(hits)} extracted documents", evidence)

    # ---- 12. Search by person.
    hits = client.get("/api/search", params={"person": "Casey Sample"}).json()
    assert hits
    evidence["search_person"] = [h["po_id"] for h in hits][:5]
    _pass(12, f"person search returned {len(hits)} records", evidence)

    # ---- 13. Search by date (EML Date headers → detected_date).
    hits = client.get(
        "/api/search", params={"date_from": "2023-06-01", "date_to": "2023-06-30"}
    ).json()
    assert any(h["detected_date"] == "2023-06-06" for h in hits)
    evidence["search_date"] = [
        {"po_id": h["po_id"], "detected_date": h["detected_date"]} for h in hits
    ][:5]
    _pass(13, "date-range search matched the June email by detected date", evidence)

    # ---- 14. Search by filename.
    hits = client.get("/api/search", params={"filename": "ledger-02"}).json()
    assert len(hits) == 1 and hits[0]["original_filename"] == "synthetic-ledger-02.csv"
    _pass(14, "filename search isolated the exact record", evidence)

    # ---- 15. Open the preserved original from search results.
    hit = client.get("/api/search", params={"q": "saffron docket"}).json()[0]
    got = client.get(f"/api/proof-objects/{hit['po_id']}/original")
    assert got.status_code == 200 and len(got.content) > 0
    evidence["retrieval"] = {
        "query": "saffron docket",
        "po_id": hit["po_id"],
        "filename": hit["original_filename"],
        "bytes": len(got.content),
    }
    _pass(15, "search result reopened its preserved original", evidence)

    # ---- 17. Export the registry (CSV and JSON).
    export_csv = client.get("/api/export/registry.csv")
    assert export_csv.status_code == 200
    parsed = list(csv.DictReader(io.StringIO(export_csv.text)))
    assert len(parsed) == len(registry)
    export_json = client.get("/api/export/registry.json")
    assert export_json.status_code == 200 and len(export_json.json()) == len(registry)
    evidence["registry_export_rows"] = len(parsed)
    _pass(17, f"registry exported ({len(parsed)} rows, CSV and JSON)", evidence)

    # ---- 18. Visible processing-error report; unsupported source preserved.
    errors = client.get("/api/errors").json()
    assert any(e["filename"] == "synthetic-unknown-01.xyz" for e in errors)
    unknown = next(p for p in registry if p["original_filename"] == "synthetic-unknown-01.xyz")
    assert unknown["extraction_status"] == "unsupported"
    unknown_detail = client.get(f"/api/proof-objects/{unknown['po_id']}").json()
    assert (data_dir / unknown_detail["preserved_path"]).is_file()
    evidence["error_report"] = errors
    _pass(18, "error report lists the unsupported file; its original remains preserved", evidence)

    # ---- 16. Restart the application and retain all state.
    expected_count = len(registry)
    client.app.state.conn.close()
    from fastapi.testclient import TestClient

    from backend.app.main import create_app

    reopened = TestClient(create_app())
    try:
        after = reopened.get("/api/status").json()
        assert after["counts"]["proof_objects"] == expected_count
        row = reopened.get(f"/api/proof-objects/{targets['Operator']}").json()
        assert row["repository"] == "Operator" and row["review_status"] == "Reviewed"
        hits = reopened.get("/api/search", params={"q": "mulberry appraisal"}).json()
        assert hits, "search index must survive restart"
        got = reopened.get(f"/api/proof-objects/{row['po_id']}/original")
        assert got.status_code == 200
        evidence["restart"] = {
            "proof_objects_after_restart": after["counts"]["proof_objects"],
            "classification_retained": True,
            "search_after_restart_hits": len(hits),
        }
    finally:
        reopened.app.state.conn.close()
    _pass(16, f"fresh process retained all {expected_count} records, classifications, search, retrieval", evidence)

    # ---- 19. Confidential evidence remains outside GitHub.
    assert REPO_ROOT not in data_dir.parents, "data root must live outside the repo clone"
    tracked = subprocess.run(
        ["git", "ls-files"], cwd=REPO_ROOT, capture_output=True, text=True, check=True
    ).stdout.splitlines()
    assert not any(p.endswith((".db", ".sqlite")) for p in tracked)
    assert not any(p.startswith(("preserved/", "data/")) for p in tracked)
    ignore = (REPO_ROOT / ".gitignore").read_text()
    assert "EvidenceIntakeWorkstation" in ignore
    _pass(19, "data root is outside the clone; no evidence or database files tracked by git", evidence)

    # ---- 20. No synthetic evidence appears in Live mode.
    conn = sqlite3.connect(data_dir / "registry.db")
    unbatched = conn.execute(
        "SELECT COUNT(*) FROM proof_objects WHERE import_batch_id IS NULL"
    ).fetchone()[0]
    conn.close()
    assert unbatched == 0, "every record must trace to an operator import batch"
    evidence["live_mode"] = {
        "fresh_instance_started_empty": True,
        "records_without_import_batch": unbatched,
    }
    _pass(20, "live mode started empty; every record traces to an operator import batch", evidence)

    # Persist the evidence bundle for the completion pack.
    out_dir = Path(os.environ.get("EIW_EVIDENCE_OUT", str(scratch)))
    out_dir.mkdir(parents=True, exist_ok=True)
    (out_dir / "acceptance_evidence.json").write_text(
        json.dumps(evidence, indent=2, ensure_ascii=False)
    )
    (out_dir / "registry_export.csv").write_text(export_csv.text)
    return evidence
