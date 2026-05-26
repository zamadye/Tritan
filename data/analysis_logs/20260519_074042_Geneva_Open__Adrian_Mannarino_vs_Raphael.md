# Market Analysis — 2026-05-19 07:40 UTC

## Market
- **Question:** Geneva Open: Adrian Mannarino vs Raphael Collignon
- **Category:** sports
- **YES Price:** 11.0%
- **Days Left:** 6
- **Volume 24h:** $71,445
- **Liquidity:** $24,401

## Statistical Prior
- **p_base:** 4.2%
- **Source:** logistic:sports
- **N (historical):** 6077
- **Raw gap:** 6.8%

## News Sources Fetched
### Macro Context
- Fear&Greed: 25/100 (Extreme Fear) | trend: deteriorating
- BTC: $77,067 (+0.1% 24h) → neutral
- Fear&Greed: 25/100 (Extreme Fear) | 7d trend: deteriorating
- BTC: $77,108 (+0.2% 24h) → neutral

### General
- [FEAR&GREED 7d trend] 25(Extr) → 28(Fear) → 27(Fear) → 31(Fear) | sentiment worsening

### Multi-Source
- [MULTI-SOURCE NEWS] 2 sources for: geneva open: adrian mannarino raphael
- [Bing News]
- [] geneva open: adrian mannarino raphael
- [Metaculus]
- [] Will the next IPC Sudan acute food insecurity analysis classify at lea
- → Community: pending
- [] Will the Senate of the Philippines remove Vice President Sara Duterte
- → Community: pending

## LLM Decision
- **Action:** SKIP
- **Confidence:** 45%
- **p_true:** 5.0%
- **Information Gap:** True
- **Crowd Bias:** False
- **Catalyst Type:** NONE
- **Catalyst Strength:** 0.10

### Reasoning
Low-information market with insufficient verifiable edge. Despite finding prediction articles, cannot verify specific matchups, form, or injuries. Previous decisions (35%, 38% confidence) correctly identified lack of edge. Market shows +7% gap (11% vs 4% base) but unclear if mispriced. No concrete evidence that YES or NO is underpriced. Cannot confirm clear path to YES becoming more likely. Confidence well below 0.70 threshold for BET.

## Gate Result
- **Passed:** ❌ NO
- **Reason:** low conf 45%<52%

## Tool Calls
- `search_web({'query': 'Adrian Mannarino vs Raphael Collignon Geneva Open 2025'})` → [Mon, 18 May 2026] Google News
[Sun, 17 May 2026] ATP Geneva Day 3 Predictions Including Casper Ruud
- `search_web({'query': 'Raphael Collignon ATP Geneva Open 2025'})` → [Mon, 18 May 2026] Google News
[Sun, 17 May 2026] ATP Geneva Day 3 Predictions Including Casper Ruud
- `get_odds({'sport': 'tennis_atp', 'team': 'Mannarino'})` → Odds API error: 404 {"message":"Unknown sport","error_code":"UNKNOWN_SPORT","details_url":"https://t
- `get_market_context({'keyword': 'Geneva Open'})` → No related markets found for 'Geneva Open'
- `search_web({'query': 'Mannarino vs Collignon prediction Geneva Open 2025 odds'})` → [Sun, 17 May 2026] Google News
[Wed, 04 Mar 2026] Mannarino vs. Collignon Prediction at the Gonet Ge
- `search_web({'query': 'Raphael Collignon form ATP 2025'})` → [Fri, 20 Mar 2026] Google News
[Tue, 03 Mar 2026] Has Boynton made Opelka's serve even better? Drape
- `search_web({'query': 'Mannarino recent results 2025'})` → [Wed, 13 Aug 2025] Google News
[Fri, 29 Aug 2025] Sinner finds way past stubborn Mannarino in Cincin
- `search_web({'query': 'Raphael Collignon recent results 2025'})` → [Fri, 29 Aug 2025] Google News
[Tue, 03 Mar 2026] Brain surgeon’s son Collignon on finding the menta
- `get_market_context({'keyword': 'Mannarino'})` → No related markets found for 'Mannarino'
- `search_web({'query': 'Mannarino vs Collignon prediction Bleacher Nation'})` → [Sun, 17 May 2026] Google News
[Sat, 16 May 2026] Mannarino vs. Collignon Prediction at the Gonet Ge
- `search_web({'query': '"Mannarino" "Collignon" prediction tennis 2025'})` → [Mon, 18 May 2026] Google News
[Sun, 17 May 2026] ATP Geneva Day 3 Predictions Including Casper Ruud
- `search_web({'query': 'Collignon ATP ranking 2025 Geneva clay'})` → [Mon, 18 May 2026] Google News
[Sun, 17 May 2026] ATP Geneva Day 3 Predictions Including Casper Ruud
- `search_web({'query': 'Adrian Mannarino ATP ranking 2025'})` → [Wed, 13 Aug 2025] Google News
[Fri, 29 Aug 2025] Mannarino: "I've lost to very, very bad players, i
- `search_web({'query': 'Raphael Collignon ATP ranking 2025'})` → [Fri, 29 Aug 2025] Google News
[Tue, 03 Mar 2026] Brain surgeon’s son Collignon on finding the menta
- `search_web({'query': 'Mannarino Collignon head to head tennis'})` → [Mon, 18 May 2026] Google News
[Sat, 16 May 2026] ATP Geneva Day 3 Predictions Including Casper Ruud
- `search_web({'query': 'Geneva Open 2025 results today'})` → [Sun, 11 Jan 2026] Google News
[Sat, 18 May 2019] Hugo Gaston Tournament Results - ESPN
[Tue, 18 Nov

## Outcome
_Pending — will be updated when market resolves_

---
*Mode: LIVE | DRY_RUN: true*