# Market Analysis — 2026-05-20 11:41 UTC

## Market
- **Question:** Hamburg European Open: Tommy Paul vs Tomas Etcheverry
- **Category:** sports
- **YES Price:** 57.0%
- **Days Left:** 6
- **Volume 24h:** $705,606
- **Liquidity:** $52,075

## Statistical Prior
- **p_base:** 60.4%
- **Source:** logistic:sports
- **N (historical):** 6077
- **Raw gap:** 3.4%

## News Sources Fetched
### Macro Context
- Fear&Greed: 27/100 (Fear) | trend: deteriorating
- BTC: $77,350 (+0.9% 24h) → neutral
- Fear&Greed: 27/100 (Fear) | 7d trend: deteriorating
- BTC: $77,350 (+0.9% 24h) → neutral
- Fed market expectations:

### General
- [FEAR&GREED 7d trend] 27(Fear) → 25(Extr) → 28(Fear) → 27(Fear) | sentiment worsening
- MicroStrategy sells any Bitcoin by May 31, 2026? → YES=50%
- [CAUSAL CHAINS] Relevant cause-effect patterns:
- → ECB rate cut → EUR weakens vs USD → EUR/USD falls
- → EU GDP beats expectations → EUR strengthens
- → EU political crisis (elections) → EUR uncertainty → falls
- → EUR/USD above 1.10 → European exports competitive → EU stocks rally

### Multi-Source
- [MULTI-SOURCE NEWS] 2 sources for: hamburg european open: tommy paul
- [Bing News]
- [Fri, 15 May 2026] hamburg european open: tommy paul
- → Hamburg Open 2026 (ATP 500): stacked clay-field before Roland Garros. Defending champ Flavio Cobolli, Zverev, Auger-Aliassime, Shelton, Fonseca, Men
- [] Hamburg Open 2026: Results, Draw, Schedule, Entry List, Prize Money and Predictions
- [Metaculus]
- [] Will a case of Bundibugyo Ebola disease be first confirmed in the US b
- → Community: pending

## LLM Decision
- **Action:** SKIP
- **Confidence:** 65%
- **p_true:** 60.4%
- **Information Gap:** False
- **Crowd Bias:** False
- **Catalyst Type:** STATISTICAL_OVERPRICING
- **Catalyst Strength:** 0.55

### Reasoning
Stat signal (n=13,967) indicates YES at 57% overpriced (historically resolves 44.7%), suggesting ~12% edge for NO. However, gap (3%) is below 5% gate threshold. Entry range 50-60% has poor 33% WR historically. No recent head-to-head form data found via search. Same market previously skipped twice with identical reasoning. Systematic gate rules require gap ≥5% to act on stat edge.

## Gate Result
- **Passed:** ❌ NO
- **Reason:** no stat edge gap=3%<5%

## Tool Calls
- `get_market_context({'keyword': 'Hamburg European Open Tommy Paul Tomas Etcheverry'})` → No related markets found for 'Hamburg European Open Tommy Paul Tomas Etcheverry'
- `get_market_context({'keyword': 'Hamburg European Open'})` → No related markets found for 'Hamburg European Open'
- `get_market_context({'keyword': 'Tommy Paul tennis'})` → No related markets found for 'Tommy Paul tennis'
- `get_market_context({'keyword': 'Etcheverry tennis'})` → No related markets found for 'Etcheverry tennis'
- `get_odds({'sport': 'tennis_atp', 'team': 'Tommy Paul'})` → Odds API error: 404 {"message":"Unknown sport","error_code":"UNKNOWN_SPORT","details_url":"https://t
- `search_web({'query': 'Tommy Paul Hamburg European Open 2025 tennis results'})` → [Mon, 18 May 2026] Google News
[Wed, 20 May 2026] Hamburg Open 2026: Ben Shelton falls to Germany's 
- `search_web({'query': 'Tomas Etcheverry Hamburg European Open 2025 tennis results'})` → [Sat, 16 May 2026] Google News
[Mon, 04 May 2026] Jack Draper tennis results, next match, news, rank
- `search_web({'query': 'Tommy Paul vs Tomas Etcheverry head to head 2025 2026'})` → [Wed, 21 Jan 2026] Google News
[Fri, 03 Apr 2026] Australian Open picks: Bublik vs. Etcheverry, Paul
- `search_web({'query': 'Tommy Paul recent results 2026 tennis form'})` → [Sun, 17 May 2026] Google News
[Mon, 11 May 2026] ATP Hamburg Day 1 Predictions Including Tommy Paul

## Outcome
_Pending — will be updated when market resolves_

---
*Mode: LIVE | DRY_RUN: true*