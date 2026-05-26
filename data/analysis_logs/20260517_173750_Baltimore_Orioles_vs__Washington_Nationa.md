# Market Analysis — 2026-05-17 17:37 UTC

## Market
- **Question:** Baltimore Orioles vs. Washington Nationals
- **Category:** sports
- **YES Price:** 52.0%
- **Days Left:** 7
- **Volume 24h:** $107,575
- **Liquidity:** $578,258

## Statistical Prior
- **p_base:** 53.0%
- **Source:** logistic:sports
- **N (historical):** 6077
- **Raw gap:** 1.0%

## News Sources Fetched
### Macro Context
- Fear&Greed: 27/100 (Fear) | trend: deteriorating
- BTC: $77,915 (-0.4% 24h) → neutral
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
- → Baltimore Orioles (20-26, fourth in the AL East) vs. Washington Nationals (23-23, third in the NL East) Washington; Sunday, 1:35 p.m. EDT PITCHING P

## LLM Decision
- **Action:** SKIP
- **Confidence:** 62%
- **p_true:** 53.0%
- **Information Gap:** True
- **Crowd Bias:** False
- **Catalyst Type:** STATISTICAL
- **Catalyst Strength:** 0.35

### Reasoning
Strong statistical signal: Markets priced at 52% YES historically resolve YES only 44.7% of the time (n=13,967), indicating a 7.3% overpricing of YES. Bookmaker odds (FanDuel Orioles -127) suggest ~54-56% true probability, which partially contradicts the historical signal but is closer to the base rate. Both teams have key injuries (Orioles: Mountcastle, Westburg; Nationals: Herz). The gap is meaningful but not massive, and past similar decisions failed the gate check (gap <5%). However, the persistent statistical edge across 13,967 observations is too significant to ignore. The market appears to overprice YES by ~7%, offering a profitable NO opportunity with moderate confidence.

## Gate Result
- **Passed:** ❌ NO
- **Reason:** no stat edge gap=1%<5%

## Tool Calls
- `get_sports_data({'sport': 'mlb', 'team': 'Baltimore Orioles'})` → INJURY [baltimore orioles] Ryan Mountcastle (1B): 60-Day-IL
INJURY [baltimore orioles] Jordan Westbu
- `get_sports_data({'sport': 'mlb', 'team': 'Washington Nationals'})` → INJURY [washington nationals] DJ Herz (SP): 60-Day-IL
INJURY [washington nationals] Cole Henry (RP):
- `search_web({'query': 'Baltimore Orioles recent news 2025'})` → [Mon, 24 Nov 2025] Google News
[Wed, 24 Dec 2025] Why the Orioles are the most fascinating team of t
- `search_web({'query': 'Baltimore Orioles vs Washington Nationals game 2025'})` → [Sat, 16 May 2026] Google News
[Sat, 16 May 2026] Game Notes: Baltimore Orioles vs Washington Nation
- `get_market_context({'keyword': 'Baltimore Orioles'})` → No related markets found for 'Baltimore Orioles'
- `get_market_context({'keyword': 'Orioles Nationals'})` → No related markets found for 'Orioles Nationals'
- `get_odds({'sport': 'baseball_mlb', 'team': 'Baltimore Orioles'})` → [ODDS] baseball_mlb — 1 events
  Washington Nationals vs Baltimore Orioles (2026-05-17)
    [FanDuel

## Outcome
_Pending — will be updated when market resolves_

---
*Mode: LIVE | DRY_RUN: true*