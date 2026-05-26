# Market Analysis — 2026-05-19 13:55 UTC

## Market
- **Question:** Will Manchester United FC win on 2026-05-24?
- **Category:** other
- **YES Price:** 29.0%
- **Days Left:** 5
- **Volume 24h:** $62,636
- **Liquidity:** $556,841

## Statistical Prior
- **p_base:** 24.5%
- **Source:** logistic:other
- **N (historical):** 7829
- **Raw gap:** 4.5%

## News Sources Fetched
### Macro Context
- Fear&Greed: 25/100 (Extreme Fear) | trend: deteriorating
- BTC: $76,889 (-0.1% 24h) → neutral
- Fear&Greed: 25/100 (Extreme Fear) | 7d trend: deteriorating
- BTC: $76,589 (-0.7% 24h) → neutral

### General
- [FEAR&GREED 7d trend] 25(Extr) → 28(Fear) → 27(Fear) → 31(Fear) | sentiment worsening

### Multi-Source
- [MULTI-SOURCE NEWS] 2 sources for: manchester united 2026-05-24
- [Bing News]
- [Thu, 14 May 2026] manchester united 2026-05-24
- → Carrick, closer than ever to being confirmed as United's permanent manager.
- [Sat, 16 May 2026] Manchester United Is Determined to Negotiate for Michael Carrick to Be Their Permanent Manager
- → The Premier League's packed Sunday slate begins with Manchester United hosting Nottingham Forest in a meeting at Old Trafford.
- [Fri, 15 May 2026] Manchester United vs. Nottingham Forest prediction, where to watch, time for Premier League match
- → The surgery is expected to rule him out of being selected for the Netherlands' World Cup campaign this summer.

## LLM Decision
- **Action:** SKIP
- **Confidence:** 52%
- **p_true:** 24.5%
- **Information Gap:** False
- **Crowd Bias:** False
- **Catalyst Type:** NONE
- **Catalyst Strength:** 0.10

### Reasoning
Market at 29% is only 5% above base rate (24%), not exceeding threshold. Brighton away is a difficult fixture on final day. No concrete catalyst identified. One key player ruled out for United. Previous analyses correctly flagged this as lacking verifiable edge. While historical patterns show 75% WR in 20-30% entries, the absence of a clear catalyst and marginal gap make this a SKIP.

## Gate Result
- **Passed:** ❌ NO
- **Reason:** no stat edge gap=5%<5%

## Tool Calls
- `get_sports_data({'sport': 'nfl', 'team': 'Manchester United'})` → No injury data found for nfl Manchester United
- `get_odds({'sport': 'soccer_epl', 'team': 'Manchester United'})` → Odds API error: 401 {"message":"Usage quota has been reached. See usage plans at https://the-odds-ap
- `get_market_context({'keyword': 'Manchester United'})` → No related markets found for 'Manchester United'
- `search_web({'query': 'Manchester United May 2026 fixture schedule'})` → [Sat, 16 May 2026] Google News
[Fri, 15 May 2026] Chelsea Women v Manchester United Women | Match | 
- `search_web({'query': 'Manchester United win on 2026-05-24 opponent'})` → [Fri, 01 May 2026] Google News
[Sun, 12 Apr 2026] Revealed: In-demand Premier League manager emerges
- `search_web({'query': 'Manchester United fixture May 24 2026 Premier League'})` → [Tue, 19 May 2026] Google News
[Thu, 07 May 2026] How to get Manchester City vs Aston Villa tickets:
- `search_web({'query': 'Premier League final day May 24 2026 fixtures'})` → [Tue, 19 May 2026] Google News
[Tue, 19 May 2026] How to get Manchester City vs Aston Villa tickets:
- `search_web({'query': '"Manchester United" "May 24" 2026 match opponent'})` → [Wed, 18 Jun 2025] Google News
[Fri, 24 Apr 2026] Brighton’s Premier League fixtures: Full 2025-26 s
- `search_web({'query': 'Manchester United Premier League 2025-26 remaining fixtures'})` → [Mon, 18 May 2026] Google News
[Sun, 17 May 2026] Premier League 2025-26 table — Latest standings - 
- `search_web({'query': 'Manchester United next match May 2026 Premier League schedule'})` → [Tue, 19 May 2026] Google News
[Mon, 18 May 2026] AFC Bournemouth vs Manchester City: Premier League
- `search_web({'query': 'Premier League matchday 38 May 24 2026 schedule all fixtures'})` → [Thu, 07 May 2026] Google News
[Wed, 13 May 2026] 2025 Premier League TV Schedule: How to watch EPL 
- `search_web({'query': 'Transfermarkt Manchester United matchday 38 Premier League 2025-26'})` → [Thu, 19 Feb 2026] Google News
[Thu, 12 Feb 2026] Premier League - Overview: Matchday 38 25/26 - Tra
- `search_web({'query': 'Manchester United form 2026 wins losses recent results'})` → [Sat, 25 Oct 2025] Google News
[Tue, 09 Dec 2025] Looking beyond short-term results to understand wh
- `search_web({'query': 'Manchester United last game season 2025-26 final day'})` → [Mon, 18 May 2026] Google News
[Sun, 17 May 2026] Premier League 2025-26 table — Latest standings - 
- `search_web({'query': 'Manchester United current form May 2026 wins'})` → [Mon, 18 May 2026] Google News
[Mon, 18 May 2026] Premier League table under Carrick gives Man Utd a
- `search_web({'query': 'Manchester United vs Brighton Premier League May 24 2026'})` → [Wed, 18 Jun 2025] Google News
[Thu, 07 May 2026] Brighton vs. Man United (May 24, 2026) Live Score 
- `search_web({'query': 'Brighton Manchester United May 24 2026 preview odds'})` → [Thu, 14 May 2026] Google News
[Tue, 05 Aug 2025] Premier League Match Predictions - Opta Analyst
[T

## Outcome
_Pending — will be updated when market resolves_

---
*Mode: LIVE | DRY_RUN: true*