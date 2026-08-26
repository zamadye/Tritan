---
name: portfolio-tracker
description: "Roll up campaign progress into daily and weekly reports, spot stalled or failing campaigns, and keep the audit trail verifiable."
version: 1.0.0
author: Hermes Airdrop Agent
license: MIT
platforms: [linux, macos, windows]
metadata:
  hermes:
    tags: [Airdrop, Reporting, Monitoring, Audit, Analytics]
    related_skills: [daily-executor, airdrop-analyzer]
---

# Portfolio Tracker

Turn the store and the ledger into something a human can act on.

## Daily report

```bash
haa plan                 # what is due today
haa evidence tail -n 20  # what actually happened recently
```

## Weekly report

```bash
haa report --days 7
haa report --days 7 --json   # machine-readable, for piping onward
```

## What to look for

| Signal | Meaning | Action |
|---|---|---|
| `streak_days` = 0 on an active campaign | It stopped running | Find out why today |
| `failure_rate_7d` > 0.3 | The flow is broken or you are being throttled | Re-check the steps; consider pausing |
| `open_issues` growing | Problems are being logged and not resolved | Triage them |
| `actions_7d` = 0 but status `active` | Nobody is doing the work | Set to `paused` or do it |
| `verdict` = `SKIP` but status `active` | Contradiction | Pause it; a SKIP must not keep running |

## Integrity check

Run this weekly. It re-hashes every artifact referenced by the ledger:

```bash
haa evidence verify
```

A mismatch means a screenshot changed after it was recorded. That is not a
cosmetic problem — the evidence trail is the only way to distinguish "I did
this" from "I believe I did this".

## Writing the report

Keep it short. Four sections, no filler:

1. **Headline** — one line. Total active campaigns, total actions, anything
   that needs a decision.
2. **Stalled or failing** — the table above, filtered to problems.
3. **Verdicts that changed** — anything re-scored this week and why.
4. **Decisions needed** — explicit asks. "Campaign X needs approval to bridge
   $4" is useful; "monitoring continues" is not.

Do not pad. A report the operator stops reading is worse than no report.

## Rules

- Report what the data says, including when it says the week was wasted.
- Never mark a campaign healthy because it is quiet.
- Never edit a past ledger entry to make a week look better.
- If `haa evidence verify` reports a mismatch, lead the report with it.
