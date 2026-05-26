# Market Analysis — 2026-05-17 19:42 UTC

## Market
- **Question:** Milwaukee Brewers vs. Minnesota Twins
- **Category:** sports
- **YES Price:** 40.0%
- **Days Left:** 6
- **Volume 24h:** $210,358
- **Liquidity:** $62,774

## Statistical Prior
- **p_base:** 35.2%
- **Source:** logistic:sports
- **N (historical):** 6077
- **Raw gap:** 4.8%

## News Sources Fetched
### Macro Context
- Fear&Greed: 27/100 (Fear) | trend: deteriorating
- BTC: $78,193 (-0.1% 24h) → neutral
- Fear&Greed: 27/100 (Fear) | 7d trend: deteriorating
- BTC: $78,230 (-0.0% 24h) → neutral
- Fed market expectations:

### General
- [FEAR&GREED 7d trend] 27(Fear) → 31(Fear) → 43(Fear) → 34(Fear) | sentiment worsening
- Philadelphia Phillies vs. Pittsburgh Pirates: O/U 7.5 → YES=50%
- [SPORTS] Recent games:
- MIL @ MIN | In Progress | Minnesota Twins(home) 20-26 score:3 vs Milwaukee Brewers(away) 26-17 score:3
- [SPORTS] Injuries:
- ?: Pavin Smith — 60-Day-IL (Surgery)
- ?: Carlos Santana — 10-Day-IL (Strain)
- ?: Jordan Lawlar — 60-Day-IL (Fracture)

### Multi-Source
- [MULTI-SOURCE NEWS] 2 sources for: milwaukee brewers minnesota twins
- [Bing News]
- [Sun, 17 May 2026] milwaukee brewers minnesota twins
- → A mess on defense puts the Twins ahead. Kody Clemens' second double of the day turned into a Little League two-run homer when the Brewers failed to 
- [Sun, 17 May 2026] Twins 3, Brewers 1: Sloppy start on mound, in the field costing Brewers
- → Robert Gasser makes his season debut for the Brewers on May 17 against the Twins ...
- [Sun, 17 May 2026] Twins 1, Brewers 0: Robert Gasser labors in long first inning
- → Here's how to watch Sunday's Minnesota Twins vs Milwaukee Brewers game, including start times, TV channels, scores and how to stream.

## LLM Decision
- **Action:** SKIP
- **Confidence:** 65%
- **p_true:** 45.2%
- **Information Gap:** True
- **Crowd Bias:** False
- **Catalyst Type:** BOOKMAKER_CONSENSUS_MISMATCH
- **Catalyst Strength:** 0.75

### Reasoning
Bookmaker odds strongly favor Brewers (1.80 implied ~55.6%) vs market YES at only 40%—a 15.6% edge. Both teams have moderate injuries (Woodruff IL for MIL, Buxton Day-to-Day for MIN) with neither side severely impacted. Historical base rate 35% suggests market may be anchored to past underperformance, but current bookmaker consensus indicates clear value. Pattern analysis shows STRONG sports WR=85%, though entry 40-50% range historically weak (9% WR)—requires caution but bookmaker gap is substantial.

## Gate Result
- **Passed:** ❌ NO
- **Reason:** no stat edge gap=5%<5%

## Tool Calls
- `get_sports_data({'sport': 'mlb', 'team': 'Brewers'})` → INJURY [milwaukee brewers] Brandon Woodruff (SP): 15-Day-IL
INJURY [milwaukee brewers] Akil Baddoo (
- `get_sports_data({'sport': 'mlb', 'team': 'Twins'})` → INJURY [minnesota twins] Byron Buxton (CF): Day-To-Day
INJURY [minnesota twins] Taj Bradley (SP): 15
- `search_web({'query': 'Milwaukee Brewers vs Minnesota Twins game preview 2025'})` → [Fri, 15 May 2026] Google News
[Sun, 22 Jun 2025] Brewers vs Twins betting preview: Why Minnesota's 
- `search_web({'query': 'Brewers Twins 2026 injury update'})` → [Sun, 17 May 2026] Google News
[Sun, 17 May 2026] Minnesota Twins vs. Milwaukee Brewers - May 17, 20
- `get_market_context({'keyword': 'Brewers Twins'})` → No related markets found for 'Brewers Twins'
- `get_market_context({'keyword': 'MLB'})` → No related markets found for 'MLB'
- `get_odds({'sport': 'baseball_mlb', 'team': 'Brewers'})` → [ODDS] baseball_mlb — 2 events
  Minnesota Twins vs Milwaukee Brewers (2026-05-17)
    [FanDuel] Mil

## Outcome
**✅ WIN** | P&L: $+0.39 | Resolved: NO

---
*Mode: LIVE | DRY_RUN: true*