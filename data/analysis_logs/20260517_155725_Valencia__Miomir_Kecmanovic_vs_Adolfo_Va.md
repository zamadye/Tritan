# Market Analysis — 2026-05-17 15:57 UTC

## Market
- **Question:** Valencia: Miomir Kecmanovic vs Adolfo Vallejo
- **Category:** sports
- **YES Price:** 59.0%
- **Days Left:** 6
- **Volume 24h:** $96,317
- **Liquidity:** $40,298

## Statistical Prior
- **p_base:** 63.3%
- **Source:** logistic:sports
- **N (historical):** 6077
- **Raw gap:** 4.3%

## News Sources Fetched
### Macro Context
- Fear&Greed: 27/100 (Fear) | trend: deteriorating
- BTC: $78,004 (-0.3% 24h) → neutral
- Fear&Greed: 27/100 (Fear) | 7d trend: deteriorating
- BTC: $77,994 (-0.2% 24h) → neutral
- Fed market expectations:

### General
- [FEAR&GREED 7d trend] 27(Fear) → 31(Fear) → 43(Fear) → 34(Fear) | sentiment worsening
- MicroStrategy sells any Bitcoin by May 31, 2026? → YES=50%

### Multi-Source
- [MULTI-SOURCE NEWS] 2 sources for: valencia: miomir kecmanovic adolfo vallejo
- [Bing News]
- [] valencia: miomir kecmanovic adolfo vallejo
- [Metaculus]
- [] Will Bitcoin trade above $120,000 before August 1, 2026?
- → Community: pending
- [] Will Haiti hold the first round of its presidential election before Se
- → Community: pending

## LLM Decision
- **Action:** SKIP
- **Confidence:** 65%
- **p_true:** 51.3%
- **Information Gap:** True
- **Crowd Bias:** False
- **Catalyst Type:** STATISTICAL_PATTERN
- **Catalyst Strength:** 0.80

### Reasoning
Strong statistical signal (n=13,967) shows markets priced at ~59% historically resolve YES only 44.7% of the time — indicating 14.3% overpricing on YES side. Market at 59% vs base rate 63% shows only +4% gap, but the historical resolution data is far more predictive. Kecmanovic (ATP) vs Vallejo (Challenger-level) at Challenger tournament, but no injury news or form indicators found to contradict the stat signal. Previous similar decision was SKIP (conf=65%, gate=FAIL due to gap<5%), but the underlying pattern is robust. Bet NO at 59¢ targets ~45¢ true probability = ~32% expected value.

## Gate Result
- **Passed:** ❌ NO
- **Reason:** no stat edge gap=4%<5%

## Tool Calls
- `get_sports_data({'sport': 'tennis', 'team': 'Kecmanovic'})` → No injury data found for tennis Kecmanovic
- `get_sports_data({'sport': 'tennis', 'team': 'Vallejo'})` → No injury data found for tennis Vallejo
- `search_web({'query': 'Miomir Kecmanovic tennis results 2025'})` → [Tue, 22 Jul 2025] Google News
[Thu, 06 Nov 2025] Tennis, ATP – Citi Open 2025: Svajda takes out Kec
- `search_web({'query': 'Adolfo Vallejo tennis player profile 2025'})` → [Fri, 24 Apr 2026] Google News
[Fri, 24 Apr 2026] Adolfo Daniel Vallejo’s Racquet – Player Profile -
- `search_web({'query': 'Valencia tennis tournament 2025 Kecmanovic Vallejo'})` → [Sun, 17 May 2026] Google News
[Sat, 16 May 2026] H2H, prediction of Miomir Kecmanovic vs Adolfo Dan
- `search_web({'query': 'Kecmanovic recent match results July 2025'})` → [Tue, 22 Jul 2025] Google News
[Sat, 05 Jul 2025] Tennis, ATP – Citi Open 2025: Svajda takes out Kec
- `search_web({'query': 'Adolfo Vallejo tennis match results 2025'})` → [Fri, 12 Dec 2025] Google News
[Thu, 02 Oct 2025] Alcaraz headlines 2025 ATP Awards; Sinner, Vachero

## Outcome
_Pending — will be updated when market resolves_

---
*Mode: LIVE | DRY_RUN: true*