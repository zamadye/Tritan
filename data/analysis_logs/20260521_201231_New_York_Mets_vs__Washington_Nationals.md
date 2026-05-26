# Market Analysis — 2026-05-21 20:12 UTC

## Market
- **Question:** New York Mets vs. Washington Nationals
- **Category:** sports
- **YES Price:** 51.0%
- **Days Left:** 6
- **Volume 24h:** $289,872
- **Liquidity:** $182,188

## Statistical Prior
- **p_base:** 51.5%
- **Source:** logistic:sports
- **N (historical):** 6077
- **Raw gap:** 0.5%

## News Sources Fetched
### Macro Context
- Fear&Greed: 29/100 (Fear) | trend: improving
- BTC: $77,653 (+0.0% 24h) → neutral
- Fear&Greed: 29/100 (Fear) | 7d trend: improving
- BTC: $77,550 (-0.0% 24h) → neutral
- Fed market expectations:

### General
- [FEAR&GREED 7d trend] 29(Fear) → 27(Fear) → 25(Extr) → 28(Fear) | sentiment improving
- Will the Fed increase interest rates by 50+ bps after the Ju → YES=50%
- Pittsburgh Pirates vs. St. Louis Cardinals → YES=50%
- [SPORTS] Recent games:
- NYM @ WSH | Scheduled | Washington Nationals(home) 25-25 score:0 vs New York Mets(away) 21-28 score:0
- TOR @ NYY | Scheduled | New York Yankees(home) 30-20 score:0 vs Toronto Blue Jays(away) 22-27 score:0
- [SPORTS] Injuries:
- ?: Derek Law — Day-To-Day (Surgery)

### Multi-Source
- [MULTI-SOURCE NEWS] 2 sources for: york mets washington nationals
- [Bing News]
- [Thu, 21 May 2026] york mets washington nationals
- → The Mets have seen firsthand why the Nationals are the top-scoring offense in Major League Baseball through the opening three games of their series.
- [Thu, 21 May 2026] NY Mets announce lineup today vs Nationals as they seek a series split
- → Follow our live updates as the New York Mets close out their four-game series against the Nationals on Thursday afternoon at Nationals Park.
- [Thu, 21 May 2026] NY Mets vs Nationals live updates, score and analysis of today's game
- → Washington's potent offense continues to chug along in our Mets vs. Nationals predictions and MLB picks on Thursday, May 21.

## LLM Decision
- **Action:** SKIP
- **Confidence:** 65%
- **p_true:** 45.5%
- **Information Gap:** True
- **Crowd Bias:** False
- **Catalyst Type:** MARKET_INEFFICIENCY_STATISTICAL_SIGNAL
- **Catalyst Strength:** 0.65

### Reasoning
Strong statistical signal from large sample (n=13,967) shows markets priced at 51% resolve YES only 44.7% of the time - a 6.3% edge for NO. Market overprices YES despite both teams having comparable injury situations to starting/relief pitchers. Sports category shows strong historical performance (76% WR). However, limited direct catalyst and small gap (+1%) reduces confidence. Previous decisions correctly identified the stat edge but skipped due to gap threshold.

## Gate Result
- **Passed:** ❌ NO
- **Reason:** no stat edge gap=1%<5%

## Tool Calls
- `get_sports_data({'sport': 'mlb', 'team': 'New York Mets'})` → INJURY [new york mets] Kodai Senga (SP): 15-Day-IL
INJURY [new york mets] A.J. Minter (RP): 60-Day-I
- `get_sports_data({'sport': 'mlb', 'team': 'Washington Nationals'})` → INJURY [washington nationals] DJ Herz (SP): 60-Day-IL
INJURY [washington nationals] Cole Henry (RP):
- `search_web({'query': 'New York Mets recent results and standings'})` → [Wed, 22 Apr 2026] Google News
[Tue, 05 May 2026] Mets finally win a game, but Lindor exits early - 
- `search_web({'query': 'Washington Nationals recent results and standings'})` → [Tue, 19 May 2026] Google News
[Wed, 20 May 2026] Mets make NL history, score 10 runs in the 12th in
- `get_odds({'sport': 'baseball_mlb', 'team': 'Mets'})` → Odds API error: 401 {"message":"Usage quota has been reached. See usage plans at https://the-odds-ap
- `get_market_context({'keyword': 'Mets Nationals MLB'})` → No related markets found for 'Mets Nationals MLB'
- `search_web({'query': 'Mets vs Nationals May 2026 game preview matchup'})` → [Wed, 20 May 2026] Google News
[Wed, 20 May 2026] Game Notes: New York Mets vs Washington Nationals 
- `search_web({'query': 'MLB standings 2026 Mets Nationals win loss record'})` → [Tue, 05 May 2026] Google News
[Tue, 19 May 2026] 2026 MLB Standings and Records: Spring Training - 
- `search_web({'query': '"New York Mets" "Washington Nationals" May 21 2026 probable pitchers betting'})` → [Thu, 21 May 2026] Google News
[Thu, 21 May 2026] Mets vs. Nationals Prediction, Odds, Probable Pitc
- `get_market_context({'keyword': 'MLB baseball today'})` → No related markets found for 'MLB baseball today'
- `search_web({'query': 'Mets Nationals May 21 2026 odds prediction starting pitchers'})` → [Thu, 21 May 2026] Google News
[Thu, 21 May 2026] Mets vs Nationals Prediction, Picks &amp; Odds for
- `search_web({'query': 'site:sportsline.com OR site:covers.com "Mets" "Nationals" May 21 2026 moneyline odds'})` → [Fri, 16 Mar 2012] Google News
[Sun, 26 Jul 2020] Sports Picks, Vegas Odds, Betting Lines, and Exper
- `search_web({'query': 'New York Mets 2026 record wins losses standings NL East'})` → [Tue, 21 Apr 2026] Google News
[Tue, 24 Mar 2026] Can the 2026 Mets Be Salvaged? - FanGraphs
[Thu, 2

## Outcome
_Pending — will be updated when market resolves_

---
*Mode: LIVE | DRY_RUN: true*