#!/usr/bin/env bash
# ---------------------------------------------------------------------------
# Install the scheduled jobs using Hermes' own cron scheduler.
#
# Hermes cron is NOT the system crontab. Jobs live in ~/.hermes/cron/jobs.json,
# are managed with `hermes cron list|edit|pause|run`, and run through the same
# guardrails as an interactive session — including approvals.cron_mode: deny.
# ---------------------------------------------------------------------------
set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
PROJECT_DIR="$(dirname "$SCRIPT_DIR")"
HERMES_HOME="${HERMES_HOME:-$HOME/.hermes}"

[[ -f "$PROJECT_DIR/.env" ]] && set -a && . "$PROJECT_DIR/.env" && set +a

if ! command -v hermes >/dev/null 2>&1; then
  echo "✗ 'hermes' not found — install it first." >&2
  exit 1
fi

if [[ -z "${HAA_PROJECT_DIR:-}" ]]; then
  export HAA_PROJECT_DIR="$PROJECT_DIR"
fi

# Prompt text is self-contained on purpose: a cron run has no conversation
# history from previous runs, so it must spell everything out.

daily_prompt="Run today's airdrop check-ins.

1. Run: haa plan
2. For each action marked 'scheduled', follow the daily-executor skill:
   open the campaign URL, verify you are logged in, perform the action,
   confirm it against the site's own feedback, screenshot it, then log it:
     haa campaign log <slug> <action> ok --points <n> --evidence <path>
3. HALT and alert on any CAPTCHA, MFA prompt, wallet signature request, or
   expired session. Never solve a challenge. Never sign.
4. Log an action as 'failed' if you could not verify it. Never log 'ok'
   without verification.
5. Finish with: haa evidence tail -n 20"

verify_prompt="Verify this morning's airdrop run.

1. Run: haa plan   and   haa evidence tail -n 40
2. Every action that was planned should have a ledger entry. List any that
   are missing.
3. Run: haa evidence verify   — report any hash mismatch prominently.
4. Run: haa report --days 1
5. Report only discrepancies. If everything matches, say so in one line."

report_prompt="Generate the weekly airdrop report.

1. Run: haa report --days 7
2. Run: haa evidence verify
3. Flag: active campaigns with a zero streak, failure_rate_7d above 0.3,
   campaigns with verdict SKIP still marked active, and any evidence mismatch.
4. Four sections: headline, stalled-or-failing, verdict changes, decisions
   needed. No filler. Report what the data says, including a wasted week."

scan_prompt="Scan the Discord communities of all active campaigns.

1. Run: haa campaign list
2. For each active campaign, open its Discord in the logged-in browser session
   and read announcements, rules, and any airdrop/points channel.
3. Log anything that changes the plan:
     haa campaign log <slug> discord_scan ok --detail \"<what changed>\"
4. Prioritise snapshot dates, deadline moves, and rule changes.
5. DRAFT any reply the operator might want to send. Do not post anything —
   automated posting violates Discord's Terms of Service."

add_job() {  # schedule prompt name profile [extra args...]
  local schedule="$1" prompt="$2" name="$3" profile="$4"; shift 4
  if hermes --profile "$profile" cron list 2>/dev/null | grep -qF "$name"; then
    echo "  · exists: $name"
    return 0
  fi
  echo "  + $name  ($schedule)"
  hermes --profile "$profile" cron create "$schedule" "$prompt" \
    --name "$name" "$@"
}

echo "Installing Hermes cron jobs into ${HERMES_HOME}/cron/"

add_job "0 9 * * *"  "$daily_prompt"  "airdrop-daily"   worker-daily \
  --skill daily-executor
add_job "0 13 * * *" "$verify_prompt" "airdrop-verify"  worker-monitor \
  --skill portfolio-tracker
add_job "0 20 * * 0" "$report_prompt" "airdrop-weekly"  worker-monitor \
  --skill portfolio-tracker
add_job "0 11 * * 1" "$scan_prompt"   "airdrop-discord" worker-discord \
  --skill discord-engager

echo
echo "✓ cron jobs installed"
echo "  hermes cron list          # inspect"
echo "  hermes cron run <job_id>  # trigger one now"
echo "  hermes cron pause <id>    # disable"
