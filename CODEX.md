# Codex / GPT-6 Astra

This repository supports Codex as a first-class production executor without making Codex an architectural dependency.

## Repository-local use

Open this repository, or a target repository that has this capability installed, in Codex. Codex reads root `AGENTS.md` for repository guidance and discovers reusable project skills under `.agents/skills/`.

For an end-to-end frontend task, invoke the workflow explicitly when useful:

```text
Use the build-dynamic-web skill to build <complete functional outcome>.
```

The skill is intentionally detailed while `AGENTS.md` remains concise so routine tasks do not carry unnecessary context.

## External capabilities

The existing `.mcp.json` contains optional 21st.dev Magic MCP configuration. MCP is capability access, not production authority.

For OpenAI API/Codex/platform work, the official OpenAI developer documentation MCP can be configured in Codex separately:

```powershell
codex mcp add openaiDeveloperDocs --url https://developers.openai.com/mcp
codex mcp list
```

Do not commit credentials. Keep authentication in the supported user/environment secret mechanism.

## Operating principle

```text
Contract / Work Order
        ↓
Production Agent
        ↓
Artifacts + Tests + Evidence
        ↓
Human Review
```

`Production Agent` may be Codex/Astra, Claude Code, a local model, or another conforming executor.

Provider-specific configuration is an adapter. Reusable production knowledge belongs in contracts, skills, references, scripts, tests, and design assets.

## Verification

A Codex installation is useful only if it can:
1. discover the repository guidance and relevant skill;
2. modify a real target application without replacing sound architecture;
3. run the application and operate the changed journey in a browser when tooling is available;
4. pass applicable repository checks;
5. produce evidence and a reviewable branch;
6. stop before merge/release without explicit human approval.
