# Market Analysis — 2026-05-21 12:57 UTC

## Market
- **Question:** Atlanta Braves vs. Miami Marlins
- **Category:** sports
- **YES Price:** 57.0%
- **Days Left:** 7
- **Volume 24h:** $107,166
- **Liquidity:** $219,266

## Statistical Prior
- **p_base:** 60.4%
- **Source:** logistic:sports
- **N (historical):** 6077
- **Raw gap:** 3.4%

## News Sources Fetched
### Macro Context
- Fear&Greed: 29/100 (Fear) | trend: improving
- BTC: $77,213 (-0.4% 24h) → neutral
- Fear&Greed: 29/100 (Fear) | 7d trend: improving
- BTC: $77,180 (-0.4% 24h) → neutral
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
- [Thu, 21 May 2026] Chris Sale strikes out 8, Austin Riley and Dominic Smith homer as Braves beat Marlins 9-1
- → The Miami Marlins will try to halt their slide on Thursday when they send ace Sandy Alcantara to the mound in the finale of their four-game home ser
- [Thu, 21 May 2026] Marlins turn to Sandy Alcantara in quest for series split vs. Braves
- → The Miami Marlins are learning one of baseball’s cruelest lessons in real time. “This game will humble you,” said Marlins starting pitcher Janson Ju

## LLM Decision
- **Action:** NO
- **Confidence:** 65%
- **p_true:** 48.4%
- **Information Gap:** False
- **Crowd Bias:** False
- **Catalyst Type:** STATISTICAL_PATTERN
- **Catalyst Strength:** 0.80

### Reasoning
Strong statistical signal (n=13,967) shows markets at 57% YES price historically resolve YES only 44.7% of the time, indicating YES is overpriced. Pattern data supports this: entry at 50-60% has only 38% win rate from 16 trades. While specific game information is limited, the large-sample statistical evidence provides a clear edge for betting NO.

## Gate Result
- **Passed:** ❌ NO
- **Reason:** no stat edge gap=3%<5%

## Tool Calls
- `get_sports_data({'sport': 'mlb', 'team': 'Braves'})` → INJURY [atlanta braves] Drake Baldwin (C): 10-Day-IL
INJURY [atlanta braves] Hurston Waldrep (SP): 1
- `get_sports_data({'sport': 'mlb', 'team': 'Marlins'})` → INJURY [miami marlins] Thomas White (SP): Day-To-Day
INJURY [miami marlins] Leo Jimenez (3B): Day-To
- `get_odds({'sport': 'baseball_mlb', 'team': 'Braves'})` → Odds API error: 401 {"message":"Usage quota has been reached. See usage plans at https://the-odds-ap
- `search_web({'query': 'Atlanta Braves vs Miami Marlins 2025 series prediction'})` → [Tue, 19 May 2026] Google News
[Sat, 16 May 2026] Braves vs Marlins Prediction, Odds, Moneyline, Spr
- `search_web({'query': 'Atlanta Braves Miami Marlins starting pitcher today 2025'})` → [Wed, 20 May 2026] Google News
[Fri, 16 Jan 2026] Miami Marlins to send down Braxton Garrett. Here’s
- `get_market_context({'keyword': 'Braves Marlins MLB'})` → No related markets found for 'Braves Marlins MLB'
- `search_web({'query': 'Braves vs Marlins May 19 2025 betting odds starting pitchers'})` → [Thu, 21 May 2026] Google News
[Tue, 19 May 2026] Braves vs Marlins Prediction, Odds, Moneyline, Spr
- `search_web({'query': 'Atlanta Braves recent form last 10 games 2025'})` → [Tue, 05 May 2026] Google News
[Wed, 05 Nov 2025] 2026 Spring Training - MLB.com
[Thu, 22 Jan 2026] 

## Outcome
_Pending — will be updated when market resolves_

---
*Mode: LIVE | DRY_RUN: true*