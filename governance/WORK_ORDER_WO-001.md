# Work Order WO-001 — Evidence Intake Workstation v1.0 Vertical Slice

- Work order ID: WO-001
- Authorized by: Adrian TRUFiT McKenzie (human consequence authority), 2026-07-13, in the governed extraction session
- Repository of record: https://github.com/AdrianTRUFiT/Evidence-Intake-Workstation
- Canonical branch: main
- Approved baseline: commit `063e897`, plus only the repository-rename redirect and this governance-only record documenting PR #2
- Development branch: `claude/session-extraction-instructions-qvfjfr`
- Assigned processor: Claude Code (this session)
- Status at issue: authorized; no application code existed at baseline

Baseline note (governance-only record of PR #2): PR #2, merged by the owner on 2026-07-12, added Claude Code skill suites under `.claude/skills/` plus 21st.dev/Magic MCP configuration (`.mcp.json`, `21ST_DEV_SETUP.md`). This is development tooling, not application implementation. No secrets were committed; the MCP config reads `API_KEY_21ST` from the environment.

## Mission

Import every case document into one governed repository where every source is preserved, every file is searchable, and nothing is lost.

## Authorized scope — the complete first vertical slice

Import mixed local files and one ZIP archive
→ preserve every original
→ calculate SHA-256 over the preserved bytes
→ extract supported text and available metadata
→ create one durable Proof Object per unique source
→ detect duplicates
→ place records into the Review and Classification Queue
→ retain separate repository identity
→ persist registry and review state in SQLite
→ search extracted content and metadata
→ reopen the preserved original.

Required source repositories: Operator, Opposing, Former Counsel, Court, Authority, Unassigned.

Required primary screens: 1. Evidence Intake, 2. Review and Classification Queue, 3. Repository Explorer, 4. Universal Search.

Required architecture: React + TypeScript frontend; Python + FastAPI backend; SQLite registry and search state; local filesystem preserved-source storage; GitHub for code, configuration, documentation, and tests only; no confidential case evidence in GitHub; no browser localStorage as the primary evidence store.

## Protected boundaries

Do not build the full LawAidAI ecosystem, PatternEchoAI integration, relationship graphs, financial analysis, or Courtroom Retrieval. Do not implement Gmail if it delays the local-file vertical slice. Do not make legal conclusions, credibility findings, admissibility decisions, or courtroom strategy. Do not mix synthetic records with Live mode. Do not replace preserved originals with extracted text. Do not claim completion based on UI screens alone.

## In-system definition

A document is not considered in the system until: its original is preserved; its source identity is retained; it has a durable Proof Object ID; its extraction status is recorded; it is searchable where extraction is supported; and the preserved original can be reopened.

## Acceptance test (all twenty must pass)

1. Import at least 25 mixed supported files.
2. Import at least one ZIP archive.
3. Preserve every original.
4. Generate SHA-256 for every unique preserved source.
5. Extract searchable text where supported.
6. Create one durable Proof Object per unique source.
7. Detect duplicates without creating uncontrolled duplicate records.
8. Place all new records in the Review Queue.
9. Classify records across separate repositories.
10. Support bulk classification.
11. Search by phrase.
12. Search by person.
13. Search by date.
14. Search by filename.
15. Open the preserved original from search results.
16. Restart the application and retain all state.
17. Export the registry.
18. Produce a visible processing-error report.
19. Confirm confidential evidence remains outside GitHub.
20. Confirm no synthetic evidence appears in Live mode.

## Completion evidence required

Commit SHA; files changed; run and stop commands; test output; import manifest; registry export; duplicate-handling proof; search-and-retrieval demonstration; preserved-original reopening proof; restart-persistence proof; error report; confirmation that no evidence or secrets were committed.

## Stop condition

Stop after the twenty acceptance criteria pass and report for human review. Do not expand scope. Do not stop at scaffolding or mock screens.

---

# Implementation Plan

## Layout

- `backend/` — Python FastAPI application
  - `app/config.py` — data root (`EIW_DATA_DIR`, default `~/EvidenceIntakeWorkstation`), mode (Live), constants
  - `app/db.py` — SQLite schema, migrations-on-start, FTS5 index
  - `app/preservation.py` — byte-for-byte preservation into content-addressed storage, SHA-256
  - `app/extraction.py` — per-type extractors: PDF (pypdf), DOCX (python-docx), XLSX (openpyxl), CSV/TXT (stdlib), EML (stdlib `email`); JPG/JPEG/PNG/TIFF registered without text extraction; unsupported types preserved and reported
  - `app/importer.py` — import pipeline including ZIP expansion (nested to depth 2), duplicate detection by SHA-256, Proof Object creation, error capture without source loss
  - `app/search.py` — FTS5 phrase search plus person/date/filename/repository/type filters
  - `app/main.py` — API routes, registry export (CSV/JSON), error report, static serving of the built frontend
  - `tests/test_acceptance.py` — the twenty criteria, end to end, using runtime-generated synthetic fixtures in temp directories only
- `frontend/` — Vite + React + TypeScript; four screens; light, warm, neutral styling; no localStorage for evidence or registry state
- `run.sh` / `stop.sh` and `run.ps1` / `stop.ps1` — start/stop the application locally
- `docs/acceptance/WO-001/` — completion evidence pack

## Evidence-safety design

- Preserved originals live under `{EIW_DATA_DIR}/preserved/<sha-prefix>/<sha256>/<original filename>`; the application never modifies or deletes them; extraction failure never removes a preserved source.
- The data root defaults to a directory outside the repository clone and is additionally covered by `.gitignore`; the exact production evidence root remains an open human decision and is configurable via `EIW_DATA_DIR`.
- SHA-256 is recorded as an integrity checkpoint over the acquired bytes; it is not treated as proof of authorship, authenticity, or admissibility.
- Proof Object IDs are durable (`PO-<sequence>-<sha-prefix>`), stored in SQLite, stable across restarts; duplicates attach occurrence records to the existing Proof Object instead of creating new ones.
- Live mode contains no seed, sample, or fallback data paths; acceptance tests run against isolated temp data roots with clearly synthetic generated fixtures that are never committed.
- Classification suggestions (e.g., people and dates from EML headers) are factual only and require operator confirmation in the Review Queue; the system draws no legal conclusions.

## Out of scope (per protected boundaries)

Gmail, OCR, audio/video transcription, MSG parsing, binder mapping, graphs, financial analysis, Courtroom Retrieval, PatternEchoAI, multi-tenant or commercial administration.
