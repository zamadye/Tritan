# Market Analysis — 2026-05-20 12:37 UTC

## Market
- **Question:** Hamburg European Open: Tommy Paul vs Tomas Etcheverry
- **Category:** sports
- **YES Price:** 56.0%
- **Days Left:** 6
- **Volume 24h:** $710,592
- **Liquidity:** $42,959

## Statistical Prior
- **p_base:** 59.0%
- **Source:** logistic:sports
- **N (historical):** 6077
- **Raw gap:** 2.9%

## News Sources Fetched
### Macro Context
- Fear&Greed: 27/100 (Fear) | trend: deteriorating
- BTC: $77,448 (+0.8% 24h) → neutral
- Fear&Greed: 27/100 (Fear) | 7d trend: deteriorating
- BTC: $77,376 (+0.9% 24h) → neutral
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
- **p_true:** 50.1%
- **Information Gap:** True
- **Crowd Bias:** False
- **Catalyst Type:** STATISTICAL_OVERPRICING
- **Catalyst Strength:** 0.72

### Reasoning
Strong statistical signal (n=13,967) shows YES at 56% historically resolves only 44.7% — market overprices Paul by ~11%. Supporting context: Tommy Paul had injury-plagued 2025 season; Etcheverry described as 'in-form' reaching new career milestone. Although gap to base rate (3%) is below 5% gate and 50-60% entry range has poor 33% WR historically, the large sample stat edge combined with injury/form context provides a verifiable edge for NO bet.

## Gate Result
- **Passed:** ❌ NO
- **Reason:** no stat edge gap=3%<5%

## Tool Calls
- `get_odds({'sport': 'tennis_atp', 'team': 'Tommy Paul'})` → Odds API error: 404 {"message":"Unknown sport","error_code":"UNKNOWN_SPORT","details_url":"https://t
- `search_web({'query': 'Tommy Paul Tomas Etcheverry Hamburg European Open 2025 odds prediction'})` → [Fri, 03 Apr 2026] Google News
[Mon, 18 May 2026] ATP Houston QF Predictions and Odds, Paul vs Etche
- `search_web({'query': 'Tommy Paul recent form tennis 2025 results'})` → [Thu, 21 Aug 2025] Google News
[Mon, 11 Aug 2025] US Open 2025: Laver Cup Form Guide - Laver Cup
[Th
- `search_web({'query': 'Tommy Paul vs Tomas Etcheverry head to head record'})` → [Mon, 18 May 2026] Google News
[Fri, 03 Apr 2026] ATP Hamburg Day 3 Predictions Including Felix Auge
- `search_web({'query': 'Hamburg European Open 2025 Tommy Paul Tomas Etcheverry'})` → [Wed, 20 May 2026] Google News
[Mon, 18 May 2026] Sports News, Transfers, Scores | Watch Live Sport 
- `get_market_context({'keyword': 'Tommy Paul Tomas Etcheverry Hamburg'})` → No related markets found for 'Tommy Paul Tomas Etcheverry Hamburg'
- `search_web({'query': '"Tommy Paul" "Etcheverry" Hamburg 2025 tennis'})` → [Tue, 19 May 2026] Google News
[Mon, 18 May 2026] ATP Hamburg Best Bets Including Ben Shelton vs Dan
- `get_market_context({'keyword': 'Hamburg European Open tennis'})` → No related markets found for 'Hamburg European Open tennis'
- `search_web({'query': 'Tommy Paul injury status 2025 clay season'})` → [Thu, 23 Oct 2025] Google News
[Sun, 28 Sep 2025] Tommy Paul out of Paris Masters, signaling end of 
- `search_web({'query': 'Tomas Etcheverry recent results clay court 2025'})` → [Tue, 12 May 2026] Google News
[Sat, 16 May 2026] Argentina's in-form Etcheverry reaches new career 
- `search_web({'query': 'Tommy Paul Tomas Etcheverry Hamburg 2025 prediction preview'})` → [Wed, 20 May 2026] Google News
[Mon, 18 May 2026] PREDICTION, PREVIEW, H2H: Tiafoe, Paul, De Minaur 
- `search_web({'query': 'Etcheverry clay court 2025 form results'})` → [Tue, 12 May 2026] Google News
[Mon, 18 May 2026] Argentina's in-form Etcheverry reaches new career 

## Outcome
_Pending — will be updated when market resolves_

---
*Mode: LIVE | DRY_RUN: true*