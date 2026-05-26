# Market Analysis — 2026-05-17 20:06 UTC

## Market
- **Question:** Milwaukee Brewers vs. Minnesota Twins
- **Category:** sports
- **YES Price:** 46.0%
- **Days Left:** 6
- **Volume 24h:** $219,999
- **Liquidity:** $58,196

## Statistical Prior
- **p_base:** 44.0%
- **Source:** logistic:sports
- **N (historical):** 6077
- **Raw gap:** 2.0%

## News Sources Fetched
### Macro Context
- Fear&Greed: 27/100 (Fear) | trend: deteriorating
- BTC: $78,359 (+0.2% 24h) → neutral
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
- → The Milwaukee Brewers go for the sweep of the Minnesota Twins on May 17 at Target Field. Robert Gasser, freshly called up from Class AAA Nashville, 
- [Sun, 17 May 2026] Twins 1, Brewers 0: Robert Gasser labors in long first inning
- → Here's how to watch Sunday's Minnesota Twins vs Milwaukee Brewers game, including start times, TV channels, scores and how to stream.
- [Sun, 17 May 2026] Where to watch Milwaukee Brewers vs Minnesota Twins: TV channel, start time, streaming for May 17
- → Jackson Chourio hit a go-ahead solo homer in the sixth inning and made a run-saving catch in the seventh, Logan Henderson struck out seven in five i

## LLM Decision
- **Action:** SKIP
- **Confidence:** 58%
- **p_true:** 44.0%
- **Information Gap:** True
- **Crowd Bias:** False
- **Catalyst Type:** NONE
- **Catalyst Strength:** 0.20

### Reasoning
Bookmaker odds favor Brewers at 55% vs market 46% (+9% edge), BUT entry range 40-50% has historical WR of only 9% from 11 trades. Gap from base rate is minimal (-2%). No breaking catalyst. Byron Buxton Day-To-Day adds uncertainty. Historical pattern strongly suggests avoiding this price range.

## Gate Result
- **Passed:** ❌ NO
- **Reason:** no stat edge gap=2%<5%

## Tool Calls
- `get_sports_data({'sport': 'mlb', 'team': 'Brewers'})` → INJURY [milwaukee brewers] Brandon Woodruff (SP): 15-Day-IL
INJURY [milwaukee brewers] Akil Baddoo (
- `get_sports_data({'sport': 'mlb', 'team': 'Twins'})` → INJURY [minnesota twins] Byron Buxton (CF): Day-To-Day
INJURY [minnesota twins] Taj Bradley (SP): 15
- `search_web({'query': 'Milwaukee Brewers vs Minnesota Twins game odds and preview'})` → [Sun, 17 May 2026] Google News
[Fri, 15 May 2026] Brewers vs. Twins (May 17, 2026) Pregame - ESPN
[S
- `search_web({'query': 'Milwaukee Brewers injuries news today'})` → [Sun, 17 May 2026] Google News
[Fri, 15 May 2026] Fantasy baseball: Gasser, Rodriguez called up for 
- `search_web({'query': 'Minnesota Twins injuries news today'})` → [Sat, 16 May 2026] Google News
[Sun, 17 May 2026] Twins Injury Update: Latest on Byron Buxton's hip,
- `get_market_context({'keyword': 'Brewers Twins'})` → No related markets found for 'Brewers Twins'

## Outcome
**✅ WIN** | P&L: $+0.39 | Resolved: NO

---
*Mode: LIVE | DRY_RUN: true*