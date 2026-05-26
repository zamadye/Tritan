# Market Analysis — 2026-05-20 13:41 UTC

## Market
- **Question:** Hamburg European Open: Tommy Paul vs Tomas Etcheverry
- **Category:** sports
- **YES Price:** 51.0%
- **Days Left:** 6
- **Volume 24h:** $902,006
- **Liquidity:** $114,160

## Statistical Prior
- **p_base:** 51.5%
- **Source:** logistic:sports
- **N (historical):** 6077
- **Raw gap:** 0.5%

## News Sources Fetched
### Macro Context
- Fear&Greed: 27/100 (Fear) | trend: deteriorating
- BTC: $77,001 (+0.1% 24h) → neutral
- Fear&Greed: 27/100 (Fear) | 7d trend: deteriorating
- BTC: $77,407 (+0.9% 24h) → neutral
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
- **p_true:** 51.5%
- **Information Gap:** False
- **Crowd Bias:** False
- **Catalyst Type:** STATISTICAL
- **Catalyst Strength:** 0.30

### Reasoning
Statistical signal shows YES is overpriced (market 51% vs historical resolution 44.7%), but the 1% gap between market and base rate is below the 5% threshold required for a bet. No verifiable catalyst (injury, form change) found from searches. Past decisions correctly skipped similar opportunities. Entry range 50-60% has low historical win rate (33%). While the sports pattern is strong overall, the small edge and lack of direct catalyst warrant a skip.

## Gate Result
- **Passed:** ❌ NO
- **Reason:** no stat edge gap=1%<5%

## Tool Calls
- `get_odds({'sport': 'tennis_atp', 'team': 'Tommy Paul'})` → Odds API error: 404 {"message":"Unknown sport","error_code":"UNKNOWN_SPORT","details_url":"https://t
- `search_web({'query': 'Tommy Paul vs Tomas Etcheverry Hamburg European Open 2025'})` → [Wed, 20 May 2026] Google News
[Mon, 18 May 2026] Sports News, Transfers, Scores | Watch Live Sport 
- `search_web({'query': 'Hamburg European Open 2026 Tommy Paul Tomas Etcheverry'})` → [Wed, 20 May 2026] Google News
[Wed, 20 May 2026] Sports News, Transfers, Scores | Watch Live Sport 
- `search_web({'query': 'Tommy Paul injury update May 2026'})` → [Thu, 23 Oct 2025] Google News
[Fri, 23 Jan 2026] Tommy Paul out of Paris Masters, signaling end of 
- `search_web({'query': 'Tomas Etcheverry injury May 2026'})` → [Wed, 29 Apr 2026] Google News
[Sat, 16 May 2026] Jack Draper out of Italian Open and French Open wi
- `search_web({'query': 'Hamburg European Open 2026 results Tommy Paul'})` → [Tue, 19 May 2026] Google News
[Wed, 20 May 2026] Altmaier tops Shelton for Hamburg QF spot: 'It's a
- `search_web({'query': 'Tommy Paul Hamburg 2026 score'})` → [Wed, 20 May 2026] Google News
[Mon, 18 May 2026] Hamburg Open 2026: Results, Draw, Schedule, Entry 

## Outcome
_Pending — will be updated when market resolves_

---
*Mode: LIVE | DRY_RUN: true*