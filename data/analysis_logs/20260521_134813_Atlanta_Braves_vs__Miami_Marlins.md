# Market Analysis — 2026-05-21 13:48 UTC

## Market
- **Question:** Atlanta Braves vs. Miami Marlins
- **Category:** sports
- **YES Price:** 57.0%
- **Days Left:** 7
- **Volume 24h:** $111,489
- **Liquidity:** $223,694

## Statistical Prior
- **p_base:** 60.4%
- **Source:** logistic:sports
- **N (historical):** 6077
- **Raw gap:** 3.4%

## News Sources Fetched
### Macro Context
- Fear&Greed: 29/100 (Fear) | trend: improving
- BTC: $76,772 (-0.5% 24h) → neutral
- Fear&Greed: 29/100 (Fear) | 7d trend: improving
- BTC: $76,772 (-0.5% 24h) → neutral
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
- → The Miami Marlins will try to halt their slide on Thursday when they send ace Sandy Alcantara to the mound in the finale of their four-game home ser
- [Thu, 21 May 2026] Marlins turn to Sandy Alcantara in quest for series split vs. Braves
- → Atlanta Braves (34-16, first in the NL East) vs. Miami Marlins (22-28, fourth in the NL East) Miami; Thursday, 6:40 p.m. EDT PITCHING PROBABLES: Bra

## LLM Decision
- **Action:** NO
- **Confidence:** 65%
- **p_true:** 48.4%
- **Information Gap:** True
- **Crowd Bias:** False
- **Catalyst Type:** STATISTICAL_MISPRICING
- **Catalyst Strength:** 0.80

### Reasoning
Extremely strong statistical signal (n=13,967) shows markets at 57% YES historically resolve YES only 44.7% of the time, creating 12.3% edge for NO. Entry 50-60% pattern shows WR=38% for YES. Market overprices YES based on historical mispricing patterns.

## Gate Result
- **Passed:** ❌ NO
- **Reason:** no stat edge gap=3%<5%

## Tool Calls
- `get_sports_data({'sport': 'mlb', 'team': 'Braves'})` → INJURY [atlanta braves] Drake Baldwin (C): 10-Day-IL
INJURY [atlanta braves] Hurston Waldrep (SP): 1
- `get_sports_data({'sport': 'mlb', 'team': 'Marlins'})` → INJURY [miami marlins] Thomas White (SP): Day-To-Day
INJURY [miami marlins] Leo Jimenez (3B): Day-To
- `search_web({'query': 'Atlanta Braves vs Miami Marlins game today'})` → [Wed, 20 May 2026] Google News
[Tue, 19 May 2026] Braves vs. Marlins (May 20, 2026) Live Score - ESP
- `search_web({'query': 'Braves vs Marlins May 20 2026 odds'})` → [Wed, 20 May 2026] Google News
[Thu, 21 May 2026] How to watch Braves vs. Marlins: TV channel and st
- `get_odds({'sport': 'baseball_mlb', 'team': 'Braves'})` → Odds API error: 401 {"message":"Usage quota has been reached. See usage plans at https://the-odds-ap
- `get_market_context({'keyword': 'Braves Marlins'})` → No related markets found for 'Braves Marlins'

## Outcome
_Pending — will be updated when market resolves_

---
*Mode: LIVE | DRY_RUN: true*