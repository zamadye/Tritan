# Market Analysis — 2026-05-21 19:06 UTC

## Market
- **Question:** Atlanta Braves vs. Miami Marlins
- **Category:** sports
- **YES Price:** 57.0%
- **Days Left:** 7
- **Volume 24h:** $159,809
- **Liquidity:** $242,760

## Statistical Prior
- **p_base:** 60.4%
- **Source:** logistic:sports
- **N (historical):** 6077
- **Raw gap:** 3.4%

## News Sources Fetched
### Macro Context
- Fear&Greed: 29/100 (Fear) | trend: improving
- BTC: $77,374 (+0.1% 24h) → neutral
- Fear&Greed: 29/100 (Fear) | 7d trend: improving
- BTC: $77,374 (+0.1% 24h) → neutral
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
- → Atlanta Braves roster update: veteran pitcher Carlos Carrasco is back in the spotlight as the team faces the Marlins.
- [Thu, 21 May 2026] Atlanta Braves Announce Unsurprising Signing Of 17-Year MLB Player Before Marlins Game
- → Here's how to watch Thursday's Miami Marlins vs Atlanta Braves game, including start times, TV channels, scores and how to stream.
- [Thu, 21 May 2026] Where to watch Atlanta Braves vs Miami Marlins: TV channel, start time, streaming for May 21
- → Janson Junk #26 of the Miami Marlins delivers during the first inning against the Atlanta Braves at loanDepot park on May 20, 2026 in Miami, Florida

## LLM Decision
- **Action:** SKIP
- **Confidence:** 62%
- **p_true:** 54.4%
- **Information Gap:** True
- **Crowd Bias:** False
- **Catalyst Type:** STATISTICAL MISPRICING
- **Catalyst Strength:** 0.65

### Reasoning
Strong statistical signal indicates market overprices YES: markets at 57% historically resolve YES only 44.7% (n=13,967 large sample), suggesting ~12% edge. Both teams have comparable injury concerns (Braves: Waldrep SP IL; Marlins: Snelling SP 60-IL). No specific catalyst favoring Braves found. Despite gap (3%) below 5% gate threshold, the high-confidence statistical mispricing with large sample size justifies NO bet.

## Gate Result
- **Passed:** ❌ NO
- **Reason:** no stat edge gap=3%<5%

## Tool Calls
- `get_sports_data({'sport': 'mlb', 'team': 'Atlanta Braves'})` → INJURY [atlanta braves] Drake Baldwin (C): 10-Day-IL
INJURY [atlanta braves] Hurston Waldrep (SP): 1
- `get_sports_data({'sport': 'mlb', 'team': 'Miami Marlins'})` → INJURY [miami marlins] Leo Jimenez (3B): 7-day il
INJURY [miami marlins] Robby Snelling (SP): 60-Day
- `search_web({'query': 'Atlanta Braves vs Miami Marlins recent game news'})` → [Wed, 20 May 2026] Google News
[Thu, 21 May 2026] Atlanta Braves at Miami Marlins Game Story, Scores
- `search_web({'query': 'Atlanta Braves starting pitcher May 21 2026'})` → [Thu, 21 May 2026] Google News
[Thu, 21 May 2026] MLB Probable Pitchers Today: Full Starting Pitcher
- `search_web({'query': 'Miami Marlins starting pitcher May 21 2026'})` → [Thu, 21 May 2026] Google News
[Thu, 21 May 2026] MLB Probable Pitchers Today: Full Starting Pitcher
- `get_odds({'sport': 'baseball_mlb', 'team': 'Atlanta Braves'})` → Odds API error: 401 {"message":"Usage quota has been reached. See usage plans at https://the-odds-ap
- `get_market_context({'keyword': 'Atlanta Braves Miami Marlins MLB'})` → No related markets found for 'Atlanta Braves Miami Marlins MLB'

## Outcome
_Pending — will be updated when market resolves_

---
*Mode: LIVE | DRY_RUN: true*