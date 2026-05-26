# Market Analysis — 2026-05-21 18:53 UTC

## Market
- **Question:** Atlanta Braves vs. Miami Marlins
- **Category:** sports
- **YES Price:** 57.0%
- **Days Left:** 7
- **Volume 24h:** $159,348
- **Liquidity:** $225,978

## Statistical Prior
- **p_base:** 60.4%
- **Source:** logistic:sports
- **N (historical):** 6077
- **Raw gap:** 3.4%

## News Sources Fetched
### Macro Context
- Fear&Greed: 29/100 (Fear) | trend: improving
- BTC: $77,462 (+0.1% 24h) → neutral
- Fear&Greed: 29/100 (Fear) | 7d trend: improving
- BTC: $77,751 (+0.4% 24h) → neutral
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
- → Atlanta Braves roster update: veteran pitcher Carlos Carrasco is back in the spotlight as the team faces the Marlins.
- [Thu, 21 May 2026] Atlanta Braves Announce Unsurprising Signing Of 17-Year MLB Player Before Marlins Game
- → Janson Junk #26 of the Miami Marlins delivers during the first inning against the Atlanta Braves at loanDepot park on May 20, 2026 in Miami, Florida

## LLM Decision
- **Action:** SKIP
- **Confidence:** 65%
- **p_true:** 56.4%
- **Information Gap:** True
- **Crowd Bias:** False
- **Catalyst Type:** STATISTICAL MISPRICING AND INJURY REPORTS
- **Catalyst Strength:** 0.60

### Reasoning
Stat signal shows markets at 57% resolve YES only 44.7% of the time (n=13,967), indicating market overpricing YES. Injury reports show both teams have significant injuries, but a historical dominance article suggests Braves may have an edge. However, the gap between market price (57%) and base rate (60%) is only +3%, which is below the typical 5% threshold for statistical edge. The strong historical mispricing pattern provides moderate evidence for a NO bet.

## Gate Result
- **Passed:** ❌ NO
- **Reason:** no stat edge gap=3%<5%

## Tool Calls
- `get_sports_data({'sport': 'mlb', 'team': 'Atlanta Braves'})` → INJURY [atlanta braves] Drake Baldwin (C): 10-Day-IL
INJURY [atlanta braves] Hurston Waldrep (SP): 1
- `get_sports_data({'sport': 'mlb', 'team': 'Miami Marlins'})` → INJURY [miami marlins] Leo Jimenez (3B): 7-day il
INJURY [miami marlins] Robby Snelling (SP): 60-Day
- `search_web({'query': 'Atlanta Braves vs Miami Marlins 2025 season record'})` → [Thu, 21 May 2026] Google News
[Thu, 21 May 2026] Atlanta's road dominance and history against Sandy
- `search_web({'query': 'Atlanta Braves recent performance MLB 2025'})` → [Tue, 05 May 2026] Google News
[Tue, 03 Mar 2026] 2026 MLB Standings and Records: Spring Training - 
- `search_web({'query': 'Sandy Alcantara Miami Marlins 2025 performance'})` → [Wed, 20 Aug 2025] Google News
[Fri, 27 Feb 2026] Sandy Alcantara's nine-strikeout performance - MLB
- `get_market_context({'keyword': 'Braves Marlins'})` → No related markets found for 'Braves Marlins'
- `get_odds({'sport': 'baseball_mlb', 'team': 'Atlanta Braves'})` → Odds API error: 401 {"message":"Usage quota has been reached. See usage plans at https://the-odds-ap
- `search_web({'query': 'Atlanta Braves vs Miami Marlins starting pitcher 2025'})` → [Wed, 20 May 2026] Google News
[Sat, 09 Aug 2025] Miami Marlins to send down Braxton Garrett. Here’s

## Outcome
_Pending — will be updated when market resolves_

---
*Mode: LIVE | DRY_RUN: true*