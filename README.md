# Dynamic Web Builder

This repository is a governed, executor-neutral frontend production system. Codex/Astra and Claude Code are supported execution adapters; repository contracts, skills, tests, and human approval remain authoritative.

It combines:

- UI/UX Pro Max design intelligence;
- companion brand, design-system, styling, banner, and slide skills;
- 21st.dev Magic MCP and CLI component access;
- reusable end-to-end build skills for Codex and Claude Code;
- provider-specific agents/adapters without making a provider the architectural authority;
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
Inspect → Contract → Design → Assemble → Implement → Operate → Test → Fix → Evidence → Human Review
```

## Codex / GPT-6 Astra

Codex reads `AGENTS.md` for concise repository-wide authority and boundaries and discovers the detailed reusable workflow under `.agents/skills/build-dynamic-web/SKILL.md`. See `CODEX.md` for Codex-specific setup. This keeps always-loaded context small and loads detailed production guidance only when the task requires it.

## Claude Code — Windows installation

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

### Executor-neutral / Codex

- `AGENTS.md` — concise repository authority, boundaries, and completion rules
- `.agents/skills/build-dynamic-web/SKILL.md` — Codex/OpenAI-compatible reusable production workflow
- `.mcp.json` — optional external capability configuration
- `CODEX.md` — Codex/Astra adapter and setup guidance

### Claude Code adapter

- `.claude/skills/build-dynamic-web/SKILL.md` — Claude Code completion contract and execution workflow
- `.claude/agents/dynamic-web-builder.md` — dedicated frontend assembly agent
- `.claude-plugin/plugin.json` — cloud/plugin package manifest
- `.claude-plugin/marketplace.json` — TRUFiT plugin marketplace catalog
- `install-dynamic-web-builder.ps1` — Windows personal-scope installer
- `scripts/setup-claude-cloud.sh` — cloud prerequisite installer
- `CLOUD_INSTALL.md` — cloud environment and plugin instructions

## Delivery authority

UI/UX Pro Max supplies design intelligence. 21st.dev supplies optional component discovery and generation. Playwright supplies browser operation. The selected Production Agent executes the requested work and produces artifacts, tests, and evidence; it is not the architectural authority. The target repository's governance and architecture remain authoritative.

No branch may be merged without explicit human authorization.
