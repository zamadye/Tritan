# Market Analysis — 2026-05-17 20:29 UTC

## Market
- **Question:** Geneva Open: Jenson Brooksby vs Casper Ruud
- **Category:** sports
- **YES Price:** 22.0%
- **Days Left:** 7
- **Volume 24h:** $73,214
- **Liquidity:** $35,744

## Statistical Prior
- **p_base:** 13.0%
- **Source:** logistic:sports
- **N (historical):** 6077
- **Raw gap:** 9.0%

## News Sources Fetched
### Macro Context
- Fear&Greed: 27/100 (Fear) | trend: deteriorating
- BTC: $78,258 (-0.0% 24h) → neutral
- Fear&Greed: 27/100 (Fear) | 7d trend: deteriorating
- BTC: $78,247 (-0.0% 24h) → neutral
- Fed market expectations:

### General
- [FEAR&GREED 7d trend] 27(Fear) → 31(Fear) → 43(Fear) → 34(Fear) | sentiment worsening
- Philadelphia Phillies vs. Pittsburgh Pirates: O/U 7.5 → YES=50%

### Multi-Source
- [MULTI-SOURCE NEWS] 2 sources for: geneva open: jenson brooksby casper
- [Bing News]
- [Sat, 16 May 2026] geneva open: jenson brooksby casper
- → May in Switzerland and sees Novak Djokovic as the defending champion but unlike previous years, he won't return to play in the tournament in ...
- [] Geneva Open 2026: Results, Draw, Schedule, Entry List, Prize Money and Predictions
- [Metaculus]
- [] Will the next IPC Sudan acute food insecurity analysis classify at lea
- → Community: pending

## LLM Decision
- **Action:** NO
- **Confidence:** 63%
- **p_true:** 11.0%
- **Information Gap:** False
- **Crowd Bias:** False
- **Catalyst Type:** STATISTICAL_OVERPRICING
- **Catalyst Strength:** 0.55

### Reasoning
Market is overpricing Brooksby's chances. YES price (22%) is 9 points above the base rate (13%, n=6077). Casper Ruud is a elite clay court player (multiple Roland Garros finalist) while Brooksby was ranked ~507 in early 2025 - significant ranking/skill gap favors Ruud. No specific catalyst found to justify the elevated YES price. Historical base rate suggests Brooksby wins only ~13% of similar matchups, yet market prices him at 22%. This represents a statistical edge for BET_NO.

## Gate Result
- **Passed:** ✅ YES
- **Reason:** BET NO $1.00

## Tool Calls
- `search_web({'query': 'Jenson Brooksby recent form 2024 Geneva Open'})` → [Tue, 18 Nov 2025] Google News
[Wed, 12 Dec 2018] Men's tennis calendar and 2025 ATP Tour schedule: 
- `search_web({'query': 'Casper Ruud recent results 2024 clay court form'})` → [Thu, 02 Apr 2026] Google News
[Tue, 12 May 2026] ATP Power Rankings: Is it Sinner Time on Clay? - N
- `get_market_context({'keyword': 'Geneva Open Brooksby Ruud tennis'})` → No related markets found for 'Geneva Open Brooksby Ruud tennis'
- `get_odds({'sport': 'tennis_atp', 'team': 'Brooksby Ruud'})` → Odds API error: 404 {"message":"Unknown sport","error_code":"UNKNOWN_SPORT","details_url":"https://t
- `get_odds({'sport': 'tennis_atp_italian_open', 'team': 'Brooksby Ruud'})` → No odds available for tennis_atp_italian_open
- `search_web({'query': 'Casper Ruud Jenson Brooksby head to head record ATP'})` → [Fri, 15 May 2026] Google News
[Sun, 28 Sep 2025] Jenson Brooksby vs Casper Ruud: Live Scores, Resul
- `search_web({'query': '"Geneva Open 2025" Brooksby Ruud draw bracket'})` → No search results for: "Geneva Open 2025" Brooksby Ruud draw bracket
- `search_web({'query': 'Jenson Brooksby ranking 2025 current form results'})` → [Thu, 02 Oct 2025] Google News
[Thu, 21 Aug 2025] Home favourite Shang earns opening win in Shanghai
- `search_web({'query': 'Casper Ruud 2025 season results wins losses clay court'})` → [Mon, 06 Apr 2026] Google News
[Sun, 07 Dec 2025] Carlos Alcaraz: Monte-Carlo draw, history, recent 
- `search_web({'query': 'Jenson Brooksby 2025 season results wins losses current ranking'})` → [Wed, 16 Apr 2025] Google News
[Wed, 02 Apr 2025] 2025 Roland Garros entry list: Defending champion 
- `search_web({'query': 'Brooksby ATP ranking 2025 May June July'})` → [Mon, 22 Dec 2025] Google News
[Mon, 05 Jan 2026] Inside Brooksby's comeback: From unranked &amp; un
- `search_web({'query': 'Casper Ruud ATP ranking May 2025 clay court season'})` → [Mon, 20 Apr 2026] Google News
[Tue, 18 Nov 2025] Madrid Open 2026: Iga Swiatek searches for clay re

## Outcome
_Pending — will be updated when market resolves_

---
*Mode: LIVE | DRY_RUN: true*