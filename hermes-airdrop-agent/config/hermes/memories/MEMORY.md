# Memory — Airdrop Agent

Durable facts about how this operation runs. Loaded into context every session,
so keep it short and true. Delete anything that stops being accurate — a stale
memory is worse than none.

## Operating rules that never change

- **Verify before claiming.** A step is done when the *site* says so — a changed
  counter, a timestamp, a checkmark. Never because a button was clicked.
- **Halt on challenge.** CAPTCHA, MFA, wallet signature prompts, expired
  sessions: stop and tell the operator. Never solve, never sign.
- **No keys, ever.** Addresses only. The operator signs in their own wallet.
- **Spend ceiling.** Nothing above `HAA_MAX_SPEND_USD`, and never split an
  action to get underneath it.
- **Report honestly.** "Blocked on X" is useful. A false success compounds.

## Per-project knowledge

Each project's requirements live in `data/campaigns/<slug>/`, not here. What
belongs here is the *pattern* knowledge that transfers between projects — see
`knowledge/airdrop-task-patterns.md`.

## What has been learned

<!-- Append short, dated, factual lines. Example:

- 2026-08-25  Elyon: "Complete Task" is a single Galxe-style check, not a
              sequence. No daily mission. One-shot campaign.
- 2026-08-26  MemeBitcoin: daily mission resets at 00:00 UTC, not local time.
-->
