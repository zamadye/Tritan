# Market Analysis — 2026-05-20 10:33 UTC

## Market
- **Question:** Hamburg European Open: Tommy Paul vs Tomas Etcheverry
- **Category:** sports
- **YES Price:** 57.0%
- **Days Left:** 6
- **Volume 24h:** $703,108
- **Liquidity:** $88,013

## Statistical Prior
- **p_base:** 60.4%
- **Source:** logistic:sports
- **N (historical):** 6077
- **Raw gap:** 3.4%

## News Sources Fetched
### Macro Context
- Fear&Greed: 27/100 (Fear) | trend: deteriorating
- BTC: $77,517 (+0.8% 24h) → neutral
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
- **Confidence:** 58%
- **p_true:** 60.4%
- **Information Gap:** False
- **Crowd Bias:** False
- **Catalyst Type:** STATISTICAL_PATTERN
- **Catalyst Strength:** 0.30

### Reasoning
Stat signal (n=13,967) suggests YES at 57% overpriced (historically 44.7%), but gap (3%) below gate threshold. No specific injury/form news found for either player. Past decisions on identical market were SKIP. Entry zone 50-60% has poor WR (33%). Insufficient concrete evidence to override gate rule.

## Gate Result
- **Passed:** ❌ NO
- **Reason:** no stat edge gap=3%<5%

## Tool Calls
- `get_odds({'sport': 'tennis_atp', 'team': 'Tommy Paul'})` → Odds API error: 404 {"message":"Unknown sport","error_code":"UNKNOWN_SPORT","details_url":"https://t
- `get_odds({'sport': 'soccer_epl'})` → Odds API error: 401 {"message":"Usage quota has been reached. See usage plans at https://the-odds-ap
- `search_web({'query': 'Tommy Paul vs Tomas Etcheverry Hamburg European Open 2024'})` → [Mon, 18 May 2026] Google News
[Tue, 19 May 2026] ATP Hamburg Day 3 Predictions Including Felix Auge
- `search_web({'query': 'Tommy Paul injury news Hamburg European Open 2024'})` → [Mon, 08 Sep 2025] Google News
[Mon, 22 Apr 2024] Ben Shelton, Tommy Paul to miss 2025 Laver Cup aft
- `get_market_context({'keyword': 'Hamburg European Open'})` → No related markets found for 'Hamburg European Open'
- `search_web({'query': 'Tommy Paul current form 2024 clay court results'})` → [Mon, 18 May 2026] Google News
[Mon, 11 May 2026] ATP Hamburg Day 3 Predictions Including Felix Auge
- `search_web({'query': 'Tommy Paul vs Tomas Etcheverry head to head record'})` → [Mon, 18 May 2026] Google News
[Fri, 03 Apr 2026] ATP Hamburg Day 3 Predictions Including Felix Auge
- `search_web({'query': 'ATP Hamburg 2024 Tommy Paul results'})` → [Tue, 19 May 2026] Google News
[Sun, 17 May 2026] Altmaier tops Shelton for Hamburg QF spot: 'It's a
- `search_web({'query': 'Tommy Paul recent results 2024 clay'})` → [Mon, 18 May 2026] Google News
[Sun, 05 Apr 2026] ATP Hamburg Day 3 Predictions Including Felix Auge
- `search_web({'query': 'Tomas Etcheverry recent results 2024 clay'})` → [Mon, 18 May 2026] Google News
[Sat, 10 Jan 2026] ATP Hamburg Day 3 Predictions Including Felix Auge

## Outcome
_Pending — will be updated when market resolves_

---
*Mode: LIVE | DRY_RUN: true*