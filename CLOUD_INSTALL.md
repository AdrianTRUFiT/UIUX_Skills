# Install Dynamic Web Builder in Claude Code Cloud

Claude Code cloud sessions start from a fresh repository clone. Local Windows files and user-level `~/.claude` configuration do not carry into the cloud. This repository is therefore packaged as a Claude Code plugin marketplace.

## A. One-time cloud environment prerequisites

In Claude Code on the web, open the target environment settings.

Allow network access to:

- `registry.npmjs.org`
- `21st.dev`
- `api.21st.dev`
- `github.com`
- `api.github.com`

Use this environment setup script:

```bash
#!/usr/bin/env bash
set -euo pipefail
npm install --global @21st-dev/cli@latest @playwright/cli@latest
playwright-cli install-browser --with-deps
playwright-cli install --skills
```

Add `API_KEY_21ST` as an environment variable when 21st.dev authentication will be used in cloud sessions. Treat environment variables as shared environment configuration, not a private per-user secret store.

Create a new cloud session after changing the environment. Resuming an old session does not rerun the setup script.

## B. Install from the current development branch

Until PR #3 is approved and merged, open the target application repository in Claude Code cloud and run:

```text
/plugin marketplace add https://github.com/AdrianTRUFiT/UIUX_Skills.git#claude/dynamic-web-builder-v1
/plugin install dynamic-web-builder@trufit-builders --scope project
/reload-plugins
```

Then invoke:

```text
/dynamic-web-builder:build-dynamic-web Build <the complete functional outcome>
```

The plugin is namespaced in marketplace installations. The dedicated agent is available as:

```text
@dynamic-web-builder:dynamic-web-builder
```

## C. Install after PR #3 is merged

After the plugin marketplace reaches `main`:

```text
/plugin marketplace add AdrianTRUFiT/UIUX_Skills
/plugin install dynamic-web-builder@trufit-builders --scope project
/reload-plugins
```

Then use:

```text
/dynamic-web-builder:build-dynamic-web Build <the complete functional outcome>
```

## D. Make a target repository load it automatically

After the marketplace is on `main`, add this to the target repository's `.claude/settings.json` and commit it:

```json
{
  "extraKnownMarketplaces": {
    "trufit-builders": {
      "source": {
        "source": "github",
        "repo": "AdrianTRUFiT/UIUX_Skills"
      }
    }
  },
  "enabledPlugins": {
    "dynamic-web-builder@trufit-builders": true
  }
}
```

Cloud sessions load repository-committed `.claude/settings.json`, skills, agents, rules, hooks, and MCP configuration after workspace trust is accepted.

## E. First cloud verification command

Use a small but real target repository and issue:

```text
/dynamic-web-builder:build-dynamic-web Build a functional contact-request page integrated into the existing app. The form must validate input, save submissions through the repository's existing persistence pattern or a bounded local adapter, show loading/success/error states, remain correct after reload, work on mobile and desktop, and be operated with Playwright before delivery. Create a branch, commit, push, and prepare a pull request. Do not merge.
```

The installation is verified only when Claude successfully:

1. recognizes the namespaced skill;
2. starts the target application;
3. operates the completed user journey with Playwright;
4. passes repository checks and production build;
5. pushes a review branch without merging it.
