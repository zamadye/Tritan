# Market Analysis — 2026-05-17 18:25 UTC

## Market
- **Question:** Milwaukee Brewers vs. Minnesota Twins
- **Category:** sports
- **YES Price:** 52.0%
- **Days Left:** 6
- **Volume 24h:** $183,424
- **Liquidity:** $90,085

## Statistical Prior
- **p_base:** 53.0%
- **Source:** logistic:sports
- **N (historical):** 6077
- **Raw gap:** 1.0%

## News Sources Fetched
### Macro Context
- Fear&Greed: 27/100 (Fear) | trend: deteriorating
- BTC: $77,985 (-0.2% 24h) → neutral
- Fear&Greed: 27/100 (Fear) | 7d trend: deteriorating
- BTC: $78,106 (-0.1% 24h) → neutral
- Fed market expectations:

### General
- [FEAR&GREED 7d trend] 27(Fear) → 31(Fear) → 43(Fear) → 34(Fear) | sentiment worsening
- Philadelphia Phillies vs. Pittsburgh Pirates: O/U 7.5 → YES=50%
- [SPORTS] Recent games:
- MIL @ MIN | Scheduled | Minnesota Twins(home) 20-26 score:0 vs Milwaukee Brewers(away) 26-17 score:0
- [SPORTS] Injuries:
- ?: Pavin Smith — 60-Day-IL (Surgery)
- ?: Carlos Santana — 10-Day-IL (Strain)
- ?: Jordan Lawlar — 60-Day-IL (Fracture)

### Multi-Source
- [MULTI-SOURCE NEWS] 2 sources for: milwaukee brewers minnesota twins
- [Bing News]
- [Sun, 17 May 2026] milwaukee brewers minnesota twins
- → The Milwaukee Brewers go for the sweep of the Minnesota Twins on May 17 at Target Field. Robert Gasser, freshly called up from Class AAA Nashville, 
- [Sun, 17 May 2026] Milwaukee Brewers vs Minnesota Twins score, lineups, live updates
- → Gasser’s back… back… back… back again ...
- [Sun, 17 May 2026] Game thread #44: Milwaukee Brewers (26-17) @ Minnesota Twins (20-26)
- → Here's how to watch Sunday's Minnesota Twins vs Milwaukee Brewers game, including start times, TV channels, scores and how to stream.

## LLM Decision
- **Action:** SKIP
- **Confidence:** 63%
- **p_true:** 47.0%
- **Information Gap:** True
- **Crowd Bias:** False
- **Catalyst Type:** HISTORICAL_STATISTICAL_EDGE
- **Catalyst Strength:** 0.65

### Reasoning
Strong statistical edge: Markets priced at 52% YES historically resolve YES only 44.7% of the time (n=13,967). This 7.3% overpricing gap exceeds the 5% threshold. Bookmaker odds (Brewers 51-53.5% implied) align with market, confirming no hidden value on YES side. Both teams have similar injury profiles (Brewers: Woodruff IL; Twins: Buxton DTD, Bradley IL). Past decisions were SKIP due to insufficient gap, but current gap is actionable. SPORTS pattern shows 85% WR from 13 trades, supporting statistical-based betting. No direct catalyst for Brewers winning - market overpricing is the edge.

## Gate Result
- **Passed:** ❌ NO
- **Reason:** no stat edge gap=1%<5%

## Tool Calls
- `get_sports_data({'sport': 'mlb', 'team': 'Milwaukee Brewers'})` → INJURY [milwaukee brewers] Brandon Woodruff (SP): 15-Day-IL
INJURY [milwaukee brewers] Akil Baddoo (
- `get_sports_data({'sport': 'mlb', 'team': 'Minnesota Twins'})` → INJURY [minnesota twins] Byron Buxton (CF): Day-To-Day
INJURY [minnesota twins] Taj Bradley (SP): 15
- `get_odds({'sport': 'baseball_mlb', 'team': 'Milwaukee Brewers'})` → [ODDS] baseball_mlb — 2 events
  Minnesota Twins vs Milwaukee Brewers (2026-05-17)
    [FanDuel] Mil
- `get_odds({'sport': 'baseball_mlb', 'team': 'Minnesota Twins'})` → [ODDS] baseball_mlb — 1 events
  Minnesota Twins vs Milwaukee Brewers (2026-05-17)
    [FanDuel] Mil
- `search_web({'query': 'Milwaukee Brewers recent performance results May 2026'})` → [Sun, 17 May 2026] Google News
[Fri, 15 May 2026] Where to watch Milwaukee Brewers vs Minnesota Twin
- `search_web({'query': 'Minnesota Twins recent form pitching rotation May 2026'})` → [Sun, 17 May 2026] Google News
[Tue, 10 Mar 2026] Brewers vs. Twins Prediction, Odds, &amp; Expert A
- `search_web({'query': 'Brewers vs Twins May 17 2026 starting pitchers betting odds'})` → [Sun, 17 May 2026] Google News
[Sun, 17 May 2026] How to watch Brewers vs. Twins: TV channel and str

## Outcome
**✅ WIN** | P&L: $+0.39 | Resolved: NO

---
*Mode: LIVE | DRY_RUN: true*