# Market Analysis — 2026-05-17 19:55 UTC

## Market
- **Question:** Baltimore Orioles vs. Washington Nationals
- **Category:** sports
- **YES Price:** 94.0%
- **Days Left:** 6
- **Volume 24h:** $219,155
- **Liquidity:** $22,155

## Statistical Prior
- **p_base:** 98.4%
- **Source:** logistic:sports
- **N (historical):** 6077
- **Raw gap:** 4.4%

## News Sources Fetched
### Macro Context
- Fear&Greed: 27/100 (Fear) | trend: deteriorating
- BTC: $78,333 (+0.1% 24h) → neutral
- Fear&Greed: 27/100 (Fear) | 7d trend: deteriorating
- BTC: $78,414 (+0.3% 24h) → neutral
- Fed market expectations:

### General
- [FEAR&GREED 7d trend] 27(Fear) → 31(Fear) → 43(Fear) → 34(Fear) | sentiment worsening
- Philadelphia Phillies vs. Pittsburgh Pirates: O/U 7.5 → YES=50%
- [SPORTS] Recent games:
- BAL @ WSH | In Progress | Washington Nationals(home) 23-23 score:3 vs Baltimore Orioles(away) 20-26 score:6
- [SPORTS] Injuries:
- ?: Pavin Smith — 60-Day-IL (Surgery)
- ?: Carlos Santana — 10-Day-IL (Strain)
- ?: Jordan Lawlar — 60-Day-IL (Fracture)

### Multi-Source
- [MULTI-SOURCE NEWS] 2 sources for: baltimore orioles washington nationals
- [Bing News]
- [Sun, 17 May 2026] baltimore orioles washington nationals
- → Here's how to watch Sunday's Washington Nationals vs Baltimore Orioles game, including start times, TV channels, scores and how to stream.
- [Sun, 17 May 2026] Where to watch Baltimore Orioles vs Washington Nationals: TV channel, start time, streaming for May 17
- → View the Baltimore Orioles vs. Washington Nationals game played on May 17, 2026. Box score, stats, play-by-play timeline, highlights, odds &amp; mor
- [Sun, 17 May 2026] Baltimore Orioles vs. Washington Nationals - Boxscore: May 17, 2026
- → Baltimore Orioles (20-26, fourth in the AL East) vs. Washington Nationals (23-23, third in the NL East) Washington; Sunday, 1:35 p.m. EDT PITCHING P

## LLM Decision
- **Action:** SKIP
- **Confidence:** 60%
- **p_true:** 92.0%
- **Information Gap:** False
- **Crowd Bias:** False
- **Catalyst Type:** NONE
- **Catalyst Strength:** 0.00

### Reasoning
Market at 94% YES, base rate 98% (gap +4% below 5% gate). Bookmaker odds (93.5-97% implied) confirm market pricing is reasonable. No breaking news or injury catalyst to create edge. Previous decisions for this market already flagged insufficient gap. Sports pattern shows 100% WR for 90-100% entries, but gap too small for statistically significant edge.

## Gate Result
- **Passed:** ❌ NO
- **Reason:** no stat edge gap=4%<5%

## Tool Calls
- `get_sports_data({'sport': 'mlb', 'team': 'Baltimore Orioles'})` → INJURY [baltimore orioles] Ryan Mountcastle (1B): 60-Day-IL
INJURY [baltimore orioles] Jordan Westbu
- `get_odds({'sport': 'baseball_mlb', 'team': 'Baltimore Orioles'})` → [ODDS] baseball_mlb — 2 events
  Washington Nationals vs Baltimore Orioles (2026-05-17)
    [FanDuel
- `search_web({'query': 'Baltimore Orioles vs Washington Nationals 2026 May 17 preview'})` → [Sun, 17 May 2026] Google News
[Sun, 17 May 2026] Game Notes: Baltimore Orioles vs Washington Nation
- `search_web({'query': 'Baltimore Orioles recent performance 2026 May'})` → [Sun, 17 May 2026] Google News
[Sun, 17 May 2026] Craig Albernaz on the Orioles' tough loss - MLB.co
- `get_market_context({'keyword': 'Baltimore Orioles'})` → No related markets found for 'Baltimore Orioles'
- `search_web({'query': 'Washington Nationals 2026 record wins losses'})` → [Fri, 15 May 2026] Google News
[Fri, 15 May 2026] 2026 Mets Standings and Record: Regular Season | N
- `get_sports_data({'sport': 'mlb', 'team': 'Washington Nationals'})` → INJURY [washington nationals] DJ Herz (SP): 60-Day-IL
INJURY [washington nationals] Cole Henry (RP):
- `search_web({'query': 'Orioles Nationals odds May 17 2026 who will win'})` → [Sun, 17 May 2026] Google News
[Sun, 17 May 2026] Washington Nationals vs. Baltimore Orioles - May 1

## Outcome
_Pending — will be updated when market resolves_

---
*Mode: LIVE | DRY_RUN: true*