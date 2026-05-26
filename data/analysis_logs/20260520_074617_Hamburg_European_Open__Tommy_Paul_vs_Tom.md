# Market Analysis — 2026-05-20 07:46 UTC

## Market
- **Question:** Hamburg European Open: Tommy Paul vs Tomas Etcheverry
- **Category:** sports
- **YES Price:** 56.0%
- **Days Left:** 7
- **Volume 24h:** $651,177
- **Liquidity:** $157,991

## Statistical Prior
- **p_base:** 59.0%
- **Source:** logistic:sports
- **N (historical):** 6077
- **Raw gap:** 2.9%

## News Sources Fetched
### Macro Context
- Fear&Greed: 27/100 (Fear) | trend: deteriorating
- BTC: $77,298 (+0.1% 24h) → neutral
- Fear&Greed: 27/100 (Fear) | 7d trend: deteriorating
- BTC: $77,298 (+0.1% 24h) → neutral
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
- **p_true:** 59.0%
- **Information Gap:** False
- **Crowd Bias:** False
- **Catalyst Type:** STATISTICAL_MEAN_REVERSION
- **Catalyst Strength:** 0.45

### Reasoning
Statistical signal suggests market overprices YES (44.7% historical resolution vs 56% price), but gap is only 3%, below 5% gate threshold. No concrete catalyst found for specific match outcome. Tommy Paul has injury history but no direct evidence affecting this match. Entry price zone 50-60% has poor 43% historical win rate. SKIP due to insufficient edge despite statistical signal.

## Gate Result
- **Passed:** ❌ NO
- **Reason:** no stat edge gap=3%<5%

## Tool Calls
- `get_sports_data({'sport': 'tennis', 'team': 'Tommy Paul'})` → No injury data found for tennis Tommy Paul
- `get_odds({'sport': 'tennis_atp', 'team': 'Tommy Paul'})` → Odds API error: 404 {"message":"Unknown sport","error_code":"UNKNOWN_SPORT","details_url":"https://t
- `search_web({'query': 'Tommy Paul Hamburg European Open 2024 2025 form results'})` → [Fri, 24 Oct 2025] Google News
[Fri, 16 May 2025] Tommy Paul abruptly ends 2025 season after withdra
- `get_market_context({'keyword': 'Hamburg European Open tennis'})` → No related markets found for 'Hamburg European Open tennis'
- `search_web({'query': 'Tomas Etcheverry 2025 season results form clay court'})` → [Tue, 12 May 2026] Google News
[Tue, 07 Apr 2026] Argentina's in-form Etcheverry reaches new career 
- `search_web({'query': 'Tommy Paul vs Etcheverry head to head tennis record'})` → [Mon, 23 Mar 2026] Google News
[Sat, 08 Feb 2020] ATP Miami Day 7 Predictions Including Taylor Fritz
- `get_market_context({'keyword': 'Etcheverry'})` → No related markets found for 'Etcheverry'
- `search_web({'query': '"Tommy Paul" "Etcheverry" Hamburg 2025 tennis prediction'})` → [Mon, 18 May 2026] Google News
[Wed, 20 May 2026] ATP Hamburg Day 3 Predictions Including Felix Auge
- `search_web({'query': 'Hamburg Open 2025 Tommy Paul results draw'})` → [Wed, 20 May 2026] Google News
[Wed, 13 May 2026] Hamburg Open 2026: Results, Draw, Schedule, Entry 
- `search_web({'query': 'Tommy Paul injury 2025 foot problem season'})` → [Thu, 23 Oct 2025] Google News
[Sun, 28 Sep 2025] Tommy Paul out of Paris Masters, signaling end of 
- `search_web({'query': 'Tomas Etcheverry 2025 clay court results ranking'})` → [Sat, 16 May 2026] Google News
[Sat, 10 Jan 2026] Jack Draper - latest news and results - Sky Sports

## Outcome
_Pending — will be updated when market resolves_

---
*Mode: LIVE | DRY_RUN: true*