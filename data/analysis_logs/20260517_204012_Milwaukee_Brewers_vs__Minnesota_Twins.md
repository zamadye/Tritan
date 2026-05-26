# Market Analysis — 2026-05-17 20:40 UTC

## Market
- **Question:** Milwaukee Brewers vs. Minnesota Twins
- **Category:** sports
- **YES Price:** 25.0%
- **Days Left:** 6
- **Volume 24h:** $239,024
- **Liquidity:** $25,555

## Statistical Prior
- **p_base:** 16.1%
- **Source:** logistic:sports
- **N (historical):** 6077
- **Raw gap:** 8.9%

## News Sources Fetched
### Macro Context
- Fear&Greed: 27/100 (Fear) | trend: deteriorating
- BTC: $78,297 (+0.1% 24h) → neutral
- Fear&Greed: 27/100 (Fear) | 7d trend: deteriorating
- BTC: $78,303 (+0.0% 24h) → neutral
- Fed market expectations:

### General
- [FEAR&GREED 7d trend] 27(Fear) → 31(Fear) → 43(Fear) → 34(Fear) | sentiment worsening
- Philadelphia Phillies vs. Pittsburgh Pirates: O/U 7.5 → YES=50%
- [SPORTS] Recent games:
- MIL @ MIN | In Progress | Minnesota Twins(home) 20-26 score:4 vs Milwaukee Brewers(away) 26-17 score:3
- [SPORTS] Injuries:
- ?: Pavin Smith — 60-Day-IL (Surgery)
- ?: Carlos Santana — 10-Day-IL (Strain)
- ?: Jordan Lawlar — 60-Day-IL (Fracture)

### Multi-Source
- [MULTI-SOURCE NEWS] 2 sources for: milwaukee brewers minnesota twins
- [Bing News]
- [Sun, 17 May 2026] milwaukee brewers minnesota twins
- → The Milwaukee Brewers go for the sweep of the Minnesota Twins on May 17 at Target Field. Robert Gasser, freshly called up from Class AAA Nashville, 
- [Sun, 17 May 2026] Twins 1, Brewers 0: Robert Gasser labors in long first inning
- → A mess on defense puts the Twins ahead. Kody Clemens' second double of the day turned into a Little League two-run homer when the Brewers failed to 
- [Sun, 17 May 2026] Twins 4, Brewers 3: Christian Yelich homers in return but Milwaukee still down
- → Here's how to watch Sunday's Minnesota Twins vs Milwaukee Brewers game, including start times, TV channels, scores and how to stream.

## LLM Decision
- **Action:** SKIP
- **Confidence:** 0%
- **p_true:** 16.1%
- **Information Gap:** False
- **Crowd Bias:** False
- **Catalyst Type:** NONE
- **Catalyst Strength:** 0.00

### Reasoning


## Gate Result
- **Passed:** ❌ NO
- **Reason:** low conf 0%<52%

## Tool Calls
- `get_odds({'sport': 'baseball_mlb', 'team': 'Brewers'})` → [ODDS] baseball_mlb — 2 events
  Minnesota Twins vs Milwaukee Brewers (2026-05-17)
    [FanDuel] Mil
- `get_odds({'sport': 'baseball_mlb', 'team': 'Twins'})` → [ODDS] baseball_mlb — 2 events
  Minnesota Twins vs Milwaukee Brewers (2026-05-17)
    [FanDuel] Mil
- `get_sports_data({'sport': 'mlb', 'team': 'Brewers'})` → INJURY [milwaukee brewers] Brandon Woodruff (SP): 15-Day-IL
INJURY [milwaukee brewers] Akil Baddoo (
- `get_sports_data({'sport': 'mlb', 'team': 'Twins'})` → INJURY [minnesota twins] Byron Buxton (CF): Day-To-Day
INJURY [minnesota twins] Taj Bradley (SP): 15
- `search_web({'query': 'Milwaukee Brewers vs Minnesota Twins May 17 2026 preview pitching matchup'})` → [Sun, 17 May 2026] Google News
[Sun, 17 May 2026] Where to watch Milwaukee Brewers vs Minnesota Twin
- `search_web({'query': 'Milwaukee Brewers recent results injuries roster 2026'})` → [Wed, 15 Apr 2026] Google News
[Thu, 26 Mar 2026] Milwaukee Brewers Injury Report 2026: Key Injuries
- `get_market_context({'keyword': 'Brewers Twins'})` → No related markets found for 'Brewers Twins'
- `search_web({'query': 'FanDuel Brewers Twins May 17 2026 odds moneyline prediction'})` → [Sun, 17 May 2026] Google News
[Sun, 17 May 2026] Brewers vs Twins Prediction, Odds, Moneyline, Spre
- `search_web({'query': 'Milwaukee Brewers starting pitcher May 17 2026'})` → [Sun, 17 May 2026] Google News
[Sun, 17 May 2026] Orioles Twins Baseball - Journal-News.com
[Sun, 17
- `search_web({'query': '"Brewers" "Twins" "May 17" odds starting pitcher 2026'})` → [Sun, 17 May 2026] Google News
[Sun, 17 May 2026] How to watch Brewers vs. Twins: TV channel and str
- `search_web({'query': 'Milwaukee Brewers season record 2026 standings'})` → [Fri, 15 May 2026] Google News
[Fri, 15 May 2026] 2026 Brewers Standings and Record: Regular Season 

## Outcome
**✅ WIN** | P&L: $+0.39 | Resolved: NO

---
*Mode: LIVE | DRY_RUN: true*