# SESSION EXTRACTION — EVIDENCE INTAKE WORKSTATION

## 1. Project Identity

- Project name: Evidence Intake Workstation
- Project type: Local-first litigation evidence-acquisition, review, repository, and search application
- Parent ecosystem: LawAidAI — the orchestration layer that will eventually coordinate independent workstations; LawAidAI is the parent, not the project. The wider environment is BizTech Wellness AI / AdrianTRUFiT governed development; the governed Notion workspace sits under the parent page "SoulHubⓈ"
- Human owner and consequence authority: Adrian TRUFiT McKenzie (workspace shell names "Adrian" as final authority)
- Current status: Existing project requiring continuation or recovery
- Date of extraction: 2026-07-12 (revised same day on explicit human direction)

Status basis: project-creation intake is partially complete. The extraction is committed in a dedicated GitHub repository, and a dedicated Notion governed workspace has been duplicated and renamed, but the workspace's Source Register and Project Control Center still contain only template placeholder records, the extraction file has not been registered in the Source Register, and no application code or runtime exists anywhere in the dedicated repository.

Identity rule (explicit human decision, this session): the project is the Evidence Intake Workstation — one workstation with one job. It is not LawAidAI, not a litigation operating system, not a legal-research product, and not an autonomous legal adviser. Every processor that works on this project receives a bounded workstation mission, never an ecosystem mission.

## North Star

(Explicit human decision, this session. This is the acceptance philosophy for every current and future feature of this workstation.)

When this workstation is complete, Adrian should never again have to wonder:

- Do I have this document?
- Where did it come from?
- Which version is correct?
- Where is the original?
- Which issue does it support?
- Can I find it in under 10 seconds?

Any proposed feature, screen, or change is measured against these six questions. A feature that does not help answer one of them does not belong in this workstation.

---

## 2. Buildable Opportunity

### Mission (one sentence — explicit human decision, this session)

Import every case document into one governed repository where every source is preserved, every file is searchable, and nothing is lost.

Everything else in this document is implementation of that sentence, not additional mission.

### What that means in practice

Build a working Evidence Intake Workstation that allows Adrian to place a large, mixed litigation record into one governed acquisition flow and convert it into preserved, indexed, searchable records. The workstation accepts common case materials — PDFs, Word files, spreadsheets, emails, images, ZIP productions — then preserves the source, records where it came from, calculates a SHA-256 integrity checkpoint, extracts available text and metadata, assigns a durable Proof Object ID, places the item into a review and classification queue, stores the registry persistently, makes the record searchable, and allows retrieval of the preserved original.

This is worth building because Adrian has accumulated thousands of litigation records across approximately three years, but does not yet have a dependable method to account for, organize, search, and retrieve them as trial approaches.

When it exists, Adrian can begin loading the actual case immediately instead of continuing to design downstream intelligence against an incomplete record.

This is more than an idea or report because it is a concrete operational pipeline with identified inputs, outputs, storage requirements, screens, repository boundaries, and acceptance criteria — and because a dedicated governed repository and governed Notion workspace for it already exist.

---

## 3. One-Sentence Definition

The Evidence Intake Workstation imports every one of Adrian's case documents into one governed repository where every source is preserved, every file is searchable, nothing is lost, and the preserved original can always be reopened.

---

## 4. Larger Vision and First Build

### Larger Vision

The architecture is workstations, not a monolithic AI (explicit human direction, this session). Each workstation has one job and does it well; each can be built, tested, verified, and used independently. LawAidAI is the orchestration layer that eventually coordinates them. The workstation family supported by the session:

- Evidence Intake Workstation (this project)
- Financial Analysis Workstation
- Communication Intelligence Workstation
- Courtroom Retrieval Workstation
- PatternEchoAI (pattern-memory runtime)

Additional capabilities discussed for the parent ecosystem: Gmail acquisition, relationship mapping, perspective comparison, trial preparation, and physical binder mapping.

The governing human-centered principle carried from the source record:

The system performs the legwork. The operator performs the judgment. The Court makes the decision.

### First Build

The first build is Evidence Intake Workstation v1.0, whose entire mission is the one sentence above.

Its implementation shape is one complete operational path:

Mixed source files
→ acquisition
→ source preservation
→ SHA-256 integrity checkpoint
→ text and metadata extraction
→ Proof Object registration
→ review and classification
→ repository storage
→ universal search
→ original-source retrieval

This first build gives every later workstation a trusted factual foundation without requiring financial reasoning, pattern detection, trial prediction, semantic graph visualization, or courtroom systems to be built now.

---

## 5. Primary User, Operator, and Beneficiary

- Primary user: Adrian TRUFiT McKenzie
- Operator: Adrian TRUFiT McKenzie
- Primary beneficiary: Adrian, acting as a self-represented litigant preparing for financial issues, pretrial proceedings, negotiation, and trial
- Future buyers or external users: UNKNOWN
- Commercial customer: UNKNOWN

Relevant operating realities:

- Adrian is not approaching this as a professional software engineer.
- The interface must favor clarity, direct actions, and one reliable direction.
- Adrian already understands much of the case history and needs help with legwork, organization, continuity, and retrieval.
- The system must reduce cognitive load rather than requiring Adrian to operate complex technical machinery.
- Adrian needs both digital retrieval and eventual physical binder coordination.
- Time is material because the case is progressing toward trial.

---

## 6. Problem Solved

### Present problem

Adrian has a high-volume litigation record spread across:

- Gmail;
- attorney-provided ZIP archives;
- MyCase materials;
- court filings;
- financial documents;
- PDFs;
- Word documents;
- spreadsheets;
- parenting-app records;
- images;
- audio;
- video;
- Notion material;
- local folders;
- former-counsel records.

The material is not yet comprehensively inventoried, normalized, classified, or searchable in one operational system.

### Current workaround

Adrian currently relies on a mixture of:

- personal memory;
- Gmail search;
- Windows folders;
- ZIP archives;
- manually created Markdown;
- Notion records;
- NotebookLM;
- AI Studio prototypes;
- physical records;
- recollection of communications and events.

