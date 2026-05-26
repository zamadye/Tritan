# Market Analysis — 2026-05-21 22:34 UTC

## Market
- **Question:** Atlanta Braves vs. Miami Marlins
- **Category:** sports
- **YES Price:** 57.0%
- **Days Left:** 7
- **Volume 24h:** $282,509
- **Liquidity:** $213,280

## Statistical Prior
- **p_base:** 60.4%
- **Source:** logistic:sports
- **N (historical):** 6077
- **Raw gap:** 3.4%

## News Sources Fetched
### Macro Context
- Fear&Greed: 29/100 (Fear) | trend: improving
- BTC: $77,633 (+0.3% 24h) → neutral
- Fear&Greed: 29/100 (Fear) | 7d trend: improving
- BTC: $77,633 (+0.3% 24h) → neutral
- Fed market expectations:

### General
- [FEAR&GREED 7d trend] 29(Fear) → 27(Fear) → 25(Extr) → 28(Fear) | sentiment improving
- Will the Fed increase interest rates by 50+ bps after the Ju → YES=50%
- [SPORTS] Recent games:
- ATL @ MIA | Scheduled | Miami Marlins(home) 22-28 score:0 vs Atlanta Braves(away) 34-16 score:0
- [SPORTS] Injuries:
- ?: Derek Law — Day-To-Day (Surgery)
- ?: Spencer Giesting — Day-To-Day (Not Specified)
- ?: A.J. Puk — 60-Day-IL (Surgery)

### Multi-Source
- [MULTI-SOURCE NEWS] 2 sources for: atlanta braves miami marlins
- [Bing News]
- [Thu, 21 May 2026] atlanta braves miami marlins
- → Here's how to watch Thursday's Miami Marlins vs Atlanta Braves game, including start times, TV channels, scores and how to stream.
- [Thu, 21 May 2026] Where to watch Atlanta Braves vs Miami Marlins: TV channel, start time, streaming for May 21
- → The Atlanta Braves are looking to take the final three games of their series against the Miami Marlins after getting shut out 12-0 in the opener. Th
- [Thu, 21 May 2026] Braves vs. Marlins Prediction, Odds, Probable Pitchers, Prop Bets for Thursday, May 21
- → The Braves are the best team in baseball and there is no denying that. On Wednesday, they just did something for the first time in over two decades.

## LLM Decision
- **Action:** SKIP
- **Confidence:** 65%
- **p_true:** 52.4%
- **Information Gap:** False
- **Crowd Bias:** False
- **Catalyst Type:** STATISTICAL_PATTERN
- **Catalyst Strength:** 0.70

### Reasoning
Strong statistical signal shows markets at 57% YES price historically resolve YES only 44.7% of time (n=13,967), creating a 12.3 percentage point edge for NO. No direct catalyst or new information, but market appears to systematically overprice YES in this range. Previous decisions on this market were SKIP due to insufficient gap, but statistical evidence now stronger.

## Gate Result
- **Passed:** ❌ NO
- **Reason:** no stat edge gap=3%<5%

## Tool Calls
- `get_sports_data({'sport': 'mlb', 'team': 'Braves'})` → INJURY [atlanta braves] Hurston Waldrep (SP): 60-Day-IL
INJURY [atlanta braves] Drake Baldwin (C): 1
- `search_web({'query': 'Atlanta Braves vs Miami Marlins June 2025'})` → [Sat, 09 Aug 2025] Google News
[Sun, 10 Aug 2025] Miami Marlins at Atlanta Braves Game Story, Scores
- `search_web({'query': 'Braves Marlins pitching matchup June 2025'})` → [Wed, 01 Apr 2026] Google News
[Wed, 27 Aug 2025] Predicting the winner of every MLB game on Wednesd
- `get_market_context({'keyword': 'Braves Marlins'})` → No related markets found for 'Braves Marlins'
- `get_market_context({'keyword': 'MLB'})` → No related markets found for 'MLB'
- `get_sports_data({'sport': 'mlb', 'team': 'Marlins'})` → INJURY [miami marlins] Robby Snelling (SP): 60-Day-IL
INJURY [miami marlins] Leo Jimenez (3B): 7-day
- `get_odds({'sport': 'baseball_mlb', 'team': 'Braves'})` → Odds API error: 401 {"message":"Usage quota has been reached. See usage plans at https://the-odds-ap
- `search_web({'query': 'Atlanta Braves vs Miami Marlins odds August 2025 betting lines'})` → [Thu, 21 May 2026] Google News
[Wed, 20 May 2026] Braves vs Marlins Prediction, Odds, Moneyline, Spr

## Outcome
_Pending — will be updated when market resolves_

---
*Mode: LIVE | DRY_RUN: true*