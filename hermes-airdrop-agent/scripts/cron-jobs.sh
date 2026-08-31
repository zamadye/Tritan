#!/usr/bin/env bash
# ---------------------------------------------------------------------------
# Install the scheduled jobs using Hermes' own cron scheduler.
#
# Hermes cron is NOT the system crontab. Jobs live in ~/.hermes/cron/jobs.json,
# are managed with `hermes cron list|edit|pause|run`, and run through the same
# guardrails as an interactive session — including approvals.cron_mode: deny.
# The system crontab cannot enforce that.
#
# ---------------------------------------------------------------------------
# SCHEDULE SHAPE (3 layers)
# ---------------------------------------------------------------------------
#   08:30 daily   orchestrator  reviews state, flags what needs attention
#   09:00 daily   lead          runs each project's daily actions
#   13:00 daily   monitor       verifies the morning run + evidence hashes
#   20:00 Sunday  monitor       weekly report
#   11:00 Monday  discord       community scan
#
# The orchestrator runs BEFORE the workers on purpose: it is the layer that
# decides whether today's work is even worth doing, and it is the one that
# pages the operator when something is stalled.
#
# Every browser job starts with a CDP preflight. Chrome runs on the host, so
# if the operator closed the window the job must fail fast and say so — not
# spend an hour discovering that every click fails.
# ---------------------------------------------------------------------------
set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
PROJECT_DIR="$(dirname "$SCRIPT_DIR")"
HERMES_HOME="${HERMES_HOME:-$HOME/.hermes}"

[[ -f "$PROJECT_DIR/.env" ]] && set -a && . "$PROJECT_DIR/.env" && set +a

if ! command -v hermes >/dev/null 2>&1; then
  echo "✗ 'hermes' not found — install it first (./install.sh)." >&2
  exit 1
fi

[[ -n "${HAA_PROJECT_DIR:-}" ]] || export HAA_PROJECT_DIR="$PROJECT_DIR"

# ---------------------------------------------------------------------------
# Prompts.
#
# Each one is SELF-CONTAINED on purpose. A cron run has no conversation history
# from previous runs, so it cannot rely on anything the agent "already knows".
# Spell out the commands, the rules, and what to report.
# ---------------------------------------------------------------------------

PREFLIGHT='0. PREFLIGHT — run this first and stop if it fails:
     haa browser check
   If the CDP endpoint is not reachable, do NOT continue. Alert the operator:
   "Chrome is not running. Run ./scripts/start-browser.sh." A closed Chrome
   window is the single most common cause of a wasted run.'

orchestrator_prompt="Review the state of every airdrop campaign and decide what needs attention today.

${PREFLIGHT}

1. Run: haa report --days 7
2. Run: haa campaign list
3. Flag anything that needs a human decision:
   - an ACTIVE campaign with a zero streak (it stopped running)
   - a campaign whose verdict is SKIP but is still ACTIVE (contradiction)
   - failure_rate_7d above 0.3 (the flow is broken or we are being throttled)
   - any campaign with a halted action still unresolved
4. For each flagged item, state plainly what the operator must do.
5. If nothing needs attention, say so in ONE line. Do not pad.

You are the layer that talks to the operator. Be specific: 'Elyon needs a
wallet signature for the connect step' is useful; 'monitoring continues' is not."

lead_prompt="Run today's actions for every active campaign.

${PREFLIGHT}

1. Run: haa plan
2. For each action marked 'scheduled', work through it IN THE ORDER the plan
   gives. Skip anything marked 'needs_approval' or 'blocked' — those wait for
   the operator.
3. Every campaign has its own task format and its own rules. Read what THIS
   project asks for before acting:
     haa campaign show <slug>
   Never assume one project's flow applies to another. A daily mission on one
   campaign may not exist on the next.
4. For each action: open the page, confirm you are logged in, do the action,
   then VERIFY it against the site's own confirmation — a changed counter, a
   timestamp, a checkmark. Reload the page before accepting a state change.
5. Screenshot the confirmation, then log it:
     haa campaign log <slug> <action> ok --points <n> --evidence <path>
6. HALT and alert on any CAPTCHA, MFA prompt, wallet signature request, or
   expired session. Never solve a challenge. Never sign.
7. Log an action as 'failed' if you could not verify it. NEVER log 'ok'
   without verification — that is the one mistake that makes everything else
   worthless.
8. Finish with: haa evidence tail -n 20"

verify_prompt="Verify this morning's airdrop run.

1. Run: haa plan
2. Run: haa evidence tail -n 40
3. Every action that was planned should have a ledger entry. List any missing.
4. Run: haa evidence verify
   Report any hash mismatch PROMINENTLY — it means a proof changed after it was
   recorded, which undermines the whole audit trail.
5. Run: haa report --days 1
6. Report only discrepancies. If everything matches, say so in one line."

report_prompt="Generate the weekly airdrop report.

1. Run: haa report --days 7
2. Run: haa evidence verify
3. Flag: active campaigns with a zero streak, failure_rate_7d above 0.3,
   campaigns with verdict SKIP still marked active, and any evidence mismatch.
4. Four sections: headline, stalled-or-failing, verdict changes, decisions
   needed. No filler. Report what the data says, including a wasted week."

scan_prompt="Scan the Discord communities of all active campaigns.

${PREFLIGHT}

1. Run: haa campaign list
2. For each active campaign, open its Discord in the logged-in browser session
   and read announcements, rules, and any airdrop/points channel.
3. Log anything that changes the plan:
     haa campaign log <slug> discord_scan ok --detail \"<what changed>\"
4. Prioritise snapshot dates, deadline moves, and rule changes.
5. DRAFT any reply the operator might want to send. Do not post anything —
   automated posting violates Discord's Terms of Service."

# ---------------------------------------------------------------------------

add_job() {  # schedule prompt name profile [extra args...]
  local schedule="$1" prompt="$2" name="$3" profile="$4"; shift 4
  if hermes --profile "$profile" cron list 2>/dev/null | grep -qF "$name"; then
    echo "  · exists: $name"
    return 0
  fi
  echo "  + $name  ($schedule)  [$profile]"
  hermes --profile "$profile" cron create "$schedule" "$prompt" \
    --name "$name" "$@"
}

echo "Installing Hermes cron jobs into ${HERMES_HOME}/cron/"
echo

# layer 1 — orchestrator, runs before the workers
add_job "30 8 * * *" "$orchestrator_prompt" "airdrop-orchestrator" worker-orchestrator

# layer 2 — lead, applies each project's own rules
add_job "0 9 * * *"  "$lead_prompt"          "airdrop-daily"       worker-lead \
  --skill daily-executor --skill quest-executor

# layer 3 — specialist workers
add_job "0 13 * * *" "$verify_prompt"        "airdrop-verify"      worker-monitor \
  --skill portfolio-tracker
add_job "0 20 * * 0" "$report_prompt"        "airdrop-weekly"      worker-monitor \
  --skill portfolio-tracker
add_job "0 11 * * 1" "$scan_prompt"          "airdrop-discord"     worker-discord \
  --skill discord-engager

echo
echo "✓ cron jobs installed"
echo "  hermes cron list          # inspect"
echo "  hermes cron run <job_id>  # trigger one now"
echo "  hermes cron pause <id>    # disable"
echo
echo "Note: every browser job starts with a CDP preflight. Chrome runs on the"
echo "host, so if its window is closed the job stops immediately and tells you."
