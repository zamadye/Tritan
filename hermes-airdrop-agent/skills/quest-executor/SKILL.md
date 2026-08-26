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

## Execution

For each step in order:

1. Read the requirement exactly as the site states it. Quote it in your notes —
   requirements change and a paraphrase is not evidence of what was asked.
2. Do the step.
3. **Verify against the site's own confirmation**, not against your assumption.
   A quest board that still shows "incomplete" means it is incomplete, whatever
   the transaction looked like.
4. Screenshot.
5. Log:

```bash
haa campaign log <slug> <step> ok --detail "quest 3/5 complete, 200 pts" --points 200
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
