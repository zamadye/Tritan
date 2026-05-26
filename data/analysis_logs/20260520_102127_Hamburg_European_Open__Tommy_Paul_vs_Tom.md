# Market Analysis — 2026-05-20 10:21 UTC

## Market
- **Question:** Hamburg European Open: Tommy Paul vs Tomas Etcheverry
- **Category:** sports
- **YES Price:** 57.0%
- **Days Left:** 6
- **Volume 24h:** $698,173
- **Liquidity:** $55,328

## Statistical Prior
- **p_base:** 60.4%
- **Source:** logistic:sports
- **N (historical):** 6077
- **Raw gap:** 3.4%

## News Sources Fetched
### Macro Context
- Fear&Greed: 27/100 (Fear) | trend: deteriorating
- BTC: $77,507 (+1.0% 24h) → risk-ON
- Fear&Greed: 27/100 (Fear) | 7d trend: deteriorating
- BTC: $77,507 (+1.0% 24h) → risk-ON
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
- **Confidence:** 63%
- **p_true:** 60.4%
- **Information Gap:** True
- **Crowd Bias:** False
- **Catalyst Type:** STATISTICAL_PATTERN
- **Catalyst Strength:** 0.55

### Reasoning
Strong statistical signal (n=13,967) shows YES at 57% resolves only 44.7% historically—suggesting ~12% systematic overpricing. However: (1) Gap=3% below 5% gate threshold, (2) Entry 50-60% category has very weak WR=33% from 9 trades, (3) No fresh injury/form/news data found to confirm edge is still valid, (4) Prior identical decisions both SKIPPED with similar confidence. While the crowd_bias=true and information_gap=true suggest potential edge, insufficient fresh information to validate current applicability of historical pattern. Prior pending outcomes unresolved—need more data before committing capital.

## Gate Result
- **Passed:** ❌ NO
- **Reason:** no stat edge gap=3%<5%

## Tool Calls
- `get_odds({'sport': 'tennis_atp', 'team': 'Tommy Paul'})` → Odds API error: 404 {"message":"Unknown sport","error_code":"UNKNOWN_SPORT","details_url":"https://t
- `get_odds({'sport': 'tennis_atp'})` → Odds API error: 404 {"message":"Unknown sport","error_code":"UNKNOWN_SPORT","details_url":"https://t
- `get_sports_data({'sport': 'tennis', 'team': 'Tommy Paul'})` → No injury data found for tennis Tommy Paul
- `search_web({'query': 'Tommy Paul vs Tomas Etcheverry Hamburg European Open 2025 odds'})` → [Mon, 18 May 2026] Google News
[Fri, 03 Apr 2026] Hamburg Open 2026: Ben Shelton falls to Germany's 
- `search_web({'query': 'Tommy Paul recent results form 2025 Hamburg European Open'})` → [Mon, 18 May 2026] Google News
[Mon, 04 May 2026] ATP Hamburg Day 3 Predictions Including Felix Auge
- `search_web({'query': 'Tomas Etcheverry recent results Hamburg 2025'})` → [Wed, 21 May 2025] Google News
[Fri, 23 May 2025] Muller upsets Zverev in Hamburg for biggest win of
- `search_web({'query': 'Paul Etcheverry head to head ATP 2025'})` → [Mon, 18 May 2026] Google News
[Fri, 03 Apr 2026] ATP Hamburg Day 3 Predictions Including Felix Auge

## Outcome
_Pending — will be updated when market resolves_

---
*Mode: LIVE | DRY_RUN: true*