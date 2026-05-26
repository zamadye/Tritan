# Market Analysis — 2026-05-21 18:08 UTC

## Market
- **Question:** Cleveland Guardians vs. Detroit Tigers
- **Category:** sports
- **YES Price:** 46.0%
- **Days Left:** 6
- **Volume 24h:** $431,089
- **Liquidity:** $41,913

## Statistical Prior
- **p_base:** 44.0%
- **Source:** logistic:sports
- **N (historical):** 6077
- **Raw gap:** 2.0%

## News Sources Fetched
### Macro Context
- Fear&Greed: 29/100 (Fear) | trend: improving
- BTC: $77,844 (+0.5% 24h) → neutral
- Fear&Greed: 29/100 (Fear) | 7d trend: improving
- BTC: $77,618 (+0.2% 24h) → neutral
- Fed market expectations:

### General
- [FEAR&GREED 7d trend] 29(Fear) → 27(Fear) → 25(Extr) → 28(Fear) | sentiment improving
- Will the Fed increase interest rates by 50+ bps after the Ju → YES=50%
- Pittsburgh Pirates vs. St. Louis Cardinals → YES=50%
- [SPORTS] Recent games:
- CLE @ DET | In Progress | Detroit Tigers(home) 20-30 score:0 vs Cleveland Guardians(away) 29-22 score:2
- [SPORTS] Injuries:
- ?: Derek Law — Day-To-Day (Surgery)
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
- **Confidence:** 58%
- **p_true:** 44.0%
- **Information Gap:** False
- **Crowd Bias:** False
- **Catalyst Type:** INJURY_ASYMMETRY
- **Catalyst Strength:** 0.55

### Reasoning
Tigers have significant pitching injuries (Verlander 60-Day IL, Skubal 15-Day IL) which should disadvantage them, yet Guardians only priced at 46% YES. However, the gap is only -2% which is below the 5% gate threshold for actionable bets. Market appears to already reflect injury information. Historical pattern from past decisions (gap<5% → SKIP) is consistent here. With 6 days left and insufficient edge despite injury asymmetry, best action is to wait or skip.

## Gate Result
- **Passed:** ❌ NO
- **Reason:** no stat edge gap=2%<5%

## Tool Calls
- `get_sports_data({'sport': 'mlb', 'team': 'Guardians'})` → INJURY [cleveland guardians] Gabriel Arias (SS): 10-Day-IL
INJURY [cleveland guardians] Peyton Palle
- `get_sports_data({'sport': 'mlb', 'team': 'Tigers'})` → INJURY [detroit tigers] Justin Verlander (SP): 60-Day-IL
INJURY [detroit tigers] Troy Melton (RP): 6
- `search_web({'query': 'Cleveland Guardians vs Detroit Tigers 2025 matchup preview'})` → [Wed, 01 Oct 2025] Google News
[Wed, 01 Oct 2025] Guardians vs. Tigers AL Wild Card Game 2 Predictio
- `search_web({'query': 'Guardians Tigers injury report October 2025'})` → [Tue, 19 May 2026] Google News
[Thu, 02 Oct 2025] Detroit Tigers Get New Gleyber Torres Update Durin
- `get_market_context({'keyword': 'Guardians Tigers'})` → No related markets found for 'Guardians Tigers'
- `get_odds({'sport': 'baseball_mlb', 'team': 'Guardians'})` → Odds API error: 401 {"message":"Usage quota has been reached. See usage plans at https://the-odds-ap
- `search_web({'query': 'Cleveland Guardians Detroit Tigers AL Wild Card Game 2 pitching matchup October 2025'})` → [Thu, 02 Oct 2025] Google News
[Thu, 26 Mar 2026] LIVE: Tigers-Guardians AL Wild Card Series Game 3 

## Outcome
_Pending — will be updated when market resolves_

---
*Mode: LIVE | DRY_RUN: true*