### Practical friction

- The full record cannot be accounted for quickly.
- Important attachments may be separated from the email or communication that references them.
- Complete conversation context may be difficult to reconstruct.
- Opposing, operator, former-counsel, court, and authority materials risk becoming mixed.
- Search results may expose only isolated excerpts rather than the full source context.
- Trial preparation cannot reliably depend on material that has not been ingested.
- Downstream financial analysis and courtroom retrieval remain incomplete while the source record is fragmented.

### Cost

- substantial manual time;
- duplicated effort;
- risk of overlooked evidence;
- risk of incomplete preparation;
- inability to retrieve supporting material under pressure;
- increased cognitive load;
- risk of building higher-level intelligence on incomplete inputs.

### Desired ending condition

The North Star: Adrian never again has to wonder whether he has a document, where it came from, which version is correct, where the original is, which issue it supports, or whether he can find it in under 10 seconds.

---

## 7. Core Value

The workstation replaces a major portion of the manual labor normally performed by:

- a litigation file clerk;
- a document-processing assistant;
- an evidence organizer;
- a trial binder assistant;
- a paralegal performing first-pass classification.

Its direct value is not autonomous legal analysis.

Its direct value is:

- completeness;
- preservation;
- organization;
- traceability;
- searchability;
- faster review;
- lower cognitive load;
- faster retrieval.

The workstation creates the trusted factual foundation required by every later workstation in the parent ecosystem.

---

## 8. First Usable Version

Everything in this section is implementation of the one-sentence mission, not additional mission. The success condition remains: every source preserved, every file searchable, nothing lost.

### Required Now

- Multi-file upload
- ZIP archive import
- PDF support
- DOCX support
- TXT support
- CSV support
- XLSX support
- EML support
- JPG, JPEG, PNG, and TIFF registration
- Preserved local source storage
- SHA-256 integrity checkpoint
- Available text extraction
- Available metadata extraction
- Durable Proof Object ID
- Duplicate detection
- SQLite registry
- Review and Classification Queue
- Bulk classification
- Separate source repositories
- Repository Explorer
- Universal Search
- Original-source retrieval
- Persistent state across application restarts
- Registry export
- Processing-error report

### Useful Later

- Gmail direct ingestion
- MSG parsing
- MyCase-specific importer
- Parenting-app-specific importer
- Notion export importer
- OCR for image-only documents
- Audio transcription
- Video transcription
- Thread reconstruction across multiple source types
- Physical binder mapping
- Financial issue association
- Communication Intelligence handoff
- Relationship mapping
- Event-centered preparation
- Courtroom Retrieval handoff

### Do Not Build Yet

- PatternEchoAI integration
- predictive legal strategy
- autonomous contradiction findings
- autonomous admissibility decisions
- automated credibility determinations
- semantic graph animation
- confidence scoring
- judicial-outcome prediction
- advanced trial scoring
- complex parenting analysis
- the parent ecosystem or any other workstation
- commercial SaaS administration
- multi-tenant customer management

---

## 9. Required User and Operator Journey

1. Adrian opens the Evidence Intake Workstation.
2. Adrian chooses an acquisition source:
   - multiple files;
   - folder where supported;
   - ZIP archive;
   - later, Gmail or another connector.
3. Adrian chooses or confirms the source repository:
   - Operator;
   - Opposing;
   - Former Counsel;
   - Court;
   - Authority;
   - Unassigned.
4. The system:
   - copies the source into preserved storage;
   - retains the original filename and source path;
   - calculates SHA-256;
   - detects duplicates;
   - extracts supported text;
   - records available metadata;
   - creates a Proof Object;
   - records failures without losing the source;
   - places the record in the Review Queue.
5. Adrian reviews suggested facts and classifications:
   - document type;
   - repository;
   - source collection;
   - detected people;
   - detected date;
   - topic;
   - review status;
   - operator notes.
6. Adrian accepts, edits, or bulk-applies classifications.
7. The approved record appears in the Repository Explorer.
8. Adrian searches by:
   - filename;
   - phrase;
   - person;
   - date;
   - source;
   - file type;
   - repository;
   - topic.
9. Search results show:
   - source identity;
   - factual text preview;
   - repository;
   - metadata;
   - extraction status;
   - review status;
   - direct action to open the preserved original.
10. The system preserves:
    - the original source;
    - Proof Object record;
    - hash;
    - extraction result;
    - classification history;
    - operator notes;
    - errors;
    - source-retrieval path.
11. Adrian continues loading the case while later workstations are built against the same trusted repository.

---

## 10. Required Capabilities

| Capability | Status |
| --- | --- |
| Evidence Intake screen | EXPLICITLY APPROVED |
| Multi-file upload | EXPLICITLY APPROVED |
| ZIP import | EXPLICITLY APPROVED |
| Source preservation | EXPLICITLY APPROVED |
| SHA-256 integrity checkpoint | EXPLICITLY APPROVED |
| Proof Object registration | EXPLICITLY APPROVED |
| Review and Classification Queue | EXPLICITLY APPROVED |
| Repository Explorer | EXPLICITLY APPROVED |
| Universal Search | EXPLICITLY APPROVED |
| Original-source retrieval | EXPLICITLY APPROVED |
| SQLite persistence | SUPPORTED BY SESSION STRATEGY |
| Local filesystem evidence storage | SUPPORTED BY SESSION STRATEGY |
| Operator repository | EXPLICITLY APPROVED |
| Opposing repository | EXPLICITLY APPROVED |
| Former Counsel repository | EXPLICITLY APPROVED |
| Court repository | EXPLICITLY APPROVED |
| Authority repository | EXPLICITLY APPROVED |
| Unassigned repository | SUPPORTED BY SESSION STRATEGY |
| Duplicate detection | SUPPORTED BY SESSION STRATEGY |
| Registry export | SUPPORTED BY SESSION STRATEGY |
| Error report | SUPPORTED BY SESSION STRATEGY |
| Bulk classification | SUPPORTED BY SESSION STRATEGY |
| PDF text extraction | SUPPORTED BY SESSION STRATEGY |
| DOCX text extraction | SUPPORTED BY SESSION STRATEGY |
| XLSX/CSV extraction | SUPPORTED BY SESSION STRATEGY |
| EML parsing | SUPPORTED BY SESSION STRATEGY |
| Image registration | SUPPORTED BY SESSION STRATEGY |
| Gmail direct ingestion | CANDIDATE |
| MSG parsing | CANDIDATE |
| OCR | DEFERRED |
| Audio transcription | DEFERRED |
| Video transcription | DEFERRED |
| Physical binder mapping | DEFERRED |
| Financial Analysis Workstation handoff | DEFERRED |
| Communication Intelligence Workstation handoff | DEFERRED |
| Courtroom Retrieval Workstation handoff | DEFERRED |
| Relationship graph | DEFERRED |
| PatternEchoAI integration | DEFERRED |
| Automatic legal conclusions during intake | REJECTED OR SUPERSEDED |
| Synthetic evidence in live mode | REJECTED OR SUPERSEDED |
| Browser localStorage as primary evidence store | REJECTED OR SUPERSEDED |
| Confidential evidence in GitHub | REJECTED OR SUPERSEDED |

