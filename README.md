# Dynamic Web Builder

This repository is now a governed frontend production system for Claude Code.

It combines:

- UI/UX Pro Max design intelligence;
- companion brand, design-system, styling, banner, and slide skills;
- 21st.dev Magic MCP and CLI component access;
- a commandable end-to-end build skill;
- a dedicated dynamic-web-builder agent;
- Playwright CLI browser verification;
- Windows and Claude Code cloud installation paths.

## What the builder is for

Use the builder when the requested outcome is a working website, application page, dashboard, portal, form workflow, or interactive product surface.

The builder does not treat any of the following as completion:

- a static mockup;
- a screenshot recreation;
- a disconnected component gallery;
- dead buttons or fake links;
- hardcoded success behavior;
- code that compiles but has not been operated in a browser.

The required delivery loop is:

```text
Inspect → Contract → Design → Assemble → Implement → Operate → Test → Fix → Commit → Push → Human Review
```

## Windows installation

From PowerShell:

```powershell
Set-Location "D:\DEV\UIUX_Skills"
git fetch origin
git switch claude/dynamic-web-builder-v1
git pull --ff-only
Set-ExecutionPolicy -Scope Process Bypass -Force
.\install-dynamic-web-builder.ps1
```

Then enter any application repository and run:

```powershell
dynamic-web
```

Inside Claude Code:

```text
/build-dynamic-web Build <the complete functional outcome>
```

## Claude Code cloud installation

See [`CLOUD_INSTALL.md`](CLOUD_INSTALL.md).

Until the feature branch is merged, open a target application repository in Claude Code cloud and ask Claude to run:

```bash
claude plugin marketplace add AdrianTRUFiT/UIUX_Skills@claude/dynamic-web-builder-v1 --scope project
claude plugin install dynamic-web-builder@trufit-builders --scope project
```

Then run:

```text
/reload-plugins
/dynamic-web-builder:build-dynamic-web Build <the complete functional outcome>
```

## Core assets

- `.claude/skills/build-dynamic-web/SKILL.md` — completion contract and execution workflow
- `.claude/agents/dynamic-web-builder.md` — dedicated frontend assembly agent
- `.claude-plugin/plugin.json` — cloud/plugin package manifest
- `.claude-plugin/marketplace.json` — TRUFiT plugin marketplace catalog
- `install-dynamic-web-builder.ps1` — Windows personal-scope installer
- `scripts/setup-claude-cloud.sh` — cloud prerequisite installer
- `CLOUD_INSTALL.md` — cloud environment and plugin instructions

## Delivery authority

UI/UX Pro Max supplies design intelligence. 21st.dev supplies optional component discovery and generation. Playwright supplies browser operation. Claude Code remains responsible for integrating real routes, state, data, persistence, validation, loading, empty, success, error, responsive, accessibility, test, build, and GitHub delivery behavior.

No branch may be merged without explicit human authorization.
