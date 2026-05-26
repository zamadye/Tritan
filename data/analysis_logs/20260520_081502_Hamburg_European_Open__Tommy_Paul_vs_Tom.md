# Market Analysis — 2026-05-20 08:15 UTC

## Market
- **Question:** Hamburg European Open: Tommy Paul vs Tomas Etcheverry
- **Category:** sports
- **YES Price:** 56.0%
- **Days Left:** 6
- **Volume 24h:** $652,263
- **Liquidity:** $144,042

## Statistical Prior
- **p_base:** 59.0%
- **Source:** logistic:sports
- **N (historical):** 6077
- **Raw gap:** 2.9%

## News Sources Fetched
### Macro Context
- Fear&Greed: 27/100 (Fear) | trend: deteriorating
- BTC: $77,188 (+0.2% 24h) → neutral
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
- **Confidence:** 63%
- **p_true:** 50.1%
- **Information Gap:** True
- **Crowd Bias:** False
- **Catalyst Type:** STATISTICAL_REVERSION
- **Catalyst Strength:** 0.72

### Reasoning
Strong statistical signal (n=13,967) shows markets at 56% YES resolve YES only 44.7% of the time — a clear ~11% overpricing of YES. Pattern data confirms Entry 50-60% trades have only 38% WR. No direct catalyst (injury/form) found for either player, but the crowd is systematically overpricing YES in this price range. Past decisions SKIPped due to small base-rate gap (3% < 5% gate), but the historical resolution data (44.7% vs 56% market price) provides a genuine information edge. Confidence moderate (0.63) due to absence of a fresh direct catalyst — this is a pure statistical reversion play.

## Gate Result
- **Passed:** ❌ NO
- **Reason:** no stat edge gap=3%<5%

## Tool Calls
- `get_odds({'sport': 'tennis_atp', 'team': 'Tommy Paul'})` → Odds API error: 404 {"message":"Unknown sport","error_code":"UNKNOWN_SPORT","details_url":"https://t
- `search_web({'query': 'Tommy Paul vs Tomas Etcheverry Hamburg European Open 2025'})` → [Mon, 18 May 2026] Google News
[Mon, 18 May 2026] Hamburg Open 2026: Ben Shelton falls to Germany's 
- `search_web({'query': 'Tommy Paul Hamburg European Open form 2025'})` → [Fri, 24 Oct 2025] Google News
[Fri, 16 May 2025] Tommy Paul abruptly ends 2025 season after withdra
- `get_market_context({'keyword': 'Tommy Paul Etcheverry Hamburg tennis'})` → No related markets found for 'Tommy Paul Etcheverry Hamburg tennis'
- `search_web({'query': 'Tommy Paul foot injury 2025 season'})` → [Thu, 23 Oct 2025] Google News
[Sun, 28 Sep 2025] Tommy Paul out of Paris Masters, signaling end of 
- `search_web({'query': 'Tomas Etcheverry Hamburg Open 2025 form'})` → [Mon, 18 May 2026] Google News
[Thu, 18 Sep 2025] ATP Hamburg Day 3 Predictions Including Felix Auge
- `get_market_context({'keyword': 'Hamburg European Open tennis'})` → No related markets found for 'Hamburg European Open tennis'
- `search_web({'query': '"Tommy Paul" injury 2025 Hamburg'})` → [Sun, 17 May 2026] Google News
[Thu, 23 Oct 2025] ATP tennis Hamburg and Geneva previews, picks, and
- `get_sports_data({'sport': 'nba'})` → INJURY [atlanta hawks] Keshon Gilbert (G): Out
INJURY [atlanta hawks] Jock Landale (C): Out
INJURY [

## Outcome
_Pending — will be updated when market resolves_

---
*Mode: LIVE | DRY_RUN: true*