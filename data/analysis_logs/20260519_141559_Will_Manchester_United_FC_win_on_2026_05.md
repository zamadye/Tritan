# Market Analysis — 2026-05-19 14:15 UTC

## Market
- **Question:** Will Manchester United FC win on 2026-05-24?
- **Category:** other
- **YES Price:** 29.0%
- **Days Left:** 5
- **Volume 24h:** $62,724
- **Liquidity:** $554,337

## Statistical Prior
- **p_base:** 24.5%
- **Source:** logistic:other
- **N (historical):** 7829
- **Raw gap:** 4.5%

## News Sources Fetched
### Macro Context
- Fear&Greed: 25/100 (Extreme Fear) | trend: deteriorating
- BTC: $76,811 (+0.0% 24h) → neutral
- Fear&Greed: 25/100 (Extreme Fear) | 7d trend: deteriorating
- BTC: $76,692 (+0.0% 24h) → neutral

### General
- [FEAR&GREED 7d trend] 25(Extr) → 28(Fear) → 27(Fear) → 31(Fear) | sentiment worsening

### Multi-Source
- [MULTI-SOURCE NEWS] 2 sources for: manchester united 2026-05-24
- [Bing News]
- [Mon, 18 May 2026] manchester united 2026-05-24
- → Manchester United's ⁠goal by Matheus Cunha in Sunday's 3-2 Premier League victory over Nottingham Forest should ⁠have been ruled out for handball, r
- [Thu, 14 May 2026] Soccer-PGMO apologise to Forest, saying Cunha goal for Man United should not have counted
- → Carrick, closer than ever to being confirmed as United's permanent manager.
- [Fri, 15 May 2026] Manchester United Is Determined to Negotiate for Michael Carrick to Be Their Permanent Manager
- → The surgery is expected to rule him out of being selected for the Netherlands' World Cup campaign this summer.

## LLM Decision
- **Action:** SKIP
- **Confidence:** 48%
- **p_true:** 24.5%
- **Information Gap:** False
- **Crowd Bias:** False
- **Catalyst Type:** NONE
- **Catalyst Strength:** 0.10

### Reasoning
Market at 29% is only 5% above base rate (24%), not exceeding the 5% threshold needed for a statistical edge. Past decisions on this exact market twice resulted in SKIP for the same reason. The fixture (Brighton away) is historically difficult. Extreme Fear sentiment (25/100) creates some crowd pessimism that could slightly favor Man Utd, but this is indirect and insufficient. No new verifiable information found via odds API (quota reached) or breaking news to justify a contrarian bet. Insufficient concrete edge to act.

## Gate Result
- **Passed:** ❌ NO
- **Reason:** no stat edge gap=5%<5%

## Tool Calls
- `get_sports_data({'sport': 'soccer', 'team': 'Manchester United'})` → No injury data found for soccer Manchester United
- `get_odds({'sport': 'soccer_epl', 'team': 'Manchester United'})` → Odds API error: 401 {"message":"Usage quota has been reached. See usage plans at https://the-odds-ap
- `search_web({'query': 'Manchester United fixture May 24 2026'})` → [Thu, 09 Apr 2026] Google News
[Wed, 18 Jun 2025] Man Utd Break 24-Year Tradition With Announcement 
- `search_web({'query': 'Manchester United vs Brighton May 2026 Premier League'})` → [Tue, 19 May 2026] Google News
[Tue, 19 May 2026] Premier League 2025-26 fixtures: Dates, schedule, 
- `get_market_context({'keyword': 'Manchester United'})` → No related markets found for 'Manchester United'
- `search_web({'query': 'Manchester United 2025-26 season form results standings'})` → [Sat, 11 Apr 2026] Google News
[Sat, 10 Jan 2026] Premier League Live Scores, Stats &amp; Blog | 202
- `search_web({'query': '"May 24" "Manchester United" 2026 Premier League'})` → [Tue, 19 May 2026] Google News
[Mon, 18 May 2026] Premier League 2025-26 fixtures: Dates, schedule, 

## Outcome
_Pending — will be updated when market resolves_

---
*Mode: LIVE | DRY_RUN: true*