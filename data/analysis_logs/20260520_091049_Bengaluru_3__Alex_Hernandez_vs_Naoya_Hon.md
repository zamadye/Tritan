# Market Analysis — 2026-05-20 09:10 UTC

## Market
- **Question:** Bengaluru 3: Alex Hernandez vs Naoya Honda
- **Category:** sports
- **YES Price:** 57.0%
- **Days Left:** 6
- **Volume 24h:** $141,717
- **Liquidity:** $32,938

## Statistical Prior
- **p_base:** 60.4%
- **Source:** logistic:sports
- **N (historical):** 6077
- **Raw gap:** 3.4%

## News Sources Fetched
### Macro Context
- Fear&Greed: 27/100 (Fear) | trend: deteriorating
- BTC: $77,370 (+0.5% 24h) → neutral
- Fear&Greed: 27/100 (Fear) | 7d trend: deteriorating
- BTC: $77,343 (+0.5% 24h) → neutral
- Fed market expectations:

### General
- [FEAR&GREED 7d trend] 27(Fear) → 25(Extr) → 28(Fear) → 27(Fear) | sentiment worsening
- MicroStrategy sells any Bitcoin by May 31, 2026? → YES=50%

### Multi-Source
- [MULTI-SOURCE NEWS] 2 sources for: bengaluru alex hernandez naoya honda
- [Bing News]
- [] bengaluru alex hernandez naoya honda
- [Metaculus]
- [] Will a case of Bundibugyo Ebola disease be first confirmed in the US b
- → Community: pending
- [] Will the next IPC Sudan acute food insecurity analysis classify at lea
- → Community: pending

## LLM Decision
- **Action:** SKIP
- **Confidence:** 58%
- **p_true:** 56.4%
- **Information Gap:** True
- **Crowd Bias:** False
- **Catalyst Type:** STATISTICAL
- **Catalyst Strength:** 0.60

### Reasoning
Stat signal shows markets at 57% historically resolve YES only 44.7% of the time (n=13,967), suggesting YES is overpriced by ~12%. Unable to verify existence of this specific fight, opponent Naoya Honda, or 'Bengaluru 3' event - no search results, no related markets. Alexander Hernandez is real but betting irregularity history raises concerns. Combined with stat edge and crowd overpricing, leaning NO despite verification gaps.

## Gate Result
- **Passed:** ❌ NO
- **Reason:** no stat edge gap=3%<5%

## Tool Calls
- `get_odds({'sport': 'mma_mixed_martial_arts', 'team': 'Hernandez'})` → Odds API error: 401 {"message":"Usage quota has been reached. See usage plans at https://the-odds-ap
- `get_sports_data({'sport': 'nba', 'team': 'Hernandez'})` → No injury data found for nba Hernandez
- `search_web({'query': 'Alex Hernandez vs Naoya Honda MMA fight 2025'})` → No search results for: Alex Hernandez vs Naoya Honda MMA fight 2025
- `search_web({'query': '"Bengaluru 3" MMA event Alex Hernandez'})` → No search results for: "Bengaluru 3" MMA event Alex Hernandez
- `get_market_context({'keyword': 'Alex Hernandez Naoya Honda'})` → No related markets found for 'Alex Hernandez Naoya Honda'
- `search_web({'query': 'Alex Hernandez MMA fighter'})` → [Mon, 11 May 2026] Google News
[Sat, 17 Jan 2026] UFC Fighter Alexander Hernandez Explains Himself A
- `search_web({'query': 'Naoya Honda MMA fighter'})` → [Sun, 14 Sep 2025] Google News
[] Naoya Inoue Dominates Murodjon Akhmadaliev to Retain Undisputed Su

## Outcome
_Pending — will be updated when market resolves_

---
*Mode: LIVE | DRY_RUN: true*