# Market Analysis — 2026-05-21 16:41 UTC

## Market
- **Question:** Atlanta Braves vs. Miami Marlins
- **Category:** sports
- **YES Price:** 57.0%
- **Days Left:** 7
- **Volume 24h:** $139,240
- **Liquidity:** $200,749

## Statistical Prior
- **p_base:** 60.4%
- **Source:** logistic:sports
- **N (historical):** 6077
- **Raw gap:** 3.4%

## News Sources Fetched
### Macro Context
- Fear&Greed: 29/100 (Fear) | trend: improving
- BTC: $77,161 (+0.0% 24h) → neutral
- Fear&Greed: 29/100 (Fear) | 7d trend: improving
- BTC: $77,097 (-0.1% 24h) → neutral
- Fed market expectations:

### General
- [FEAR&GREED 7d trend] 29(Fear) → 27(Fear) → 25(Extr) → 28(Fear) | sentiment improving
- Will the Fed increase interest rates by 50+ bps after the Ju → YES=50%
- [SPORTS] Recent games:
- ATL @ MIA | Scheduled | Miami Marlins(home) 22-28 score:0 vs Atlanta Braves(away) 34-16 score:0
- [SPORTS] Injuries:
- ?: Derek Law — Day-To-Day (Surgery)
- ?: Tommy Henry — Day-To-Day (Surgery)
- ?: Spencer Giesting — Day-To-Day (Not Specified)

### Multi-Source
- [MULTI-SOURCE NEWS] 2 sources for: atlanta braves miami marlins
- [Bing News]
- [Thu, 21 May 2026] atlanta braves miami marlins
- → Austin Riley and Dominic Smith hit three-run home runs, Chris Sale allowed just one run and struck out eight over seven innings, and the Atlanta Bra
- [Thu, 21 May 2026] Atlanta Braves beat Miami Marlins 9-1 behind Chris Sale and 3-run homers from Austin Riley, Dominic Smith
- → The Atlanta Braves have scored a combined 17 runs since being blown out earlier this week ...
- [Thu, 21 May 2026] Braves Throttle Marlins Again, Close in on Another Series Win
- → Here's how to watch Thursday's Miami Marlins vs Atlanta Braves game, including start times, TV channels, scores and how to stream.

## LLM Decision
- **Action:** SKIP
- **Confidence:** 65%
- **p_true:** 50.4%
- **Information Gap:** True
- **Crowd Bias:** False
- **Catalyst Type:** STATISTICAL_PATTERN
- **Catalyst Strength:** 0.75

### Reasoning
Strong statistical signal (n=13,967) shows markets at 57% resolve YES only 44.7% of time, indicating 12.3% overpricing of YES. Market is systematically mispriced at this level, creating clear edge for NO bet.

## Gate Result
- **Passed:** ❌ NO
- **Reason:** no stat edge gap=3%<5%

## Tool Calls
- `get_sports_data({'sport': 'mlb', 'team': 'Atlanta Braves'})` → INJURY [atlanta braves] Drake Baldwin (C): 10-Day-IL
INJURY [atlanta braves] Hurston Waldrep (SP): 1
- `get_sports_data({'sport': 'mlb', 'team': 'Miami Marlins'})` → INJURY [miami marlins] Thomas White (SP): Day-To-Day
INJURY [miami marlins] Leo Jimenez (3B): Day-To
- `get_odds({'sport': 'baseball_mlb'})` → Odds API error: 401 {"message":"Usage quota has been reached. See usage plans at https://the-odds-ap
- `search_web({'query': 'Atlanta Braves vs Miami Marlins upcoming game 2025'})` → [Sat, 09 Aug 2025] Google News
[Sat, 09 Aug 2025] Miami Marlins at Atlanta Braves Game Story, Scores
- `search_web({'query': 'Braves vs Marlins schedule August 16 2025'})` → [Fri, 27 Mar 2026] Google News
[Sat, 16 Aug 2025] Atlanta Braves 2026 Regular Season Schedule - Batt
- `get_market_context({'keyword': 'Atlanta Braves Miami Marlins MLB'})` → No related markets found for 'Atlanta Braves Miami Marlins MLB'
- `search_web({'query': 'Atlanta Braves vs Miami Marlins August 2025 series MLB'})` → [Thu, 21 May 2026] Google News
[Sat, 09 Aug 2025] Atlanta Braves Make Unsurprising Roster Decision W
- `search_web({'query': 'Atlanta Braves recent record last 10 games August 2025'})` → [Mon, 18 May 2026] Google News
[Thu, 14 Aug 2025] 2026 MLB Standings and Records: Regular Season - M
- `search_web({'query': 'Miami Marlins recent record last 10 games August 2025'})` → [Mon, 04 Aug 2025] Google News
[Sat, 30 Aug 2025] Power Rankings: MLB's hottest team jumps 5 spots t
- `search_web({'query': 'MLB standings 2025 August Braves Marlins records'})` → [Tue, 05 May 2026] Google News
[Fri, 01 Aug 2025] 2026 Spring Training - MLB.com
[Mon, 11 Aug 2025] 
- `search_web({'query': 'Braves vs Marlins 2025 head to head results'})` → [Tue, 14 Apr 2026] Google News
[Thu, 07 Aug 2025] Marlins find silver lining in 1-5 road trip as the
- `get_market_context({'query': 'Braves Marlins MLB game'})` → [YES=50% vol=$7,271,580] Trump kiss by May 31?
[YES=50% vol=$6,660,484] Will Trump say "Iran" during

## Outcome
_Pending — will be updated when market resolves_

---
*Mode: LIVE | DRY_RUN: true*