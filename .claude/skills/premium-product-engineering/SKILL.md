---
name: premium-product-engineering
description: Reusable premium application engineering layer for high-end functional software. Use when improving a working app, designing a new application, refining mobile UX, creating operator workflows, performing design review, validating user journeys, conducting product QA, or raising an application from technically functional to professional product quality. Works with build-dynamic-web, ui-ux-pro-max, ui-styling, design-system, and brand. Existing repository truth and project governance always outrank this skill.
---

# Premium Product Engineering

## Mission

Turn technically functional software into a professional product.

This skill complements the existing Dynamic Web Builder.

Dynamic Web Builder owns functional construction and browser-operated delivery.

Premium Product Engineering strengthens:

- product definition
- task clarity
- information hierarchy
- mobile product quality
- interaction design
- design-before-build discipline
- functional acceptance
- failure states
- visual consistency
- accessibility
- adversarial QA
- fresh-eyes review
- reusable learning

Do not replace the Dynamic Web Builder.

Do not create a parallel application architecture.

## Governing Principle

Simple outside.
Sophisticated inside.

A feature is not complete because:

- it renders
- it compiles
- it has attractive cards
- controls exist
- a screenshot looks good

It is complete when the intended user can perform the intended job correctly.

## Phase 1 — Inspect

Before implementation:

1. Read project CLAUDE.md and repository governance.
2. Read relevant README and architecture documentation.
3. Inspect the implementation being changed.
4. Inspect existing components and design-system patterns.
5. Identify routes, state, persistence, APIs and data contracts.
6. Identify test/build/proof requirements.
7. Identify safety boundaries.
8. Start the current application when practical.
9. Operate the current workflow before changing it.

Repository truth outranks assumptions.

Never redesign a working system merely because another design is possible.

## Phase 2 — Contract the User Job

Convert the request into a real user workflow.

Example:

OPEN
→ UNDERSTAND
→ ACT
→ CONFIRM
→ CONTINUE

For list-based software:

OPEN LISTS
→ CREATE LIST
→ NAME LIST
→ ADD ITEM
→ OPEN ITEM
→ MOVE / COPY / REMOVE
→ REFRESH
→ VERIFY STATE

For portfolio software:

OPEN PORTFOLIO
→ SEE TOTAL
→ SEE CHANGE
→ SEE POSITIONS
→ OPEN POSITION
→ REVIEW
→ TAKE ALLOWED ACTION

Write the acceptance journey before visual implementation.

## Phase 3 — Product Design Package

For meaningful UI changes, establish:

1. User
2. User job
3. Primary question
4. Primary action
5. Information hierarchy
6. Empty state
7. Populated state
8. Loading state
9. Error/unavailable state
10. Protected/refusal state
11. Mobile behavior
12. Desktop behavior
13. Interaction model
14. Reference lessons
15. Acceptance journey
16. Explicit do-not-build list

Use:

templates/product-engineering/DESIGN_PACKAGE_TEMPLATE.md

Do not begin major visual implementation without knowing what the screen is for.

## Phase 4 — Route to Existing Skills

Use the existing specialized skills rather than duplicating them.

Use UI/UX Pro Max for:

- layout reasoning
- application interface patterns
- typography
- colors
- responsive patterns
- interaction conventions
- framework-specific UX guidance

Use Design System for:

- tokens
- primitives
- semantic states
- component contracts
- variants

Use UI Styling for:

- implementation styling
- Tailwind
- shadcn
- accessibility details
- component treatment

Use Brand for:

- identity
- visual language
- typography
- messaging
- consistency

Use Dynamic Web Builder for:

- real implementation
- routes
- state
- persistence
- data
- validation
- browser operation
- tests
- build
- Git delivery

Do not recreate capabilities that already exist.

## Phase 5 — Reference Analysis

Reference screenshots are evidence, not templates.

Extract:

- hierarchy
- information density
- navigation pattern
- tap/action placement
- spacing
- sheet/dialog behavior
- empty-state treatment
- disclosure depth
- row anatomy
- mobile rhythm

