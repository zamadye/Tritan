# Market Analysis — 2026-05-17 18:12 UTC

## Market
- **Question:** Milwaukee Brewers vs. Minnesota Twins
- **Category:** sports
- **YES Price:** 56.0%
- **Days Left:** 6
- **Volume 24h:** $178,009
- **Liquidity:** $367,640

## Statistical Prior
- **p_base:** 59.0%
- **Source:** logistic:sports
- **N (historical):** 6077
- **Raw gap:** 2.9%

## News Sources Fetched
### Macro Context
- Fear&Greed: 27/100 (Fear) | trend: deteriorating
- BTC: $78,106 (-0.1% 24h) → neutral
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
- [Sat, 16 May 2026] Game thread #44: Milwaukee Brewers (26-17) @ Minnesota Twins (20-26)
- → View news about the Milwaukee Brewers vs. Minnesota Twins game played on May 17, 2026 including player news, injury news, predictions, analysis and 

## LLM Decision
- **Action:** SKIP
- **Confidence:** 55%
- **p_true:** 59.0%
- **Information Gap:** False
- **Crowd Bias:** False
- **Catalyst Type:** NONE
- **Catalyst Strength:** 0.10

### Reasoning
Conflicting signals prevent actionable edge: bookmaker odds (Brewers ~59%) suggest YES underpriced by 3%, but historical stat signal (n=13,967) shows markets at 56% resolve YES only 44.7%, pulling in opposite direction. Gap of 3% is below 5% threshold. No new catalyst. Past decisions for this exact market were also SKIP. Cannot resolve signal conflict with available information.

## Gate Result
- **Passed:** ❌ NO
- **Reason:** no stat edge gap=3%<5%

## Tool Calls
- `get_sports_data({'sport': 'mlb', 'team': 'Brewers'})` → INJURY [milwaukee brewers] Brandon Woodruff (SP): 15-Day-IL
INJURY [milwaukee brewers] Akil Baddoo (
- `get_sports_data({'sport': 'mlb', 'team': 'Twins'})` → INJURY [minnesota twins] Byron Buxton (CF): Day-To-Day
INJURY [minnesota twins] Taj Bradley (SP): 15
- `get_odds({'sport': 'baseball_mlb', 'team': 'Brewers'})` → [ODDS] baseball_mlb — 2 events
  Minnesota Twins vs Milwaukee Brewers (2026-05-17)
    [FanDuel] Mil
- `search_web({'query': 'Milwaukee Brewers vs Minnesota Twins May 2026 preview predictions'})` → [Sun, 17 May 2026] Google News
[Sun, 17 May 2026] Brewers vs Twins Prediction, Odds &amp; Player Pro
- `search_web({'query': 'Milwaukee Brewers starting pitcher May 17 2026'})` → [Sun, 17 May 2026] Google News
[Sun, 17 May 2026] How to watch Brewers vs. Twins: TV channel and str
- `get_market_context({'keyword': 'Brewers Twins'})` → No related markets found for 'Brewers Twins'
- `search_web({'query': 'Brewers Twins May 17 2026 starting pitchers probable'})` → [Sun, 17 May 2026] Google News
[Sun, 17 May 2026] Milwaukee Brewers vs Minnesota Twins score, lineup

## Outcome
**✅ WIN** | P&L: $+0.39 | Resolved: NO

---
*Mode: LIVE | DRY_RUN: true*