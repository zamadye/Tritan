# Market Analysis — 2026-05-21 10:44 UTC

## Market
- **Question:** Will Wolverhampton Wanderers FC win on 2026-05-24?
- **Category:** other
- **YES Price:** 36.0%
- **Days Left:** 3
- **Volume 24h:** $50,117
- **Liquidity:** $570,673

## Statistical Prior
- **p_base:** 28.8%
- **Source:** logistic:other
- **N (historical):** 7829
- **Raw gap:** 7.2%

## News Sources Fetched
### Macro Context
- Fear&Greed: 29/100 (Fear) | trend: improving
- BTC: $77,206 (-0.4% 24h) → neutral
- Fear&Greed: 29/100 (Fear) | 7d trend: improving
- BTC: $77,572 (+0.1% 24h) → neutral

### General
- [FEAR&GREED 7d trend] 29(Fear) → 27(Fear) → 25(Extr) → 28(Fear) | sentiment improving

### Multi-Source
- [MULTI-SOURCE NEWS] 2 sources for: wolverhampton wanderers 2026-05-24
- [Bing News]
- [Wed, 13 May 2026] wolverhampton wanderers 2026-05-24
- → Fulham will reportedly look to sign 30-year-old Wolverhampton Wanderers striker Hwang Hee-chan this summer. A report by Sports Boom has revealed tha
- [] Fulham in transfer tussle to sign Hwang Hee-chan
- [Metaculus]
- [] Will a case of Bundibugyo Ebola disease be first confirmed in the US b
- → Community: pending

## LLM Decision
- **Action:** SKIP
- **Confidence:** 45%
- **p_true:** 28.8%
- **Information Gap:** False
- **Crowd Bias:** False
- **Catalyst Type:** NONE
- **Catalyst Strength:** 0.10

### Reasoning
Market already prices in Burnley injury news (36% vs 29% base rate). Historical pattern shows 30-40% entry range underperforms (46% WR). No verifiable edge or fresh catalyst found.

## Gate Result
- **Passed:** ❌ NO
- **Reason:** low conf 45%<52%

## Tool Calls
- `get_odds({'sport': 'soccer_epl', 'team': 'Wolverhampton'})` → Odds API error: 401 {"message":"Usage quota has been reached. See usage plans at https://the-odds-ap
- `search_web({'query': 'Wolverhampton Wanderers FC May 24 2026 match preview'})` → [Thu, 21 May 2026] Google News
[Wed, 20 May 2026] Premier League 2025-26 fixtures: Dates, schedule, 
- `search_web({'query': 'Wolves Burnley May 24 2026 team news injuries'})` → [Wed, 20 May 2026] Google News
[Wed, 20 May 2026] Burnley vs Wolves: Predictions, Picks, Odds &amp; 
- `get_market_context({'keyword': 'Wolverhampton Wanderers'})` → No related markets found for 'Wolverhampton Wanderers'
- `search_web({'query': 'Burnley vs Wolves May 24 2026 odds predictions Squawka'})` → [Wed, 20 May 2026] Google News
[Mon, 18 May 2026] Burnley vs Wolves: Predictions, Picks, Odds &amp; 
- `search_web({'query': 'Burnley Wolves injuries team news May 2026'})` → [Thu, 21 May 2026] Google News
[Mon, 18 May 2026] Burnley v Wolves early team news: 3 ruled out inju
- `search_web({'query': 'Burnley Wolves Premier League May 24 2026 match preview'})` → [Mon, 18 May 2026] Google News
[Wed, 20 May 2026] Burnley vs. Wolves (May 24, 2026) Live Score - ESP
- `search_web({'query': 'Premier League 2025-26 standings table May 2026'})` → [Thu, 21 May 2026] Google News
[Tue, 19 May 2026] Premier League 2025-26 table — Latest standings - 
- `search_web({'query': 'Wolves Premier League form May 2026 recent results'})` → [Sun, 18 Jan 2026] Google News
[Sun, 17 May 2026] Wolves 0-0 Newcastle (18 Jan, 2026) Final Score - 
- `search_web({'query': '"Burnley" "Wolves" "May 24" 2026 team news injuries lineup'})` → [Wed, 22 Apr 2026] Google News
[Fri, 01 May 2026] How Burnley could get relegated from the Premier L
- `search_web({'query': 'Burnley Wanderers Premier League 2026 relegation'})` → [Mon, 11 May 2026] Google News
[Tue, 19 May 2026] Nottingham Forest and Leeds secure Premier League 

## Outcome
_Pending — will be updated when market resolves_

---
*Mode: LIVE | DRY_RUN: true*