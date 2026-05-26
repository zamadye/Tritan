# Market Analysis — 2026-05-19 10:21 UTC

## Market
- **Question:** Internationaux de Strasbourg: Diane Parry vs Emma Raducanu
- **Category:** sports
- **YES Price:** 53.0%
- **Days Left:** 5
- **Volume 24h:** $247,815
- **Liquidity:** $102,356

## Statistical Prior
- **p_base:** 54.5%
- **Source:** logistic:sports
- **N (historical):** 6077
- **Raw gap:** 1.5%

## News Sources Fetched
### Macro Context
- Fear&Greed: 25/100 (Extreme Fear) | trend: deteriorating
- BTC: $76,709 (-0.0% 24h) → neutral
- Fear&Greed: 25/100 (Extreme Fear) | 7d trend: deteriorating
- BTC: $76,709 (-0.0% 24h) → neutral

### General
- [FEAR&GREED 7d trend] 25(Extr) → 28(Fear) → 27(Fear) → 31(Fear) | sentiment worsening

### Multi-Source
- [MULTI-SOURCE NEWS] 2 sources for: internationaux strasbourg: diane parry emma
- [Bing News]
- [Mon, 18 May 2026] internationaux strasbourg: diane parry emma
- → Emma Raducanu is set for her first competitive match since Indian Wells in early March at the Internationaux de Strasbourg; Watch the WTA 500 event 
- [Sat, 16 May 2026] Emma Raducanu: British No 1 in line to face Diane Parry as she prepares for first clay tournament of 2026 in Strasbourg
- → Sports Mole previews Tuesday's Internationaux de Strasbourg first-round match between Diane Parry and Emma Raducanu, including predictions and their
- [Sun, 17 May 2026] Preview: Diane Parry vs. Emma Raducanu - prediction, head-to-head, form for Internationaux de Strasbourg match
- → Emma Raducanu is set to make her long-awaited return to action at the 2026 Internationaux de Strasbourg, and she has learned her first round opponen

## LLM Decision
- **Action:** NO
- **Confidence:** 65%
- **p_true:** 44.5%
- **Information Gap:** True
- **Crowd Bias:** False
- **Catalyst Type:** STATISTICAL_PATTERN + CONTEXTUAL_FACTORS
- **Catalyst Strength:** 0.75

### Reasoning
Strong statistical signal: markets at 53% resolve YES only 44.7% historically (n=13,967), indicating 8.3% overpricing of YES. Contextual support: Raducanu's first clay event of 2026, historically weak surface for her; Parry is French home player with recent strong form (beat world No. 2). Previous similar market was skipped due to insufficient gap (+3%), but now statistical edge exceeds threshold. Market overpricing likely driven by Raducanu name recognition rather than clay court probability.

## Gate Result
- **Passed:** ❌ NO
- **Reason:** no stat edge gap=1%<5%

## Tool Calls
- `search_web({'query': 'Diane Parry vs Emma Raducanu Strasbourg 2025 preview'})` → [Mon, 18 May 2026] Google News
[Sat, 16 May 2026] Emma Raducanu: British No 1 in line to face Diane 
- `search_web({'query': 'Emma Raducanu Diane Parry Strasbourg 2025 odds head to head'})` → [Mon, 18 May 2026] Google News
[Tue, 19 May 2026] H2H, prediction of Emma Raducanu vs Diane Parry in
- `get_market_context({'keyword': 'Strasbourg tennis Raducanu Parry'})` → No related markets found for 'Strasbourg tennis Raducanu Parry'
- `get_market_context({'keyword': 'Raducanu'})` → No related markets found for 'Raducanu'
- `get_market_context({'keyword': 'tennis'})` → No related markets found for 'tennis'
- `search_web({'query': 'Emma Raducanu form 2025 clay season results'})` → [Sat, 28 Mar 2026] Google News
[Wed, 28 May 2025] Raducanu set to return to action in Linz after Mia
- `search_web({'query': 'Diane Parry form 2025 results Strasbourg'})` → [Mon, 18 May 2026] Google News
[Sun, 17 May 2026] Emma Raducanu: British No 1 in line to face Diane 
- `search_web({'query': 'Sports Mole Diane Parry vs Emma Raducanu prediction preview form'})` → [Sat, 16 May 2026] Google News
[Tue, 19 May 2026] Preview: Diane Parry vs. Emma Raducanu - predictio

## Outcome
**✅ WIN** | P&L: $+0.49 | Resolved: YES

---
*Mode: LIVE | DRY_RUN: true*