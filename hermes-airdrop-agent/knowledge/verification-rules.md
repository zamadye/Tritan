# Verification Rules

What counts as proof that a step happened. This is the file that stops the
system from lying to its operator.

---

## The one rule

> **A step is done when the site says so. Not when the button was clicked.**

An operation that records successes it did not confirm is worse than one that
does nothing, because the operator keeps believing it works while nothing is
happening.

---

## Evidence hierarchy

From strongest to weakest. Use the strongest available; if only a weak one
exists, say so in the log.

| Strength | Evidence | Example |
|---|---|---|
| **Strong** | On-chain transaction hash | `0xabc…` visible in the site's history *and* on an explorer |
| **Strong** | A state change that persists across a reload | Points counter went 150 → 300 and is still 300 after refresh |
| **Good** | A timestamped confirmation | "Last check-in: 2026-08-26 09:14 UTC" |
| **Good** | A task row flipping to completed | Quest board shows ✓ |
| **Weak** | A toast/popup that disappears | "Success!" — gone in 3 seconds, unverifiable later |
| **Not evidence** | The absence of an error | Proves nothing. Pages fail silently all the time. |
| **Not evidence** | A button appearing disabled after clicking | Could be a client-side state change with no server write |

**Always reload the page before accepting a state change.** A counter that
incremented client-side but never reached the server will revert on reload.
This single habit catches most false successes.

---

## Per task type

| Task | What proves it |
|---|---|
| Register | You can log out and log back in, or the dashboard shows the account |
| Connect wallet | The address is displayed on the dashboard after a reload |
| Submit email | The value is shown back, or a confirmation message appears |
| Connect social | The task row shows completed **on the quest platform** |
| Daily mission | Today's date appears next to the mission, or the counter incremented and survives a reload |
| Swap / bridge / stake | Transaction hash, confirmed on an explorer |
| Claim | Balance increased, or a claim history entry exists |

---

## Screenshot discipline

- Capture the **confirmation**, not the page before the action
- Include whatever identifies it: the account, the date, the counter
- Save to `data/campaigns/<slug>/screenshots/`
- Reference the path with `--evidence` so the ledger hashes it

`haa evidence verify` re-hashes every referenced artifact. A mismatch means a
proof changed after it was recorded — that leads the report, because the
evidence trail is the only way to distinguish "I did this" from "I believe I
did this".

---

## When verification is impossible

Some projects give no confirmation UI at all. That is a real situation, not an
excuse to guess.

Log it as `ok` **only** with an explicit note:

```bash
haa campaign log <slug> <action> ok --detail "no confirmation UI; button state changed only"
```

Never silently mark it done. The operator needs to know which claims are solid
and which are hopeful.

---

## Failure versus halt

These are different and must be logged differently.

| Situation | Log as | Then |
|---|---|---|
| The action failed (error, 503, element not found) | `failed` | Retry once. Then move on and report. |
| A human must intervene (CAPTCHA, MFA, signature) | `halted` | Stop. Alert. Do not retry — retrying a challenge makes it worse. |
| The step does not apply (already done, region-blocked, KYC) | `skipped` | Record why. Do not work around it. |
| It worked and you proved it | `ok` | Screenshot, log, continue. |

---

## The spend rule

Nothing above `HAA_MAX_SPEND_USD` without an explicit decision from the
operator. And **never split an action into smaller ones to get under the
limit** — that defeats the entire purpose of having a limit.

If the cost is close to the limit, ask anyway. Being asked once is cheaper than
being wrong once.
