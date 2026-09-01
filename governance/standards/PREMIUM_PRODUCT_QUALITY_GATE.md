# Premium Product Quality Gate

Use before declaring a significant application surface complete.

## A. USER JOB

- Can the intended user identify the purpose of the screen?
- Is the primary action obvious?
- Can the user complete the intended workflow?
- Does the workflow survive refresh where persistence is expected?
- Does changing one object accidentally mutate unrelated objects?

## B. STATES

Verify relevant states:

- empty
- one item
- populated
- many items
- loading
- unavailable
- invalid
- duplicate
- error
- protected
- destructive confirmation
- success

## C. MOBILE

At approximately 390px:

- primary action visible quickly
- no important control requires hover
- touch targets practical
- no clipped text
- no horizontal overflow
- no overlapping controls
- sheet/dialog fully usable
- keyboard does not bury critical controls
- system telemetry does not displace the user job

## D. DESKTOP

- hierarchy remains clear
- layout does not become needlessly sparse
- advanced controls do not overwhelm primary workflow
- resizing does not break state or navigation

## E. INTERACTION

- actions provide immediate feedback
- destructive behavior is deliberate
- disabled/protected states are understandable
- loading is honest
- errors are actionable where possible
- browser back/forward behavior remains sensible
- deep links work where applicable

## F. ACCESSIBILITY

- semantic interactive controls
- visible keyboard focus
- keyboard-operable workflow
- labels/accessibility names
- readable contrast
- touch targets
- reduced-motion support where motion exists
- decorations are not exposed as controls
- no keyboard trap

## G. DATA / STATE

- no fabricated data
- loading does not masquerade as zero
- missing data does not masquerade as zero
- stale state is handled intentionally
- canonical identity remains intact
- persistence follows project contract
- no unrelated state corruption

## H. ENGINEERING

- existing architecture preserved
- existing framework preserved
- no unnecessary dependency
- no test weakened
- no secret exposed
- project checks pass
- production build succeeds

## I. FRESH-EYES REVIEW

Ignore the implementation details and inspect as a new user.

Ask:

- What is this?
- What matters?
- What should I do?
- What looks clickable?
- Is anything visually prominent but functionally irrelevant?
- Is anything functionally important but visually buried?
- Does this feel like a deliberate product rather than an internal admin screen?
- Does mobile feel native to its size rather than compressed?

Fix meaningful failures before delivery.
