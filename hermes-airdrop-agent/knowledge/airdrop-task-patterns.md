# Airdrop Task Patterns

Every airdrop is different. This file exists so an agent **recognises** a
requirement instead of guessing at it. Read the project's own task list first;
use this only to interpret what you find.

---

## The atomic task types

Almost every airdrop checklist decomposes into these. Identify which ones a
project uses, in what order, and which repeat.

### 1. Register

Create an account. Almost always the first step and a hard prerequisite for
everything after it.

- **Needs:** an email address, sometimes a password you must record somewhere
  the operator can reach
- **Referral links** (`?r=CODE`, `/ref/CODE`) must be used *exactly as given*.
  Registering without the code usually means the account is not attributed,
  and there is no way to fix it afterwards.
- **Verify:** the account exists — you can log out and log back in, or the
  dashboard shows your address/email

### 2. Connect wallet

Link an EVM (or Solana/Cosmos) address.

- **Needs:** the operator to sign in their own wallet. **This is never done by
  the agent.** Stop and ask.
- Two different things get conflated here: *submitting an address as text*
  (a form field — the agent can do it) versus *signing a message to prove
  ownership* (the operator must do it). Read which one the site wants.
- **Verify:** the address appears on the dashboard, and any "connected" badge
  is present

### 3. Connect social (Twitter/X, Discord, Telegram)

OAuth or a follow/join check, often via Galxe, Layer3, Zealy, or QuestN.

- **Needs:** an already-authenticated social session in the browser profile
- These frequently open a popup or a new tab — check both
- **Verify:** the task row flips to completed **on the quest platform**, not
  just the OAuth redirect succeeding

### 4. Submit email address

A plain form field. Distinct from register: some projects ask for it
separately, after the account exists.

- **Verify:** a confirmation message, or the value shown back on the dashboard

### 5. Complete task / easy task

Vague on purpose. Could be: read a page, follow an account, join a channel,
answer a quiz, make one trade, hold a balance.

- **Never assume.** Open it and read what it actually requires.
- If it needs a signature or a spend, escalate — do not proceed

### 6. Daily mission

Recurring. This is the one that makes a campaign worth running.

- **Establish the reset time and its timezone.** Projects reset at 00:00 UTC,
  at 00:00 in some local zone, or on a rolling 24 hours. Getting this wrong
  means either double-running or missing days.
- Schedule it with `haa campaign add-action <slug> "daily_mission@<cron>"`
- A streak is the whole point: a missed day is worth more than the day itself

### 7. On-chain actions (swap, bridge, stake, provide liquidity)

The expensive ones. Always gated.

- Check cost against `HAA_MAX_SPEND_USD` **before** acting
- The operator signs. Always.
- Record the transaction hash in the log detail so it can be checked later

---

## Worked examples

### MemeBitcoin

```
Register (referral) → Connect Twitter → Complete Easy Task
→ Submit Email Address → Submit EVM Address → Complete Daily Mission
```

- Six steps. Five are one-shot; the last recurs.
- Needs: an email, a Twitter session, an EVM address, and a signature for the
  wallet step.
- Ordering matters: the email and EVM steps presuppose the account exists.

### Elyon

```
Register (referral) → Connect EVM Wallet → Complete Task
```

- Three steps, all one-shot. No daily mission — do not invent one.
- "Reward Confirmed For All Valid Users" is marketing copy, not a task. Ignore
  it; it is not something you complete.
- Needs: an EVM wallet signature, and whatever "Complete Task" turns out to be
  once you open it.

**The point:** these two share the word "airdrop" and almost nothing else. One
needs Twitter and an email; the other needs neither. One recurs daily; the
other is finished in an afternoon. Any plan that treats them the same is wrong.

---

## Reading a raw announcement

Announcements arrive as loose Telegram text. Extract:

| Field | Where to look |
|---|---|
| Project name | The heading, usually after an emoji |
| Registration URL | The link that carries a referral marker (`?r=`, `/ref/`) |
| Referral code | Inside that URL — do not drop it |
| Task list | Lines starting with `➖`, `-`, `•`, or numbered |
| Reward info | `🎁` lines — **note it, do not act on it** |
| Links to ignore | Telegram channel links, "bot version" links, other groups |

Then **open the registration URL and read the real task list**. Announcements
go stale within days. Where the announcement and the site disagree, the site
wins — and record the disagreement, because it tells you the announcement
cannot be trusted next time either.

---

## What is not a task

- Reward announcements ("Confirmed for all valid users")
- Links to Telegram channels or other groups
- "Share this post"
- Anything requiring you to post publicly on the operator's behalf — draft it,
  never post it
