---
name: wallet-isolation
description: "Keep wallet tiers separated so a mistake on a farming wallet cannot reach your main funds. Addresses only — never keys."
version: 1.0.0
author: Hermes Airdrop Agent
license: MIT
platforms: [linux, macos, windows]
metadata:
  hermes:
    tags: [Wallet, Security, Risk-Management, Hygiene]
    related_skills: [quest-executor, daily-executor]
---

# Wallet Isolation

Separate your capital into tiers so that the risky part of this activity cannot
reach the part that matters. This is ordinary operational security, and it is
worth doing even if you only ever use one wallet.

## The tiers

| Tier | Purpose | Used by the agent? |
|---|---|---|
| `main` | Long-term holdings. Cold storage if at all possible. | **Never** |
| `farming` | Daily interactions. Funded with what you can afford to lose. | Yes |
| `high-risk` | Unaudited contracts, brand-new protocols, testnets with value. | Yes |

```bash
haa wallets add --address 0xMain...  --tier main      --label "cold"
haa wallets add --address 0xFarm1... --tier farming   --label "farm-1"
haa wallets add --address 0xRisk1... --tier high-risk --label "experiment"
haa wallets audit
```

`haa wallets audit` fails if there is no `main` tier, no `farming` tier, or more
than one `main` — each of which defeats the point of having tiers.

## Rules that are enforced in code, not by convention

- **A campaign cannot be attached to a `main`-tier wallet.** `Store.save()`
  raises. The CLI refuses. This is not a warning you can talk yourself out of.
- **No private key, seed phrase, or keystore is ever stored.** `haa doctor`
  refuses to start if it finds key material in `.env`; the evidence ledger
  refuses to log it; `haa wallets add` rejects an address that looks like a
  key. Keys belong in a hardware wallet you control.
- **Spend actions always require approval.** `bridge`, `swap`, `stake`,
  `deposit`, `transfer`, `approve`, `claim`, `withdraw` cannot be pre-approved
  from config — the allow-list only covers non-spend actions.
- **A per-action spend ceiling** (`HAA_MAX_SPEND_USD`) halts anything above it.

## Funding hygiene

Fund each tier directly from the exchange. Do not chain transfers between your
own wallets — not to hide anything, but because a single compromised wallet
that can reach your others is a much larger loss. Tiers that cannot reach each
other contain the blast radius.

Keep the amounts small. The `farming` tier should hold only what a bad contract
interaction could take.

## What this skill deliberately does not do

**It does not help you present multiple wallets as multiple people.**

Specifically, there is no fingerprint spoofing, no per-wallet proxy assignment,
and no timing jitter designed to defeat a protocol's clustering. Those exist
for one purpose: to make one operator's wallets look like several unrelated
humans so a fraud-detection system allocates rewards multiple times. That is
deception of the counterparty, and a protocol that detects it is not
malfunctioning — it is working.

This system uses **one real Chrome instance with one real browser profile**
(see `README.md`). That is a deliberate consequence of the position above, not
an oversight: a genuine browser identity is exactly what a single genuine
participant looks like.

Two practical consequences worth stating plainly:

- Getting flagged costs you the allocation *and* usually the reputation of
  every address linked to it.
- Projects publish their anti-sybil rules. If a project says one identity gets
  one allocation, running thirty wallets is not a clever interpretation of the
  rules — it is breaking them, and the detection system is the enforcement.

If a project's rules permit multiple wallets per person (some testnets do), use
the tiers above and say so openly. If they do not, use one wallet.

## Reviewing an approval before signing

Before signing anything, read the payload:

- `setApprovalForAll` — grants an operator every token in a collection
- Unlimited ERC-20 approval — grants an unbounded token balance
- `permit2` — signature-based allowance; readable only with care
- Any call to a contract you have not verified

If you cannot read it, do not sign it. Revoke old approvals periodically.
