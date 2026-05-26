# Market Analysis — 2026-05-21 20:14 UTC

## Market
- **Question:** Atlanta Braves vs. Miami Marlins
- **Category:** sports
- **YES Price:** 57.0%
- **Days Left:** 7
- **Volume 24h:** $205,118
- **Liquidity:** $269,052

## Statistical Prior
- **p_base:** 60.4%
- **Source:** logistic:sports
- **N (historical):** 6077
- **Raw gap:** 3.4%

## News Sources Fetched
### Macro Context
- Fear&Greed: 29/100 (Fear) | trend: improving
- BTC: $77,653 (+0.0% 24h) → neutral
- Fear&Greed: 29/100 (Fear) | 7d trend: improving
- BTC: $77,551 (-0.0% 24h) → neutral
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
- → The Braves are the best team in baseball and there is no denying that. On Wednesday, they just did something for the first time in over two decades.

## LLM Decision
- **Action:** NO
- **Confidence:** 65%
- **p_true:** 47.6%
- **Information Gap:** True
- **Crowd Bias:** False
- **Catalyst Type:** STATISTICAL_OVERPRICING_PATTERN
- **Catalyst Strength:** 0.82

### Reasoning
Markets at 57% YES price historically resolve YES only 44.7% of the time (n=13,967), indicating systematic overpricing. The market overprices YES by ~12.3 percentage points. NO is priced at 43% but has 55.3% true probability, creating positive expected value. Injury reports show both teams have pitching issues but no decisive advantage. Recent 7-1 Braves victory may have inflated YES price.

## Gate Result
- **Passed:** ❌ NO
- **Reason:** no stat edge gap=3%<5%

## Tool Calls
- `get_sports_data({'sport': 'mlb', 'team': 'Atlanta Braves'})` → INJURY [atlanta braves] Hurston Waldrep (SP): 60-Day-IL
INJURY [atlanta braves] Drake Baldwin (C): 1
- `get_sports_data({'sport': 'mlb', 'team': 'Miami Marlins'})` → INJURY [miami marlins] Robby Snelling (SP): 60-Day-IL
INJURY [miami marlins] Leo Jimenez (3B): 7-day
- `get_odds({'sport': 'baseball_mlb', 'team': 'Atlanta Braves'})` → Odds API error: 401 {"message":"Usage quota has been reached. See usage plans at https://the-odds-ap
- `search_web({'query': 'Atlanta Braves vs Miami Marlins 2025 recent results'})` → [Tue, 26 Aug 2025] Google News
[Wed, 27 Aug 2025] Atlanta Braves at Miami Marlins Game Story, Scores
- `search_web({'query': 'Miami Marlins starting pitcher today injury update'})` → [Thu, 21 May 2026] Google News
[Thu, 21 May 2026] Marlins Receive Tough Injury Update on Top Pitchin
- `get_market_context({'keyword': 'Atlanta Braves Miami Marlins'})` → No related markets found for 'Atlanta Braves Miami Marlins'
- `search_web({'query': 'Atlanta Braves recent games August 2025'})` → [Sun, 31 Aug 2025] Google News
[Sun, 31 Aug 2025] Atlanta Braves at Philadelphia Phillies Game Story
- `search_web({'query': 'Miami Marlins recent games August 2025'})` → [Sun, 24 Aug 2025] Google News
[Sun, 31 Aug 2025] Toronto Blue Jays at Miami Marlins Game Story, Sco
- `search_web({'query': 'Atlanta Braves vs Miami Marlins starting pitcher August 2025'})` → [Sat, 09 Aug 2025] Google News
[Fri, 08 Aug 2025] Braves 7-1 Marlins (Aug 9, 2025) Game Recap - ESPN
- `search_web({'query': 'Braves Marlins series August 2025 preview'})` → [Tue, 26 Aug 2025] Google News
[Sat, 09 Aug 2025] Atlanta Braves at Miami Marlins Preview - 08/27/20
- `get_market_context({'keyword': 'baseball MLB'})` → No related markets found for 'baseball MLB'
- `get_market_context({'keyword': 'MLB baseball prediction market'})` → No related markets found for 'MLB baseball prediction market'

## Outcome
_Pending — will be updated when market resolves_

---
*Mode: LIVE | DRY_RUN: true*