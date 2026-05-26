# Market Analysis — 2026-05-21 18:16 UTC

## Market
- **Question:** Atlanta Braves vs. Miami Marlins
- **Category:** sports
- **YES Price:** 57.0%
- **Days Left:** 7
- **Volume 24h:** $157,543
- **Liquidity:** $223,316

## Statistical Prior
- **p_base:** 60.4%
- **Source:** logistic:sports
- **N (historical):** 6077
- **Raw gap:** 3.4%

## News Sources Fetched
### Macro Context
- Fear&Greed: 29/100 (Fear) | trend: improving
- BTC: $77,644 (+0.2% 24h) → neutral
- Fear&Greed: 29/100 (Fear) | 7d trend: improving
- BTC: $77,772 (+0.3% 24h) → neutral
- Fed market expectations:

### General
- [FEAR&GREED 7d trend] 29(Fear) → 27(Fear) → 25(Extr) → 28(Fear) | sentiment improving
- Will the Fed increase interest rates by 50+ bps after the Ju → YES=50%
- Pittsburgh Pirates vs. St. Louis Cardinals → YES=50%
- [SPORTS] Recent games:
- ATL @ MIA | Scheduled | Miami Marlins(home) 22-28 score:0 vs Atlanta Braves(away) 34-16 score:0
- [SPORTS] Injuries:
- ?: Derek Law — Day-To-Day (Surgery)
- ?: Spencer Giesting — Day-To-Day (Not Specified)

### Multi-Source
- [MULTI-SOURCE NEWS] 2 sources for: atlanta braves miami marlins
- [Bing News]
- [Thu, 21 May 2026] atlanta braves miami marlins
- → Here's how to watch Thursday's Miami Marlins vs Atlanta Braves game, including start times, TV channels, scores and how to stream.
- [Thu, 21 May 2026] Where to watch Atlanta Braves vs Miami Marlins: TV channel, start time, streaming for May 21
- → Janson Junk #26 of the Miami Marlins delivers during the first inning against the Atlanta Braves at loanDepot park on May 20, 2026 in Miami, Florida
- [Thu, 21 May 2026] The Miami Marlins keep hanging around until everything breaks
- → The Atlanta Braves are looking to take the final three games of their series against the Miami Marlins after getting shut out 12-0 in the opener. Th

## LLM Decision
- **Action:** SKIP
- **Confidence:** 63%
- **p_true:** 52.4%
- **Information Gap:** True
- **Crowd Bias:** False
- **Catalyst Type:** STATISTICAL
- **Catalyst Strength:** 0.70

### Reasoning
Strong statistical mispricing: markets at 57% resolve YES only 44.7% historically (n=13,967), indicating ~12% edge for NO. While the base rate suggests YES is underpriced by +3%, the larger historical sample (13,967 vs 6,077) and direct market calibration data take precedence. Injury data shows Braves have 3 players on IL (including SP Waldrep) vs Marlins with 3 players on IL - roughly balanced. No team-specific news or form data available to override the statistical signal. The contradiction between base rate (slightly favors YES) and market calibration (strongly favors NO) creates uncertainty, but the market overpricing evidence is stronger with larger sample size.

## Gate Result
- **Passed:** ❌ NO
- **Reason:** no stat edge gap=3%<5%

## Tool Calls
- `get_sports_data({'sport': 'mlb', 'team': 'Atlanta Braves'})` → INJURY [atlanta braves] Drake Baldwin (C): 10-Day-IL
INJURY [atlanta braves] Hurston Waldrep (SP): 1
- `get_sports_data({'sport': 'mlb', 'team': 'Miami Marlins'})` → INJURY [miami marlins] Robby Snelling (SP): 60-Day-IL
INJURY [miami marlins] Leo Jimenez (3B): 10-Da
- `search_web({'query': 'Atlanta Braves recent results 2025'})` → [Sat, 20 Sep 2025] Google News
[Sun, 28 Sep 2025] Atlanta Braves at Detroit Tigers Game Story, Score
- `search_web({'query': 'Braves vs Marlins 2025 results'})` → [Tue, 26 Aug 2025] Google News
[Thu, 07 Aug 2025] Atlanta Braves at Miami Marlins Game Story, Scores
- `get_odds({'sport': 'baseball_mlb', 'team': 'Braves'})` → Odds API error: 401 {"message":"Usage quota has been reached. See usage plans at https://the-odds-ap
- `get_market_context({'keyword': 'Atlanta Braves'})` → No related markets found for 'Atlanta Braves'
- `get_market_context({'keyword': 'Miami Marlins'})` → No related markets found for 'Miami Marlins'

## Outcome
_Pending — will be updated when market resolves_

---
*Mode: LIVE | DRY_RUN: true*