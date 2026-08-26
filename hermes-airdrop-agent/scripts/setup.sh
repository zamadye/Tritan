#!/usr/bin/env bash
# ---------------------------------------------------------------------------
# Developer setup: venv, package, tests. No system changes, no Hermes install.
# ---------------------------------------------------------------------------
set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
PROJECT_DIR="$(dirname "$SCRIPT_DIR")"
cd "$PROJECT_DIR"

PY="${PYTHON:-python3}"
if [[ ! -d .venv ]]; then
  echo "→ creating .venv"
  "$PY" -m venv .venv
fi
# shellcheck disable=SC1091
source .venv/bin/activate

echo "→ installing"
pip install --quiet --upgrade pip
pip install --quiet -e ".[dev]"

if [[ ! -f .env ]]; then
  cp .env.example .env
  echo "→ created .env from .env.example (add your API key)"
fi

echo "→ running tests"
python -m pytest

echo
echo "✓ ready.  Activate with: source .venv/bin/activate"
