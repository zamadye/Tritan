# Market Analysis — 2026-05-18 14:52 UTC

## Market
- **Question:** New York Mets vs. Washington Nationals
- **Category:** sports
- **YES Price:** 56.0%
- **Days Left:** 7
- **Volume 24h:** $58,505
- **Liquidity:** $254,917

## Statistical Prior
- **p_base:** 59.0%
- **Source:** logistic:sports
- **N (historical):** 6077
- **Raw gap:** 2.9%

## News Sources Fetched
### Macro Context
- Fear&Greed: 28/100 (Fear) | trend: deteriorating
- BTC: $76,363 (-2.1% 24h) → risk-OFF
- Fear&Greed: 28/100 (Fear) | 7d trend: deteriorating
- BTC: $76,350 (-2.1% 24h) → risk-OFF
- Fed market expectations:

### General
- [FEAR&GREED 7d trend] 28(Fear) → 27(Fear) → 31(Fear) → 43(Fear) | sentiment worsening
- Will the Fed increase interest rates by 25 bps after the Jun → YES=50%
- [SPORTS] Recent games:
- BAL @ WSH | Final | Washington Nationals(home) 23-24 score:3 vs Baltimore Orioles(away) 21-26 score:7
- NYY @ NYM | Final | New York Mets(home) 20-26 score:7 vs New York Yankees(away) 28-19 score:6
- [SPORTS] Injuries:
- ?: Pavin Smith — 60-Day-IL (Surgery)
- ?: Carlos Santana — 10-Day-IL (Strain)

### Multi-Source
- [MULTI-SOURCE NEWS] 2 sources for: york mets washington nationals
- [Bing News]
- [Mon, 18 May 2026] york mets washington nationals
- → Here are five things to watch and predictions as the Mets and Nationals play a four-game series in Washington, D.C.
- [Mon, 18 May 2026] Mets at Nationals: 5 things to watch and series predictions | May 18-21
- → Here's how to watch Monday's Washington Nationals vs New York Mets game, including start times, TV channels, scores and how to stream.
- [Mon, 18 May 2026] Where to watch New York Mets vs Washington Nationals: TV channel, start time, streaming for May 18
- → The New York Mets look to build on one of their most dramatic wins of the season when they open a four-game series at the Washington Nationals on Mo

## LLM Decision
- **Action:** SKIP
- **Confidence:** 65%
- **p_true:** 48.9%
- **Information Gap:** True
- **Crowd Bias:** False
- **Catalyst Type:** STATISTICAL_MISPRICING
- **Catalyst Strength:** 0.75

### Reasoning
Strong statistical evidence from STAT SIGNAL (n=13,967) shows markets at 56% resolve YES only 44.7% of the time, indicating significant overpricing of YES. While the gap is only 3%, the historical resolution data provides a clear edge with +25.7% expected value on NO bet. Injury reports don't provide clear advantage to either team.

## Gate Result
- **Passed:** ❌ NO
- **Reason:** no stat edge gap=3%<5%

## Tool Calls
- `search_web({'query': 'Polymarket "New York Mets vs. Washington Nationals" YES price 56%'})` → No search results for: Polymarket "New York Mets vs. Washington Nationals" YES price 56%
- `search_web({'query': 'Polymarket New York Mets Washington Nationals prediction market 2025'})` → [Sun, 17 May 2026] Google News
[Fri, 15 May 2026] Yankees vs Mets prediction for Sunday: Trade MLB a
- `get_sports_data({'sport': 'mlb', 'team': 'Mets'})` → INJURY [new york mets] Jared Young (1B): 10-Day-IL
INJURY [new york mets] Jorge Polanco (1B): 10-Day
- `get_odds({'sport': 'baseball_mlb', 'team': 'Mets'})` → Odds API error: 401 {"message":"Usage quota has been reached. See usage plans at https://the-odds-ap
- `get_market_context({'keyword': 'Mets Nationals'})` → No related markets found for 'Mets Nationals'
- `search_web({'query': 'Washington Nationals vs New York Mets MLB May 2026 series'})` → [Mon, 18 May 2026] Google News
[Sun, 17 May 2026] Where to watch New York Mets vs Washington Nationa
- `search_web({'query': 'MLB Mets Nationals upcoming series pitching matchup'})` → [Mon, 18 May 2026] Google News
[Thu, 26 Mar 2026] MLB Probable Pitchers Today: Full Starting Pitcher
- `get_sports_data({'sport': 'mlb', 'team': 'Nationals'})` → INJURY [washington nationals] DJ Herz (SP): 60-Day-IL
INJURY [washington nationals] Cole Henry (RP):
- `search_web({'query': 'New York Mets 2026 season record standings results'})` → [Fri, 15 May 2026] Google News
[Tue, 05 May 2026] Subway Series History: Mets vs. Yankees All-Time S
- `search_web({'query': 'Washington Nationals 2026 season record standings results'})` → [Tue, 05 May 2026] Google News
[Wed, 25 Mar 2026] 2026 MLB Standings and Records: Spring Training - 
- `search_web({'query': '"Mets" "Nationals" May 2026 odds pitcher probable'})` → [Mon, 18 May 2026] Google News
[Sat, 16 May 2026] MLB Probable Pitchers Today: Full Starting Pitcher
- `search_web({'query': 'MLB May 18 2026 Mets Nationals probable pitchers odds'})` → [Mon, 18 May 2026] Google News
[Mon, 18 May 2026] MLB Probable Pitchers Today: Full Starting Pitcher
- `get_market_context({'keyword': 'MLB baseball'})` → No related markets found for 'MLB baseball'

## Outcome
_Pending — will be updated when market resolves_

---
*Mode: LIVE | DRY_RUN: true*