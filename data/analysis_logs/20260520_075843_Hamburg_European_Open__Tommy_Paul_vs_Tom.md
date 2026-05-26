# Market Analysis — 2026-05-20 07:58 UTC

## Market
- **Question:** Hamburg European Open: Tommy Paul vs Tomas Etcheverry
- **Category:** sports
- **YES Price:** 56.0%
- **Days Left:** 7
- **Volume 24h:** $651,445
- **Liquidity:** $142,827

## Statistical Prior
- **p_base:** 59.0%
- **Source:** logistic:sports
- **N (historical):** 6077
- **Raw gap:** 2.9%

## News Sources Fetched
### Macro Context
- Fear&Greed: 27/100 (Fear) | trend: deteriorating
- BTC: $77,202 (+0.1% 24h) → neutral
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
- **Confidence:** 55%
- **p_true:** 59.0%
- **Information Gap:** False
- **Crowd Bias:** False
- **Catalyst Type:** NONE
- **Catalyst Strength:** 0.30

### Reasoning
Strong statistical signal (n=13,967) suggests YES is overpriced (44.7% historical resolution vs 56% price), but gap is only 3% (<5% threshold). Entry zone 50-60% has poor 38% WR. No concrete catalyst emerged. Previous decisions on identical market were SKIP for same gap reason. If forced to bet, NO is the better side, but edge is insufficient for confident action.

## Gate Result
- **Passed:** ❌ NO
- **Reason:** no stat edge gap=3%<5%

## Tool Calls
- `search_web({'query': 'Tommy Paul vs Tomas Etcheverry Hamburg European Open 2025'})` → [Mon, 18 May 2026] Google News
[Mon, 18 May 2026] Hamburg Open 2026: Ben Shelton falls to Germany's 
- `search_web({'query': 'Hamburg European Open Tommy Paul Etcheverry head to head recent form'})` → [Mon, 18 May 2026] Google News
[Fri, 03 Apr 2026] ATP Hamburg Day 3 Predictions Including Felix Auge
- `get_market_context({'keyword': 'Hamburg European Open'})` → No related markets found for 'Hamburg European Open'
- `search_web({'query': 'Tommy Paul recent results 2025 tennis'})` → [Sun, 31 Aug 2025] Google News
[Mon, 08 Dec 2025] Alexander Bublik beats battling Tommy Paul in 2025
- `search_web({'query': 'Tomas Etcheverry recent results 2025 tennis'})` → [Tue, 12 May 2026] Google News
[Thu, 20 Nov 2025] Argentina's in-form Etcheverry reaches new career 
- `search_web({'query': '"Hamburg Open 2026" draw Tommy Paul'})` → [Tue, 19 May 2026] Google News
[Wed, 20 May 2026] What is the Hamburg tennis schedule? - ATP Tour
[W
- `search_web({'query': '"Hamburg Open 2026" Etcheverry'})` → [Tue, 19 May 2026] Google News
[Tue, 19 May 2026] What is the Hamburg tennis schedule? - ATP Tour
[M
- `search_web({'query': 'Tommy Paul vs Tomas Martin Etcheverry prediction odds picks ATP Hamburg Open 2026 dimers.com'})` → [Tue, 19 May 2026] Google News
[Sun, 17 May 2026] Tommy Paul vs. Tomas Martin Etcheverry prediction,
- `search_web({'query': 'Hamburg Open 2026 Tommy Paul Tomas Etcheverry head to head'})` → [Mon, 18 May 2026] Google News
[Wed, 20 May 2026] ATP Hamburg Day 3 Predictions Including Felix Auge
- `search_web({'query': 'Tommy Paul vs Tomas Martin Etcheverry preview head-to-head odds prediction Hamburg Open 2026 Sportskeeda'})` → [Tue, 19 May 2026] Google News
[Fri, 28 Mar 2025] Tommy Paul vs Tomas Martin Etcheverry preview, hea
- `search_web({'query': 'PREDICTION PREVIEW H2H Tiafoe Paul De Minaur Auger-Aliassime Hamburg Open Tennis Tonic'})` → [Wed, 20 May 2026] Google News
[Tue, 19 May 2026] PREDICTION, PREVIEW, H2H: Tiafoe, Paul, De Minaur 
- `search_web({'query': '"Tommy Paul" "Etcheverry" odds Hamburg 2026'})` → [Tue, 19 May 2026] Google News
[Tue, 19 May 2026] Tommy Paul vs. Tomas Martin Etcheverry prediction,
- `get_odds({'sport': 'tennis_atp_italian_open', 'team': 'Tommy Paul'})` → Odds API error: 401 {"message":"Usage quota has been reached. See usage plans at https://the-odds-ap
- `search_web({'query': '"Hamburg Open 2026" predictions tennis'})` → [Wed, 20 May 2026] Google News
[Tue, 19 May 2026] Hamburg Open 2026: Results, Draw, Schedule, Entry 
- `get_market_context({'keyword': 'Tommy Paul'})` → No related markets found for 'Tommy Paul'

## Outcome
_Pending — will be updated when market resolves_

---
*Mode: LIVE | DRY_RUN: true*