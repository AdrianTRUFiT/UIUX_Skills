# Evidence Intake Workstation

Sole implementation and governance repository of record for the Evidence Intake Workstation (explicit human decision, 2026-07-12).

- Mission: import every case document into one governed repository where every source is preserved, every file is searchable, and nothing is lost — see `governance/MISSION.md` (includes the North Star acceptance philosophy).
- Project truth: `intake/SESSION_EXTRACTION.md`.
- Governance workspace: Evidence Intake Workstation — Governed Project Workspace (Notion).
- Parent ecosystem: LawAidAI. Its orchestration repository is `AdrianTRUFiT/my-lawaid-ai`, which must not contain this workstation's implementation truth.
- Evidence is never committed to this repository; GitHub stores code, configuration, documentation, and tests only.

## Running locally

- Windows: `.\run.ps1` — then open http://127.0.0.1:8741. Stop with `.\stop.ps1`.
- Linux/macOS: `./run.sh` and `./stop.sh`.
- Requirements: Python 3.11+ (backend), Node 18+ (one-time frontend build).
- The evidence store and registry live in `~/EvidenceIntakeWorkstation`
  (override with `EIW_DATA_DIR`). They are never part of this repository.

## Verification

- Full acceptance suite (WO-001, twenty criteria): `python3 -m backend.tests.run_acceptance`
  (or `pytest backend/tests` where pytest is available). The suite generates
  synthetic fixtures at runtime in temporary directories — no real evidence
  is used or committed.

Build authorization: WO-001 (`governance/WORK_ORDER_WO-001.md`).
