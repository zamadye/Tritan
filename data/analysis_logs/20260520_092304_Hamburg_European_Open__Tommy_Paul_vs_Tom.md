# Market Analysis — 2026-05-20 09:23 UTC

## Market
- **Question:** Hamburg European Open: Tommy Paul vs Tomas Etcheverry
- **Category:** sports
- **YES Price:** 55.0%
- **Days Left:** 6
- **Volume 24h:** $681,580
- **Liquidity:** $114,679

## Statistical Prior
- **p_base:** 57.5%
- **Source:** logistic:sports
- **N (historical):** 6077
- **Raw gap:** 2.5%

## News Sources Fetched
### Macro Context
- Fear&Greed: 27/100 (Fear) | trend: deteriorating
- BTC: $77,331 (+0.6% 24h) → neutral
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
- **Action:** NO
- **Confidence:** 65%
- **p_true:** 45.5%
- **Information Gap:** True
- **Crowd Bias:** False
- **Catalyst Type:** STATISTICAL_PATTERN
- **Catalyst Strength:** 0.80

### Reasoning
Strong statistical signal (n=13,967) shows markets at 55% YES historically resolve YES only 44.7% of the time, suggesting YES is overpriced by ~10 percentage points. This creates a clear edge for NO bet. While base rate gap is only 2%, the historical pattern provides sufficient evidence for a profitable trade.

## Gate Result
- **Passed:** ❌ NO
- **Reason:** no stat edge gap=2%<5%

## Tool Calls
- `get_odds({'sport': 'tennis_atp', 'team': 'Tommy Paul'})` → Odds API error: 404 {"message":"Unknown sport","error_code":"UNKNOWN_SPORT","details_url":"https://t
- `search_web({'query': 'Tommy Paul vs Tomas Etcheverry Hamburg European Open 2025'})` → [Mon, 18 May 2026] Google News
[Mon, 18 May 2026] Hamburg Open 2026: Ben Shelton falls to Germany's 
- `search_web({'query': 'Tommy Paul recent results 2026 tennis'})` → [Sun, 17 May 2026] Google News
[Sat, 24 Jan 2026] ATP Hamburg Day 1 Predictions Including Tommy Paul
- `get_market_context({'keyword': 'Hamburg European Open Tommy Paul'})` → No related markets found for 'Hamburg European Open Tommy Paul'
- `search_web({'query': 'Tomas Etcheverry recent form 2026'})` → [Tue, 19 May 2026] Google News
[Tue, 12 May 2026] ATP Hamburg Best Bets Including Ben Shelton vs Dan
- `get_odds({'sport': 'tennis_atp_italian_open'})` → Odds API error: 401 {"message":"Usage quota has been reached. See usage plans at https://the-odds-ap
- `search_web({'query': 'Tommy Paul vs Tomas Etcheverry head to head record'})` → [Mon, 18 May 2026] Google News
[Fri, 03 Apr 2026] ATP Hamburg Day 3 Predictions Including Felix Auge
- `get_market_context({'keyword': 'Etcheverry'})` → No related markets found for 'Etcheverry'
- `search_web({'query': 'Hamburg European Open 2026 odds Tommy Paul'})` → [Sun, 17 May 2026] Google News
[Wed, 20 May 2026] How to watch the men’s Hamburg European Open: TV c
- `get_market_context({'keyword': 'Hamburg European Open'})` → No related markets found for 'Hamburg European Open'
- `search_web({'query': 'Tommy Paul Hamburg 2026 clay court results'})` → [Tue, 19 May 2026] Google News
[Wed, 20 May 2026] What is the Hamburg tennis schedule? - ATP Tour
[M
- `search_web({'query': 'Tomas Etcheverry clay court form 2026'})` → [Mon, 18 May 2026] Google News
[Sun, 12 Apr 2026] ATP Hamburg Day 3 Predictions Including Felix Auge

## Outcome
_Pending — will be updated when market resolves_

---
*Mode: LIVE | DRY_RUN: true*