# Market Analysis — 2026-05-17 23:14 UTC

## Market
- **Question:** Will Arsenal win the 2025–26 English Premier League?
- **Category:** other
- **YES Price:** 83.0%
- **Days Left:** 9
- **Volume 24h:** $78,138
- **Liquidity:** $63,111

## Statistical Prior
- **p_base:** 64.8%
- **Source:** logistic:other
- **N (historical):** 7829
- **Raw gap:** 18.2%

## News Sources Fetched
### Macro Context
- Fear&Greed: 27/100 (Fear) | trend: deteriorating
- BTC: $77,863 (-0.4% 24h) → neutral
- Fear&Greed: 27/100 (Fear) | 7d trend: deteriorating
- BTC: $77,959 (-0.3% 24h) → neutral
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
- **Confidence:** 48%
- **p_true:** 64.8%
- **Information Gap:** False
- **Crowd Bias:** False
- **Catalyst Type:** MOMENTUM_SHIFT
- **Catalyst Strength:** 0.30

### Reasoning
Arsenal appears to have momentum with 2 games left and described as 'in control' per Bookies.com and Yahoo Sports. However, the market (83%) already reflects this advantage. With Man City still in contention and only 2 games remaining, true probability likely around 70-80%, making the 83% price roughly efficient. No concrete edge: odds API unavailable but search results show tight race where either team can clinch. Previous decisions correctly skipped with similar reasoning. No breaking catalyst to shift odds meaningfully beyond current pricing.

## Gate Result
- **Passed:** ❌ NO
- **Reason:** low conf 48%<52%

## Tool Calls
- `get_odds({'sport': 'soccer_epl', 'team': 'Arsenal'})` → Odds API error: 401 {"message":"Usage quota has been reached. See usage plans at https://the-odds-ap
- `search_web({'query': 'Arsenal Premier League title race 2025-26 standings 2026'})` → [Sun, 17 May 2026] Google News
[Sun, 17 May 2026] Premier League 2025-26 table — Latest standings - 
- `search_web({'query': 'Arsenal win Premier League 2025-26 champion'})` → [Sun, 17 May 2026] Google News
[Sun, 17 May 2026] Premier League 2025-26 table — Latest standings - 
- `search_web({'query': 'Premier League 2025-26 standings Arsenal points difference'})` → [Sun, 17 May 2026] Google News
[Sat, 25 Apr 2026] Premier League 2025-26 table — Latest standings - 
- `search_web({'query': 'Arsenal leads Premier League 2025-26 by points'})` → [Sun, 17 May 2026] Google News
[Sun, 17 May 2026] Premier League 2025-26 table — Latest standings - 
- `get_market_context({'keyword': 'Arsenal Premier League'})` → No related markets found for 'Arsenal Premier League'
- `search_web({'query': 'Arsenal Premier League title odds 2025-26'})` → [Sun, 17 May 2026] Google News
[Tue, 12 May 2026] Premier League Winner Odds 2025/26 - Arsenal in Co

## Outcome
_Pending — will be updated when market resolves_

---
*Mode: LIVE | DRY_RUN: true*