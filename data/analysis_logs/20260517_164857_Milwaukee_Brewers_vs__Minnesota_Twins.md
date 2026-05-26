# Market Analysis — 2026-05-17 16:48 UTC

## Market
- **Question:** Milwaukee Brewers vs. Minnesota Twins
- **Category:** sports
- **YES Price:** 56.0%
- **Days Left:** 7
- **Volume 24h:** $168,849
- **Liquidity:** $365,872

## Statistical Prior
- **p_base:** 59.0%
- **Source:** logistic:sports
- **N (historical):** 6077
- **Raw gap:** 2.9%

## News Sources Fetched
### Macro Context
- Fear&Greed: 27/100 (Fear) | trend: deteriorating
- BTC: $78,124 (-0.1% 24h) → neutral
- Fear&Greed: 27/100 (Fear) | 7d trend: deteriorating
- BTC: $78,036 (-0.3% 24h) → neutral
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

### Multi-Source
- [MULTI-SOURCE NEWS] 2 sources for: milwaukee brewers minnesota twins
- [Bing News]
- [Sun, 17 May 2026] milwaukee brewers minnesota twins
- → Here's how to watch Sunday's Minnesota Twins vs Milwaukee Brewers game, including start times, TV channels, scores and how to stream.
- [Sun, 17 May 2026] Where to watch Milwaukee Brewers vs Minnesota Twins: TV channel, start time, streaming for May 17
- → &quot;I think we came into this series ​knowing that you cannot give away opportunities against the Brewers just because of the brand of baseball th
- [Sat, 16 May 2026] Brewers turn to another young pitcher in finale vs. Twins
- → View news about the Milwaukee Brewers vs. Minnesota Twins game played on May 17, 2026 including player news, injury news, predictions, analysis and 

## LLM Decision
- **Action:** SKIP
- **Confidence:** 45%
- **p_true:** 59.0%
- **Information Gap:** False
- **Crowd Bias:** False
- **Catalyst Type:** STATISTICAL_PATTERN_ONLY
- **Catalyst Strength:** 0.30

### Reasoning
Stat signal indicates YES overpriced (56% market resolves YES 44.7% historically), but gap is only 3% (below 5% gate threshold). No bookmaker odds to cross-verify. No direct injury/lineup catalyst found. Both teams have comparable injury situations. Two previous decisions on same market were SKIP for identical reasons. Pattern alone insufficient for actionable bet without concrete catalyst.

## Gate Result
- **Passed:** ❌ NO
- **Reason:** no stat edge gap=3%<5%

## Tool Calls
- `get_sports_data({'sport': 'mlb', 'team': 'Brewers'})` → INJURY [milwaukee brewers] Brandon Woodruff (SP): 15-Day-IL
INJURY [milwaukee brewers] Akil Baddoo (
- `get_sports_data({'sport': 'mlb', 'team': 'Twins'})` → INJURY [minnesota twins] Byron Buxton (CF): Day-To-Day
INJURY [minnesota twins] Taj Bradley (SP): 15
- `get_odds({'sport': 'baseball_mlb', 'team': 'Brewers Twins'})` → [ODDS] baseball_mlb — 0 events
- `search_web({'query': 'Milwaukee Brewers vs Minnesota Twins June 2025 prediction'})` → [Sun, 17 May 2026] Google News
[Fri, 15 May 2026] Brewers vs Twins Prediction, Odds, Moneyline, Spre
- `search_web({'query': 'Milwaukee Brewers vs Minnesota Twins betting odds preview'})` → [Sun, 17 May 2026] Google News
[Fri, 15 May 2026] Brewers vs Twins Prediction, Odds, Moneyline, Spre
- `get_market_context({'keyword': 'MLB baseball'})` → No related markets found for 'MLB baseball'
- `search_web({'query': 'Brewers Twins injury report May 2026'})` → [Sat, 16 May 2026] Google News
[Sun, 17 May 2026] Brewers vs. Twins (May 16, 2026) Live Score - ESPN
- `search_web({'query': 'Milwaukee Brewers recent form wins losses May 2026'})` → [Fri, 15 May 2026] Google News
[Fri, 15 May 2026] 2026 MLB Standings and Records: Regular Season - M
- `search_web({'query': 'Brewers Twins May 17 2026 starting pitcher lineup'})` → [Sun, 17 May 2026] Google News
[Sun, 17 May 2026] How to watch Brewers vs. Twins: TV channel and str
- `search_web({'query': 'Milwaukee Brewers Minnesota Twins head to head 2026'})` → [Sat, 16 May 2026] Google News
[Sun, 17 May 2026] Milwaukee Brewers vs Minnesota Twins Live Stream: 

## Outcome
**✅ WIN** | P&L: $+0.39 | Resolved: NO

---
*Mode: LIVE | DRY_RUN: true*