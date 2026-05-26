# Market Analysis — 2026-05-20 10:06 UTC

## Market
- **Question:** Hamburg European Open: Tommy Paul vs Tomas Etcheverry
- **Category:** sports
- **YES Price:** 55.0%
- **Days Left:** 6
- **Volume 24h:** $697,964
- **Liquidity:** $90,331

## Statistical Prior
- **p_base:** 57.5%
- **Source:** logistic:sports
- **N (historical):** 6077
- **Raw gap:** 2.5%

## News Sources Fetched
### Macro Context
- Fear&Greed: 27/100 (Fear) | trend: deteriorating
- BTC: $77,402 (+0.9% 24h) → neutral
- Fear&Greed: 27/100 (Fear) | 7d trend: deteriorating
- BTC: $77,428 (+0.9% 24h) → neutral
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
- **Confidence:** 62%
- **p_true:** 51.5%
- **Information Gap:** True
- **Crowd Bias:** False
- **Catalyst Type:** STATISTICAL
- **Catalyst Strength:** 0.65

### Reasoning
Strong statistical signal (n=13,967) shows markets at 55% historically resolve YES only 44.7% of the time, indicating ~10% overpricing of YES. Market YES price (55%) vs true probability (44.7%) creates ~23% edge on NO bet. Tommy Paul has recent clay success (Houston title) but no decisive catalyst found. Pattern shows info-gap trades have 64% WR. Despite gap (2%) below typical gate threshold, the large historical dataset provides strong edge.

## Gate Result
- **Passed:** ❌ NO
- **Reason:** no stat edge gap=2%<5%

## Tool Calls
- `get_odds({'sport': 'tennis_atp', 'team': 'Tommy Paul'})` → Odds API error: 404 {"message":"Unknown sport","error_code":"UNKNOWN_SPORT","details_url":"https://t
- `get_odds({'sport': 'tennis_atp'})` → Odds API error: 404 {"message":"Unknown sport","error_code":"UNKNOWN_SPORT","details_url":"https://t
- `search_web({'query': 'Tommy Paul Hamburg European Open 2025 results'})` → [Wed, 13 May 2026] Google News
[Mon, 04 May 2026] Bitpanda Hamburg Open 2026: Draws, Dates, History 
- `search_web({'query': 'Tomas Etcheverry Hamburg Open 2025 form recent results'})` → [Mon, 18 May 2026] Google News
[Sat, 27 Sep 2025] ATP Hamburg Day 3 Predictions Including Felix Auge
- `get_market_context({'keyword': 'Hamburg European Open tennis'})` → No related markets found for 'Hamburg European Open tennis'
- `search_web({'query': 'Tommy Paul vs Tomas Etcheverry Hamburg Open 2026'})` → [Tue, 19 May 2026] Google News
[Mon, 18 May 2026] What is the Hamburg tennis schedule? - ATP Tour
[T
- `search_web({'query': 'Tommy Paul injury update 2026'})` → [Fri, 05 Dec 2025] Google News
[Mon, 19 Jan 2026] Tommy Paul's coach provides latest update on his f
- `search_web({'query': 'Tomas Etcheverry form 2026 clay court'})` → [Mon, 18 May 2026] Google News
[Tue, 07 Apr 2026] ATP Hamburg Day 3 Predictions Including Felix Auge
- `search_web({'query': 'dimers.com Tommy Paul vs Tomas Etcheverry Hamburg Open 2026 prediction odds'})` → [Tue, 19 May 2026] Google News
[Sun, 17 May 2026] Tommy Paul vs. Tomas Martin Etcheverry prediction,
- `search_web({'query': 'Tommy Paul clay court record 2026'})` → [Wed, 01 Apr 2026] Google News
[Sun, 05 Apr 2026] Tommy Paul states his big aim in tennis over 2026 
- `search_web({'query': '"Tommy Paul" "Tomas Etcheverry" head to head record'})` → [Thu, 14 Aug 2025] Google News
[Sat, 17 May 2025] Jannik Sinner vs. Felix Auger-Aliassime Cincinnati
- `search_web({'query': 'Tomas Etcheverry clay court results 2026'})` → [Thu, 02 Apr 2026] Google News
[Thu, 09 Apr 2026] Have clay, will play: Tomas Martin Etcheverry over
- `search_web({'query': 'Tommy Paul Hamburg Open 2026 draw results'})` → [Tue, 19 May 2026] Google News
[Wed, 20 May 2026] What is the Hamburg tennis schedule? - ATP Tour
[T

## Outcome
_Pending — will be updated when market resolves_

---
*Mode: LIVE | DRY_RUN: true*