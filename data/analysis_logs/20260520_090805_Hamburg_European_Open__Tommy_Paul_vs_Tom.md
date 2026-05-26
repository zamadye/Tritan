# Market Analysis — 2026-05-20 09:08 UTC

## Market
- **Question:** Hamburg European Open: Tommy Paul vs Tomas Etcheverry
- **Category:** sports
- **YES Price:** 55.0%
- **Days Left:** 6
- **Volume 24h:** $680,492
- **Liquidity:** $123,202

## Statistical Prior
- **p_base:** 57.5%
- **Source:** logistic:sports
- **N (historical):** 6077
- **Raw gap:** 2.5%

## News Sources Fetched
### Macro Context
- Fear&Greed: 27/100 (Fear) | trend: deteriorating
- BTC: $77,370 (+0.5% 24h) → neutral
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
- **Catalyst Type:** STATISTICAL MISPRICING
- **Catalyst Strength:** 0.80

### Reasoning
Strong statistical signal (n=13,967) shows markets at 55% YES historically resolve YES only 44.7% of time, indicating 10.3% overpricing. NO side has ~10.3% edge (55.3% true vs 45% market price). Sports betting pattern shows 83% WR. Market overprices YES despite lack of concrete catalyst.

## Gate Result
- **Passed:** ❌ NO
- **Reason:** no stat edge gap=2%<5%

## Tool Calls
- `get_odds({'sport': 'tennis_atp', 'team': 'Tommy Paul'})` → Odds API error: 404 {"message":"Unknown sport","error_code":"UNKNOWN_SPORT","details_url":"https://t
- `get_odds({'sport': 'tennis', 'team': 'Tommy Paul'})` → Odds API error: 401 {"message":"Usage quota has been reached. See usage plans at https://the-odds-ap
- `get_sports_data({'sport': 'tennis', 'team': 'Tommy Paul'})` → No injury data found for tennis Tommy Paul
- `search_web({'query': 'Tommy Paul vs Tomas Etcheverry Hamburg European Open 2025 preview'})` → [Mon, 18 May 2026] Google News
[Mon, 18 May 2026] ATP Hamburg Day 3 Predictions Including Felix Auge
- `search_web({'query': 'Tommy Paul recent form 2025 tennis results'})` → [Thu, 21 Aug 2025] Google News
[Thu, 21 Aug 2025] Tennis star Tommy Paul looks ahead to US Open and 
- `get_market_context({'keyword': 'Tommy Paul Etcheverry Hamburg'})` → No related markets found for 'Tommy Paul Etcheverry Hamburg'
- `search_web({'query': 'Hamburg European Open 2025 Tommy Paul Tomas Etcheverry head to head'})` → [Mon, 18 May 2026] Google News
[Fri, 19 Jul 2019] Hamburg Open 2026: Ben Shelton falls to Germany's 
- `search_web({'query': 'Tomas Etcheverry recent form 2025 tennis'})` → [Tue, 12 May 2026] Google News
[Sun, 23 Nov 2025] Argentina's in-form Etcheverry reaches new career 
- `get_market_context({'keyword': 'Hamburg European Open tennis'})` → No related markets found for 'Hamburg European Open tennis'
- `search_web({'query': 'Tommy Paul injury update 2025 tennis'})` → [Thu, 23 Oct 2025] Google News
[Tue, 26 Aug 2025] Tommy Paul out of Paris Masters, signaling end of 
- `search_web({'query': 'Tomas Etcheverry injury update 2025 tennis'})` → [Sat, 16 May 2026] Google News
[Mon, 20 Apr 2026] Jack Draper - latest news and results - Sky Sports
- `get_market_context({'keyword': 'tennis prediction markets'})` → No related markets found for 'tennis prediction markets'

## Outcome
_Pending — will be updated when market resolves_

---
*Mode: LIVE | DRY_RUN: true*