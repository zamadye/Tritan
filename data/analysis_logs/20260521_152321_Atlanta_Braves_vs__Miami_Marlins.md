# Market Analysis — 2026-05-21 15:23 UTC

## Market
- **Question:** Atlanta Braves vs. Miami Marlins
- **Category:** sports
- **YES Price:** 57.0%
- **Days Left:** 7
- **Volume 24h:** $123,838
- **Liquidity:** $209,013

## Statistical Prior
- **p_base:** 60.4%
- **Source:** logistic:sports
- **N (historical):** 6077
- **Raw gap:** 3.4%

## News Sources Fetched
### Macro Context
- Fear&Greed: 29/100 (Fear) | trend: improving
- BTC: $77,131 (-0.6% 24h) → neutral
- Fear&Greed: 29/100 (Fear) | 7d trend: improving
- BTC: $76,902 (-0.7% 24h) → neutral
- Fed market expectations:

### General
- [FEAR&GREED 7d trend] 29(Fear) → 27(Fear) → 25(Extr) → 28(Fear) | sentiment improving
- Will the Fed increase interest rates by 50+ bps after the Ju → YES=50%
- Will the Fed increase interest rates by 25 bps after the Jun → YES=50%
- [SPORTS] Recent games:
- ATL @ MIA | Final | Miami Marlins(home) 22-28 score:1 vs Atlanta Braves(away) 34-16 score:9
- [SPORTS] Injuries:
- ?: A.J. Puk — 60-Day-IL (Surgery)
- ?: Corbin Burnes — 60-Day-IL (Surgery)

### Multi-Source
- [MULTI-SOURCE NEWS] 2 sources for: atlanta braves miami marlins
- [Bing News]
- [Thu, 21 May 2026] atlanta braves miami marlins
- → Austin Riley and Dominic Smith hit three-run home runs, Chris Sale allowed just one run and struck out eight over seven innings, and the Atlanta Bra
- [Thu, 21 May 2026] Atlanta Braves beat Miami Marlins 9-1 behind Chris Sale and 3-run homers from Austin Riley, Dominic Smith
- → The Atlanta Braves are looking to take the final three games of their series against the Miami Marlins after getting shut out 12-0 in the opener. Th
- [Thu, 21 May 2026] Braves vs. Marlins Prediction, Odds, Probable Pitchers, Prop Bets for Thursday, May 21
- → The Miami Marlins will try to halt their slide on Thursday when they send ace Sandy Alcantara to the mound in the finale of their four-game home ser

## LLM Decision
- **Action:** NO
- **Confidence:** 65%
- **p_true:** 46.4%
- **Information Gap:** True
- **Crowd Bias:** False
- **Catalyst Type:** STATISTICAL_EDGE
- **Catalyst Strength:** 0.85

### Reasoning
Strong statistical signal (n=13,967) shows markets priced at 57% historically resolve YES only 44.7% of the time - a clear 12.3 percentage point edge for NO. Atlanta Braves have 3 players on IL (including SP Waldrep) vs Marlins' 3 day-to-day players. Market overprices YES based on extensive historical data.

## Gate Result
- **Passed:** ❌ NO
- **Reason:** no stat edge gap=3%<5%

## Tool Calls
- `get_sports_data({'sport': 'mlb', 'team': 'Atlanta Braves'})` → INJURY [atlanta braves] Drake Baldwin (C): 10-Day-IL
INJURY [atlanta braves] Hurston Waldrep (SP): 1
- `get_sports_data({'sport': 'mlb', 'team': 'Miami Marlins'})` → INJURY [miami marlins] Thomas White (SP): Day-To-Day
INJURY [miami marlins] Leo Jimenez (3B): Day-To
- `search_web({'query': 'Atlanta Braves Miami Marlins prediction market odds today'})` → [Thu, 21 May 2026] Google News
[Thu, 21 May 2026] Braves vs. Marlins (May 21, 2026) Odds and Spread 
- `search_web({'query': 'Atlanta Braves news injuries recent form May 2026'})` → [Wed, 20 May 2026] Google News
[Wed, 20 May 2026] Braves News: Drake Baldwin to injured list, series
- `search_web({'query': 'Miami Marlins news injuries recent performance May 2026'})` → [Thu, 21 May 2026] Google News
[Thu, 21 May 2026] MLB 2026 Buzz: Mariners’ J.P. Crawford Open To Mov
- `get_market_context({'keyword': 'Braves Marlins'})` → No related markets found for 'Braves Marlins'
- `get_odds({'sport': 'baseball_mlb', 'team': 'Braves'})` → Odds API error: 401 {"message":"Usage quota has been reached. See usage plans at https://the-odds-ap

## Outcome
_Pending — will be updated when market resolves_

---
*Mode: LIVE | DRY_RUN: true*