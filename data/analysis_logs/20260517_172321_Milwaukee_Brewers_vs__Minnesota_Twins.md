# Market Analysis — 2026-05-17 17:23 UTC

## Market
- **Question:** Milwaukee Brewers vs. Minnesota Twins
- **Category:** sports
- **YES Price:** 56.0%
- **Days Left:** 7
- **Volume 24h:** $170,156
- **Liquidity:** $373,458

## Statistical Prior
- **p_base:** 59.0%
- **Source:** logistic:sports
- **N (historical):** 6077
- **Raw gap:** 2.9%

## News Sources Fetched
### Macro Context
- Fear&Greed: 27/100 (Fear) | trend: deteriorating
- BTC: $77,924 (-0.4% 24h) → neutral
- Fear&Greed: 27/100 (Fear) | 7d trend: deteriorating
- BTC: $78,015 (-0.2% 24h) → neutral

### General
- [FEAR&GREED 7d trend] 27(Fear) → 31(Fear) → 43(Fear) → 34(Fear) | sentiment worsening
- [SPORTS] Recent games:
- MIL @ MIN | Scheduled | Minnesota Twins(home) 20-26 score:0 vs Milwaukee Brewers(away) 26-17 score:0
- [SPORTS] Injuries:
- ?: Pavin Smith — 60-Day-IL (Surgery)
- ?: Carlos Santana — 10-Day-IL (Strain)
- ?: Jordan Lawlar — 60-Day-IL (Fracture)
- ?: Denzel Clarke — 10-Day-IL (Bruise)

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
- **Confidence:** 65%
- **p_true:** 50.9%
- **Information Gap:** True
- **Crowd Bias:** False
- **Catalyst Type:** STATISTICAL MISPRICING PATTERN
- **Catalyst Strength:** 0.70

### Reasoning
Statistical signal shows markets at 56% YES resolve YES only 44.7% historically (n=13,967), suggesting YES is overpriced by ~11.3%. This creates an edge on NO side (Twins win). Bookmaker odds (Twins at 2.14, ~47% implied) align closer to historical resolution. Pattern shows 85% WR from similar trades. Past decisions were SKIP due to insufficient gap, but statistical signal now provides clear mispricing evidence.

## Gate Result
- **Passed:** ❌ NO
- **Reason:** no stat edge gap=3%<5%

## Tool Calls
- `get_sports_data({'sport': 'mlb', 'team': 'Brewers'})` → INJURY [milwaukee brewers] Brandon Woodruff (SP): 15-Day-IL
INJURY [milwaukee brewers] Akil Baddoo (
- `get_sports_data({'sport': 'mlb', 'team': 'Twins'})` → INJURY [minnesota twins] Byron Buxton (CF): Day-To-Day
INJURY [minnesota twins] Taj Bradley (SP): 15
- `search_web({'query': 'Milwaukee Brewers vs Minnesota Twins series June 2025'})` → [Sun, 22 Jun 2025] Google News
[Sun, 22 Jun 2025] Milwaukee Brewers at Minnesota Twins Game Story, S
- `search_web({'query': 'Brewers Twins series 2025 predictions odds'})` → [Sun, 17 May 2026] Google News
[Fri, 15 May 2026] Brewers vs Twins Prediction, Odds, Moneyline, Spre
- `get_odds({'sport': 'baseball_mlb', 'team': 'Brewers'})` → [ODDS] baseball_mlb — 1 events
  Minnesota Twins vs Milwaukee Brewers (2026-05-17)
    [FanDuel] Mil
- `get_market_context({'query': 'Brewers Twins'})` → [YES=50% vol=$6,387,952] Will Fulham FC win on 2026-05-17?
[YES=50% vol=$6,141,105] Will Manchester 
- `search_web({'query': 'Brewers Twins May 17 2026 starting pitchers'})` → [Sun, 17 May 2026] Google News
[Sun, 17 May 2026] Henderson, Patrick combine for dominant outing in 

## Outcome
**✅ WIN** | P&L: $+0.39 | Resolved: NO

---
*Mode: LIVE | DRY_RUN: true*