"EXPLICITLY APPROVED" statuses are carried from the committed source extraction record, which documents the originating strategy session's explicit human decisions.

### Screens or surfaces

- Evidence Intake
- Review Queue
- Repository Explorer
- Universal Search

### Workflows

- Acquisition
- Preservation
- Hashing
- Extraction
- Registration
- Review
- Classification
- Search
- Retrieval
- Export
- Error review

### Data and content inputs

- PDF, DOCX, TXT, CSV, XLSX, EML, JPG, JPEG, PNG, TIFF, ZIP
- source paths and collection labels
- operator-entered classifications and notes

### Outputs

- preserved source file;
- Proof Object;
- extracted text or companion file;
- metadata record;
- duplicate status;
- review-queue entry;
- searchable registry;
- search result;
- registry export;
- processing-error report.

### Automations

- hashing;
- MIME/type detection;
- duplicate detection;
- supported extraction;
- Proof Object ID assignment;
- review-queue creation;
- search indexing.

### Integrations

- Local filesystem: required
- SQLite: required
- Gmail: candidate for later or parallel implementation only if it does not delay local intake
- GitHub: code and configuration only
- Google AI Studio: prototype/build environment
- Fable 5: proposed implementation processor

### Processor roles

- Acquisition processor
- Preservation processor
- Hashing processor
- Extraction processor
- Registration processor
- Classification-suggestion processor
- Search-index processor

Processors may not make final legal conclusions. Every processor receives the bounded workstation mission, never an ecosystem mission.

### Administrative controls

- source repository assignment;
- source collection assignment;
- review status;
- bulk classification;
- export;
- backup path;
- error review.

### Review and approval

- Suggested classifications require operator confirmation.
- Legal significance is not determined at intake.
- Failed extraction does not invalidate or delete a preserved source.

### Evidence and proof

- Original source is preserved.
- SHA-256 records the acquired bytes as an integrity checkpoint.
- The hash does not itself prove authorship, truth, historical authenticity, or admissibility.
- Every derived record must trace back to the preserved source.

### Reporting

- import summary;
- item counts;
- duplicate count;
- extraction success count;
- extraction failure count;
- unsupported-file report;
- registry export.

---

## 11. Existing Assets and Source Material

### AdrianTRUFiT/Evidence-Intake-Worstation (dedicated project repository)

- Asset type: GitHub repository
- Known location: https://github.com/AdrianTRUFiT/Evidence-Intake-Worstation
- Purpose: Dedicated governed project repository, initialized from the universal governed project template; holds this extraction at `intake/SESSION_EXTRACTION.md`
- Verification status: VERIFIED REPOSITORY — LOCATION KNOWN (inspected directly in this session)
- Relevance: Current home of the project's intake record. Contents at extraction time: `README.md` (template title "universal-governed-project-template"), `START_HERE.md` (bootstrap placeholder), `bootstrap.txt` (bootstrap marker), `governance/AUTHORITY_MODEL.md`, `governance/MISSION.md` (unfilled placeholder), `intake/SESSION_EXTRACTION.md`. Note: the repository name is misspelled "Worstation" (missing "k"). No application code is present.

### Committed source extraction record

- Asset type: Project-truth document (originally titled "SESSION EXTRACTION — LAWAIDAI EVIDENCE INTAKE WORKSTATION")
- Known location: `intake/SESSION_EXTRACTION.md` in AdrianTRUFiT/Evidence-Intake-Worstation (superseded in place by this revision; prior versions remain in git history at commits `f808e80` and `2c8a4e9`)
- Purpose: Governing record of the originating strategy session — decisions, capabilities, constraints, acceptance criteria
- Verification status: VERIFIED ARTIFACT — LOCATION KNOWN (read directly in this session)
- Relevance: Primary source for the project truth carried into this document. Its LawAidAI-first identity framing is superseded by this session's explicit identity decision.

### Evidence Intake Workstation — Governed Project Workspace (Notion)

- Asset type: Notion governed project workspace
- Known location: https://app.notion.com/p/39bfbe4423dd80a5a886de5b5626b9b2 (under parent page "SoulHubⓈ")
- Purpose: The project's governance environment — Control Center, Source Register, Decision/HOLD Ledger, Architecture Register, Work Orders, Processor Registry, Activation Packets, Proof Records, Handoffs, Assets, Context Index. Division of authority (human-accepted, this session): GitHub owns implementation; Notion owns governance; the session extraction connects the two.
- Verification status: VERIFIED ARTIFACT — LOCATION KNOWN (inspected directly in this session)
- Relevance: Duplicated and renamed for this project, but every Control Center record still carries Status "Template" with placeholder values, and the Source Register contains only template rows — the GitHub extraction file has not been registered. Initialization is incomplete.

### Universal Project Foundry Knowledge Base

