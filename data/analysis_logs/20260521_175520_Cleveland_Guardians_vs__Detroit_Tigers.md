# Market Analysis — 2026-05-21 17:55 UTC

## Market
- **Question:** Cleveland Guardians vs. Detroit Tigers
- **Category:** sports
- **YES Price:** 44.0%
- **Days Left:** 6
- **Volume 24h:** $386,874
- **Liquidity:** $35,218

## Statistical Prior
- **p_base:** 41.0%
- **Source:** logistic:sports
- **N (historical):** 6077
- **Raw gap:** 3.0%

## News Sources Fetched
### Macro Context
- Fear&Greed: 29/100 (Fear) | trend: improving
- BTC: $77,772 (+0.3% 24h) → neutral
- Fear&Greed: 29/100 (Fear) | 7d trend: improving
- BTC: $77,738 (+0.4% 24h) → neutral
- Fed market expectations:

### General
- [FEAR&GREED 7d trend] 29(Fear) → 27(Fear) → 25(Extr) → 28(Fear) | sentiment improving
- Will the Fed increase interest rates by 50+ bps after the Ju → YES=50%
- [SPORTS] Recent games:
- CLE @ DET | In Progress | Detroit Tigers(home) 20-30 score:0 vs Cleveland Guardians(away) 29-22 score:0
- [SPORTS] Injuries:
- ?: Derek Law — Day-To-Day (Surgery)
- ?: Tommy Henry — Day-To-Day ()
- ?: Spencer Giesting — Day-To-Day (Not Specified)

### Multi-Source
- [MULTI-SOURCE NEWS] 2 sources for: cleveland guardians detroit tigers
- [Bing News]
- [Thu, 21 May 2026] cleveland guardians detroit tigers
- → The Cleveland Guardians go for the four-game series sweep when they battle the American League Central Division-rival Detroit Tigers on Thursday aft
- [Thu, 21 May 2026] Guardians vs. Tigers prediction, odds, time: 2026 MLB picks for Thursday, May 21 from advanced model
- → DETROIT — Here are the starting lineups for Thursday’s game between the Guardians and Tigers. Where: Comerica Park, 1:10 p.m. TV/radio: Cleveland Gu
- [Thu, 21 May 2026] Guardians, Detroit Tigers starting lineups for May 21, 2026: Game No. 52
- → The Guardians (29-22) look to finish off a sweep of the Tigers (20-30) this afternoon at Comerica Park. It took scoring a couple runs in the tenth, 

## LLM Decision
- **Action:** SKIP
- **Confidence:** 45%
- **p_true:** 41.0%
- **Information Gap:** False
- **Crowd Bias:** False
- **Catalyst Type:** NONE
- **Catalyst Strength:** 0.10

### Reasoning
Market appears fairly priced at 44% YES with only 3% gap above base rate (41%). Critical injury information (Tigers missing Skubal/Verlander) is 15 days old and already priced in. No new catalysts or breaking news identified. Previous analyses of same matchup also concluded SKIP due to insufficient edge.

## Gate Result
- **Passed:** ❌ NO
- **Reason:** no stat edge gap=3%<5%

## Tool Calls
- `get_sports_data({'sport': 'mlb', 'team': 'Cleveland Guardians'})` → INJURY [cleveland guardians] Gabriel Arias (SS): 10-Day-IL
INJURY [cleveland guardians] Peyton Palle
- `get_sports_data({'sport': 'mlb', 'team': 'Detroit Tigers'})` → INJURY [detroit tigers] Justin Verlander (SP): 60-Day-IL
INJURY [detroit tigers] Troy Melton (RP): 6
- `get_odds({'sport': 'baseball_mlb', 'team': 'Cleveland Guardians'})` → Odds API error: 401 {"message":"Usage quota has been reached. See usage plans at https://the-odds-ap
- `get_odds({'sport': 'baseball_mlb', 'team': 'Detroit Tigers'})` → Odds API error: 401 {"message":"Usage quota has been reached. See usage plans at https://the-odds-ap
- `search_web({'query': 'Cleveland Guardians vs Detroit Tigers 2025 prediction'})` → [Thu, 21 May 2026] Google News
[Wed, 20 May 2026] Cleveland Guardians vs. Detroit Tigers prediction,
- `search_web({'query': 'Guardians Tigers series April 2025'})` → [Wed, 29 Apr 2026] Google News
[Mon, 29 Sep 2025] Cleveland Guardians TV schedule 2026: How to watch
- `get_market_context({'keyword': 'Guardians Tigers'})` → No related markets found for 'Guardians Tigers'

## Outcome
_Pending — will be updated when market resolves_

---
*Mode: LIVE | DRY_RUN: true*