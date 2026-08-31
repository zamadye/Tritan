---
name: airdrop-analyzer
description: "Evaluate an airdrop opportunity on four dimensions (Team, Product, Narrative, Timing) and return a scored PRIORITIZE / CONSIDER / SKIP verdict."
version: 1.0.0
author: Hermes Airdrop Agent
license: MIT
platforms: [linux, macos, windows]
metadata:
  hermes:
    tags: [Airdrop, Research, Analysis, Crypto, Due-Diligence]
    related_skills: [portfolio-tracker, wallet-isolation]
---

# Airdrop Project Analyzer

Decide whether a project is worth weeks of attention. Most are not.

This skill is the **evidence-gathering** half. The scoring half is deterministic
code in `hermes_airdrop/analyzer.py` — do not re-implement it in prose. Your job
is to fill in twelve 0–3 ratings with citations, then call the CLI.

## Source of the framework

The four dimensions come from HTX Insights, *"The Last Time I'll Talk About
Backpack, and Also Discussing My Airdrop Farming Principles"* (Princess
Christine / @0xsexybanana, 2026-03-23). It contrasts a "shotgun" approach
(participate in everything, compete on execution) with a "sniper" approach
(screen hard, participate deeply in a few). This skill implements the sniper
screen.

## Ratings

Every rating is an integer **0–3**:

| | Meaning |
|---|---|
| 0 | Absent, or actively bad |
| 1 | Weak, or you could not verify it |
| 2 | Clearly present |
| 3 | Strong, independently verified |

A `1` is honest. It lowers confidence and pushes the verdict to human review —
which is the correct outcome when you could not confirm something. Do not
inflate to a 2 to make a project look better.

### 1. Team — "smart enough, good enough execution, good enough heart"

- `--team-insight` — Do founder posts show genuine understanding of their
  industry, or only slogans? Read 20+ posts before rating.
- `--team-execution` — Have they shipped, on schedule, and iterated?
- `--team-integrity` — Humble? Honest about failures? Not just shilling?

All three are required — none can be missing. A `0` anywhere in Team zeroes the
whole dimension.

### 2. Product — "PMF, competent delivery, responsible attitude to quality"

- `--product-pmf` — Does it solve a problem people actually pay to solve?
- `--product-delivery` — Use it yourself. Any low-level bug in normal use?
- `--product-responsibility` — Does the team own quality and fix things fast?

`--product-delivery 0` is a hard veto on its own. The source is blunt: teams
that ship shoddy products do not run good airdrops.

### 3. Narrative — "new, un-falsified track with a valuation premium"

- `--narrative-web3` — Is the narrative promising and not yet falsified?
- `--narrative-web2` — Does it align with a Web2 capital trend (AI, robotics)?
- `--narrative-premium` — Does it command a valuation premium *today*?

### 4. Timing & Cost — these three are **inverted**: 0 is good

- `--timing-fomo` — 0 = calm. 3 = your entire feed is telling you to farm it.
- `--timing-cost` — 0 = ~free per action. 3 = expensive per action.
- `--timing-crowding` — 0 = few farmers. 3 = everyone is farming it.

`--timing-crowding 3` is a hard veto: an overcrowded airdrop yields minimal or
negative returns no matter how good the project is.

## Procedure

Everything below happens in the **browser**. There is no API for any of it, and
a docs page is marketing — it is not evidence.

1. Read the docs, then **open the product and use it**. Complete a real flow:
   connect a wallet on the farming tier, do one small action, watch how the UI
   behaves. Reading is not evidence of delivery.
2. Read the founders' posts — at least 20, spanning months, not just launch week.
3. Check the investors and the funding round. Note who is *not* there.
4. Estimate cost per action and current crowding from community size and volume.
5. Screenshot what you saw — the product working (or not) is the strongest
   signal in the whole assessment.
6. Run the scorer:

```bash
haa analyze --project "Project Name" --url "https://..." \
  --team-insight 2 --team-execution 3 --team-integrity 2 \
  --product-pmf 2 --product-delivery 3 --product-responsibility 2 \
  --narrative-web3 3 --narrative-web2 2 --narrative-premium 2 \
  --timing-fomo 1 --timing-cost 1 --timing-crowding 1 \
  --save-to
```

`--save-to` writes the verdict onto a campaign record so the decision is
auditable months later.

## Interpreting the result

| Decision | Meaning |
|---|---|
| `PRIORITIZE` | ≥ 7.0/10, no veto. Worth 4+ weeks of consistent action. |
| `CONSIDER` | 5.0–6.9. Watch it; do not commit volume yet. |
| `SKIP` | < 5.0, or a hard veto. Record why and move on. |

**Confidence below 0.70 means human review.** That happens when too many
ratings are 1 or 2 — i.e. you guessed. Go verify, then re-score.

## Hard vetoes (force SKIP regardless of score)

- Product delivery is unusable
- Everyone is already farming it
- The operator is hesitating — *"if you feel hesitant, it's best not to participate"*
- High participation cost during peak FOMO

A veto caps the overall score at 4.0, so a report can never read "9/10 but
skipped" and confuse whoever reads it next month.

## Rules

- **Be ruthless.** The default answer is SKIP. A SKIP costs nothing; a bad
  PRIORITIZE costs weeks.
- Never rate a product you have not used.
- Never rate a founder you have not read.
- Do not let a strong narrative compensate for a broken product — the weighting
  already reflects that, and the veto will catch it anyway.
- One decision per project. Do not re-score the same project repeatedly until
  you get the answer you wanted.