- Asset type: Notion doctrine and template library
- Known location: https://app.notion.com/p/42faa94b7ed14b07b2ec60fcb117d7a1 (linked from the workspace shell and pre-registered in the Source Register)
- Purpose: Reusable governance doctrine referenced by every governed project
- Verification status: VERIFIED ARTIFACT — LOCATION KNOWN (link confirmed in this session; contents not reviewed)
- Relevance: Governs process, not project-specific truth; must not be duplicated into the project

### AdrianTRUFiT/my-lawaid-ai

- Asset type: GitHub repository
- Known location: https://github.com/AdrianTRUFiT/my-lawaid-ai
- Purpose: Per the source extraction record, the intended permanent source repository for a fresh LawAidAI build
- Verification status: VERIFIED REPOSITORY — LOCATION KNOWN (per the committed source extraction record; not re-inspected in this session)
- Relevance: The source record directed the v1.0 build into this repository. This session's workstation-architecture decision (independent workstations, bounded missions) points instead toward the dedicated workstation repository; explicit human confirmation of the code repository of record is still required (see Section 16). my-lawaid-ai remains a parent-ecosystem asset.

### AdrianTRUFiT/universal-governed-project-template

- Asset type: GitHub template repository
- Known location: https://github.com/AdrianTRUFiT/universal-governed-project-template
- Purpose: Governed project initialization template
- Verification status: VERIFIED REPOSITORY — LOCATION KNOWN (per the source extraction record; corroborated in this session by the dedicated repository's README, which carries the template's title)
- Relevance: Structural basis of the dedicated project repository

### LawAidAI Operating Environment deck

- Asset type: Visual architecture deck (PDF, "LawAidAI_Operating_Environment(1).pdf")
- Known location: Uploaded in the originating strategy session; not present in the dedicated repository or verified elsewhere in this session
- Verification status: EXISTS AS SESSION KNOWLEDGE — ARTIFACT LOCATION UNVERIFIED
- Relevance: Visual reference for the parent ecosystem; this workstation's scope stays bounded far below the deck's full scope

### AI Studio prototype (parent-ecosystem interfaces)

- Asset type: Application prototype
- Known location: Google AI Studio project; exact persistent project URL and repository linkage UNKNOWN
- Purpose: Demonstrated Command Center, navigation, repository separation, intake concepts, financial folders, trial milestones, and binder mapping
- Verification status: CLAIMED BUT UNVERIFIED
- Relevance: Useful visual and interaction references; must not be assumed to contain production-ready intake

### Evidence Factory / Gmail prototype

- Asset type: Prototype capability
- Known location: Prior AI Studio build; exact location UNKNOWN
- Purpose: Demonstrated Gmail OAuth, message parsing, Proof Object concepts, communication navigation, and graph ideas
- Verification status: CLAIMED BUT UNVERIFIED
- Relevance: May provide reusable ideas; simulated fallback data and browser-local persistence were identified as unacceptable for production evidence intake

### Doctrine and NotebookLM knowledge base

- Asset type: Research and operating doctrine
- Known location: NotebookLM; exact notebook and export location UNKNOWN
- Purpose: Iterative architecture, Florida family-law research, trial preparation, evidence doctrine, and system principles
- Verification status: EXISTS AS SESSION KNOWLEDGE — ARTIFACT LOCATION UNVERIFIED
- Relevance: Supports parent-ecosystem context; must not expand this workstation into open-ended doctrine or legal reasoning

### Case Acquisition Workstation sample script

- Asset type: Python prototype code
- Known location: Appeared in the originating strategy session; repository/file location UNKNOWN
- Purpose: Demonstrated directory setup, SHA-256 hashing, CSV inventory, Markdown stubs, and error logging
- Verification status: EXISTS AS SESSION KNOWLEDGE — ARTIFACT LOCATION UNVERIFIED
- Relevance: Candidate logic reference; not established as the current implementation

### Universal Session-to-Build Extraction Instruction

- Asset type: Project-extraction instruction
- Known location: Embedded in the Notion workspace pages "00 — START HERE — Project Initialization" and "05 — Universal Session Extraction Prompt"; also supplied verbatim in this session
- Verification status: VERIFIED ARTIFACT — LOCATION KNOWN
- Relevance: Governs this document's structure and evidentiary distinctions. The North Star section was added on explicit human direction and is a permanent project-specific addition to that structure.

---

## 12. Existing Project State

### Confirmed Existing Artifacts

- Dedicated GitHub repository AdrianTRUFiT/Evidence-Intake-Worstation, initialized from the universal governed project template, containing bootstrap/governance placeholders and this extraction (`intake/SESSION_EXTRACTION.md`), with branches `main` and `claude/session-extraction-instructions-qvfjfr`
- Dedicated Notion workspace "Evidence Intake Workstation — Governed Project Workspace" containing the operating scripts (00 START HERE, 01 Onboarding, 02 Repository Bootstrap, 03 Check-Out and Handoff, 05 Universal Session Extraction Prompt) and eleven governance databases (Project Control Center, Source Register, Decision/Governance/HOLD Ledger, Architecture and Requirements Register, Build Phases and Work Orders, Team and Processor Registry, Worker Activation Packets, Runtime/Tests/Proof Records, Handoffs and Closure Records, Assets and Output Routing, Context Index)
- The committed source extraction record documenting the originating strategy session (per that record: verified my-lawaid-ai repository and README, LawAidAI Operating Environment PDF deck, universal governed project template repository, AI Studio interface screenshots, and session-developed Proof Object / intake / repository / search / workflow specifications)

### Approved Doctrines and Decisions

Decided directly in this session:

- The project identity is the Evidence Intake Workstation; LawAidAI is the parent ecosystem, not the project.
- The first-build mission is one sentence: import every case document into one governed repository where every source is preserved, every file is searchable, and nothing is lost.
- The North Star (Section above) is the permanent acceptance philosophy for every feature.
- The architecture is independent workstations, each with one job, orchestrated by LawAidAI.
- GitHub owns implementation; Notion owns governance; the session extraction connects the two.

Carried from the committed source extraction record:

