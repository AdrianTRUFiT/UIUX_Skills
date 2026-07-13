# WO-001 Build Verification Statement

- Work order: WO-001 — Evidence Intake Workstation v1.0 vertical slice (`governance/WORK_ORDER_WO-001.md`)
- Verification date: 2026-07-13
- Verifying processor: Claude Code (build session)
- Honest status: **IMPLEMENTED IN FULL; VERIFIED AT CORE LEVEL; FULL API-LEVEL ACCEPTANCE RUN AND UI VERIFICATION HELD BY SESSION NETWORK POLICY**

No completion is claimed beyond what is evidenced below. Nothing in this
build is a mock: every listed capability is real, committed code, and the
verification gaps are environment gaps, not implementation gaps.

## What was verified in this session

`python3 -m backend.tests.run_core_verification` — 19 of 19 checks passed
(output: `core_verification_output.txt`, evidence:
`core_verification_evidence.json`). This exercises the framework-independent
core with 27 synthetic mixed files plus a ZIP production in an isolated
temporary data root, in live mode.

## Criterion-by-criterion status

| # | Acceptance criterion | Status |
| --- | --- | --- |
| 1 | Import ≥ 25 mixed supported files | **PROVEN** (27 files, one governed batch) |
| 2 | Import ≥ 1 ZIP archive | **PROVEN** (archive preserved + members expanded with archive source paths) |
| 3 | Preserve every original | **PROVEN** (30/30 on disk, byte-for-byte) |
| 4 | SHA-256 per unique preserved source | **PROVEN** (recomputed hashes match registry) |
| 5 | Extract searchable text where supported | **PROVEN for TXT/CSV/EML/DOCX/XLSX** (stdlib extractors); PDF extraction implemented twice over (pypdf primary, pdftotext fallback) but unverifiable in this session — both libraries blocked by egress policy |
| 6 | One durable Proof Object per unique source | **PROVEN** |
| 7 | Duplicate detection without uncontrolled records | **PROVEN** (occurrence records attach to existing PO) |
| 8 | All new records enter the Review Queue | **PROVEN** |
| 9 | Classify across separate repositories | IMPLEMENTED (API layer with history); **PENDING API-LEVEL RUN** |
| 10 | Bulk classification | IMPLEMENTED (API layer); **PENDING API-LEVEL RUN** |
| 11 | Search by phrase | **PROVEN** (FTS5) |
| 12 | Search by person | **PROVEN** |
| 13 | Search by date | **PROVEN** (detected dates from EML headers) |
| 14 | Search by filename | **PROVEN** |
| 15 | Open preserved original from search results | **PROVEN at core level** (search hit → preserved path → bytes intact); HTTP endpoint pending API-level run |
| 16 | Restart with all state retained | **PROVEN at core level** (registry + search index across reconnect); process-level restart pending API run |
| 17 | Export the registry | IMPLEMENTED (CSV + JSON endpoints); **PENDING API-LEVEL RUN** |
| 18 | Visible processing-error report | **PROVEN at core level** (unsupported file listed AND preserved); endpoint pending |
| 19 | Confidential evidence outside GitHub | **PROVEN** (data root outside clone; `.gitignore`; no evidence or database files tracked) |
| 20 | No synthetic evidence in Live mode | **PROVEN** (fresh live instance empty; every record traces to an operator import batch) |

## Environment blockers (per agent-proxy policy: reported, not routed around)

The build session's egress policy denies, with 403 at the proxy or
destination: `registry.npmjs.org`, `pypi.org`, `files.pythonhosted.org`,
`cdn.jsdelivr.net`, `unpkg.com`, `cdnjs.cloudflare.com`, `esm.sh`,
`github.com`/`raw.githubusercontent.com` (fetch), `deb.debian.org`, and —
after an initial working window — `archive.ubuntu.com` /
`security.ubuntu.com` (behavior consistent with burst-rate banning;
`python3-mdurl` was denied in every window). Backend Python dependencies
therefore could not be installed in this session; the acceptance suite's
API layer (FastAPI TestClient) could not execute, and React/Vite could not
be installed for the frontend build.

## Exact completion path (one short session on any networked machine)

1. `pip install -r backend/requirements-dev.txt`
2. `python3 -m backend.tests.run_acceptance` → must print `ACCEPTANCE: ALL 20 CRITERIA PASSED`
3. `cd frontend && npm install && npm run build`
4. `./run.sh` (or `.\run.ps1`) → open http://127.0.0.1:8741 and walk the four screens
5. Attach outputs to `07 — Runtime, Tests and Proof Records` in the governed workspace and clear the two HOLD ledger entries

## Related governance records

- Decision: "WO-001 authorized" — Decision/Governance/HOLD Ledger (Approved)
- HOLD: frontend build and UI verification (npm blocked)
- HOLD: API-level acceptance run (Python package installation blocked)
