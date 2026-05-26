# Market Analysis — 2026-05-20 09:36 UTC

## Market
- **Question:** Hamburg European Open: Tommy Paul vs Tomas Etcheverry
- **Category:** sports
- **YES Price:** 55.0%
- **Days Left:** 6
- **Volume 24h:** $682,534
- **Liquidity:** $112,630

## Statistical Prior
- **p_base:** 57.5%
- **Source:** logistic:sports
- **N (historical):** 6077
- **Raw gap:** 2.5%

## News Sources Fetched
### Macro Context
- Fear&Greed: 27/100 (Fear) | trend: deteriorating
- BTC: $77,446 (+1.0% 24h) → neutral
- Fear&Greed: 27/100 (Fear) | 7d trend: deteriorating
- BTC: $77,370 (+0.5% 24h) → neutral
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
- **Confidence:** 55%
- **p_true:** 57.5%
- **Information Gap:** False
- **Crowd Bias:** False
- **Catalyst Type:** STATISTICAL_MEAN_REVERSION
- **Catalyst Strength:** 0.25

### Reasoning
Strong statistical signal (n=13,967) shows YES at 55% historically resolves only 44.7%, suggesting ~10% overpricing. However, Entry 50-60% WR is only 33% from 9 trades indicating poor performance in this range. Gap (2%) failed gate in past decisions. No catalyst or direct information edge found. Statistical pattern alone insufficient for confident bet without catalyst.

## Gate Result
- **Passed:** ❌ NO
- **Reason:** no stat edge gap=2%<5%

## Tool Calls
- `get_odds({'sport': 'tennis_atp', 'team': 'Tommy Paul'})` → Odds API error: 404 {"message":"Unknown sport","error_code":"UNKNOWN_SPORT","details_url":"https://t
- `get_odds({'sport': 'tennis_atp'})` → Odds API error: 404 {"message":"Unknown sport","error_code":"UNKNOWN_SPORT","details_url":"https://t
- `get_odds({'sport': 'tennis'})` → Odds API error: 401 {"message":"Usage quota has been reached. See usage plans at https://the-odds-ap
- `search_web({'query': 'Tommy Paul vs Tomas Etcheverry Hamburg European Open 2025 prediction'})` → [Mon, 18 May 2026] Google News
[Fri, 03 Apr 2026] ATP Hamburg Day 3 Predictions Including Felix Auge
- `search_web({'query': 'Tommy Paul vs Tomas Etcheverry Hamburg 2026 odds head to head'})` → [Mon, 18 May 2026] Google News
[Wed, 20 May 2026] ATP Hamburg Day 3 Predictions Including Felix Auge
- `get_market_context({'keyword': 'Tommy Paul Tomas Etcheverry Hamburg'})` → No related markets found for 'Tommy Paul Tomas Etcheverry Hamburg'
- `search_web({'query': 'Tommy Paul Tomas Etcheverry head to head record 2025 2026'})` → [Fri, 03 Apr 2026] Google News
[Mon, 23 Mar 2026] ATP Houston Quarterfinal Predictions Including Fra

## Outcome
_Pending — will be updated when market resolves_

---
*Mode: LIVE | DRY_RUN: true*