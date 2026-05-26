# Market Analysis — 2026-05-20 07:45 UTC

## Market
- **Question:** Hamburg European Open: Tommy Paul vs Tomas Etcheverry
- **Category:** sports
- **YES Price:** 56.0%
- **Days Left:** 7
- **Volume 24h:** $651,318
- **Liquidity:** $145,455

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
- **p_true:** 48.9%
- **Information Gap:** True
- **Crowd Bias:** False
- **Catalyst Type:** STATISTICAL_EDGE
- **Catalyst Strength:** 0.75

### Reasoning
Strong statistical signal (n=13,967) shows markets at 56% YES resolve YES only 44.7% of the time - market systematically overprices YES by ~11%. Tennis-specific odds tools unavailable, but pattern across 23 sports trades shows 83% win rate. However, gap (3%) is below typical 5% threshold, and no direct match-specific catalyst found (Paul has injury history but also recent wins; Etcheverry in form). Entry point 50-60% historically has only 43% win rate, reducing confidence. Bet against overpriced favorite in statistically overpriced range.

## Gate Result
- **Passed:** ❌ NO
- **Reason:** no stat edge gap=3%<5%

## Tool Calls
- `get_odds({'sport': 'tennis_atp', 'team': 'Tommy Paul'})` → Odds API error: 404 {"message":"Unknown sport","error_code":"UNKNOWN_SPORT","details_url":"https://t
- `get_odds({'sport': 'tennis_atp'})` → Odds API error: 404 {"message":"Unknown sport","error_code":"UNKNOWN_SPORT","details_url":"https://t
- `search_web({'query': 'Tommy Paul vs Tomas Etcheverry Hamburg European Open 2025 prediction odds'})` → [Fri, 03 Apr 2026] Google News
[Sat, 15 Feb 2025] ATP Houston QF Predictions and Odds, Paul vs Etche
- `search_web({'query': 'Tommy Paul injury update 2025'})` → [Thu, 23 Oct 2025] Google News
[Tue, 26 Aug 2025] Tommy Paul out of Paris Masters, signaling end of 
- `search_web({'query': 'Tomas Etcheverry recent form 2025'})` → [Tue, 12 May 2026] Google News
[Sun, 12 Apr 2026] Argentina's in-form Etcheverry reaches new career 
- `get_market_context({'keyword': 'Hamburg European Open'})` → No related markets found for 'Hamburg European Open'
- `search_web({'query': '"Hamburg European Open" Tommy Paul Tomas Etcheverry'})` → [Sun, 17 May 2026] Google News
[Mon, 04 May 2026] How to watch the men’s Hamburg European Open: TV c

## Outcome
_Pending — will be updated when market resolves_

---
*Mode: LIVE | DRY_RUN: true*