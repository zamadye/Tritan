# Market Analysis — 2026-05-16 16:54 UTC

## Market
- **Question:** Set Handicap: Gauff (-1.5) vs Svitolina (+1.5)
- **Category:** sports
- **YES Price:** 51.0%
- **Days Left:** 6
- **Volume 24h:** $17,544
- **Liquidity:** $5,555

## Statistical Prior
- **p_base:** 51.5%
- **Source:** logistic:sports
- **N (historical):** 6077
- **Raw gap:** 0.5%

## News Sources Fetched
### Macro Context
- Fear&Greed: 31/100 (Fear) | trend: deteriorating
- BTC: $78,176 (-1.3% 24h) → risk-OFF
- Fear&Greed: 31/100 (Fear) | 7d trend: deteriorating
- BTC: $78,233 (-1.3% 24h) → risk-OFF
- Fed market expectations:

### General
- [FEAR&GREED 7d trend] 31(Fear) → 43(Fear) → 34(Fear) → 42(Fear) | sentiment worsening
- Will the Fed decrease interest rates by 50+ bps after the Ju → YES=50%
- MicroStrategy sells any Bitcoin by May 31, 2026? → YES=50%
- [MULTI-SOURCE NEWS] 1 sources for: handicap: gauff -1.5 svitolina +1.5
- [Bing News]

## LLM Decision
- **Action:** NO
- **Confidence:** 65%
- **p_true:** 41.5%
- **Information Gap:** False
- **Crowd Bias:** False
- **Catalyst Type:** CROWD_BIAS
- **Catalyst Strength:** 0.75

### Reasoning
Strong statistical asymmetry: markets priced at 51% resolve YES only 44.7% of the time (n=13,967) — a 6.3% overpricing. Sports pattern confirms edge (WR=85% from 13 trades). No breaking news or injury reports found — Gauff and Svitolina both entering final in good form. The crowd appears to systematically overprice the YES (Gauff covering -1.5) at this price level, likely due to recency/narrative bias favoring the higher-ranked player. No specific information asymmetry found, but the consistent mispricing pattern is a strong standalone edge.

## Gate Result
- **Passed:** ❌ NO
- **Reason:** no stat edge gap=1%<3%

## Tool Calls
- `search_web({'query': 'Coco Gauff Elina Svitolina tennis match 2025'})` → [Sat, 16 May 2026] Google News
[Sat, 16 May 2026] Where to watch Coco Gauff vs. Elina Svitolina Ital
- `get_sports_data({'sport': 'nba', 'team': 'tennis Gauff'})` → No injury data found for nba tennis Gauff
- `search_web({'query': 'Gauff Svitolina Italian Open final 2025 odds prediction head to head'})` → [Fri, 15 May 2026] Google News
[Sun, 11 May 2025] Coco Gauff vs. Elina Svitolina: Italian Open Final
- `search_web({'query': 'Coco Gauff injury status form May 2025'})` → [Wed, 18 Mar 2026] Google News
[Fri, 16 Jan 2026] Coco Gauff Reveals MRI Results Ahead of 2026 Miami
- `search_web({'query': '"Gauff" "Svitolina" head to head record tennis 2025'})` → [Tue, 27 Jan 2026] Google News
[Wed, 28 Jan 2026] Ukrainian Tennis Star Elina Svitolina Reaches Firs
- `search_web({'query': 'Elina Svitolina form Italian Open 2025 results'})` → [Thu, 14 May 2026] Google News
[Fri, 15 May 2026] Italian Open 2026: Coco Gauff reaches back-to-back

## Outcome
_Pending — will be updated when market resolves_

---
*Mode: LIVE | DRY_RUN: true*