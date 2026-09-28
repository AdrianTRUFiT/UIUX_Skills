---
name: build-dynamic-web
description: Build, integrate, operate, test, and prepare a production-ready website, dashboard, portal, form workflow, or application surface when the user requests end-to-end frontend delivery.
---

# Dynamic Web Builder

Deliver the requested working product surface inside the current target repository.

A static mockup, component gallery, screenshot recreation, decorative prototype, dead controls, fake links, hardcoded success behavior, or code that merely compiles is not complete.

## 1. Inspect

- Confirm the intended target repository and inspect git status.
- Read only the manifests, routing, styling, state, data, authentication, tests, deployment configuration, and repository guidance relevant to the requested journey.
- Preserve unrelated work and established architecture.
- Convert the request into observable acceptance criteria.
- Ask only when a destructive decision, missing credential, or irreconcilable product choice prevents safe execution.

## 2. Establish the contract

Create or update a concise build contract under `docs/builds/` when the target repository uses or can reasonably accept build documentation. Capture:
- objective and intended user;
- route or entry point;
- primary journey;
- inputs, outputs, displayed/editable data;
- source of truth and persistence;
- navigation;
- permissions/authentication;
- loading, empty, success, recoverable-error, and terminal-error states;
- responsive and accessibility requirements;
- automated/browser acceptance tests;
- explicit exclusions.

The contract is an execution checklist, not a substitute for implementation.

## 3. Design

- Apply the repository's persisted design system first.
- Use available UI/UX design skills or references from this repository when useful.
- Preserve branding, semantic tokens, typography, spacing, icon language, and established interaction patterns.
- Prefer one clear primary action per screen, visible focus, readable contrast, adequate touch targets, reduced-motion support, and semantic controls.

## 4. Assemble

Use existing components first. Use 21st.dev or another approved component source only when it accelerates delivery.

For retrieved third-party code:
- inspect dependencies, behavior, accessibility, licensing metadata, and network calls;
- adapt it to the target architecture and design system;
- remove demos, placeholder content, conflicting tokens, and disconnected examples.

A missing optional component service is not a reason to stop.

## 5. Implement real behavior

Implement every applicable part of the journey:
- routes/deep links and navigation;
- typed state/data models;
- real service calls or a clearly bounded deterministic local adapter when no backend exists;
- required persistence;
- labeled forms, validation, actionable errors, pending/disabled states;
- working search, filters, tabs, menus, dialogs, drawers, uploads, and controls;
- loading, empty, success, failure, and retry behavior;
- authentication/authorization enforcement;
- mobile-first responsive behavior without horizontal overflow;
- keyboard operation, semantic HTML, screen-reader labels, and visible focus.

Do not leave TODO behavior or data that appears dynamic but cannot actually change within delivered scope.

## 6. Operate in a browser

Use available browser automation (prefer the repository's established Playwright workflow) to operate the running application as a user.

Exercise applicable:
- primary success journey;
- invalid input;
- loading/empty/failure/retry;
- persistence after reload;
- navigation and browser back;
- console errors and failed network requests;
- representative mobile, tablet, laptop, and desktop widths;
- keyboard-only operation and reduced motion.

Capture evidence where tooling supports it. Fix defects and rerun until applicable acceptance criteria pass.

If browser tooling is unavailable, state that as an unverified acceptance gate; do not claim browser verification.

## 7. Mechanical verification

Run the target repository's applicable dependency, formatting, lint, typecheck, unit, integration, end-to-end, and production-build commands.

Do not weaken tests, suppress errors, delete assertions, or use blanket type escapes merely to obtain a green result.

## 8. Deliver for human review

- Work on a focused branch unless the human explicitly names another branch.
- Keep unrelated changes out of the commit.
- Update relevant build/operator documentation.
- Commit and push verified work when authorized by the environment/task.
- Prepare a pull request when tooling permits.
- Never merge without explicit human authorization.

## Final evidence

Report:
- what was built;
- routes and user journey;
- data/persistence implementation;
- responsive/accessibility behavior;
- commands and pass/fail results;
- browser scenarios operated;
- evidence artifact paths;
- branch and commit SHA;
- genuine external blockers.

The executor is not the authority. Repository contracts and human approval are.
