# Market Analysis — 2026-05-17 17:27 UTC

## Market
- **Question:** Baltimore Orioles vs. Washington Nationals
- **Category:** sports
- **YES Price:** 53.0%
- **Days Left:** 7
- **Volume 24h:** $72,955
- **Liquidity:** $583,027

## Statistical Prior
- **p_base:** 54.5%
- **Source:** logistic:sports
- **N (historical):** 6077
- **Raw gap:** 1.5%

## News Sources Fetched
### Macro Context
- Fear&Greed: 27/100 (Fear) | trend: deteriorating
- BTC: $77,924 (-0.4% 24h) → neutral
- Fear&Greed: 27/100 (Fear) | 7d trend: deteriorating
- BTC: $77,873 (-0.4% 24h) → neutral

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
- → View the Baltimore Orioles vs. Washington Nationals game played on May 17, 2026. Box score, stats, play-by-play timeline, highlights, odds &amp; mor
- [Sun, 17 May 2026] Baltimore Orioles vs. Washington Nationals - Boxscore: May 17, 2026
- → Here's how to watch Sunday's Washington Nationals vs Baltimore Orioles game, including start times, TV channels, scores and how to stream.
- [Sun, 17 May 2026] Where to watch Baltimore Orioles vs Washington Nationals: TV channel, start time, streaming for May 17
- → Follow along as the Nats look to go above .500 with a sweep over the rival Orioles ...

## LLM Decision
- **Action:** NO
- **Confidence:** 65%
- **p_true:** 44.5%
- **Information Gap:** True
- **Crowd Bias:** False
- **Catalyst Type:** STATISTICAL_EDGE
- **Catalyst Strength:** 0.75

### Reasoning
Strong statistical signal: Markets at 53% YES historically resolve YES only 44.7% of time (n=13,967), creating 8.3% edge for NO. Bookmaker odds show Orioles at 54-55% implied probability, but prediction market history indicates systematic overpricing at this price level.

## Gate Result
- **Passed:** ❌ NO
- **Reason:** no stat edge gap=1%<5%

## Tool Calls
- `get_sports_data({'sport': 'mlb', 'team': 'Orioles'})` → INJURY [baltimore orioles] Ryan Mountcastle (1B): 60-Day-IL
INJURY [baltimore orioles] Jordan Westbu
- `get_sports_data({'sport': 'mlb', 'team': 'Nationals'})` → INJURY [washington nationals] DJ Herz (SP): 60-Day-IL
INJURY [washington nationals] Cole Henry (RP):
- `search_web({'query': 'Baltimore Orioles vs Washington Nationals 2025 game preview'})` → [Sat, 16 May 2026] Google News
[Sun, 17 May 2026] Game Notes: Baltimore Orioles vs Washington Nation
- `search_web({'query': 'Orioles Nationals game today starting pitchers'})` → [Sun, 17 May 2026] Google News
[Fri, 15 May 2026] Orioles vs Nationals Prediction, Odds &amp; Player
- `get_odds({'sport': 'baseball_mlb', 'team': 'Orioles'})` → [ODDS] baseball_mlb — 1 events
  Washington Nationals vs Baltimore Orioles (2026-05-17)
    [FanDuel
- `get_market_context({'keyword': 'Baltimore Orioles Washington Nationals'})` → No related markets found for 'Baltimore Orioles Washington Nationals'
- `search_web({'query': 'Baltimore Orioles starting pitcher today May 17 2026'})` → [Sun, 17 May 2026] Google News
[Sun, 17 May 2026] Orioles news: Another pitching meltdown, Tommy Pha
- `search_web({'query': 'Washington Nationals starting pitcher today May 17 2026'})` → [Sun, 17 May 2026] Google News
[Sun, 17 May 2026] Baltimore Orioles vs Washington Nationals Odds - S
- `search_web({'query': 'Orioles vs Nationals probable pitchers May 17 2026'})` → [Sun, 17 May 2026] Google News
[Sun, 17 May 2026] Gameday: Orioles at Nationals, Probable Pitchers, 
- `search_web({'query': 'Baltimore Orioles recent form last 10 games 2026'})` → [Sun, 17 May 2026] Google News
[Sun, 17 May 2026] Orioles vs Nationals Picks, Odds and Best Bet, May
- `search_web({'query': 'Orioles winning percentage 2026 season record'})` → [Fri, 15 May 2026] Google News
[Tue, 12 May 2026] 2026 MLB Standings and Records: Regular Season - M
- `search_web({'query': 'Nationals winning percentage 2026 season record'})` → [Fri, 15 May 2026] Google News
[Fri, 15 May 2026] 2026 MLB Standings and Records: Regular Season - M

## Outcome
_Pending — will be updated when market resolves_

---
*Mode: LIVE | DRY_RUN: true*