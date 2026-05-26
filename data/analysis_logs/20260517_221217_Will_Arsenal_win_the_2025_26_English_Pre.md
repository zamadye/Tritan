# Market Analysis — 2026-05-17 22:12 UTC

## Market
- **Question:** Will Arsenal win the 2025–26 English Premier League?
- **Category:** other
- **YES Price:** 83.0%
- **Days Left:** 9
- **Volume 24h:** $78,379
- **Liquidity:** $83,436

## Statistical Prior
- **p_base:** 64.8%
- **Source:** logistic:other
- **N (historical):** 7829
- **Raw gap:** 18.2%

## News Sources Fetched
### Macro Context
- Fear&Greed: 27/100 (Fear) | trend: deteriorating
- BTC: $78,250 (+0.1% 24h) → neutral
- Fear&Greed: 27/100 (Fear) | 7d trend: deteriorating
- BTC: $78,380 (+0.2% 24h) → neutral
- Fed market expectations:

### General
- [FEAR&GREED 7d trend] 27(Fear) → 31(Fear) → 43(Fear) → 34(Fear) | sentiment worsening
- Philadelphia Phillies vs. Pittsburgh Pirates: O/U 7.5 → YES=50%

### Multi-Source
- [MULTI-SOURCE NEWS] 2 sources for: arsenal 2025–26 english premier league
- [Bing News]
- [Tue, 05 May 2026] arsenal 2025–26 english premier league
- → Manchester City were held to a 3‑3 draw by Everton in the English Premier League, leaving Pep Guardiola’s side five points behind leaders Arsenal wi
- [Sun, 19 Apr 2026] EPL 2025-26 Points Table: When Can Arsenal Win Premier League Title – Check State Of Play After Everton Vs Man City Draw
- → Manchester City are closing in on the Premier League title after a clinical victory over Arsenal, propelled by a decisive strike from Erling Haaland
- [Fri, 17 Apr 2026] Haaland gives Man City crucial 2-1 win vs Arsenal in 2025-26 Premier League title race
- → The English Premier League 2025-26 title race comes down to Arsenal’s visit to Manchester City at the Etihad on Sunday. Let’s analyse where the matc

## LLM Decision
- **Action:** SKIP
- **Confidence:** 45%
- **p_true:** 64.8%
- **Information Gap:** True
- **Crowd Bias:** False
- **Catalyst Type:** NONE
- **Catalyst Strength:** 0.30

### Reasoning
Tight title race between Arsenal and Man City with only 2 games remaining suggests potential overpricing at 83% YES vs 65% base rate, but insufficient concrete data on exact standings, goal difference, and remaining fixtures to confirm edge. Market in final days with near-complete information makes accurate probability assessment possible but I lack the specific scenario details needed for confident action.

## Gate Result
- **Passed:** ❌ NO
- **Reason:** low conf 45%<52%

## Tool Calls
- `get_sports_data({'sport': 'soccer_epl', 'team': 'Arsenal'})` → No injury data found for soccer_epl Arsenal
- `get_sports_data({'sport': 'soccer_epl'})` → INJURY [atlanta hawks] Keshon Gilbert (G): Out
INJURY [atlanta hawks] Jock Landale (C): Out
INJURY [
- `get_odds({'sport': 'soccer_epl', 'team': 'Arsenal'})` → Odds API error: 401 {"message":"Usage quota has been reached. See usage plans at https://the-odds-ap
- `search_web({'query': 'Arsenal Premier League 2025-26 title race current standings'})` → [Sun, 17 May 2026] Google News
[Sun, 17 May 2026] Premier League 2025-26 table — Latest standings - 
- `search_web({'query': 'Arsenal Premier League title 2026 remaining games fixtures May 2026'})` → [Sun, 17 May 2026] Google News
[Wed, 13 May 2026] Arsenal and Man City's remaining Premier League fi
- `get_market_context({'keyword': 'Arsenal Premier League'})` → No related markets found for 'Arsenal Premier League'
- `get_market_context({'keyword': 'Premier League winner'})` → No related markets found for 'Premier League winner'

## Outcome
_Pending — will be updated when market resolves_

---
*Mode: LIVE | DRY_RUN: true*