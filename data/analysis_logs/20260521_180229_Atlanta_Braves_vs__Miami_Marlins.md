# Market Analysis — 2026-05-21 18:02 UTC

## Market
- **Question:** Atlanta Braves vs. Miami Marlins
- **Category:** sports
- **YES Price:** 56.0%
- **Days Left:** 7
- **Volume 24h:** $154,978
- **Liquidity:** $213,844

## Statistical Prior
- **p_base:** 59.0%
- **Source:** logistic:sports
- **N (historical):** 6077
- **Raw gap:** 2.9%

## News Sources Fetched
### Macro Context
- Fear&Greed: 29/100 (Fear) | trend: improving
- BTC: $77,844 (+0.5% 24h) → neutral
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
- → MIAMI (AP) — Austin Riley and Dominic Smith hit three-run home runs, Chris Sale allowed just one run and struck out eight over seven innings, and th
- [Thu, 21 May 2026] Braves beat Marlins 9-1 behind Chris Sale and 3-run homers from Austin Riley, Dominic Smith
- → Here's how to watch Thursday's Miami Marlins vs Atlanta Braves game, including start times, TV channels, scores and how to stream.
- [Thu, 21 May 2026] Where to watch Atlanta Braves vs Miami Marlins: TV channel, start time, streaming for May 21
- → Janson Junk #26 of the Miami Marlins delivers during the first inning against the Atlanta Braves at loanDepot park on May 20, 2026 in Miami, Florida

## LLM Decision
- **Action:** SKIP
- **Confidence:** 65%
- **p_true:** 48.9%
- **Information Gap:** True
- **Crowd Bias:** False
- **Catalyst Type:** STATISTICAL_SIGNAL
- **Catalyst Strength:** 0.75

### Reasoning
Clear statistical mispricing: market at 56% resolves YES only 44.7% historically (n=13,967), indicating YES overpriced by ~11%. Injury data slightly favors Marlins (Braves SP Waldrep on IL). Entry range pattern (50-60%) shows only 44% WR, confirming overpricing. Base rate (+3% gap) contradicts stat signal, but past decisions correctly prioritized the stronger stat signal with larger sample. Edge is concrete and verifiable.

## Gate Result
- **Passed:** ❌ NO
- **Reason:** no stat edge gap=3%<5%

## Tool Calls
- `get_sports_data({'sport': 'mlb', 'team': 'Atlanta Braves'})` → INJURY [atlanta braves] Drake Baldwin (C): 10-Day-IL
INJURY [atlanta braves] Hurston Waldrep (SP): 1
- `get_sports_data({'sport': 'mlb', 'team': 'Miami Marlins'})` → INJURY [miami marlins] Leo Jimenez (3B): 10-Day-IL
INJURY [miami marlins] Thomas White (SP): Day-To-
- `search_web({'query': 'Atlanta Braves vs. Miami Marlins game preview April 2025'})` → [Mon, 13 Apr 2026] Google News
[Sat, 09 Aug 2025] Miami Marlins at Atlanta Braves prediction, pick o
- `search_web({'query': 'Miami Marlins vs Atlanta Braves series 2026 schedule probable pitchers'})` → [Thu, 21 May 2026] Google News
[Tue, 19 May 2026] MLB Probable Pitchers Today: Full Starting Pitcher
- `get_odds({'sport': 'baseball_mlb', 'team': 'Atlanta Braves'})` → Odds API error: 401 {"message":"Usage quota has been reached. See usage plans at https://the-odds-ap
- `get_market_context({'keyword': 'Atlanta Braves Miami Marlins'})` → No related markets found for 'Atlanta Braves Miami Marlins'
- `get_market_context({'keyword': 'Braves Marlins MLB'})` → No related markets found for 'Braves Marlins MLB'

## Outcome
_Pending — will be updated when market resolves_

---
*Mode: LIVE | DRY_RUN: true*