# Market Analysis — 2026-05-17 16:52 UTC

## Market
- **Question:** Baltimore Orioles vs. Washington Nationals
- **Category:** sports
- **YES Price:** 53.0%
- **Days Left:** 7
- **Volume 24h:** $68,561
- **Liquidity:** $531,279

## Statistical Prior
- **p_base:** 54.5%
- **Source:** logistic:sports
- **N (historical):** 6077
- **Raw gap:** 1.5%

## News Sources Fetched
### Macro Context
- Fear&Greed: 27/100 (Fear) | trend: deteriorating
- BTC: $78,124 (-0.1% 24h) → neutral
- Fear&Greed: 27/100 (Fear) | 7d trend: deteriorating
- BTC: $78,088 (-0.2% 24h) → neutral

### General
- [FEAR&GREED 7d trend] 27(Fear) → 31(Fear) → 43(Fear) → 34(Fear) | sentiment worsening
- [SPORTS] Recent games:
- BAL @ WSH | Scheduled | Washington Nationals(home) 23-23 score:0 vs Baltimore Orioles(away) 20-26 score:0
- [SPORTS] Injuries:
- ?: Pavin Smith — 60-Day-IL (Surgery)
- ?: Carlos Santana — 10-Day-IL (Strain)
- ?: Jordan Lawlar — 60-Day-IL (Fracture)
- ?: Denzel Clarke — 10-Day-IL (Bruise)

### Multi-Source
- [MULTI-SOURCE NEWS] 2 sources for: baltimore orioles washington nationals
- [Bing News]
- [Sun, 17 May 2026] baltimore orioles washington nationals
- → WASHINGTON—In the final game of their three-game series with the Washington Nationals, the Orioles will face an opener, left-hander Richard Lovelady
- [Sun, 17 May 2026] Orioles swap relievers, recall Cameron Foster, option Josh Walker; O’s-Nationals lineups
- → Here's how to watch Sunday's Washington Nationals vs Baltimore Orioles game, including start times, TV channels, scores and how to stream.
- [Sun, 17 May 2026] Where to watch Baltimore Orioles vs Washington Nationals: TV channel, start time, streaming for May 17
- → Baltimore Orioles (20-26, fourth in the AL East) vs. Washington Nationals (23-23, third in the NL East) Washington; Sunday, 1:35 p.m. EDT PITCHING P

## LLM Decision
- **Action:** SKIP
- **Confidence:** 0%
- **p_true:** 54.5%
- **Information Gap:** False
- **Crowd Bias:** False
- **Catalyst Type:** NONE
- **Catalyst Strength:** 0.00

### Reasoning


## Gate Result
- **Passed:** ❌ NO
- **Reason:** no stat edge gap=1%<5%

## Tool Calls
- `get_sports_data({'sport': 'mlb', 'team': 'Baltimore Orioles'})` → INJURY [baltimore orioles] Ryan Mountcastle (1B): 60-Day-IL
INJURY [baltimore orioles] Jordan Westbu
- `get_sports_data({'sport': 'mlb', 'team': 'Washington Nationals'})` → INJURY [washington nationals] DJ Herz (SP): 60-Day-IL
INJURY [washington nationals] Cole Henry (RP):
- `search_web({'query': 'Baltimore Orioles vs Washington Nationals series 2025'})` → [Sat, 16 May 2026] Google News
[Sun, 17 May 2026] Game Notes: Baltimore Orioles vs Washington Nation
- `search_web({'query': 'Baltimore Orioles recent results 2026 season'})` → [Sat, 16 May 2026] Google News
[Wed, 13 May 2026] Baltimore Orioles at Washington Nationals Game Sto
- `search_web({'query': 'Orioles Nationals game preview analysis 2026'})` → [Sun, 17 May 2026] Google News
[Sun, 17 May 2026] Nationals 3-2 Orioles (16 May, 2026) Final Score -
- `get_market_context({'keyword': 'Baltimore Orioles Washington Nationals'})` → No related markets found for 'Baltimore Orioles Washington Nationals'
- `get_odds({'sport': 'baseball_mlb', 'team': 'Baltimore Orioles'})` → [ODDS] baseball_mlb — 1 events
  Washington Nationals vs Baltimore Orioles (2026-05-17)
    [FanDuel

## Outcome
_Pending — will be updated when market resolves_

---
*Mode: LIVE | DRY_RUN: true*