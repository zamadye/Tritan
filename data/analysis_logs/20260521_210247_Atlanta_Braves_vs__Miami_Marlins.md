# Market Analysis — 2026-05-21 21:02 UTC

## Market
- **Question:** Atlanta Braves vs. Miami Marlins
- **Category:** sports
- **YES Price:** 57.0%
- **Days Left:** 7
- **Volume 24h:** $216,552
- **Liquidity:** $222,993

## Statistical Prior
- **p_base:** 60.4%
- **Source:** logistic:sports
- **N (historical):** 6077
- **Raw gap:** 3.4%

## News Sources Fetched
### Macro Context
- Fear&Greed: 29/100 (Fear) | trend: improving
- BTC: $77,650 (+0.0% 24h) → neutral
- Fear&Greed: 29/100 (Fear) | 7d trend: improving
- BTC: $77,650 (+0.0% 24h) → neutral
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
- → MIAMI (AP) — Austin Riley and Dominic Smith hit three-run home runs, Chris Sale allowed just one run and struck out eight over seven innings, and th
- [Thu, 21 May 2026] Braves beat Marlins 9-1 behind Chris Sale and 3-run homers from Austin Riley, Dominic Smith
- → Atlanta Braves roster update: veteran pitcher Carlos Carrasco is back in the spotlight as the team faces the Marlins.

## LLM Decision
- **Action:** SKIP
- **Confidence:** 45%
- **p_true:** 60.4%
- **Information Gap:** False
- **Crowd Bias:** False
- **Catalyst Type:** NONE
- **Catalyst Strength:** 0.00

### Reasoning
Market at 57% shows overpricing per stat signal (44.7% historical resolution, n=13,967), but gap (3%) fails the 5% gate threshold. Both teams have pitching injuries (Braves: Waldrep, Marlins: Snelling, White) with no clear advantage. No fresh catalyst found. Previous decisions on this exact market also SKIPped for identical reasons. Sports entry 50-60% range shows weak 42% WR from 19 trades. Stat signal is strong but insufficient edge to justify bet.

## Gate Result
- **Passed:** ❌ NO
- **Reason:** no stat edge gap=3%<5%

## Tool Calls
- `get_sports_data({'sport': 'mlb', 'team': 'Atlanta Braves'})` → INJURY [atlanta braves] Hurston Waldrep (SP): 60-Day-IL
INJURY [atlanta braves] Drake Baldwin (C): 1
- `get_sports_data({'sport': 'mlb', 'team': 'Miami Marlins'})` → INJURY [miami marlins] Robby Snelling (SP): 60-Day-IL
INJURY [miami marlins] Leo Jimenez (3B): 7-day
- `search_web({'query': 'Atlanta Braves vs Miami Marlins 2025 game preview starting pitchers'})` → [Wed, 20 May 2026] Google News
[Wed, 20 May 2026] MLB Probable Pitchers Today: Full Starting Pitcher
- `search_web({'query': 'Atlanta Braves Marlins odds today May 2026'})` → [Thu, 21 May 2026] Google News
[Thu, 21 May 2026] Atlanta Braves at Miami Marlins odds, picks, and p
- `get_odds({'sport': 'baseball_mlb', 'team': 'Braves'})` → Odds API error: 401 {"message":"Usage quota has been reached. See usage plans at https://the-odds-ap
- `get_market_context({'keyword': 'Atlanta Braves Miami Marlins'})` → No related markets found for 'Atlanta Braves Miami Marlins'
- `search_web({'query': 'Atlanta Braves vs Miami Marlins May 2026 series preview'})` → [Thu, 21 May 2026] Google News
[Thu, 21 May 2026] Braves vs. Marlins (May 21, 2026) Pregame - ESPN
[
- `get_odds({'sport': 'baseball_mlb'})` → Odds API error: 401 {"message":"Usage quota has been reached. See usage plans at https://the-odds-ap
- `search_web({'query': 'Braves vs Marlins May 21 2026 moneyline odds DraftKings'})` → [Thu, 21 May 2026] Google News
[Thu, 21 May 2026] Atlanta Braves vs. Miami Marlins prediction, pick 

## Outcome
_Pending — will be updated when market resolves_

---
*Mode: LIVE | DRY_RUN: true*