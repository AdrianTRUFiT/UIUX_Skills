#!/usr/bin/env bash
set -euo pipefail

printf '\n== Dynamic Web Builder cloud prerequisites ==\n'

if ! command -v node >/dev/null 2>&1; then
  echo 'Node.js is required but was not found.' >&2
  exit 1
fi

npm install --global @21st-dev/cli@latest @playwright/cli@latest

playwright-cli install-browser --with-deps
playwright-cli install --skills

printf '\nInstalled versions:\n'
node --version
npm --version
21st --version || 21st --help | head -n 1
playwright-cli --version || playwright-cli --help | head -n 1

printf '\nCloud prerequisites are ready.\n'
