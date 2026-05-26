# Market Analysis — 2026-05-20 07:32 UTC

## Market
- **Question:** Hamburg European Open: Tommy Paul vs Tomas Etcheverry
- **Category:** sports
- **YES Price:** 56.0%
- **Days Left:** 7
- **Volume 24h:** $650,685
- **Liquidity:** $139,594

## Statistical Prior
- **p_base:** 59.0%
- **Source:** logistic:sports
- **N (historical):** 6077
- **Raw gap:** 2.9%

## News Sources Fetched
### Macro Context
- Fear&Greed: 27/100 (Fear) | trend: deteriorating
- BTC: $77,300 (+0.3% 24h) → neutral
- Fear&Greed: 27/100 (Fear) | 7d trend: deteriorating
- BTC: $77,263 (+0.3% 24h) → neutral
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
- **p_true:** 50.9%
- **Information Gap:** True
- **Crowd Bias:** False
- **Catalyst Type:** STATISTICAL_VALUE
- **Catalyst Strength:** 0.70

### Reasoning
Strong statistical signal from large historical sample (n=13,967) shows markets priced at 56% YES resolve YES only 44.7% of the time, indicating overpricing. While no direct match-specific catalyst (injury/form) found, the 11.3% gap between market price and historical resolution rate provides a clear edge. Past similar decisions were SKIP due to small base rate gap (3%), but the resolution rate gap is substantial and statistically significant.

## Gate Result
- **Passed:** ❌ NO
- **Reason:** no stat edge gap=3%<5%

## Tool Calls
- `get_sports_data({'sport': 'tennis', 'team': 'Tommy Paul'})` → No injury data found for tennis Tommy Paul
- `get_odds({'sport': 'tennis_atp', 'team': 'Tommy Paul'})` → Odds API error: 404 {"message":"Unknown sport","error_code":"UNKNOWN_SPORT","details_url":"https://t
- `get_odds({'sport': 'tennis_atp_italian_open', 'team': 'Tommy Paul'})` → Odds API error: 401 {"message":"Usage quota has been reached. See usage plans at https://the-odds-ap
- `search_web({'query': 'Tommy Paul vs Tomas Etcheverry Hamburg European Open 2025 head to head preview'})` → [Mon, 18 May 2026] Google News
[Mon, 18 May 2026] ATP Hamburg Day 3 Predictions Including Felix Auge
- `search_web({'query': 'Tommy Paul recent form results 2025 Hamburg European Open'})` → [Mon, 18 May 2026] Google News
[Fri, 24 Oct 2025] ATP Hamburg Day 3 Predictions Including Felix Auge
- `get_market_context({'keyword': 'Hamburg European Open tennis'})` → No related markets found for 'Hamburg European Open tennis'
- `search_web({'query': 'Tommy Paul Tomas Etcheverry Hamburg 2025 prediction odds'})` → [Wed, 20 May 2026] Google News
[Mon, 18 May 2026] PREDICTION, PREVIEW, H2H: Tiafoe, Paul, De Minaur 
- `search_web({'query': 'Tommy Paul injury status 2025 season'})` → [Mon, 08 Dec 2025] Google News
[Tue, 26 Aug 2025] After longest off-season ever, Tommy Paul talks in
- `search_web({'query': 'Tennis Tonic Etcheverry vs Tommy Paul Hamburg prediction pick May 2026'})` → [Wed, 20 May 2026] Google News
[Mon, 18 May 2026] PREDICTION, PREVIEW, H2H: Tiafoe, Paul, De Minaur 
- `search_web({'query': 'Tommy Paul 2026 season results form Hamburg clay court'})` → [Tue, 19 May 2026] Google News
[Wed, 20 May 2026] What is the Hamburg tennis schedule? - ATP Tour
[S
- `search_web({'query': 'Tomas Etcheverry 2026 season results form Hamburg clay court'})` → [Tue, 19 May 2026] Google News
[Wed, 20 May 2026] What is the Hamburg tennis schedule? - ATP Tour
[M

## Outcome
_Pending — will be updated when market resolves_

---
*Mode: LIVE | DRY_RUN: true*