- Document intake is the most important first station.
- The Evidence Intake Workstation is the highest immediate build priority.
- The system performs legwork; Adrian retains judgment.
- Preserve sources before interpretation.
- Source repositories remain separate.
- Financial preparation is the primary broader case focus.
- Parenting material remains available but may be deprioritized.
- The default interface should be simple, accessible, and action-oriented.
- Intake must not make autonomous legal conclusions.
- Confidential evidence must not be committed to GitHub.
- Local persistent storage is required for evidence.
- Browser localStorage must not be the primary evidence store.

Active through the workspace shell: Notion defines intended mission knowledge; repository evidence proves implementation; runtime and test proof establish what works; human authorization determines what becomes real; generated output remains candidate until authorized.

### Specified but Not Built

- Full local Evidence Intake pipeline
- Review and Classification Queue
- SQLite registry
- Durable Proof Object implementation
- Duplicate detection
- Mixed-file text extraction
- Repository Explorer
- Universal Search
- Source-file opening
- End-to-end ZIP import
- Registry export
- Error report

### Implemented but Unverified

(per the source extraction record; described or shown in the originating session without runtime, code, or persistence verification)

- AI Studio upload interface
- Gmail OAuth prototype
- Gmail message parsing
- Communication Intelligence prototype
- Case Intelligence Graph prototype
- Repository-separation prototype
- Binder-mapping interface
- Courtroom Retrieval interface
- Financial-folder interface

### Working and Verified

No dedicated working and verified runtime was established in this session.

(The source extraction record notes that the separate PatternEchoAI runtime has verified milestone tests, but it is a downstream pattern-memory workstation and does not satisfy document intake.)

### Incomplete or Defective

- The dedicated repository name is misspelled "Evidence-Intake-Worstation" (missing "k"), inconsistent with the project name used everywhere else.
- `governance/MISSION.md` in the dedicated repository is an unfilled template placeholder. The one-sentence mission decided in this session is the natural content for it, pending initialization.
- The Notion workspace's Project Control Center records all carry Status "Template" with placeholder values; the Source Register contains only template rows; the GitHub extraction file is not registered in the Source Register — the START HERE initialization sequence is unfinished.
- Per the source record: earlier prototypes contained synthetic case data; some relied on browser-local persistence; simulated Gmail fallback records were identified as an evidence-contamination risk; some interfaces overstated authentication, immutability, readiness, or legal confidence; intake has not been proven against a real 25-file mixed set and ZIP archive; search and preserved-source reopening have not been proven end to end; AI Studio project/repository synchronization is uncertain.

### Missing

- Human confirmation of the code repository of record (see Section 16)
- Registration of the GitHub extraction file in the Notion Source Register
- Populated Project Control Center (identity, mission, current state, repository state, runtime state, next action)
- Confirmed local evidence-storage root
- Confirmed laptop and home-base path alignment
- Working extraction libraries
- Working SQLite schema
- Verified import manifest
- Verified duplicate handling
- Verified restart persistence
- Verified registry export
- Verified error report
- Verified search index
- Verified source-opening behavior
- Confirmed deployment/runtime instructions

### Rejected or Superseded

- Framing the project as "build LawAidAI" — superseded in this session by the bounded workstation identity
- The project name "LawAidAI Evidence Intake Workstation" as primary identity — superseded by "Evidence Intake Workstation"
- Building PatternEchoAI before the Evidence Intake foundation
- Treating animated relationship graphs as the first priority
- Legal classification during acquisition
- Synthetic data fallback in live evidence mode
- Browser localStorage as primary evidence custody
- Treating SHA-256 as proof of historical authenticity or legal admissibility
- Autonomous legal conclusions
- Building the entire parent ecosystem as the first milestone

---

## 13. Approved Decisions and Corrections

### Decisions made directly in this session

#### Decision: The project is the Evidence Intake Workstation; LawAidAI is the parent ecosystem, not the project

- Authority status: EXPLICIT HUMAN DECISION (this session)
- Replaced or corrected: The LawAidAI-first identity framing carried in the source extraction record
- Consequence: Every future processor receives a bounded workstation mission ("I'm building one workstation"), never an ecosystem mission ("I'm building a litigation operating system"). This is the primary scope-drift control.

#### Decision: The first-build mission is one sentence

- Authority status: EXPLICIT HUMAN DECISION (this session)
- The mission: "Import every case document into one governed repository where every source is preserved, every file is searchable, and nothing is lost."
- Replaced or corrected: Expressing the mission as dozens of enumerated capabilities
- Consequence: All capability lists in this document are implementation beneath one crystal-clear success condition usable by any implementation processor (Claude Code, Codex, Gemini, Fable, or others).

#### Decision: The North Star is the permanent acceptance philosophy

- Authority status: EXPLICIT HUMAN DECISION (this session)
- Replaced or corrected: Feature-by-feature justification without a unifying acceptance test
- Consequence: Every current and future feature is measured against the six North Star questions (Section "North Star").

#### Decision: The architecture is independent workstations orchestrated by LawAidAI

- Authority status: EXPLICIT HUMAN DECISION (this session)
- Named workstations: Evidence Intake Workstation, Financial Analysis Workstation, Communication Intelligence Workstation, Courtroom Retrieval Workstation, PatternEchoAI (pattern-memory runtime)
- Replaced or corrected: Building one monolithic AI system
- Consequence: Each workstation is built, tested, verified, and used independently while fitting the larger system; only the Evidence Intake Workstation is in scope for this project.

#### Decision: GitHub owns implementation; Notion owns governance; the session extraction connects the two

- Authority status: HUMAN-ACCEPTED REFINEMENT (this session)
- Replaced or corrected: Maintaining parallel, separately edited project records
- Consequence: `intake/SESSION_EXTRACTION.md` in GitHub is the single authoritative extraction; Notion links to it and tracks its status.

### Decisions carried from the committed source extraction record

#### Decision: Document intake is the most important first station

- Authority status: EXPLICIT HUMAN DECISION
- Replaced or corrected: Earlier emphasis on relationship graphs, PatternEchoAI, courtroom retrieval, and broader intelligence before complete acquisition
- Consequence: The Evidence Intake Workstation is the immediate build priority

