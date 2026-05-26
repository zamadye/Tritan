# Market Analysis — 2026-05-21 18:42 UTC

## Market
- **Question:** New York Mets vs. Washington Nationals
- **Category:** sports
- **YES Price:** 51.0%
- **Days Left:** 7
- **Volume 24h:** $75,541
- **Liquidity:** $188,726

## Statistical Prior
- **p_base:** 51.5%
- **Source:** logistic:sports
- **N (historical):** 6077
- **Raw gap:** 0.5%

## News Sources Fetched
### Macro Context
- Fear&Greed: 29/100 (Fear) | trend: improving
- BTC: $77,674 (+0.3% 24h) → neutral
- Fear&Greed: 29/100 (Fear) | 7d trend: improving
- BTC: $77,739 (+0.4% 24h) → neutral
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
- → As the Mets prepare to close out their series against the Nationals, manager Carlos Mendoza made a crucial pitching decision.
- [Thu, 21 May 2026] Mets make David Peterson move for series finale with Nationals
- → New York Mets star Juan Soto shared an old viral video from his time when he was a member of the Washington Nationals.

## LLM Decision
- **Action:** SKIP
- **Confidence:** 62%
- **p_true:** 43.5%
- **Information Gap:** True
- **Crowd Bias:** False
- **Catalyst Type:** STATISTICAL
- **Catalyst Strength:** 0.70

### Reasoning
Strong statistical signal (n=13,967) shows 51% markets resolve YES only 44.7% of the time, creating a ~6.3% edge for NO. Market overprices YES by 1% above base rate. Both teams have multiple pitching injuries. Past decisions skipped due to small gap (<5%), but the persistent statistical pattern suggests a profitable NO bet.

## Gate Result
- **Passed:** ❌ NO
- **Reason:** no stat edge gap=1%<5%

## Tool Calls
- `get_sports_data({'sport': 'mlb', 'team': 'Mets'})` → INJURY [new york mets] A.J. Minter (RP): 60-Day-IL
INJURY [new york mets] Clay Holmes (SP): 60-Day-I
- `get_sports_data({'sport': 'mlb', 'team': 'Washington Nationals'})` → INJURY [washington nationals] DJ Herz (SP): 60-Day-IL
INJURY [washington nationals] Cole Henry (RP):
- `search_web({'query': 'New York Mets recent performance 2024 season'})` → [Mon, 04 May 2026] Google News
[Tue, 05 May 2026] What can the 2026 Mets learn from 2024’s turnaroun
- `search_web({'query': 'Washington Nationals recent results 2024'})` → [Tue, 27 Aug 2024] Google News
[Wed, 03 Jul 2024] New York Yankees at Washington Nationals Game Stor
- `search_web({'query': '"New York Mets" "Washington Nationals" 2026 game'})` → [Wed, 20 May 2026] Google News
[Thu, 21 May 2026] New York Mets at Washington Nationals Game Story, 
- `search_web({'query': 'Mets Nationals matchup 2026 schedule'})` → [Wed, 20 May 2026] Google News
[Wed, 20 May 2026] Experts update Mets vs. Nationals prediction after
- `get_odds({'sport': 'baseball_mlb', 'team': 'Mets'})` → Odds API error: 401 {"message":"Usage quota has been reached. See usage plans at https://the-odds-ap
- `get_odds({'sport': 'baseball_mlb'})` → Odds API error: 401 {"message":"Usage quota has been reached. See usage plans at https://the-odds-ap
- `get_market_context({'keyword': 'Mets Nationals'})` → No related markets found for 'Mets Nationals'
- `get_market_context({'keyword': 'MLB'})` → No related markets found for 'MLB'

## Outcome
_Pending — will be updated when market resolves_

---
*Mode: LIVE | DRY_RUN: true*