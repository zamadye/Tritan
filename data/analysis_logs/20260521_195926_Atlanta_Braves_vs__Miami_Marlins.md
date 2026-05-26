# Market Analysis — 2026-05-21 19:59 UTC

## Market
- **Question:** Atlanta Braves vs. Miami Marlins
- **Category:** sports
- **YES Price:** 57.0%
- **Days Left:** 7
- **Volume 24h:** $199,488
- **Liquidity:** $259,444

## Statistical Prior
- **p_base:** 60.4%
- **Source:** logistic:sports
- **N (historical):** 6077
- **Raw gap:** 3.4%

## News Sources Fetched
### Macro Context
- Fear&Greed: 29/100 (Fear) | trend: improving
- BTC: $77,667 (+0.1% 24h) → neutral
- Fear&Greed: 29/100 (Fear) | 7d trend: improving
- BTC: $77,551 (-0.0% 24h) → neutral
- Fed market expectations:

### General
- [FEAR&GREED 7d trend] 29(Fear) → 27(Fear) → 25(Extr) → 28(Fear) | sentiment improving
- Will the Fed increase interest rates by 50+ bps after the Ju → YES=50%
- Pittsburgh Pirates vs. St. Louis Cardinals → YES=50%
- [SPORTS] Recent games:
- ATL @ MIA | Scheduled | Miami Marlins(home) 22-28 score:0 vs Atlanta Braves(away) 34-16 score:0
- [SPORTS] Injuries:
- ?: Derek Law — Day-To-Day (Surgery)
- ?: Spencer Giesting — Day-To-Day (Not Specified)

### Multi-Source
- [MULTI-SOURCE NEWS] 2 sources for: atlanta braves miami marlins
- [Bing News]
- [Thu, 21 May 2026] atlanta braves miami marlins
- → Atlanta Braves roster update: veteran pitcher Carlos Carrasco is back in the spotlight as the team faces the Marlins.
- [Thu, 21 May 2026] Atlanta Braves Announce Unsurprising Signing Of 17-Year MLB Player Before Marlins Game
- → Here's how to watch Thursday's Miami Marlins vs Atlanta Braves game, including start times, TV channels, scores and how to stream.
- [Thu, 21 May 2026] Where to watch Atlanta Braves vs Miami Marlins: TV channel, start time, streaming for May 21
- → The Braves are the best team in baseball and there is no denying that. On Wednesday, they just did something for the first time in over two decades.

## LLM Decision
- **Action:** SKIP
- **Confidence:** 55%
- **p_true:** 60.4%
- **Information Gap:** False
- **Crowd Bias:** False
- **Catalyst Type:** STATISTICAL_MEAN_REVERSION
- **Catalyst Strength:** 0.60

### Reasoning
Stat signal strongly suggests YES is overpriced (57% market vs 44.7% historical resolution rate), but gap of 3% is below the 5% threshold required to pass the gate. Entry range 50-60% has historically weak WR of 42% (n=19). No breaking catalyst or team-specific news found. Both teams have comparable injury situations (3 IL players each). Previous decisions on this exact market also failed the gate due to insufficient gap.

## Gate Result
- **Passed:** ❌ NO
- **Reason:** no stat edge gap=3%<5%

## Tool Calls
- `get_sports_data({'sport': 'mlb', 'team': 'Atlanta Braves'})` → INJURY [atlanta braves] Hurston Waldrep (SP): 60-Day-IL
INJURY [atlanta braves] Drake Baldwin (C): 1
- `get_sports_data({'sport': 'mlb', 'team': 'Miami Marlins'})` → INJURY [miami marlins] Robby Snelling (SP): 60-Day-IL
INJURY [miami marlins] Leo Jimenez (3B): 7-day
- `search_web({'query': 'Atlanta Braves vs Miami Marlins 2025 game'})` → [Thu, 21 May 2026] Google News
[Tue, 26 Aug 2025] Where to watch Atlanta Braves vs Miami Marlins: TV
- `search_web({'query': 'Atlanta Braves Miami Marlins baseball prediction 2025'})` → [Tue, 19 May 2026] Google News
[Mon, 13 Apr 2026] Braves vs Marlins Prediction, Odds, Moneyline, Spr
- `get_market_context({'keyword': 'Atlanta Braves'})` → No related markets found for 'Atlanta Braves'
- `get_odds({'sport': 'baseball_mlb', 'team': 'Atlanta Braves'})` → Odds API error: 401 {"message":"Usage quota has been reached. See usage plans at https://the-odds-ap

## Outcome
_Pending — will be updated when market resolves_

---
*Mode: LIVE | DRY_RUN: true*