# Market Analysis — 2026-05-20 10:49 UTC

## Market
- **Question:** Hamburg European Open: Tommy Paul vs Tomas Etcheverry
- **Category:** sports
- **YES Price:** 56.0%
- **Days Left:** 6
- **Volume 24h:** $703,538
- **Liquidity:** $73,144

## Statistical Prior
- **p_base:** 59.0%
- **Source:** logistic:sports
- **N (historical):** 6077
- **Raw gap:** 2.9%

## News Sources Fetched
### Macro Context
- Fear&Greed: 27/100 (Fear) | trend: deteriorating
- BTC: $77,473 (+0.9% 24h) → neutral
- Fear&Greed: 27/100 (Fear) | 7d trend: deteriorating
- BTC: $77,507 (+1.0% 24h) → risk-ON
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
- **Catalyst Type:** STATISTICAL
- **Catalyst Strength:** 0.70

### Reasoning
Statistical signal (n=13,967) shows YES at 56% resolves only 44.7% historically, indicating YES is overpriced by ~11%. No recent news or injuries found to contradict this. However, gap (3%) is below typical 5% gate, and entry range pattern shows low WR (33%). Edge exists but moderate due to conflicting factors.

## Gate Result
- **Passed:** ❌ NO
- **Reason:** no stat edge gap=3%<5%

## Tool Calls
- `get_odds({'sport': 'tennis_atp', 'team': 'Tommy Paul'})` → Odds API error: 404 {"message":"Unknown sport","error_code":"UNKNOWN_SPORT","details_url":"https://t
- `get_odds({'sport': 'tennis_atp'})` → Odds API error: 404 {"message":"Unknown sport","error_code":"UNKNOWN_SPORT","details_url":"https://t
- `search_web({'query': 'Tommy Paul Tomas Etcheverry Hamburg European Open 2025'})` → [Mon, 18 May 2026] Google News
[Sat, 17 May 2025] Hamburg Open 2026: Ben Shelton falls to Germany's 
- `search_web({'query': 'Tommy Paul Hamburg 2025'})` → [Sun, 17 May 2026] Google News
[Wed, 22 Apr 2026] ATP tennis Hamburg and Geneva previews, picks, and
- `search_web({'query': 'Etcheverry Hamburg 2025'})` → [Tue, 12 May 2026] Google News
[Thu, 18 Sep 2025] Entertaining Tomas Etcheverry Vs Flavio Cobolli Se
- `search_web({'query': 'Tommy Paul injury 2025'})` → [Thu, 23 Oct 2025] Google News
[Tue, 26 Aug 2025] Tommy Paul out of Paris Masters, signaling end of 
- `search_web({'query': 'Etcheverry injury 2025'})` → [Sat, 16 May 2026] Google News
[Fri, 17 Oct 2025] Jack Draper tennis results, next match, news, rank

## Outcome
_Pending — will be updated when market resolves_

---
*Mode: LIVE | DRY_RUN: true*