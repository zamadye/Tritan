# Market Analysis — 2026-05-21 14:23 UTC

## Market
- **Question:** Atlanta Braves vs. Miami Marlins
- **Category:** sports
- **YES Price:** 57.0%
- **Days Left:** 7
- **Volume 24h:** $111,696
- **Liquidity:** $235,938

## Statistical Prior
- **p_base:** 60.4%
- **Source:** logistic:sports
- **N (historical):** 6077
- **Raw gap:** 3.4%

## News Sources Fetched
### Macro Context
- Fear&Greed: 29/100 (Fear) | trend: improving
- BTC: $76,919 (-0.6% 24h) → neutral
- Fear&Greed: 29/100 (Fear) | 7d trend: improving
- BTC: $76,816 (-0.7% 24h) → neutral
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
- → The Miami Marlins are learning one of baseball’s cruelest lessons in real time. “This game will humble you,” said Marlins starting pitcher Janson Ju

## LLM Decision
- **Action:** SKIP
- **Confidence:** 0%
- **p_true:** 60.4%
- **Information Gap:** False
- **Crowd Bias:** False
- **Catalyst Type:** NONE
- **Catalyst Strength:** 0.00

### Reasoning


## Gate Result
- **Passed:** ❌ NO
- **Reason:** no stat edge gap=3%<5%

## Tool Calls
- `get_sports_data({'sport': 'mlb', 'team': 'Atlanta Braves'})` → INJURY [atlanta braves] Drake Baldwin (C): 10-Day-IL
INJURY [atlanta braves] Hurston Waldrep (SP): 1
- `get_sports_data({'sport': 'mlb', 'team': 'Miami Marlins'})` → INJURY [miami marlins] Thomas White (SP): Day-To-Day
INJURY [miami marlins] Leo Jimenez (3B): Day-To
- `get_odds({'sport': 'baseball_mlb'})` → Odds API error: 401 {"message":"Usage quota has been reached. See usage plans at https://the-odds-ap
- `search_web({'query': 'Atlanta Braves vs Miami Marlins game 2025'})` → [Tue, 26 Aug 2025] Google News
[Sat, 09 Aug 2025] Atlanta Braves at Miami Marlins Game Story, Scores
- `search_web({'query': 'Braves Marlins betting odds 2025'})` → [Tue, 19 May 2026] Google News
[Wed, 15 Apr 2026] Braves vs Marlins Prediction, Odds, Moneyline, Spr
- `get_market_context({'keyword': 'Braves'})` → No related markets found for 'Braves'
- `search_web({'query': 'Braves vs Marlins schedule August 2025'})` → [Sat, 09 Aug 2025] Google News
[Mon, 25 Aug 2025] Miami Marlins at Atlanta Braves Game Story, Scores
- `search_web({'query': 'Braves Marlins next game August 2025'})` → [Sat, 09 Aug 2025] Google News
[Wed, 27 Aug 2025] Miami Marlins at Atlanta Braves Game Story, Scores
- `search_web({'query': 'August 27 2025 Braves Marlins'})` → [Wed, 27 Aug 2025] Google News
[Wed, 27 Aug 2025] Atlanta Braves at Miami Marlins Game Story, Scores
- `search_web({'query': 'Braves Marlins odds August 27 2025'})` → [Thu, 21 May 2026] Google News
[Tue, 19 May 2026] Braves vs Marlins Prediction, Odds, Moneyline, Spr

## Outcome
_Pending — will be updated when market resolves_

---
*Mode: LIVE | DRY_RUN: true*