#### Decision: Build for Adrian's actual pro se use

- Authority status: EXPLICIT HUMAN DECISION
- Replaced or corrected: Generic legal-tech product and hypothetical external-user framing
- Consequence: UX, workflow, and scope must optimize for Adrian's preparation, accessibility, and trial pressure

#### Decision: Focus broader case preparation primarily on financial issues

- Authority status: EXPLICIT HUMAN DECISION
- Replaced or corrected: Equal emphasis on parenting, financial, credibility, communication, and every possible family-law issue
- Consequence: Parenting evidence remains preserved and searchable but is not the center of the first issue-focused build

#### Decision: Preserve separate perspective/source repositories

- Authority status: EXPLICIT HUMAN DECISION
- Replaced or corrected: Simple "my evidence versus opposing evidence" or one merged case repository
- Consequence: Operator, Opposing, Former Counsel, Court, and Authority source identities must remain intact

#### Decision: AI assists; Adrian decides

- Authority status: EXPLICIT HUMAN DECISION
- Replaced or corrected: Autonomous legal analysis, final contradiction findings, credibility decisions, or courtroom strategy generation
- Consequence: Classification suggestions require review; intake remains mechanical and factual

#### Decision: Simplicity, flow, and accessibility take priority

- Authority status: EXPLICIT HUMAN DECISION
- Replaced or corrected: Growing layers of doctrine, complex graph modes, excessive synchronization, scores, and feature-heavy dashboards
- Consequence: First build is limited to four core screens and one complete intake-to-search flow

#### Decision: An 80% useful system now is preferable to a perfect future platform

- Authority status: EXPLICIT HUMAN DECISION
- Replaced or corrected: Production-platform perfection before case use
- Consequence: The first build must be usable quickly while preserving core evidence safety and traceability

#### Decision: Initialize the Evidence Intake Workstation as its own governed project

