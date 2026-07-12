# 21st.dev Setup

This project uses [21st.dev](https://21st.dev) for UI component search, install,
and publishing, via two entry points:

- **CLI** (`21st`) — search, add, publish, and manage components from the terminal.
- **MCP server** (Magic) — declared project-wide in [`.mcp.json`](.mcp.json) so any
  MCP-capable client (Claude Code, Cursor, Windsurf, …) opened in this repo can use
  21st.dev component generation directly.

## 1. Install the CLI and sign in

Login opens the browser and saves a token locally:

```bash
npm i -g @21st-dev/cli
21st login
```

## 2. Everyday usage

```bash
21st search "pricing table"
21st add shadcn/button
21st publish ./PinList.tsx --description "A pinned items list"
21st edit pin-list --type component --visibility public
21st delete pin-list --type component --yes
```

## 3. CI / scripts / headless environments

Skip the interactive login and pass an API key instead:

```bash
21st search "pricing table" --api-key "$API_KEY_21ST"
# or simply export API_KEY_21ST before running commands
```

The MCP server config in `.mcp.json` reads the same `API_KEY_21ST` environment
variable, so one secret covers both entry points.

## Notes for Claude Code on the web (remote sessions)

The default remote-session network policy blocks `registry.npmjs.org` and
`21st.dev`, so neither the CLI install nor its API calls work there out of the
box. To use 21st.dev from remote sessions, allow these domains in the
environment's network policy (Claude Code on the web → environment settings):

- `registry.npmjs.org` (package install)
- `21st.dev` and `api.21st.dev` (CLI / MCP API)

and add `API_KEY_21ST` as an environment secret.
