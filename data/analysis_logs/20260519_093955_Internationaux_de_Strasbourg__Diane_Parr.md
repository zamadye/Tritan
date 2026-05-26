# Market Analysis — 2026-05-19 09:39 UTC

## Market
- **Question:** Internationaux de Strasbourg: Diane Parry vs Emma Raducanu
- **Category:** sports
- **YES Price:** 56.0%
- **Days Left:** 5
- **Volume 24h:** $169,614
- **Liquidity:** $75,897

## Statistical Prior
- **p_base:** 59.0%
- **Source:** logistic:sports
- **N (historical):** 6077
- **Raw gap:** 2.9%

## News Sources Fetched
### Macro Context
- Fear&Greed: 25/100 (Extreme Fear) | trend: deteriorating
- BTC: $76,716 (-0.3% 24h) → neutral
- Fear&Greed: 25/100 (Extreme Fear) | 7d trend: deteriorating
- BTC: $76,716 (-0.3% 24h) → neutral

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
- **Action:** SKIP
- **Confidence:** 55%
- **p_true:** 59.0%
- **Information Gap:** False
- **Crowd Bias:** False
- **Catalyst Type:** STATISTICAL_PATTERN
- **Catalyst Strength:** 0.45

### Reasoning
Strong statistical signal (44.7% YES rate at 56% price, n=13,967) supports NO, but gap (+3%) is below 5% gate threshold. Additionally, 50-60% entry zone historically has only 33% WR. While Raducanu's 2+ month absence and first clay match of 2026 support the bearish case, not enough concrete edge to bet. Wait for line movement or better entry.

## Gate Result
- **Passed:** ❌ NO
- **Reason:** no stat edge gap=3%<5%

## Tool Calls
- `get_sports_data({'sport': 'tennis', 'team': 'Raducanu'})` → No injury data found for tennis Raducanu
- `get_sports_data({'sport': 'tennis', 'team': 'Diane Parry'})` → No injury data found for tennis Diane Parry
- `search_web({'query': 'Raducanu vs Diane Parry Strasbourg 2025 preview prediction'})` → [Sat, 16 May 2026] Google News
[Mon, 18 May 2026] Preview: Diane Parry vs. Emma Raducanu - predictio
- `search_web({'query': 'Emma Raducanu recent form results 2025 clay court'})` → [Sat, 28 Mar 2026] Google News
[Wed, 25 Feb 2026] Raducanu set to return to action in Linz after Mia
- `get_market_context({'keyword': 'Strasbourg tennis Raducanu Parry'})` → No related markets found for 'Strasbourg tennis Raducanu Parry'
- `get_odds({'sport': 'tennis_atp', 'team': 'Raducanu'})` → Odds API error: 404 {"message":"Unknown sport","error_code":"UNKNOWN_SPORT","details_url":"https://t
- `search_web({'query': '"Diane Parry" vs "Emma Raducanu" Strasbourg odds 2026'})` → [Tue, 19 May 2026] Google News
[Sun, 17 May 2026] Tennis Picks Today: 5 Best Bets &amp; Predictions 
- `search_web({'query': 'Emma Raducanu 2026 results form clay season'})` → [Mon, 18 May 2026] Google News
[Sat, 16 May 2026] Emma Raducanu: British No 1 in line to face Diane 
- `get_market_context({'keyword': 'tennis Parry'})` → No related markets found for 'tennis Parry'
- `search_web({'query': 'Raducanu vs Parry head to head record tennis'})` → [Tue, 19 May 2026] Google News
[Sat, 16 May 2026] Tennis Picks Today: 5 Best Bets &amp; Predictions 
- `search_web({'query': 'WTA Strasbourg 2026 draw results today'})` → [Mon, 18 May 2026] Google News
[Tue, 19 May 2026] Eala vs. Oliynykova | Round of 32 Internationaux d
- `search_web({'query': 'Raducanu Parry Strasbourg prediction picks odds favorite'})` → [Sun, 17 May 2026] Google News
[Mon, 18 May 2026] Diane Parry vs. Emma Raducanu prediction, odds, pi
- `search_web({'query': 'Emma Raducanu clay court 2026 first tournament season'})` → [Mon, 18 May 2026] Google News
[Wed, 13 May 2026] Emma Raducanu: British No 1 in line to face Diane 

## Outcome
**✅ WIN** | P&L: $+0.49 | Resolved: YES

---
*Mode: LIVE | DRY_RUN: true*