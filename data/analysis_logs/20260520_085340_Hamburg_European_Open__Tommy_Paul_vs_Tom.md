# Market Analysis — 2026-05-20 08:53 UTC

## Market
- **Question:** Hamburg European Open: Tommy Paul vs Tomas Etcheverry
- **Category:** sports
- **YES Price:** 55.0%
- **Days Left:** 6
- **Volume 24h:** $679,445
- **Liquidity:** $124,310

## Statistical Prior
- **p_base:** 57.5%
- **Source:** logistic:sports
- **N (historical):** 6077
- **Raw gap:** 2.5%

## News Sources Fetched
### Macro Context
- Fear&Greed: 27/100 (Fear) | trend: deteriorating
- BTC: $77,408 (+0.4% 24h) → neutral
- Fear&Greed: 27/100 (Fear) | 7d trend: deteriorating
- BTC: $77,178 (+0.2% 24h) → neutral
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
- **p_true:** 49.5%
- **Information Gap:** False
- **Crowd Bias:** False
- **Catalyst Type:** STATISTICAL_SIGNAL
- **Catalyst Strength:** 0.70

### Reasoning
Strong statistical signal (n=13,967) shows markets at 55% YES historically resolve YES only 44.7% of the time, indicating YES is overpriced by ~10%. Tommy Paul had injury-plagued 2025 season (out of Paris Masters, injury concerns). Gap is only +2% (below 5% threshold), but stat edge is clear. Market overpricing YES at 55% vs true probability ~45%. Sports pattern strong (83% WR) but entry 50-60% weak (33% WR) — bet against crowd bias.

## Gate Result
- **Passed:** ❌ NO
- **Reason:** no stat edge gap=2%<5%

## Tool Calls
- `get_market_context({'keyword': 'Hamburg European Open Tommy Paul Etcheverry'})` → No related markets found for 'Hamburg European Open Tommy Paul Etcheverry'
- `get_odds({'sport': 'tennis_atp', 'team': 'Tommy Paul'})` → Odds API error: 404 {"message":"Unknown sport","error_code":"UNKNOWN_SPORT","details_url":"https://t
- `get_odds({'sport': 'tennis_atp'})` → Odds API error: 404 {"message":"Unknown sport","error_code":"UNKNOWN_SPORT","details_url":"https://t
- `search_web({'query': 'Tommy Paul recent match 2025 Hamburg European Open'})` → [Mon, 18 May 2026] Google News
[Mon, 04 May 2026] Hamburg Open 2026: Ben Shelton falls to Germany's 
- `search_web({'query': 'Hamburg European Open 2025 results Tommy Paul Tomas Etcheverry'})` → [Mon, 18 May 2026] Google News
[Mon, 18 May 2026] ATP Hamburg Day 3 Predictions Including Felix Auge
- `search_web({'query': 'Tommy Paul vs Tomas Etcheverry head to head 2025'})` → [Wed, 21 Jan 2026] Google News
[Sat, 08 Feb 2020] Australian Open picks: Bublik vs. Etcheverry, Paul
- `search_web({'query': 'Tommy Paul injury 2025'})` → [Thu, 23 Oct 2025] Google News
[Tue, 26 Aug 2025] Tommy Paul out of Paris Masters, signaling end of 

## Outcome
_Pending — will be updated when market resolves_

---
*Mode: LIVE | DRY_RUN: true*