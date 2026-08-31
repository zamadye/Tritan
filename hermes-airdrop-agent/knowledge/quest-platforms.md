# Quest platforms

Most airdrop tasks do not live on the project's own site. They live on a quest
platform that aggregates tasks from many projects and verifies completion for
them. Each platform behaves differently, and the differences are where runs
fail.

Sources: Layer3/Galxe/Zealy guides, Monad and Abstract tutorials, airdrops.io
campaign listings (researched 2026-08-26).

---

## Galxe

**Model:** projects publish "campaigns" made of task groups. Complete a group,
claim an NFT badge or points.

**Flow:** connect wallet → verify Twitter/Discord → browse Spaces → join a
campaign → complete each task → **Claim**.

**What actually matters:**

- **Galxe Humanity Score.** Many campaigns gate on Level 1+. Check at
  `galxe.com/score`. If the score is too low no amount of task completion
  helps — this is a *prerequisite*, model it as a gate.
- **The green ✓ then Claim.** Completing a task shows a ✓, but the reward is
  only granted after you press Claim. A run that stops at the ✓ has done
  nothing. Verify the claim landed, not the checkmark.
- **Badges are the eligibility artefact.** Projects use Galxe NFT badges to
  qualify wallets at snapshot time. The badge in the wallet is the proof, not
  the Galxe UI.
- **Social binding is per-account and sticky.** Unbinding and rebinding can
  reset progress. Do not rebind to "fix" something.

---

## Layer3

**Model:** quests, often chain-specific, with automatic on-chain verification.

**Flow:** connect wallet + socials → pick a quest → follow the steps → proof is
usually submitted automatically.

**What actually matters:**

- **Verification lag.** Layer3 can take time to recognise a transaction. The
  standard failure here is retrying the underlying swap, which produces a
  second transaction and still no verification. **Refresh and wait.** Log it as
  lag, not as a failure.
- **Address consistency.** The wallet you act with must match the one the task
  expects. A mismatch means verification silently never completes, with no
  error anywhere.
- **Quests expire and go idle.** "No active quests right now" is a normal
  state, not a broken page.

---

## Zealy (formerly Crew3)

**Model:** project "spaces" with tasks worth XP; a visible rank.

**Flow:** connect wallet + Discord → join a space → complete tasks → track XP.

**What actually matters:**

- Tasks are frequently **social** (follow, retweet, join) rather than on-chain.
  These are exactly the actions the `discord-engager` skill refuses to
  automate at scale — draft, do not mass-post.
- XP and rank are the visible signal, but the airdrop decision is the
  project's, made off their own snapshot. Zealy rank is a proxy, not a promise.

---

## QuestN / TaskOn

Same shape as Galxe: aggregate tasks, verify, claim. Treat them the same way —
read the task list on the platform, not the announcement, and verify the claim
rather than the checkmark.

---

## Talentum (Monad's own)

**Model:** wallet + username + connected socials, plus **daily streaks**.

**Flow:** connect wallet → choose a username → connect social networks on the
homepage → "Streak Now" daily.

**What actually matters:**

- The username is chosen **once** and is part of the identity. Do not let a run
  pick one arbitrarily.
- Streaks are consecutive-day. A gap resets them. Use
  `haa positions streak <slug> <name>` so a missed day is visible before it is
  too late.

---

## Platform-native wallets

Some ecosystems issue their own wallet and the campaign is built around it:

- **Abstract** generates an "Abstract Global Wallet" automatically, separate
  from your MetaMask address. Both addresses matter and they are not the same.
- **Miden** requires installing its browser extension and registering an
  address through it.
- **WOW EARN** required its own mobile wallet, with the *mining* address
  submitted to the quest — not the EVM address.

**Trap:** submitting the wrong address is the single most common silent
failure. The quest accepts it, shows nothing wrong, and never verifies. Always
confirm *which* address the task wants before filling the field.

---

## Cross-platform patterns

| Pattern | Consequence |
|---|---|
| Connect wallet + socials first | Almost universal. Model it as the first action, with everything depending on it. |
| ✓ then Claim | Two steps, not one. Verify the claim. |
| Verification lag | Refresh and wait. Never re-run the underlying action. |
| Address mismatch | Silent, permanent, no error. Confirm the address before submitting. |
| Badges/XP are proxies | The project's own snapshot decides. Never promise a reward. |
| Social tasks | Draft, never mass-post. |
| Platform score gates | Humanity Score, Onchainscore, follower counts — these are prerequisites, not tasks. |

---

## What is a prerequisite, not a task

These block everything downstream and must be modelled as gates:

- Galxe Humanity Score level
- `onchainscore.xyz` score (Base recommends 50+; it weighs **protocol
  diversity** more than raw transaction count)
- Base Verify — needs a Coinbase account or a Twitter/X account with **100+
  followers and at least a year of history**
- A minimum wallet balance on a specific chain
- Prior transaction history ("wallets must not be newly created")

If a gate cannot be satisfied, **stop and say so**. Grinding 40 actions behind
an unsatisfiable gate produces a log full of failures and no eligibility.
