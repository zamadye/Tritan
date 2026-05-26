# Market Analysis — 2026-05-21 18:22 UTC

## Market
- **Question:** Cleveland Guardians vs. Detroit Tigers
- **Category:** sports
- **YES Price:** 76.0%
- **Days Left:** 6
- **Volume 24h:** $511,288
- **Liquidity:** $27,498

## Statistical Prior
- **p_base:** 84.9%
- **Source:** logistic:sports
- **N (historical):** 6077
- **Raw gap:** 8.9%

## News Sources Fetched
### Macro Context
- Fear&Greed: 29/100 (Fear) | trend: improving
- BTC: $77,644 (+0.2% 24h) → neutral
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
- → The Guardians (29-22) look to finish off a sweep of the Tigers (20-30) this afternoon at Comerica Park. It took scoring a couple runs in the tenth, 
- [Thu, 21 May 2026] Guardians vs. Tigers prediction: Odds, recent stats, trends, and best bets for May 21
- → Here's how to watch Thursday's Detroit Tigers vs Cleveland Guardians game, including start times, TV channels, scores and how to stream.

## LLM Decision
- **Action:** SKIP
- **Confidence:** 0%
- **p_true:** 84.9%
- **Information Gap:** False
- **Crowd Bias:** False
- **Catalyst Type:** NONE
- **Catalyst Strength:** 0.00

### Reasoning


## Gate Result
- **Passed:** ❌ NO
- **Reason:** low conf 0%<52%

## Tool Calls
- `get_sports_data({'sport': 'mlb', 'team': 'Cleveland Guardians'})` → INJURY [cleveland guardians] Gabriel Arias (SS): 10-Day-IL
INJURY [cleveland guardians] Peyton Palle
- `get_sports_data({'sport': 'mlb', 'team': 'Detroit Tigers'})` → INJURY [detroit tigers] Justin Verlander (SP): 60-Day-IL
INJURY [detroit tigers] Troy Melton (RP): 6
- `search_web({'query': 'Cleveland Guardians vs Detroit Tigers injury report June 2025'})` → [Mon, 18 May 2026] Google News
[Wed, 25 Feb 2026] How to Watch Tigers Series Opener vs Guardians: TV
- `search_web({'query': 'Cleveland Guardians Detroit Tigers pitching rotation June 2025'})` → [Wed, 11 Feb 2026] Google News
[Thu, 26 Feb 2026] Current Tigers Rotation May Have Highest Upside in
- `search_web({'query': 'Cleveland Guardians Detroit Tigers today 2025'})` → [Thu, 21 May 2026] Google News
[Wed, 20 May 2026] Cleveland Guardians vs. Detroit Tigers prediction,
- `search_web({'query': 'Tigers Guardians game 2025'})` → [Thu, 21 May 2026] Google News
[Thu, 25 Sep 2025] Cleveland Guardians vs. Detroit Tigers prediction,
- `get_odds({'sport': 'baseball_mlb', 'team': 'Guardians'})` → Odds API error: 401 {"message":"Usage quota has been reached. See usage plans at https://the-odds-ap
- `get_market_context({'keyword': 'Cleveland Guardians Detroit Tigers'})` → No related markets found for 'Cleveland Guardians Detroit Tigers'

## Outcome
_Pending — will be updated when market resolves_

---
*Mode: LIVE | DRY_RUN: true*