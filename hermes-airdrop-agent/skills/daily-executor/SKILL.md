---
name: daily-executor
description: "Run the scheduled daily actions for every active campaign, verify each one completed, and record evidence — or halt and alert."
version: 1.0.0
author: Hermes Airdrop Agent
license: MIT
platforms: [linux, macos, windows]
metadata:
  hermes:
    tags: [Airdrop, Automation, Daily, Check-in, Scheduling]
    related_skills: [quest-executor, portfolio-tracker]
---

# Daily Executor

Do today's check-ins. Prove each one. Stop the moment something needs a human.

## Before you touch a browser

Confirm Chrome is reachable, then get the plan. Do not invent tasks — if it is
not in the plan, it is not today's work.

```bash
haa browser check
haa plan
```

If `browser check` fails, stop and tell the operator to run
`./scripts/start-browser.sh`. Do not spend the run discovering that every
click fails.

Read the plan's warnings too. `needs_approval` means wait for the operator;
`blocked` means do not attempt it at all.

## The loop

For each `scheduled` action:

1. **Open** the campaign URL in the browser.
2. **Check page state first**, before doing anything. If the page shows a
   CAPTCHA, an MFA prompt, or a wallet signature request, halt — see below.
3. **Confirm you are logged in.** A page that looks fine but has silently
   dropped the session will produce a "successful" action that did nothing.
4. **Perform the action.** One action. Then re-read the page.
5. **Verify it took.** Look for the confirmation the site itself gives — a
   changed counter, a timestamp, a receipt. Do not infer success from the
   absence of an error.
6. **Screenshot** the confirmation into `data/campaigns/<slug>/screenshots/`.
7. **Log it:**

```bash
haa campaign log <slug> <action> ok --points 150 \
  --evidence data/campaigns/<slug>/screenshots/2026-08-26-check_in.png
```

## Halt conditions — stop, do not improvise

Halt immediately and alert the operator when you see:

| Trigger | What to do |
|---|---|
| CAPTCHA / "verify you are human" / Cloudflare challenge | Halt. Never attempt to solve it. |
| MFA / 2FA / one-time code | Halt. The operator completes it. |
| Wallet signature or approval prompt | Halt. Signing is a human decision. |
| Session expired / "please log in" | Halt. Do not re-authenticate autonomously. |
| Anything you cannot classify | Halt. Uncertainty is a stop condition. |

```bash
haa campaign log <slug> <action> halted --detail "captcha on claim page"
```

Then alert. If Telegram is configured the operator gets paged; if not, the halt
still lands in the evidence ledger, so it must be logged either way.

## Failure handling

Retry **once**. If it fails again, log it as `failed` with the actual reason and
move on to the next action. Do not retry in a loop — repeated identical
failures are exactly what the tool-loop guardrail exists to catch, and a
campaign page rate-limiting you will only get worse.

```bash
haa campaign log <slug> <action> failed --detail "claim button disabled, HTTP 503"
```

## Rules

- **Never log `ok` without verification.** An unverified action is `failed`.
  This is the single most important rule in this skill: a farming operation
  that records successes it did not confirm is worse than one that does
  nothing, because the operator believes it is working.
- Never sign a transaction. This system holds no keys and never will.
- Never enter a credential you were not explicitly given for this run.
- Log every action with a timestamp — the ledger is the audit trail.
- Finish with `haa evidence tail` so the run ends with its own proof visible.
