# Market Analysis — 2026-05-21 20:37 UTC

## Market
- **Question:** Atlanta Braves vs. Miami Marlins
- **Category:** sports
- **YES Price:** 57.0%
- **Days Left:** 7
- **Volume 24h:** $214,801
- **Liquidity:** $267,865

## Statistical Prior
- **p_base:** 60.4%
- **Source:** logistic:sports
- **N (historical):** 6077
- **Raw gap:** 3.4%

## News Sources Fetched
### Macro Context
- Fear&Greed: 29/100 (Fear) | trend: improving
- BTC: $77,673 (+0.1% 24h) → neutral
- Fear&Greed: 29/100 (Fear) | 7d trend: improving
- BTC: $77,637 (+0.1% 24h) → neutral
- Fed market expectations:

### General
- [FEAR&GREED 7d trend] 29(Fear) → 27(Fear) → 25(Extr) → 28(Fear) | sentiment improving
- Pittsburgh Pirates vs. St. Louis Cardinals → YES=50%
- Will the Fed increase interest rates by 50+ bps after the Ju → YES=50%
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
- → MIAMI (AP) — Austin Riley and Dominic Smith hit three-run home runs, Chris Sale allowed just one run and struck out eight over seven innings, and th

## LLM Decision
- **Action:** SKIP
- **Confidence:** 55%
- **p_true:** 60.4%
- **Information Gap:** False
- **Crowd Bias:** False
- **Catalyst Type:** NONE
- **Catalyst Strength:** 0.10

### Reasoning
Stat signal indicates market at 57% historically resolves YES only 44.7% (n=13,967) — systematic overpricing. However: (1) Gap of 3% fails to meet 5% gate threshold; (2) This exact market was attempted TWICE before and FAILED both times for insufficient edge; (3) Entry 50-60% range shows weak 42% WR (n=19); (4) No specific catalysts identified — injuries are symmetric (both teams have 3 IL players), no clear pitching matchup advantage discovered; (5) Cannot confirm what specific outcome market asks (game winner? series? run line?). Despite systematic stat edge, insufficient gap + no fresh catalyst + pattern of failed attempts = SKIP.

## Gate Result
- **Passed:** ❌ NO
- **Reason:** no stat edge gap=3%<5%

## Tool Calls
- `get_sports_data({'sport': 'mlb', 'team': 'Atlanta Braves'})` → INJURY [atlanta braves] Hurston Waldrep (SP): 60-Day-IL
INJURY [atlanta braves] Drake Baldwin (C): 1
- `get_sports_data({'sport': 'mlb', 'team': 'Miami Marlins'})` → INJURY [miami marlins] Robby Snelling (SP): 60-Day-IL
INJURY [miami marlins] Leo Jimenez (3B): 7-day
- `search_web({'query': 'Atlanta Braves vs Miami Marlins game 2025'})` → [Tue, 26 Aug 2025] Google News
[Sat, 09 Aug 2025] Atlanta Braves at Miami Marlins Game Story, Scores
- `search_web({'query': 'Braves Marlins prediction odds'})` → [Thu, 21 May 2026] Google News
[Tue, 19 May 2026] Braves vs Marlins Prediction, Odds, Start Time, Pr
- `get_odds({'sport': 'baseball_mlb', 'team': 'Atlanta Braves'})` → Odds API error: 401 {"message":"Usage quota has been reached. See usage plans at https://the-odds-ap
- `search_web({'query': 'Atlanta Braves schedule September 2025'})` → [Wed, 17 Sep 2025] Google News
[Wed, 24 Sep 2025] Atlanta Braves at Washington Nationals Preview - 0
- `search_web({'query': 'Miami Marlins schedule September 2025'})` → [Tue, 19 May 2026] Google News
[Thu, 18 Sep 2025] 2026 New York Mets TV schedule: How to watch, stre

## Outcome
_Pending — will be updated when market resolves_

---
*Mode: LIVE | DRY_RUN: true*