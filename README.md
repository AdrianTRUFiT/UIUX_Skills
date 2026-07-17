# UIUX Skills — Dynamic Web Builder

Governed Claude Code frontend-production toolkit for building functional, responsive websites and application pages rather than static AI mockups.

## What this repository provides

- **UI/UX Pro Max** — design-system, layout, typography, color, accessibility, responsive, animation, and stack guidance.
- **21st CLI integration** — component and block discovery/generation from 21st.dev.
- **Dynamic Web Builder skill** — the `/build-dynamic-web` end-to-end execution command.
- **Dynamic Web Builder agent** — a dedicated Claude Code agent that implements, runs, operates, tests, fixes, commits, and pushes the requested user journey.
- **Playwright CLI verification** — deterministic browser operation so a compile or screenshot cannot be mistaken for a functioning application.

## One-time Windows installation

From a clone of this repository:

```powershell
Set-Location "D:\DEV\UIUX_Skills"
Set-ExecutionPolicy -Scope Process Bypass
.\install-dynamic-web-builder.ps1
```

The installer:

1. copies the repository's Claude skills to `%USERPROFILE%\.claude\skills`;
2. installs the `dynamic-web-builder` agent to `%USERPROFILE%\.claude\agents`;
3. installs the current 21st CLI and Playwright CLI;
4. installs the Playwright browser runtime;
5. creates the `dynamic-web` launcher;
6. adds `%USERPROFILE%\.claude\bin` to the user PATH;
7. verifies required commands and opens 21st.dev login when needed.

Open a new PowerShell window after installation.

## Daily use

Enter the actual product repository:

```powershell
Set-Location "D:\DEV\YOUR-APPLICATION"
dynamic-web
```

Then invoke the governed build command inside Claude Code:

```text
/build-dynamic-web Build the complete functional <website/page/journey>, including real routes, data, persistence, validation, responsive behavior, browser testing, and GitHub delivery.
```

The agent must extend the existing repository architecture, operate every delivered control through Playwright CLI, fix failures, run the project's mechanical checks, commit, push, and report the branch and commit. It must not merge without human authorization.

## Completion standard

The work is complete only when the requested journey operates successfully in a real browser and all applicable lint, type, test, and production-build gates pass. Static mockups, disconnected component demonstrations, dead controls, fake data behavior, and unverified screenshots do not qualify.

## Key files

- `.claude/skills/build-dynamic-web/SKILL.md`
- `.claude/agents/dynamic-web-builder.md`
- `.claude/skills/ui-ux-pro-max/SKILL.md`
- `install-dynamic-web-builder.ps1`
- `21ST_DEV_SETUP.md`

This repository owns frontend assembly capability. Each product repository continues to own its product requirements, implementation, data, tests, deployment, and release decisions.
