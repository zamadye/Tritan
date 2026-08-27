---
name: quest-executor
description: "Work through a campaign's onboarding and multi-step quest sequence, verifying each step before moving to the next."
version: 1.0.0
author: Hermes Airdrop Agent
license: MIT
platforms: [linux, macos, windows]
metadata:
  hermes:
    tags: [Airdrop, Automation, Quests, Onboarding, Browser]
    related_skills: [daily-executor, airdrop-analyzer]
---

# Quest Executor

Onboard a campaign and complete its quest sequence, step by step, with proof at
each step.

Every airdrop is different — different task format, different rules, different
requirements. Read what *this* project actually asks for before doing anything.
Never assume one project's flow applies to another.

## Prerequisite

The campaign must already have a verdict of `PRIORITIZE` or `CONSIDER`. Check:

```bash
haa campaign show <slug>
```

If the verdict is `SKIP` or missing, stop and run `airdrop-analyzer` first. Do
not onboard a project nobody has screened.

## Sequence design

A real campaign is **dozens of actions across many dApps**, not a handful.
Monad alone was ~15 separate sites. So model the dependencies instead of hoping
the order works out:

```bash
haa campaign add-action <slug> "add_rpc@once"      --tier connect --network monad-testnet
haa campaign add-action <slug> "claim_faucet@once" --tier testnet --depends-on add_rpc
haa campaign add-action <slug> "apriori_stake@once" --tier testnet --group apriori \
    --depends-on claim_faucet
```

- `--depends-on` — the planner refuses to run an action whose prerequisites are
  not done. Without it the agent swaps before the faucet ran and reports a
  failure that looks like a broken dApp.
- `--group` — one per dApp. Runs checkpoint per group, so a 40-step campaign
  **resumes** instead of restarting.
- `--tier` / `--network` — feed the tiered approval decision (see below).

Ask what is runnable right now rather than guessing:

```bash
haa plan
```

### Prerequisites that live outside the campaign

Some gates are not steps at all — the Monad faucets needed 0.03 ETH plus three
mainnet transactions, or $1 of volume on another site, or tokens on Polygon.
If no faucet can be claimed, **nothing downstream is possible**. Stop and say
so. Grinding through 40 failing actions is worse than reporting the blocker.

## Approval tiers

Approval is tiered by what is at risk, not by whether a signature happens:

| Tier | Examples | Who acts |
|---|---|---|
| `read` | navigate, snapshot, screenshot | autonomous |
| `connect` | connect wallet, add network | autonomous |
| `testnet` | testnet swap, stake, mint, deploy | autonomous |
| `mainnet` | real value, within `HAA_MAX_SPEND_USD` | autonomous + report |
| `critical` | unlimited `approve`, `setApprovalForAll`, over the limit | **human, always** |

The last row stays manual **even on testnet**. Blind-approving is a habit, and
the habit is what causes mainnet losses later.

## Things that need a human, once

**Browser extensions cannot be installed over CDP.** Projects like Primus and
Miden ask you to install their extension. There is no workaround — model these
as `--kind manual_setup`, stop, and tell the operator what to install.

## Long-horizon commitments

Some rewards need state that outlives a single run: an LP position left open
for 30 days, a 30-day daily streak, a badge that expires.

```bash
haa positions add <slug> --id lp-main --kind lp --protocol Aerodrome --until 2026-09-25
haa positions streak <slug> discover     # mark today's streak day done
haa positions list <slug>                # what is open, expiring, or at risk
```

Check `haa positions list` at the start of a run. A streak that already missed
today is worth interrupting someone for; discovering it in three weeks is not.

## Pacing

A good sequence is **3–5 persistent actions repeated over weeks**, not 200
micro-operations in an afternoon. Projects look at consistency and at on-chain
history, not at a single burst of activity.

Design for that:

