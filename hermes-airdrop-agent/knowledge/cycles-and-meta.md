# Cycles, meta and sentiment

The meta shifts. What worked in one cycle is worthless in the next, and a plan
built on last cycle's assumptions produces a lot of activity and no allocation.

Sources: HTX Insights' farming-principles piece, 2026 Base/Abstract/Monad
guides, sybil-detection writeups (researched 2026-08-26).

---

## The two farming styles

From the HTX piece, and the distinction is worth internalising because it
changes what "good" looks like:

- **Shotgun** — participate in everything, compete on execution, keep the cost
  per account low. High tolerance for waste; one big hit covers the rest.
- **Sniper** — screen hard, participate deeply in a few. Lower volume, much
  higher per-project conviction.

**This system implements Sniper.** The 4-dimension analyzer is the screen. If
you want Shotgun behaviour, that is a different tool — and note that Shotgun
at scale is precisely what anti-sybil systems are built to catch.

---

## What the meta looks like now

### Consistency beats intensity

Repeated across every 2026 guide, in almost the same words:

> *"An account with 60 days of weekly swaps looks far more organic than 60
> swaps done in a single day."* — Base farming guide

> *"One swap and one upvote per day for six months outperforms a week of heavy
> farming."* — Abstract guide

So the unit of work is **a day**, not a session. This is why `positions.py`
tracks streaks and why the daily cron exists at all. A system that can do 200
actions in an afternoon and then go quiet for a week is optimised for the
wrong thing.

### Protocol diversity beats raw volume

> *"Community analysis consistently points to protocol diversity as the key
> variable, not raw transaction volume."* — on `onchainscore.xyz`

Ten different protocols once each beats one protocol ten times. That is why
`ActionSpec.group` is per dApp: the plan should spread across protocols, not
grind one.

### Long lock-ups are the norm

Base wants an LP position left for **30 days**. Abstract wants **30
consecutive days** of daily upvotes for a permanent multiplier. Estimated
budget for a meaningful Base position: **$150–300 over 3–6 months**.

Airdrops are no longer a weekend activity. Any plan that finishes in a day is
probably not doing what the project is measuring.

---

## Narrative and sentiment

Two of the four analyzer dimensions are about this, and they are the ones most
often guessed at.

### Reading narrative

The question is not "is this project good" but "is this narrative still
unfalsified, and does Web2 capital agree?"

- A narrative that Web2 is funding heavily (AI, robotics, restaking at their
  peaks) carries a valuation premium that Web3 borrows.
- A narrative that has already been falsified — a category where the promised
  thing demonstrably did not arrive — is late, no matter how good the team is.

### Reading sentiment

The tell is in your own feed, not in the project's metrics:

- If every airdrop account you follow is posting about it, it is **crowded**.
  `--timing-crowding 3` is a hard veto: an overcrowded airdrop yields minimal
  or negative returns because the reward pool is split too many ways.
- If participation cost is high *and* the feed is loud, that is the worst
  combination — high cost, diluted reward.
- **If you hesitate, do not participate.** That is a direct quote from the
  source and it is encoded as a veto, because hesitation is usually pattern
  recognition working faster than the justification you are about to construct.

---

## Reading a project's sybil policy

Every project publishes its rules, usually in docs or a Discord announcement.
**Read them and take them at face value.**

What to look for:

- Whether multiple wallets per person are permitted at all
- Whether they use a third-party analytics firm or an on-chain clustering
  system
- Whether social identity is tied to the wallet (Base Verify does this
  explicitly)
- Whether there is a minimum account age or transaction history requirement

Then act on what you read. If the rules say one identity per allocation, run
one identity. This is not a constraint the system works around — see
`skills/wallet-isolation/SKILL.md`.

---

## Detection is real and it is layered

From the sybil-detection material, and worth knowing because it explains why
the "obvious" scaling tricks fail:

| Layer | What they check |
|---|---|
| Device | WebGL context, canvas hash, AudioContext curve, GPU model, fonts, screen |
| Network | IP, ASN, whether it is residential or datacentre |
| Session | Shared cookies, localStorage, OAuth tokens across profiles |
| Social | Discord/Twitter/Telegram/email linked across wallets |
| On-chain | Funding-source clustering, timing correlation, interaction-sequence similarity |

The practical consequence is not "get better at hiding". It is that **the
expected value of scaling by identity count is often negative** — you spend
more, get flagged, and lose the allocation on every linked address.

Which is the same conclusion the Sniper screen reaches from the other
direction: fewer, deeper, longer.

---

## What this means for the workflow

| Meta fact | How the system reflects it |
|---|---|
| Consistency beats intensity | Daily cron; streaks tracked in `positions.py` |
| Diversity beats volume | `ActionSpec.group` is per dApp; plans spread across protocols |
| Long lock-ups | `positions add --until <date>`; `expiring_soon` warns before a deadline |
| Crowding kills yield | `--timing-crowding 3` is a hard veto |
| Hesitation is signal | `--hesitating` forces a SKIP |
| Rules are published | `discord-engager` flags anti-sybil announcements; read at face value |
| Detection is layered | One real Chrome profile, one identity — see `wallet-isolation` |
