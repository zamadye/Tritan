# Market Analysis — 2026-05-17 16:07 UTC

## Market
- **Question:** Milwaukee Brewers vs. Minnesota Twins
- **Category:** sports
- **YES Price:** 57.0%
- **Days Left:** 7
- **Volume 24h:** $163,962
- **Liquidity:** $319,387

## Statistical Prior
- **p_base:** 60.4%
- **Source:** logistic:sports
- **N (historical):** 6077
- **Raw gap:** 3.4%

## News Sources Fetched
### Macro Context
- Fear&Greed: 27/100 (Fear) | trend: deteriorating
- BTC: $78,068 (-0.2% 24h) → neutral
- Fear&Greed: 27/100 (Fear) | 7d trend: deteriorating
- BTC: $77,996 (-0.2% 24h) → neutral
- Fed market expectations:

### General
- [FEAR&GREED 7d trend] 27(Fear) → 31(Fear) → 43(Fear) → 34(Fear) | sentiment worsening
- MicroStrategy sells any Bitcoin by May 31, 2026? → YES=50%
- [SPORTS] Recent games:
- MIL @ MIN | Scheduled | Minnesota Twins(home) 20-26 score:0 vs Milwaukee Brewers(away) 26-17 score:0
- [SPORTS] Injuries:
- ?: Pavin Smith — 60-Day-IL (Surgery)
- ?: Carlos Santana — 10-Day-IL (Strain)
- ?: Jordan Lawlar — 60-Day-IL (Fracture)

### Bing/Google News
- 6 articles found:
- [NewsAPI] Carson Kelly drives in 4 as the Cubs beat White Sox 10-5: Carson Kelly hit a tiebreaking single in the seventh inning and drove in four runs
- [NewsAPI] What was going on with the umpire pants in the Brewers game Friday?: When a trunk of equipment didn't arrive to Target Field on time May 15,
- [NewsAPI] Ashby becomes first 8-game winner, Brewers beat Twins 3-2 with help of interfere: Aaron Ashby became the major leagues' first eight-game win
- [NewsAPI] How Brewers Narrowly Defeated Twins: The Milwaukee Brewers pulled off a clutch victory on Friday against the Minnesota Twins.
- [NewsAPI] Minnesota Twins’ Joe Ryan Continues All-Star-Caliber Campaign on Friday: The 29-year-old keeps showing why he's one of the best pitchers in 
- [NewsAPI] Brewers escape with 3-2 victory over Twins behind obstruction call, eighth-innin: Brewers eke one out for Aaron Ashby’s MLB-leading eighth w
- [CAUSAL CHAINS] Relevant cause-effect patterns:

### Multi-Source
- [MULTI-SOURCE NEWS] 2 sources for: milwaukee brewers minnesota twins
- [Bing News]
- [Sun, 17 May 2026] milwaukee brewers minnesota twins
- → Here's how to watch Sunday's Minnesota Twins vs Milwaukee Brewers game, including start times, TV channels, scores and how to stream.
- [Sat, 16 May 2026] Where to watch Milwaukee Brewers vs Minnesota Twins: TV channel, start time, streaming for May 17
- → View news about the Milwaukee Brewers vs. Minnesota Twins game played on May 17, 2026 including player news, injury news, predictions, analysis and 
- [Sun, 17 May 2026] Milwaukee Brewers vs. Minnesota Twins - News: May 17, 2026
- → &quot;I think we came into this series ​knowing that you cannot give away opportunities against the Brewers just because of the brand of baseball th

## LLM Decision
- **Action:** SKIP
- **Confidence:** 55%
- **p_true:** 52.4%
- **Information Gap:** True
- **Crowd Bias:** False
- **Catalyst Type:** STATISTICAL_PATTERN
- **Catalyst Strength:** 0.70

### Reasoning
Bookmaker consensus (FanDuel/Paddy Power) shows Brewers true probability ~55% vs Polymarket 57%, suggesting slight overpricing. Strong historical stat signal (n=13,967) indicates markets at 57% resolve YES only 44.7% of time, supporting overpricing thesis. Injury reports show both teams have key players out but no game-changing absences. No breaking news affecting specific matchup. Gap small (2%) but consistent evidence suggests YES is overpriced.

## Gate Result
- **Passed:** ❌ NO
- **Reason:** no stat edge gap=3%<5%

## Tool Calls
- `get_sports_data({'sport': 'mlb', 'team': 'Brewers'})` → INJURY [milwaukee brewers] Brandon Woodruff (SP): 15-Day-IL
INJURY [milwaukee brewers] Akil Baddoo (
- `get_sports_data({'sport': 'mlb', 'team': 'Twins'})` → INJURY [minnesota twins] Byron Buxton (CF): Day-To-Day
INJURY [minnesota twins] Taj Bradley (SP): 15
- `search_web({'query': 'Milwaukee Brewers vs Minnesota Twins 2025 MLB'})` → [Sun, 17 May 2026] Google News
[Fri, 15 May 2026] Minnesota Twins vs Milwaukee Brewers Prediction &a
- `search_web({'query': 'Brewers Twins injury report May 2026'})` → [Sun, 17 May 2026] Google News
[Sun, 17 May 2026] Brewers vs. Twins (May 17, 2026) Live Score - ESPN
- `search_web({'query': 'ESPN Brewers Twins May 17 2026 injury'})` → [Sun, 17 May 2026] Google News
[Sun, 17 May 2026] Brewers vs. Twins (May 17, 2026) Live Score - ESPN
- `get_odds({'sport': 'mlb', 'team': 'Brewers'})` → [ODDS] baseball_mlb — 1 events
  Minnesota Twins vs Milwaukee Brewers (2026-05-17)
    [FanDuel] Mil
- `get_market_context({'keyword': 'Brewers'})` → No related markets found for 'Brewers'

## Outcome
**✅ WIN** | P&L: $+0.39 | Resolved: NO

---
*Mode: LIVE | DRY_RUN: true*