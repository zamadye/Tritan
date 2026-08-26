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

## Autonomy contract — read this before anything else

**Nobody tells you which button to click. You decide.**

There is no selector, no XPath, no coordinate, no "click the third div" anywhere
in this system. Airdrop UIs change weekly and differ completely between
projects; anything prescriptive would be both brittle and wrong. What you are
given is an *outcome* ("complete the daily mission on Loqua") and a browser.
How you get there is your judgement, re-derived from the live page every time.

Your perception tools, in order of preference:

| Tool | Use it for |
|---|---|
| `browser_snapshot` | The default. Returns the page's accessibility tree with ref IDs (`@e1`, `@e7`) for every interactive element. **This is how you find things** — not by guessing selectors. |
| `browser_snapshot full=true` | When the compact view hides the element you need |
| `browser_vision` | When the tree is ambiguous — a wall of similar buttons, an icon with no label, a canvas-rendered widget. Ask it a direct question: *"which element is the daily claim button?"* |
| `browser_get_images` | When the action depends on an image (CAPTCHA-adjacent art, a banner, a QR) |
| `browser_console` | Only to read state, never to drive the page |

**Refs are per-snapshot.** `@e7` means "the seventh interactive element in the
snapshot you just took". After any navigation, click, or DOM change the
numbering can shift. So:

- Take a fresh snapshot before every action. Never reuse a ref from an earlier
  one.
- If a click hits something unexpected, snapshot again rather than retrying
  blindly.

## The loop

You own the *how*. These are the outcomes each action must reach, not a script:

- **Be on the right page**, and know that you are.
- **Know the page state before acting.** A CAPTCHA, an MFA prompt, or a wallet
  signature request means halt — see below.
- **Know you are logged in.** A page that looks fine but silently dropped the
  session will produce a "successful" action that did nothing.
- **Do the one thing**, then look at the page again.
- **Confirm it took, using the site's own feedback** — a changed counter, a
  timestamp, a receipt. Not the absence of an error.
- **Capture proof**, then record it:

```bash
haa campaign log <slug> <action> ok --points 150 \
  --evidence data/campaigns/<slug>/screenshots/2026-08-26-check_in.png
```

If the page does something you did not expect — a new modal, a redesigned
layout, a step that was not there yesterday — **adapt, and write down what
changed**. That note is how the next run avoids the same surprise.


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
