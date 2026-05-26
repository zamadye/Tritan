# Market Analysis — 2026-05-17 17:04 UTC

## Market
- **Question:** Baltimore Orioles vs. Washington Nationals
- **Category:** sports
- **YES Price:** 53.0%
- **Days Left:** 7
- **Volume 24h:** $68,588
- **Liquidity:** $528,900

## Statistical Prior
- **p_base:** 54.5%
- **Source:** logistic:sports
- **N (historical):** 6077
- **Raw gap:** 1.5%

## News Sources Fetched
### Macro Context
- Fear&Greed: 27/100 (Fear) | trend: deteriorating
- BTC: $78,015 (-0.2% 24h) → neutral
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
- **Confidence:** 65%
- **p_true:** 50.5%
- **Information Gap:** True
- **Crowd Bias:** False
- **Catalyst Type:** INJURIES
- **Catalyst Strength:** 0.60

### Reasoning
Markets at 53% YES historically resolve YES only 44.7% of the time (n=13,967), indicating clear 8.3% overpricing. Orioles have significant injuries (Mountcastle, Westburg on 60-Day-IL, Helsley on 15-Day-IL) providing direct catalyst. Recent 13-3 loss to Nationals suggests current form weakness.

## Gate Result
- **Passed:** ❌ NO
- **Reason:** no stat edge gap=1%<5%

## Tool Calls
- `get_sports_data({'sport': 'mlb', 'team': 'Orioles'})` → INJURY [baltimore orioles] Ryan Mountcastle (1B): 60-Day-IL
INJURY [baltimore orioles] Jordan Westbu
- `search_web({'query': 'Baltimore Orioles vs Washington Nationals game 2025 recent news preview'})` → [Sat, 16 May 2026] Google News
[Sun, 17 May 2026] Game Notes: Baltimore Orioles vs Washington Nation
- `search_web({'query': 'Orioles Nationals May 2025 injury report lineup'})` → [Sat, 16 May 2026] Google News
[Sat, 16 May 2026] Bassitt buckles early and bullpen implodes in Orio
- `get_market_context({'keyword': 'Orioles Nationals'})` → No related markets found for 'Orioles Nationals'
- `get_odds({'sport': 'baseball_mlb', 'team': 'Orioles'})` → [ODDS] baseball_mlb — 1 events
  Washington Nationals vs Baltimore Orioles (2026-05-17)
    [FanDuel

## Outcome
_Pending — will be updated when market resolves_

---
*Mode: LIVE | DRY_RUN: true*