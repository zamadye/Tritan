# Market Analysis — 2026-05-18 14:28 UTC

## Market
- **Question:** Atlanta Braves vs. Miami Marlins
- **Category:** sports
- **YES Price:** 49.0%
- **Days Left:** 7
- **Volume 24h:** $125,505
- **Liquidity:** $300,327

## Statistical Prior
- **p_base:** 48.5%
- **Source:** logistic:sports
- **N (historical):** 6077
- **Raw gap:** 0.5%

## News Sources Fetched
### Macro Context
- Fear&Greed: 28/100 (Fear) | trend: deteriorating
- BTC: $76,677 (-1.8% 24h) → risk-OFF
- Fear&Greed: 28/100 (Fear) | 7d trend: deteriorating
- BTC: $76,783 (-1.6% 24h) → risk-OFF
- Fed market expectations:

### General
- [FEAR&GREED 7d trend] 28(Fear) → 27(Fear) → 31(Fear) → 43(Fear) | sentiment worsening
- Will the Fed increase interest rates by 25 bps after the Jun → YES=50%
- [SPORTS] Recent games:
- MIA @ TB | Final | Tampa Bay Rays(home) 30-15 score:6 vs Miami Marlins(away) 21-26 score:3
- BOS @ ATL | Final | Atlanta Braves(home) 32-15 score:8 vs Boston Red Sox(away) 19-27 score:1
- [SPORTS] Injuries:
- ?: Pavin Smith — 60-Day-IL (Surgery)
- ?: Carlos Santana — 10-Day-IL (Strain)

### Multi-Source
- [MULTI-SOURCE NEWS] 2 sources for: atlanta braves miami marlins
- [Bing News]
- [Mon, 18 May 2026] atlanta braves miami marlins
- → Here's how to watch Monday's Miami Marlins vs Atlanta Braves game, including start times, TV channels, scores and how to stream.
- [Mon, 18 May 2026] Where to watch Atlanta Braves vs Miami Marlins: TV channel, start time, streaming for May 18
- → Here is your TV guide for the upcoming NL East slate between the Atlanta Braves and the Miami Marlins ...
- [Mon, 18 May 2026] How to Watch, Probable Starters for Braves vs Marlins Series
- → The Miami Marlins are in need of a momentum boost against the Atlanta Braves.

## LLM Decision
- **Action:** SKIP
- **Confidence:** 48%
- **p_true:** 48.5%
- **Information Gap:** False
- **Crowd Bias:** False
- **Catalyst Type:** NONE
- **Catalyst Strength:** 0.05

### Reasoning
No verifiable edge. Gap is only -1% (market 49% vs base rate 48%), far below the 5% threshold required. Past decisions on identical market also resulted in SKIP. Entry points in 40-50% range have historically low WR (33%). Injuries found (Braves missing Acuna Jr., Marlins missing pitchers) but no information suggests market hasn't already priced this in. Macro risk-off environment doesn't directly affect baseball outcomes. No actionable catalyst identified.

## Gate Result
- **Passed:** ❌ NO
- **Reason:** no stat edge gap=1%<5%

## Tool Calls
- `get_sports_data({'sport': 'mlb', 'team': 'Braves'})` → INJURY [atlanta braves] Eli White (CF): 7-Day IL
INJURY [atlanta braves] Ronald Acuna Jr. (RF): 10-D
- `get_sports_data({'sport': 'mlb', 'team': 'Marlins'})` → INJURY [miami marlins] Robby Snelling (SP): 15-Day-IL
INJURY [miami marlins] Ronny Henriquez (RP): 6
- `search_web({'query': 'Atlanta Braves recent performance 2024'})` → [Tue, 05 May 2026] Google News
[Tue, 03 Mar 2026] 2026 MLB Standings and Records: Spring Training - 
- `search_web({'query': 'Miami Marlins recent performance 2024'})` → [Tue, 05 May 2026] Google News
[Sat, 20 Dec 2025] 2026 MLB Standings and Records: Spring Training - 
- `search_web({'query': 'Braves vs Marlins matchup 2024'})` → [Thu, 07 Aug 2025] Google News
[Tue, 14 Apr 2026] How to Watch Marlins vs. Braves: TV Channel &amp; 
- `get_market_context({'keyword': 'Braves Marlins'})` → No related markets found for 'Braves Marlins'
- `get_odds({'sport': 'baseball_mlb', 'team': 'Braves'})` → Odds API error: 401 {"message":"Usage quota has been reached. See usage plans at https://the-odds-ap
- `search_web({'query': 'Atlanta Braves 2025 season results record'})` → [Thu, 14 May 2026] Google News
[Tue, 05 May 2026] Atlanta Braves | History, Notable Players, &amp; F
- `search_web({'query': 'Miami Marlins 2025 season record'})` → [Tue, 05 May 2026] Google News
[Fri, 03 Apr 2026] 2026 MLB Standings and Records: Spring Training - 
- `search_web({'query': '"Braves vs Marlins" April 2024 prediction odds'})` → [Sun, 22 Sep 2024] Google News
[Thu, 09 Apr 2026] Braves vs Marlins Prediction, Odds, Moneyline, Spr

## Outcome
_Pending — will be updated when market resolves_

---
*Mode: LIVE | DRY_RUN: true*