- Authority status: HUMAN-ACCEPTED REFINEMENT (evidenced by the created dedicated repository, the committed extraction, and the duplicated, renamed Notion workspace; reinforced by this session's identity decision)
- Replaced or corrected: Leaving the project only as a section of the broader planning session
- Consequence: The project has a dedicated governed repository and workspace; initialization must be finished there before any work order is authorized

#### Decision: Use Fable 5 and the universal template to construct the intake system

- Authority status: SESSION STRATEGY — REQUIRES HUMAN AUTHORIZATION
- Consequence: The project-creation system may prepare an authorized build package after initialization

#### Decision: Use React/TypeScript, FastAPI, SQLite, and local filesystem

- Authority status: HUMAN-ACCEPTED REFINEMENT
- Replaced or corrected: Browser-only AI Studio prototype architecture
- Consequence: The first build should use a local persistent full-stack architecture unless initialization reveals an existing approved template constraint

---

## 14. Constraints and Protected Boundaries

### Scope

- This project is one workstation: evidence intake, review, repository, search, and retrieval.
- Do not expand the first build into the parent ecosystem or any other workstation.
- Do not block local file intake on Gmail.
- Do not start PatternEchoAI integration.
- Do not build advanced reasoning before the record is captured.
- Every feature must serve the North Star's six questions.

### Time

- Trial preparation is approaching.
- The workstation must become usable as quickly as practical.
- A bounded, complete first version is preferable to a large incomplete system.

### Privacy and security

- Divorce and family-law records are confidential.
- Evidence must not be committed to a public GitHub repository.
- GitHub stores code, configuration, documentation, and tests only.
- Evidence belongs in local governed storage.
- Secrets and OAuth credentials must not be committed.
- Source and derived files must remain distinguishable.

### Evidence safety

- Preserve original source files.
- Derived text may not replace the source.
- SHA-256 is an integrity checkpoint, not proof of authorship or admissibility.
- Failed extraction must not destroy or reject the source.
- Synthetic records must never enter live evidence repositories.
- Every result must retain source provenance.

### Ownership

- Adrian remains the project owner and consequence authority.
- Adrian remains responsible for legal judgment.
- Court decisions remain with the judge.

### Platform use and governed-process boundaries

- Dedicated governed repository: AdrianTRUFiT/Evidence-Intake-Worstation (extraction record and governance shell).
- GitHub owns implementation; Notion owns governance; the session extraction connects the two. Two separately edited full copies of the extraction must not be maintained.
- Per the workspace's START HERE rule: after the extraction is saved in GitHub and registered in Notion, stop — do not create a work order, assign a processor, or begin the build until authorized.
- Fable 5 may build the application only after authorization.
- AI Studio prototypes are references, not automatically the production runtime.
- Universal governance, work-order, proof, and handoff systems already exist in the workspace shell and Foundry Knowledge Base; they must not be recreated per-project.

### Local-first requirements

- Local filesystem for evidence
- SQLite for registry and search state
- Persistent operation across restarts
- Ability to work without permanent cloud availability
- No primary reliance on browser localStorage

### Visual direction

- Light, warm, neutral interface
- Calm and professional
- Minimal cognitive load
- No dark cosmic interface
- Clear typography
- No fabricated readiness scores
- No visual effects that compete with use

### Naming and terminology

- Evidence Intake Workstation (the project)
- LawAidAI (parent-ecosystem name only — never the name of this project)
- Proof Object
- Review and Classification Queue
- Repository Explorer
- Universal Search
- Operator, Opposing, Former Counsel, Court, Authority, Unassigned
- Workstation family names: Financial Analysis Workstation, Communication Intelligence Workstation, Courtroom Retrieval Workstation, PatternEchoAI

### Prohibited actions

- autonomous legal conclusions;
- autonomous admissibility determinations;
- fabricated evidence;
- evidence committed to GitHub;
- source alteration;
- repository merging;
- hidden legal classification at intake;
- claiming a runtime works without tests;
- claiming full implementation based on screenshots;
- allowing unsupported files to disappear silently;
- expanding a processor's mission from workstation to ecosystem.

---

## 15. Business or Value Model

### Intended value

The first value event is operational: Adrian successfully imports and searches his own litigation record.

### Beneficiary

- Adrian, as the self-represented operator

### Buyer

- Not applicable to the first build
- Future external buyer: UNKNOWN

### Smallest value event

A mixed folder and ZIP archive are imported; all originals are preserved; records enter review; a phrase search retrieves the correct document and opens the source.

### Pricing

UNKNOWN

### Commercial model

UNKNOWN

### Contribution to larger ecosystem

The workstation becomes the trusted factual input layer for the other workstations: Financial Analysis, Communication Intelligence, Courtroom Retrieval, PatternEchoAI, and future governed evidence and decision-support systems orchestrated by LawAidAI.

---

## 16. Unknowns, Contradictions, and Human Decisions Needed

### Unknowns

- Final confirmation of the code repository of record (see Contradictions)
- Whether the misspelled repository name "Evidence-Intake-Worstation" should be renamed or kept
- Exact local root path for the production evidence store
- Whether the first operational build will run on the laptop, home-base desktop, or both
- Whether the dedicated repository should receive the full universal template contents (its current files are minimal bootstrap placeholders)
- Exact Fable 5 access and write permissions
- Whether Gmail ingestion is included in v1.0 or immediately follows local intake
- Exact supported OCR library
- Exact MSG parsing feasibility
- Whether image metadata extraction is required in v1.0
- Exact backup destination
- Exact registry-export format beyond CSV or JSON
- Whether the first interface must reuse current AI Studio visual components
- Exact amount and structure of the initial real test dataset

### Contradictions

1. Repository of record: the committed source extraction directed the v1.0 build inside AdrianTRUFiT/my-lawaid-ai, while the project-creation flow created the dedicated repository AdrianTRUFiT/Evidence-Intake-Worstation. This session's workstation-architecture decision (each workstation built, tested, and verified independently) points toward the dedicated workstation repository, but the human has not explicitly named the code repository of record, so this is recorded rather than silently resolved.
2. Gmail: earlier discussion treated Gmail as the most important communication backbone, while the bounded first build must not allow Gmail to delay local intake. Resolution recorded for initialization: local intake is required; Gmail remains candidate or parallel work only.
3. Proof Object scope: earlier concepts described every artifact as a Proof Object; later corrections distinguished people, findings, deadlines, and issues from Proof Objects. Current rule: source artifacts become Proof Objects; abstract concepts do not.
4. Hash meaning: earlier prototypes described hashes as immutability or authentication. Current rule: SHA-256 is an integrity checkpoint only.
5. Intake reasoning: earlier prototypes included automated legal mapping during ingestion. Current rule: intake may suggest factual classifications but must not make final legal conclusions.
6. Build scope: earlier direction asked AI Studio to build the complete system from A to Z. Superseded twice — first by narrowing to Evidence Intake v1.0, then by this session's identity decision that the project is one workstation, full stop.

Resolved this session (recorded for the ledger): the naming contradiction between "LawAidAI Evidence Intake Workstation" and "Evidence Intake Workstation" was resolved by explicit human decision in favor of "Evidence Intake Workstation".

### Human Decisions Required Before Initialization

Completing the remaining initialization steps (registering the extraction in the Notion Source Register and populating the Project Control Center) requires no new decision. Before the first build work order is authorized, the human must confirm:

- The code repository of record: AdrianTRUFiT/Evidence-Intake-Worstation (consistent with the workstation-architecture decision) or AdrianTRUFiT/my-lawaid-ai (as stated in the source record).

### Human Decisions That Can Wait Until Build Planning

- Repository rename to correct the "Worstation" spelling
- Exact local evidence-storage path
- Exact frontend visual reuse
- Gmail inclusion timing
- OCR library
- MSG support
- Backup destination
- Export format
- First real test corpus

---

## 17. Material Risks

1. Scope drift — the build could expand from one workstation into the parent ecosystem, graphs, pattern analysis, or courtroom reasoning before intake is usable. The bounded workstation identity and one-sentence mission exist specifically to prevent this.
2. Confidential-evidence exposure — actual case evidence could be placed in a GitHub repository or transmitted into an inappropriate cloud environment.
3. False completeness — a polished UI could be accepted without real persistence, extraction, search, and original-source retrieval.
4. Source/provenance loss — derived text could replace originals, repository/source identity could be lost, or unsupported files, ZIP nesting, duplicates, and extraction failures could disappear silently and undermine trust in the inventory ("nothing is lost" is the mission's hardest guarantee).
5. Governed-record split-brain — with two candidate repositories (Evidence-Intake-Worstation and my-lawaid-ai) and an unregistered Notion workspace, project truth could fork across locations, defeating the round-trip-integrity and no-rediscovery doctrine.

---

## 18. Success Definition

### Governing philosophy

The North Star: when this workstation is complete, Adrian should never again have to wonder whether he has a document, where it came from, which version is correct, where the original is, which issue it supports, or whether he can find it in under 10 seconds. Every acceptance judgment traces back to these six questions.

### First-version accomplishment

The first version must fulfill the mission for a real mixed set of litigation files: every source preserved, every file searchable, nothing lost — as persistent, reviewable Proof Objects.

### Observable user success

Adrian can:

- import a real folder or multi-file set;
- import a ZIP archive;
- see every source accounted for;
- review and classify records;
- search by phrase, person, date, filename, and repository;
- open the preserved original;
- restart and retain all work.

### Observable operator success

Adrian no longer needs to rely primarily on memory, Gmail browsing, or scattered folders to locate a known record.

### Acceptance criteria

1. Import at least 25 mixed files.
2. Import at least one ZIP archive.
3. Preserve every original.
4. Generate SHA-256 for every preserved source.
5. Extract searchable text where supported.
6. Create one durable Proof Object per unique source.
7. Detect duplicate sources.
8. Place all new items in the Review Queue.
9. Classify items across separate repositories.
10. Support bulk classification.
11. Search by phrase.
12. Search by person.
13. Search by date.
14. Search by filename.
15. Open the preserved original from the result.
16. Persist all state across restart.
17. Export the registry.
18. Produce a visible error report for unsupported or failed files.
19. Keep confidential test evidence outside GitHub.
20. Demonstrate that no synthetic evidence appears in live mode.

### Required evidence

- test output;
- import manifest;
- database persistence proof;
- sample registry export;
- duplicate-handling proof;
- search-result proof;
- original-source-opening proof;
- restart-persistence proof;
- error report;
- commit SHA for code;
- confirmation that test evidence was not committed.

### Conditions meaning the project is not ready

- intake is only a visual mock;
- files disappear after restart;
- search does not index extracted content;
- originals cannot be reopened;
- source repository is lost;
- synthetic data enters live mode;
- evidence is stored in GitHub;
- failures are silent;
- duplicate handling is absent;
- the system claims legal conclusions during intake.

---

## 19. Recommended First Build Objective

Build and verify Evidence Intake Workstation v1.0 — mission: import every case document into one governed repository where every source is preserved, every file is searchable, and nothing is lost — inside the repository the human confirms as the code repository of record (see Section 16), implemented as one complete local workflow for mixed-file and ZIP acquisition, source preservation, SHA-256 integrity checkpoints, supported text extraction, durable Proof Object registration, review and classification, repository browsing, universal search, and original-source retrieval, meeting the twenty acceptance criteria in Section 18 and answering the six North Star questions.

Do not expand the first build beyond this objective. Do not expand any processor's mission from workstation to ecosystem.

---

## 20. Source Session Record

### Main session materials used

- The committed source extraction record at `intake/SESSION_EXTRACTION.md` in AdrianTRUFiT/Evidence-Intake-Worstation, which documents the originating strategy session covering operating doctrine, pro se litigation-preparation needs, Florida family-law context, evidence preservation, Gmail as communication history, Proof Objects, perspective/source repositories, AI Studio prototypes, the universal governed template, Fable 5 build capability, PatternEchoAI sequencing, financial-case focus, courtroom retrieval, binder coordination, and the urgent need for document intake
- Direct inspection of the dedicated GitHub repository (file tree, git history, branch state)
- Direct inspection of the Notion workspace "Evidence Intake Workstation — Governed Project Workspace" (shell page, START HERE initialization script, Project Control Center records, Source Register rows)
- The Universal Session-to-Build Extraction Instruction supplied in this session and embedded in the workspace
- Direct human review and correction of the extraction in this session

### Most important human decisions extracted

From this session directly:

- The project is the Evidence Intake Workstation; LawAidAI is the parent ecosystem, not the project.
- The mission is one sentence: import every case document into one governed repository where every source is preserved, every file is searchable, and nothing is lost.
- The North Star is the permanent acceptance philosophy.
- The architecture is independent workstations, each with one job, orchestrated by LawAidAI.
- GitHub owns implementation; Notion owns governance; the session extraction connects the two.

Carried from the source record:

- Document intake is the most important first station.
- Adrian needs a usable intake system now.
- The system is for Adrian's actual case before it is a product for anyone else.
- AI must support rather than replace Adrian's judgment.
- Financial preparation is the primary broader case focus.
- An 80% useful operational system is preferable to a perfect future platform.

### Strategic conclusions developed

- PatternEchoAI is downstream and must not displace intake.
- The first build contains four primary screens and one complete intake-to-search flow.
- Local files and ZIP archives must be supported before optional connectors delay the build.
- Source preservation, review, and search are more important than graphs or automated reasoning.
- Separate repositories must retain source identity.
- Code lives in GitHub; evidence lives in local storage.
- Initialization must finish in Notion (registration and Control Center population) before any work order is authorized.

### Source limitations

- The originating strategy conversation is not directly available; its decisions are carried from the committed extraction record.
- AdrianTRUFiT/my-lawaid-ai and the universal template repository were not re-inspected in this session.
- The Universal Project Foundry Knowledge Base contents were not reviewed.
- NotebookLM contents and AI Studio source code remain unavailable.
- No verified Evidence Intake runtime or acceptance-test output exists.

### Areas where session history was insufficient

- Explicit confirmation of the code repository of record
- Exact local environment (machine, paths, evidence-storage root) for the first operational build

---

## 21. Initialization Readiness

Project name: Evidence Intake Workstation

Recommended repository name: evidence-intake-workstation
(the existing dedicated repository is AdrianTRUFiT/Evidence-Intake-Worstation, which contains a spelling error; renaming is a human decision)

Recommended Notion workspace name: Evidence Intake Workstation — Governed Project Workspace
(already exists at https://app.notion.com/p/39bfbe4423dd80a5a886de5b5626b9b2)

Project type: Local-first litigation evidence-acquisition, review, repository, and search application — one workstation in a family of independent workstations orchestrated by the LawAidAI parent ecosystem

Extraction status: READY FOR PROJECT INITIALIZATION

Strategy status: SUFFICIENT WITH MARKED UNKNOWNS

Human authorization status: EXPLICITLY AUTHORIZED
(the intake build was authorized in the source record; in this session the human directly set the project identity, one-sentence mission, and North Star, and accepted this extraction as the authoritative initialization document. The first build work order itself remains unauthorized, per the workspace's stop rule.)

Existing dedicated repository: Yes — AdrianTRUFiT/Evidence-Intake-Worstation (governance and intake record only; no application code)

Existing dedicated runtime: No verified dedicated runtime

Primary unresolved decision: Explicit confirmation of the code repository of record (the workstation-architecture decision points to the dedicated repository; the source record named my-lawaid-ai), followed by the exact local evidence-storage root

Recommended next action: Complete the unfinished START HERE initialization steps — register the GitHub link to `intake/SESSION_EXTRACTION.md` in the Notion Source Register, populate the Project Control Center (identity, one-sentence mission, North Star, current state, repository state, runtime state, next action), fill `governance/MISSION.md` with the one-sentence mission, and obtain the human's repository-of-record confirmation — then stop, per the workspace rule, until the first bounded work order for Evidence Intake Workstation v1.0 is authorized.
