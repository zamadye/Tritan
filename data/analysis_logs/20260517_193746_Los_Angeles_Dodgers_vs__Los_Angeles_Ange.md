# Market Analysis — 2026-05-17 19:37 UTC

## Market
- **Question:** Los Angeles Dodgers vs. Los Angeles Angels
- **Category:** sports
- **YES Price:** 57.0%
- **Days Left:** 7
- **Volume 24h:** $298,239
- **Liquidity:** $564,289

## Statistical Prior
- **p_base:** 60.4%
- **Source:** logistic:sports
- **N (historical):** 6077
- **Raw gap:** 3.4%

## News Sources Fetched
### Macro Context
- Fear&Greed: 27/100 (Fear) | trend: deteriorating
- BTC: $78,193 (-0.1% 24h) → neutral
- Fear&Greed: 27/100 (Fear) | 7d trend: deteriorating
- BTC: $78,230 (+0.0% 24h) → neutral
- Fed market expectations:

### General
- [FEAR&GREED 7d trend] 27(Fear) → 31(Fear) → 43(Fear) → 34(Fear) | sentiment worsening
- Philadelphia Phillies vs. Pittsburgh Pirates: O/U 7.5 → YES=50%
- [SPORTS] Injuries:
- ?: Pavin Smith — 60-Day-IL (Surgery)
- ?: Carlos Santana — 10-Day-IL (Strain)
- ?: Jordan Lawlar — 60-Day-IL (Fracture)
- ?: Denzel Clarke — 10-Day-IL (Bruise)
- ?: Brooks Kriske — 15-Day-IL (Pinched Nerve)

### Multi-Source
- [MULTI-SOURCE NEWS] 2 sources for: angeles dodgers angeles angels
- [Bing News]
- [Sun, 17 May 2026] angeles dodgers angeles angels
- → The Los Angeles Dodgers, first in the NL West with a 28-18 record, face the Los Angeles Angels, who are fifth in the AL West with a 16-30 record. Th
- [Sun, 17 May 2026] Los Angeles Dodgers vs. Los Angeles Angels: Live stream, TV channel, odds for Sunday, May 17
- → The Los Angeles Dodgers removed Mookie Betts from the lineup.
- [Sun, 17 May 2026] Mookie Betts status update: Dodgers remove shortstop from lineup before Angels game
- → The Los Angeles Dodgers moved left-handed reliever Jack Dreyer to the injured list with left-shoulder discomfort.

## LLM Decision
- **Action:** SKIP
- **Confidence:** 65%
- **p_true:** 56.4%
- **Information Gap:** True
- **Crowd Bias:** False
- **Catalyst Type:** MARKET_OVERPRICING
- **Catalyst Strength:** 0.60

### Reasoning
Strong stat signal shows systematic overpricing: market at 57% YES historically resolves YES only 44.7% of time (n=13,967) - a 12.3% edge. Bookmakers support Dodgers as favorites (~59%), but Polymarket crowd bias consistently overprices YES at this level. Angels on 3-game losing streak and recent 6-0 loss create potential for competitive regression. Large sample meta-signal indicates crowd overconfidence in favorites at 57% price point.

## Gate Result
- **Passed:** ❌ NO
- **Reason:** no stat edge gap=3%<5%

## Tool Calls
- `get_sports_data({'sport': 'mlb', 'team': 'Dodgers'})` → INJURY [los angeles dodgers] Jack Dreyer (RP): 15-Day-IL
INJURY [los angeles dodgers] Blake Snell (S
- `get_sports_data({'sport': 'mlb', 'team': 'Angels'})` → INJURY [los angeles angels] Travis d'Arnaud (C): 10-Day-IL
INJURY [los angeles angels] Ben Joyce (RP
- `search_web({'query': 'Los Angeles Dodgers vs Los Angeles Angels May 2025 game preview'})` → [Fri, 15 May 2026] Google News
[Fri, 15 May 2026] Dodgers vs. Angels Prediction, MLB Picks for Frida
- `search_web({'query': 'Dodgers Angels upcoming series 2026 pitching matchup'})` → [Fri, 15 May 2026] Google News
[Fri, 15 May 2026] Dodgers Announce Starting Pitchers For Rivalry Ser
- `search_web({'query': '"Dodgers" "Angels" May 2026 series schedule'})` → [Sun, 17 May 2026] Google News
[Sat, 16 May 2026] Where to watch Los Angeles Dodgers vs Los Angeles 
- `get_odds({'sport': 'baseball_mlb', 'team': 'Dodgers'})` → [ODDS] baseball_mlb — 2 events
  Los Angeles Angels vs Los Angeles Dodgers (2026-05-17)
    [FanDuel
- `get_market_context({'query': 'Dodgers Angels'})` → [YES=50% vol=$6,567,544] Will Newcastle United FC win on 2026-05-17?
[YES=50% vol=$6,497,669] Will F

## Outcome
_Pending — will be updated when market resolves_

---
*Mode: LIVE | DRY_RUN: true*