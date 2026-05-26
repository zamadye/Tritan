# Market Analysis — 2026-05-19 02:49 UTC

## Market
- **Question:** Geneva Open: Adrian Mannarino vs Raphael Collignon
- **Category:** sports
- **YES Price:** 12.0%
- **Days Left:** 6
- **Volume 24h:** $68,199
- **Liquidity:** $30,289

## Statistical Prior
- **p_base:** 4.8%
- **Source:** logistic:sports
- **N (historical):** 6077
- **Raw gap:** 7.2%

## News Sources Fetched
### Macro Context
- Fear&Greed: 25/100 (Extreme Fear) | trend: deteriorating
- BTC: $76,735 (-0.1% 24h) → neutral
- Fear&Greed: 25/100 (Extreme Fear) | 7d trend: deteriorating
- BTC: $76,704 (-0.2% 24h) → neutral

### General
- [FEAR&GREED 7d trend] 25(Extr) → 28(Fear) → 27(Fear) → 31(Fear) | sentiment worsening

### Multi-Source
- [MULTI-SOURCE NEWS] 2 sources for: geneva open: adrian mannarino raphael
- [Bing News]
- [Sat, 16 May 2026] geneva open: adrian mannarino raphael
- → May in Switzerland and sees Novak Djokovic as the defending champion but unlike previous years, he won't return to play in the tournament in ...
- [] Geneva Open 2026: Results, Draw, Schedule, Entry List, Prize Money and Predictions
- [Metaculus]
- [] Will the next IPC Sudan acute food insecurity analysis classify at lea
- → Community: pending

## LLM Decision
- **Action:** SKIP
- **Confidence:** 38%
- **p_true:** 5.0%
- **Information Gap:** False
- **Crowd Bias:** False
- **Catalyst Type:** NONE
- **Catalyst Strength:** 0.15

### Reasoning
Low-information market with no verifiable edge despite finding prediction articles. Key issues: (1) Both previous evaluations correctly SKIPped this same market - no new information emerged to change assessment; (2) Found dimers.com and Bleacher Nation prediction articles for this match (May 18) but cannot access specific odds/predictions; (3) Collignon is a rising player who upset Dimitrov in Brisbane but also lost to Musetti at AO - form unclear; (4) Mannarino's 2026 season described as mixed with some wins (Open Occitanie) but overall inconsistent; (5) Market at 12% already shows 7% premium over 5% base rate - crowd may be pricing Collignon upset probability; (6) No head-to-head data found, no injury reports, no concrete catalyst; (7) Tennis markets on prediction platforms are notoriously low-information - edge requires deep ATP ranking/form knowledge not available via search. Confidence insufficient for any action.

## Gate Result
- **Passed:** ❌ NO
- **Reason:** low conf 38%<52%

## Tool Calls
- `get_odds({'sport': 'tennis_atp', 'team': 'Mannarino'})` → Odds API error: 404 {"message":"Unknown sport","error_code":"UNKNOWN_SPORT","details_url":"https://t
- `get_odds({'sport': 'tennis_atp'})` → Odds API error: 404 {"message":"Unknown sport","error_code":"UNKNOWN_SPORT","details_url":"https://t
- `search_web({'query': 'Adrian Mannarino 2025 season results Geneva Open form'})` → [Sat, 01 Nov 2025] Google News
[Fri, 08 Aug 2025] ATP Metz Day 1 Predictions Including Arthur Cazaux
- `search_web({'query': 'Raphael Collignon tennis 2025 results form ATP'})` → [Tue, 17 Mar 2026] Google News
[Tue, 03 Mar 2026] Joao Fonseca: Miami draw, history, recent results 
- `get_market_context({'keyword': 'Mannarino Collignon Geneva Open'})` → No related markets found for 'Mannarino Collignon Geneva Open'
- `search_web({'query': 'Mannarino vs Collignon head to head record ATP tennis'})` → [Mon, 18 May 2026] Google News
[Tue, 03 Mar 2026] ATP Geneva Day 3 Predictions Including Casper Ruud
- `search_web({'query': 'Geneva Open 2025 ATP draw seedings tennis'})` → [Wed, 13 May 2026] Google News
[Fri, 08 Aug 2025] Gonet Geneva Open 2026: Draws, dates, history &amp
- `search_web({'query': '"Adrian Mannarino" 2026 season results ranking form'})` → [Sat, 07 Feb 2026] Google News
[Mon, 09 Feb 2026] Mannarino and the Art of Fueling Confidence - tenn
- `search_web({'query': '"Raphael Collignon" 2026 season results ranking form ATP'})` → [Thu, 08 Jan 2026] Google News
[Tue, 21 Apr 2026] Collignon upsets idol Dimitrov in Brisbane: 'It wa
- `search_web({'query': 'Geneva Open 2026 tennis draw first round matches'})` → [Wed, 13 May 2026] Google News
[Sat, 16 May 2026] Gonet Geneva Open 2026: Draws, dates, history &amp
- `search_web({'query': 'Mannarino clay court form 2026 results'})` → [Mon, 18 May 2026] Google News
[Sun, 08 Feb 2026] ATP Geneva Day 3 Predictions Including Casper Ruud
- `search_web({'query': 'Collignon clay court 2026 results ATP'})` → [Sun, 17 May 2026] Google News
[Mon, 20 Apr 2026] Hamburg Open 2026: All matches, live scores and ho
- `search_web({'query': '"Mannarino" "Collignon" Geneva Open 2026 prediction odds'})` → [Sat, 16 May 2026] Google News
[Sun, 17 May 2026] Adrian Mannarino vs. Raphael Collignon prediction,
- `search_web({'query': 'Adrian Mannarino ATP ranking May 2026 recent matches'})` → [Mon, 20 Apr 2026] Google News
[Wed, 04 Feb 2026] Scouting Report: Sinner chases five in a row, Zver
- `search_web({'query': 'Raphael Collignon ATP ranking May 2026 recent wins'})` → [Tue, 20 Jan 2026] Google News
[Tue, 03 Mar 2026] Tennis, ATP – Australian Open 2026: Musetti downs 

## Outcome
_Pending — will be updated when market resolves_

---
*Mode: LIVE | DRY_RUN: true*