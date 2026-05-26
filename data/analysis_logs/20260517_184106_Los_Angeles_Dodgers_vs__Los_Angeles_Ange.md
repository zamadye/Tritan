# Market Analysis — 2026-05-17 18:41 UTC

## Market
- **Question:** Los Angeles Dodgers vs. Los Angeles Angels
- **Category:** sports
- **YES Price:** 57.0%
- **Days Left:** 7
- **Volume 24h:** $80,974
- **Liquidity:** $341,419

## Statistical Prior
- **p_base:** 60.4%
- **Source:** logistic:sports
- **N (historical):** 6077
- **Raw gap:** 3.4%

## News Sources Fetched
### Macro Context
- Fear&Greed: 27/100 (Fear) | trend: deteriorating
- BTC: $78,104 (-0.1% 24h) → neutral
- Fear&Greed: 27/100 (Fear) | 7d trend: deteriorating
- BTC: $78,099 (-0.0% 24h) → neutral
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
- → The Los Angeles Dodgers’ lineup, pitching matchups and how to watch Sunday's game against the Los Angeles Angels.
- [Sun, 17 May 2026] Dodgers lineup vs Angels: Mookie Betts and Will Smith out
- → The Los Angeles Dodgers set their lineup for the final game of a three-game series against the Los Angeles Angels. The Dodgers ran rampant in the se
- [Sun, 17 May 2026] Dodgers Looking For Freeway Series Sweep: Lineup
- → The Los Angeles Angels activated Grayson Rodriguez from the injured list in advance of the right-hander's ​debut with the club in a home start ‌agai

## LLM Decision
- **Action:** NO
- **Confidence:** 65%
- **p_true:** 46.4%
- **Information Gap:** True
- **Crowd Bias:** False
- **Catalyst Type:** STATISTICAL_EDGE
- **Catalyst Strength:** 0.85

### Reasoning
Markets at 57% historically resolve YES only 44.7% of the time (n=13,967). This indicates a 12.3% overpricing of YES. The market is pricing Dodgers win at 57%, but historical data suggests the true probability is closer to 44.7%. Bookmaker odds show Dodgers at ~59% implied, but the stat signal based on 13,967 observations shows persistent overpricing at this price point. The previous decisions cited a 3% gap (market vs base rate) as too small, but the stat signal reveals a much larger 12.3% edge based on actual resolution rates. This is a strong statistical edge for NO.

## Gate Result
- **Passed:** ❌ NO
- **Reason:** no stat edge gap=3%<5%

## Tool Calls
- `get_sports_data({'sport': 'mlb', 'team': 'Los Angeles Dodgers'})` → INJURY [los angeles dodgers] Jack Dreyer (RP): 15-Day-IL
INJURY [los angeles dodgers] Blake Snell (S
- `search_web({'query': 'Los Angeles Dodgers recent results and news 2025'})` → [Fri, 17 Oct 2025] Google News
[Sun, 02 Nov 2025] Milwaukee Brewers at Los Angeles Dodgers Game Stor
- `search_web({'query': 'Los Angeles Angels recent results and news 2025'})` → [Sat, 13 Sep 2025] Google News
[Sat, 01 Nov 2025] Los Angeles Angels at Seattle Mariners Game Story,
- `get_odds({'sport': 'baseball_mlb', 'team': 'Los Angeles Dodgers'})` → [ODDS] baseball_mlb — 1 events
  Los Angeles Angels vs Los Angeles Dodgers (2026-05-17)
    [FanDuel
- `get_market_context({'keyword': 'Los Angeles Dodgers'})` → No related markets found for 'Los Angeles Dodgers'
- `search_web({'query': 'Dodgers Angels May 17 2026 MLB game'})` → [Sun, 17 May 2026] Google News
[Sun, 17 May 2026] Los Angeles Dodgers at Los Angeles Angels Game Sto
- `search_web({'query': 'Dodgers vs Angels 2026 season series pitching matchup'})` → [Sat, 16 May 2026] Google News
[Sun, 17 May 2026] Dodgers Lineup vs Angels: Kyle Tucker Out, Alex Ca
- `search_web({'query': 'Dodgers Angels May 17 2026 injury report starting pitchers'})` → [Sun, 17 May 2026] Google News
[Sun, 17 May 2026] Fantasy baseball: Gasser, Rodriguez called up for 

## Outcome
_Pending — will be updated when market resolves_

---
*Mode: LIVE | DRY_RUN: true*