```bash
haa campaign add-action <slug> "check_in@0 9 * * *"      --kind browser
haa campaign add-action <slug> "swap_small@0 10 * * 3"   --kind manual
haa campaign add-action <slug> "provide_liquidity@0 11 * * 6" --kind manual
```

Use `--kind manual` for anything that spends money. `--kind wallet` marks an
action as one you will sign yourself; the planner will block the agent from
attempting it.

## Autonomy contract

**You are never given a selector, a coordinate, or a click sequence.** Every
airdrop has its own UI and they all change; anything prescriptive would break
within a week and would be wrong on the next project anyway.

You are told *what the project wants* (from its own task list, recorded by the
lead). **How to make the page do it is your decision**, re-derived from the
live page each time.

Find things with `browser_snapshot` — it returns the accessibility tree with
ref IDs (`@e1`, `@e7`) for every interactive element. When the tree is
ambiguous (a row of identical buttons, an unlabelled icon, a canvas widget),
use `browser_vision` and ask it directly. Refs are **per-snapshot**: take a
fresh one before every action, and never reuse a ref from before a navigation
or a click.

## Full control of the browser — reason forward, do not ask

The managed browser is fully yours. Open tabs, navigate, click, type, scroll,
read, take screenshots. There is no exception for ordinary tasks: every click
and every next step is your decision, derived from the task you were given and
the live page in front of you.

**Do not stop to ask "what should I do next?"** You were given an outcome, not
a script. When one step finishes, look at the page, decide what the task
requires next, and do it. A human handed you the goal precisely so they would
not have to narrate each click.

The ONLY things that stop you are:

- a **signature / unlimited approval** — a human must sign (it moves real value)
- a **CAPTCHA / MFA** — a human must solve it
- the task being **genuinely complete** — then you report what you did and the
  evidence, and stop. Completion is a result, not a question.

Anything else — a modal you did not expect, a reordered layout, a cookie
banner, a "continue" button — you handle yourself and keep going.
## Execution

For each step in order:

1. **Read the requirement as the site states it, and quote it.** Requirements
   change; a paraphrase is not evidence of what was asked.
2. **Work out how to satisfy it on the page in front of you.** Snapshot,
   identify the relevant elements, act. If the layout is not what you expected,
   adapt — do not force a sequence that was right last week.
3. **Verify against the site's own confirmation**, not against your assumption.
   A quest board that still shows "incomplete" means it is incomplete, whatever
   the transaction looked like.
4. Screenshot.
5. Log:

```bash
haa campaign log <slug> <step> ok --detail "quest 3/5 complete, 200 pts" --points 200
```

6. **If the flow differed from what was recorded, update the record.** The next
   run should not rediscover the same surprise:

```bash
haa campaign log <slug> <step> ok --detail "layout changed: claim moved under a 'Rewards' tab"
```


## Spend steps

Anything that moves funds — bridge, swap, stake, deposit, approve — is gated:

- Check the cost against `HAA_MAX_SPEND_USD` in `.env` first.
- If it exceeds the limit, stop and ask. Do not split it into smaller
  transactions to get under the limit; that defeats the control.
- The signature itself is always performed by the operator. This system does
  not hold keys.
- Read the approval payload. `setApprovalForAll` and unlimited ERC-20 approvals
  are how wallets get drained. Surface them explicitly and let the operator
  decide.

## Halt conditions

Same list as `daily-executor`: CAPTCHA, MFA, signature prompts, expired
sessions, and anything unclassifiable. Halt, log as `halted`, alert.

One more, specific to onboarding: if a step is **permanently unavailable** to
you (region-blocked, waitlist, KYC required), log it as `skipped` with the
reason and stop the sequence. Do not look for a way around a control the
project deliberately put in place.

## Rules

- Complete steps **in order**. Later steps often depend on earlier state.
- One step at a time. Verify before the next.
- Never proceed past a failed step — the later steps will fail too and you will
  have burned time and possibly money.
- Every completed step gets a screenshot and a ledger entry.
- If the campaign has no verification UI, say so in the log rather than
  claiming success.
