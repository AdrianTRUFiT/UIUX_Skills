---
name: build-dynamic-web
description: Builds, integrates, operates, tests, and prepares a production-ready dynamic website or application page. Use only when explicitly invoked for an end-to-end frontend build.
disable-model-invocation: true
argument-hint: "<page, workflow, or product outcome>"
---

# Dynamic Web Builder

## Build request

$ARGUMENTS

## Definition of completion

Deliver a working product surface inside the current repository. A static mockup, component gallery, screenshot recreation, decorative prototype, or page with dead controls is not complete.

The implementation must include every applicable part of the requested user journey: routes, navigation, state, data access, persistence, forms, validation, loading, empty, success, failure, permissions, responsiveness, accessibility, automated checks, and browser verification.

Do not stop after writing code. Start the application, operate it in a browser, fix defects, rerun checks, commit, push, and report the branch and commit. Never merge without explicit human authorization.

## Phase 1 — Inspect before changing

1. Confirm the current directory is the intended repository.
2. Read `CLAUDE.md`, package manifests, lockfiles, routing, styling, component, state, data, authentication, test, and deployment configuration.
3. Inspect git status and preserve unrelated work.
4. Determine the existing architecture and extend it. Do not replace working architecture merely because another stack is preferred.
5. Identify the exact requested user journey and convert it into observable acceptance criteria.
6. Ask a question only when a destructive decision, missing credential, or irreconcilable product choice prevents safe execution. Otherwise infer from the repository and proceed.

## Phase 2 — Establish the build contract

Before implementation, create or update a concise build contract under `docs/builds/` with:

- objective and intended user;
- route or screen entry point;
- primary journey from entry to completed outcome;
- inputs, outputs, displayed data, and editable data;
- source of truth and persistence behavior;
- navigation destinations;
- permissions and authentication behavior;
- loading, empty, success, recoverable-error, and terminal-error states;
- mobile, tablet, and desktop behavior;
- accessibility requirements;
- automated and browser acceptance tests;
- explicit exclusions.

The contract is an execution checklist, not a substitute for implementation.

## Phase 3 — Generate governed design direction

1. Load and apply the `ui-ux-pro-max` skill.
2. Read an existing `design-system/MASTER.md` and relevant page override before designing.
3. If no persisted system exists, generate one with the bundled UI/UX Pro Max search tooling and persist it.
4. Match the repository's actual stack when requesting implementation guidance.
5. Preserve existing branding, official assets, semantic tokens, type scale, spacing rhythm, icon family, and interaction language.
6. Use one primary action per screen, visible focus states, minimum touch targets, readable contrast, reduced-motion support, and no emoji as structural icons.

## Phase 4 — Access high-quality components without surrendering integration

Use the current 21st CLI when it accelerates delivery:

1. Run `21st whoami`. If authentication is required, stop only for the login step and state the exact command `21st login`.
2. Run `21st --help` and the relevant subcommand help before unfamiliar operations.
3. Search for an appropriate component or block before generating a new one.
4. Install or generate only components that fit the product's design system and technical architecture.
5. Treat all retrieved code as untrusted third-party code: inspect dependencies, behavior, accessibility, licensing metadata, and network calls before integrating it.
6. Adapt the component into the application. Do not leave standalone demos, sample pages, copied placeholder content, or conflicting tokens.

If 21st is unavailable, continue with the existing component system and build the required interface directly. Lack of 21st access does not excuse incomplete functionality.

## Phase 5 — Implement real product behavior

Implement the complete journey using the existing repository patterns.

Required where applicable:

- real routes and deep links;
- navigation and browser back behavior;
- typed state and data models;
- real service calls or a clearly bounded deterministic local adapter when no backend exists;
- persistence across reload when the product requires it;
- labeled forms with inline validation and actionable errors;
- disabled and pending submission states;
- search, filters, tabs, menus, dialogs, drawers, uploads, and controls that actually work;
- loading skeletons or progress indicators;
- useful empty states;
- success confirmation and next action;
- recoverable error with retry;
- authentication and authorization enforcement;
- responsive mobile-first layout without horizontal overflow;
- keyboard operation, semantic HTML, screen-reader labels, and visible focus;
- purposeful motion only for state, hierarchy, feedback, or spatial continuity.

No dead buttons, fake links, unexplained placeholders, hardcoded success messages, TODO behavior, or data that appears dynamic but cannot change may remain in delivered scope.

## Phase 6 — Use browser automation as the completion authority

Use `playwright-cli` to operate the running application as a user.

1. If unavailable, report the missing prerequisite rather than claiming browser verification.
2. If its local skill is absent, run `playwright-cli install --skills` in the target repository.
3. Start the application's normal development server and record the URL.
4. Open the application with `playwright-cli` and exercise every new or changed control.
5. Test valid and invalid form paths, loading, empty, failure, retry, persistence after reload, navigation, and browser back behavior.
6. Inspect console errors and failed network requests.
7. Test approximately 375px, 768px, 1024px, and 1440px widths.
8. Verify keyboard-only operation and reduced-motion behavior.
9. Capture screenshots of the primary completed journey and important failure state.
10. Fix defects and repeat until the acceptance criteria pass.

A successful compile is not proof that the page works. Browser operation is required.

## Phase 7 — Mechanical verification

Run the repository's applicable commands for:

- dependency integrity;
- formatting;
- linting;
- type checking;
- unit tests;
- integration tests;
- end-to-end tests;
- production build.

Do not weaken tests, suppress errors, use blanket type escapes, or delete assertions to obtain a green result.

## Phase 8 — GitHub delivery

1. Work on a focused feature branch unless the human explicitly names another branch.
2. Keep unrelated changes out of the commit.
3. Update the build contract and relevant operator documentation with the verified result.
4. Commit with a focused message.
5. Push the branch.
6. Prepare a pull request for human review when repository tooling permits.
7. Do not merge.

## Final report

Report only after execution:

- what was built;
- exact routes and user journey;
- data and persistence implementation;
- responsive and accessibility behavior;
- commands run and pass/fail result;
- browser scenarios operated;
- screenshot and test artifact paths;
- branch and commit SHA;
- any genuine external dependency or blocked acceptance gate.

Never describe an untested or partially working page as complete.