# Worked example: Monad

A real, complex campaign, used as the reference case for how this system is
supposed to decompose work. Sources: airdrops.io/monad, dropstab.com Monad
testnet tutorial, oneclick.fi Monad guide (researched 2026-08-26).

**Monad's testnet has ended and mainnet launched.** This is kept as a structural
example — the shape of the work, not a live target. Current campaigns will have
different dApps but the same structure.

---

## Why this is the hard case

Not 2 steps. Roughly **30–50 distinct actions across ~15 separate dApps**, with
ordering constraints between them and prerequisites that live outside the
campaign entirely.

## The shape of it

### Layer A — prerequisites (outside the campaign, can block everything)

| Requirement | Needed by |
|---|---|
| EVM wallet with Monad RPC added | everything |
| 0.03 ETH + 3 Ethereum mainnet transactions | the official Monad faucet |
| $1.00+ of transactions on Gas.zip | the Gas.zip faucet |
| ~18.1 POL on Polygon | the Nerzo faucet |
| A Morkie ID (minted on another chain) | the Morkie faucet |

**These are not steps in the campaign.** They are gates. If none of the
faucets can be claimed, nothing downstream is possible — and the right response
is to stop and say so, not to grind through 40 failing actions.

This is what `depends_on` exists for: model the gate, let the planner refuse
the rest.

### Layer B — one-shot onboarding

```
add Monad RPC to wallet
claim faucet (whichever one you qualify for)
connect wallet on the campaign dashboard
connect X / Twitter
connect Discord
create account on Talentum (+ choose a username)
```

### Layer C — the long tail, one action per dApp

```
Layer3        complete the Monad campaign quests
Monadverse    mint NFT (free)
Lil Chogstars mint NFT (free)
Herb Genesis  mint NFT (free)
Owlto         deploy a test smart contract
PancakeSwap   swap on testnet
aPriori       stake MON
Uniswap       swap (select Monad via the network button)
Orbiter       swap
Ambient       swap and/or provide LP
Izumi         trade or provide LP
Kintsu        stake and unstake
MoMoney       Farcaster mini-app
Monad Twist   Farcaster mini-app
Magic Eden    publish an NFT to Monad testnet
```

Each of these is its own site with its own UI. **Each gets its own `group`**,
so a run is checkpointed per dApp and can resume instead of restarting.

### Layer D — recurring

```
faucet claim          daily (most reset on a 6-12h timer)
Talentum streak       daily ("Streak Now")
Discord #social-credit role   once, but re-checkable
```

---

## How this maps onto the data model

```bash
# Layer A — the gate. Everything else depends on it.
haa campaign add-action monad "add_rpc@once"      --kind browser --tier connect --network monad-testnet
haa campaign add-action monad "claim_faucet@once" --kind browser --tier testnet --network monad-testnet

# Layer B
haa campaign add-action monad "connect_wallet@once" --kind browser --tier connect \
    --depends-on add_rpc
haa campaign add-action monad "connect_x@once"      --kind browser --tier connect
haa campaign add-action monad "talentum_signup@once" --kind browser --tier connect

# Layer C — one group per dApp
haa campaign add-action monad "apriori_stake@once"  --kind browser --tier testnet \
    --group apriori --network monad-testnet --depends-on claim_faucet
haa campaign add-action monad "uniswap_swap@once"   --kind browser --tier testnet \
    --group uniswap --network monad-testnet --depends-on claim_faucet

# Layer D
haa campaign add-action monad "faucet_daily@0 9 * * *"  --kind browser --tier testnet
haa campaign add-action monad "talentum_streak@0 9 * * *" --kind browser --tier testnet
```

Note what is **absent**: no selector, no XPath, no click sequence, no
coordinates. Each entry names an outcome and where it happens. The agent works
out how, from the live page, every run.

## What the tiered approval buys here

Almost all of Monad is testnet. Under the old "the operator signs everything"
rule this campaign would need **30–50 human interventions** for tokens with no
value.

Under the tiered model:

| Action | Tier | Who acts |
|---|---|---|
| Navigate, read a quest board, screenshot | `read` | autonomous |
| Connect wallet, add network | `connect` | autonomous |
| Testnet swap, stake, mint, deploy | `testnet` | autonomous |
| Unlimited `approve`, `setApprovalForAll` | `critical` | **human — even on testnet** |

The last row stays manual on testnet deliberately. Blind-approving is a habit,
and the habit is what causes mainnet losses later.

## What still needs a human

**Browser extensions.** Primus asks you to install its extension; Miden asks
you to install the Miden Wallet extension. **CDP automation cannot install a
Chrome extension.** There is no workaround.

Model these as `--kind manual_setup`: the run stops, tells the operator what to
install, and resumes afterwards. Pretending otherwise produces a run that
silently fails at that step.

## Traps worth recording

- **Faucet timers.** Most reset every 6–12 hours. Claiming twice in one run
  just produces a failure that looks like a broken faucet.
- **Layer3 verification lag.** It can take time to recognise a transaction.
  Refresh and wait; do not retry the underlying action.
- **Address consistency.** The wallet you act with must match the one the task
  expects, or verification silently never completes.
- **"Layer3 task not recorded"** is usually lag or a wrong address, not a
  failure. Log it as such rather than re-running the swap.