Never blindly copy:

- trademarks
- proprietary branding
- exact palette
- exact typography
- copyrighted copy
- complete screen composition

Build the project's own product identity.

## Phase 6 — Mobile-First Operator Test

For mobile-focused work, test around 390px width.

The first usable viewport should prioritize:

1. screen purpose
2. current state
3. primary action
4. primary content

System diagnostics and implementation details belong deeper unless the user's job requires them.

Verify:

- primary action visible quickly
- essential controls are tap-visible
- no hover-only workflow
- practical touch targets
- no clipped text
- no overlapping controls
- no unintended horizontal scrolling
- sheets/dialogs fit
- destructive actions deliberate
- empty states understandable
- populated states usable
- large system chrome does not bury the task

Mobile is not compressed desktop.

## Phase 7 — Implement the Smallest Complete Slice

Change the smallest coherent surface that completes the acceptance journey.

Prefer existing:

- components
- tokens
- design primitives
- state abstractions
- persistence
- APIs
- services
- routes
- tests

Do not introduce a new framework, state system, persistence system, component library, database, auth provider, or deployment architecture merely to improve presentation.

New infrastructure requires explicit justification.

## Phase 8 — Operate the Product

Screenshots are insufficient.

Actually perform the workflow in the browser.

Examples:

CREATE
→ SAVE
→ OPEN
→ EDIT
→ REFRESH
→ VERIFY

SEARCH
→ SELECT
→ ADD
→ REMOVE
→ VERIFY

BUY-LIST STYLE FLOW
→ ADD
→ REVIEW
→ REMOVE
→ VERIFY NO UNRELATED STATE CHANGED

Use Playwright/browser operation when available.

## Phase 9 — Test Product States

Where relevant test:

- empty
- one item
- many items
- long names
- duplicate input
- invalid input
- unavailable data
- loading
- API failure
- persistence failure
- permission/protected action
- destructive confirmation
- refresh/reload
- narrow mobile
- larger mobile
- tablet
- desktop

Failure behavior is product behavior.

## Phase 10 — Accessibility

Verify where applicable:

- semantic controls
- keyboard operation
- visible focus
- readable contrast
- screen-reader labels
- practical touch targets
- no hover dependency
- reduced-motion behavior
- no keyboard traps
- no hidden essential action

Accessibility is part of completion.

## Phase 11 — Adversarial QA

Try to break the feature.

Use:

governance/standards/PREMIUM_PRODUCT_QUALITY_GATE.md

Do not make the human reviewer discover predictable defects.

## Phase 12 — Fresh-Eyes Review

After technical testing, forget the implementation and look at the feature as a first-time user.

Ask:

- What is this screen?
- What matters?
- What should I do?
- Is the action obvious?
- Is internal system information competing with the user job?
- Does anything look decorative but do nothing?
- Are parallel elements treated consistently?
- Is there unexplained visual clutter?
- Does mobile feel intentionally designed?
- Would an experienced user consider this operational?

Fix meaningful failures.

## Phase 13 — Verify Repository

Run the repository's actual verification chain.

Examples may include:

- lint
- typecheck
- unit tests
- integration tests
- production build
- proof gates
- browser tests

Never weaken verification merely to obtain green output.

## Phase 14 — Delivery Report

Return:

- user workflow completed
- design/package decisions
- files changed
- browser journey tested
- mobile result
- empty/populated/error-state result
- accessibility result
- repository verification
- known limitation
- architecture preserved
- project safety rules preserved
- commit SHA
- branch/PR status

Stop at the bounded objective.

Do not expand scope simply because adjacent work exists.

## Phase 15 — Learn

When a failure is genuinely reusable, preserve:

SYMPTOM
→ VERIFIED CAUSE
→ FIX
→ VERIFICATION

General lessons belong in the reusable troubleshooting library.

Project-specific lessons remain inside the project.

Never record guesses as proven causes.
