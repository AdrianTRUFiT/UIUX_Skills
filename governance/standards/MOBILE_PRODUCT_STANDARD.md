# Mobile Product Standard

## Principle

Mobile is a first-class application surface.

It is not desktop compressed into a phone.

## First View Priority

1. What screen is this?
2. What is the current state?
3. What can I do?
4. What content matters now?

Diagnostics, provenance, telemetry, implementation metadata, and advanced
analysis are secondary unless the operator's task explicitly requires them.

## Actions

Essential actions must be directly discoverable by tap.

Avoid:

- hover-only controls
- tiny icon-only actions without accessible labels
- deeply buried primary actions
- browser prompt/alert/confirm as polished product UX
- oversized headers that push the task below the fold

## Lists

Operational list interfaces should normally support:

CREATE
→ NAME
→ OPEN
→ ADD
→ REMOVE
→ RENAME
→ DELETE

where the project's rules permit those actions.

A row should provide enough information to identify the item and take the
next appropriate action without becoming a telemetry dump.

## Sheets and Dialogs

Use compact application-native interactions for:

- create
- rename
- delete
- add
- move
- filter
- context actions

The user should remain oriented to the screen beneath the interaction.

## Empty States

An empty state should explain:

- what is empty
- why the surface exists
- what the user can do next

## Validation

Test approximately:

- 390px primary mobile
- 768px transition/tablet
- project desktop breakpoint

Also test a shorter mobile viewport when bottom sheets or keyboards are involved.
