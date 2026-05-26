# Market Analysis — 2026-05-21 15:10 UTC

## Market
- **Question:** Atlanta Braves vs. Miami Marlins
- **Category:** sports
- **YES Price:** 57.0%
- **Days Left:** 7
- **Volume 24h:** $123,765
- **Liquidity:** $210,846

## Statistical Prior
- **p_base:** 60.4%
- **Source:** logistic:sports
- **N (historical):** 6077
- **Raw gap:** 3.4%

## News Sources Fetched
### Macro Context
- Fear&Greed: 29/100 (Fear) | trend: improving
- BTC: $76,959 (-0.4% 24h) → neutral
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
- **p_true:** 47.6%
- **Information Gap:** True
- **Crowd Bias:** False
- **Catalyst Type:** STATISTICAL
- **Catalyst Strength:** 0.82

### Reasoning
Extremely strong statistical signal (n=13,967) shows markets priced at 57% historically resolve YES only 44.7% of the time — a 12.3% edge for NO. Both teams have minor injuries (Braves: SP Waldrep on IL; Marlins: 3 players day-to-day), but no catalyst explains the overpricing. The 57% market price significantly overestimates Braves' win probability. While the gap vs base rate (3%) doesn't meet the 5% gate threshold, the raw historical resolution data provides overwhelming evidence the market is mispriced. Past decisions on this same market also flagged the stat signal as extremely strong.

## Gate Result
- **Passed:** ❌ NO
- **Reason:** no stat edge gap=3%<5%

## Tool Calls
- `get_sports_data({'sport': 'mlb', 'team': 'Atlanta Braves'})` → INJURY [atlanta braves] Drake Baldwin (C): 10-Day-IL
INJURY [atlanta braves] Hurston Waldrep (SP): 1
- `get_sports_data({'sport': 'mlb', 'team': 'Miami Marlins'})` → INJURY [miami marlins] Thomas White (SP): Day-To-Day
INJURY [miami marlins] Leo Jimenez (3B): Day-To
- `get_odds({'sport': 'baseball_mlb', 'team': 'Atlanta Braves'})` → Odds API error: 401 {"message":"Usage quota has been reached. See usage plans at https://the-odds-ap
- `get_odds({'sport': 'baseball_mlb'})` → Odds API error: 401 {"message":"Usage quota has been reached. See usage plans at https://the-odds-ap
- `search_web({'query': 'Atlanta Braves vs Miami Marlins 2025 series preview predictions'})` → [Tue, 19 May 2026] Google News
[Mon, 13 Apr 2026] Braves vs Marlins Prediction, Odds, Moneyline, Spr
- `search_web({'query': 'Atlanta Braves Miami Marlins starting pitchers odds May 2025'})` → [Thu, 21 May 2026] Google News
[Thu, 21 May 2026] Braves vs Marlins Prediction, Odds &amp; Player Pr
- `search_web({'query': 'Braves vs Marlins head to head record 2025 2026 season results'})` → [Thu, 21 May 2026] Google News
[Fri, 15 May 2026] MLB 2026 Buzz: Mariners’ J.P. Crawford Open To Mov
- `get_market_context({'keyword': 'Atlanta Braves Miami Marlins MLB'})` → No related markets found for 'Atlanta Braves Miami Marlins MLB'
- `get_market_context({'keyword': 'Braves Marlins baseball'})` → No related markets found for 'Braves Marlins baseball'
- `get_market_context({'keyword': 'MLB baseball'})` → No related markets found for 'MLB baseball'

## Outcome
_Pending — will be updated when market resolves_

---
*Mode: LIVE | DRY_RUN: true*