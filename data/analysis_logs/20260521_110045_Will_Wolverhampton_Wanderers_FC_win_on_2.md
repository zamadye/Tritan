# Market Analysis — 2026-05-21 11:00 UTC

## Market
- **Question:** Will Wolverhampton Wanderers FC win on 2026-05-24?
- **Category:** other
- **YES Price:** 36.0%
- **Days Left:** 3
- **Volume 24h:** $50,125
- **Liquidity:** $567,151

## Statistical Prior
- **p_base:** 28.8%
- **Source:** logistic:other
- **N (historical):** 7829
- **Raw gap:** 7.2%

## News Sources Fetched
### Macro Context
- Fear&Greed: 29/100 (Fear) | trend: improving
- BTC: $77,240 (-0.3% 24h) → neutral
- Fear&Greed: 29/100 (Fear) | 7d trend: improving
- BTC: $77,170 (-0.3% 24h) → neutral

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
- **Catalyst Strength:** 0.00

### Reasoning
No verifiable edge found after investigation. Market (36% YES) already prices in Burnley injury news, sitting 7% above historical base rate (29%). Odds API unavailable (quota), but past analysis confirmed market efficiency. No new breaking injury news or lineup changes discovered. Pattern shows 30-40% entry win rate of only 46% (11 trades). Previous two SKIP decisions with 45% confidence remain valid. Three days to match with no unpriced catalyst identified.

## Gate Result
- **Passed:** ❌ NO
- **Reason:** low conf 45%<52%

## Tool Calls
- `get_odds({'sport': 'soccer_epl', 'team': 'Wolverhampton'})` → Odds API error: 401 {"message":"Usage quota has been reached. See usage plans at https://the-odds-ap
- `search_web({'query': 'Wolverhampton Wanderers FC May 24 2026 match preview'})` → [Thu, 21 May 2026] Google News
[Wed, 20 May 2026] Premier League 2025-26 fixtures: Dates, schedule, 
- `search_web({'query': 'Wolverhampton Wanderers injury update May 2026'})` → [Sun, 17 May 2026] Google News
[Sun, 17 May 2026] Wolverhampton Wanderers vs Fulham Match Preview &a
- `search_web({'query': 'Wolves vs Burnley May 24 2026'})` → [Mon, 18 May 2026] Google News
[Thu, 21 May 2026] Burnley vs. Wolves (May 24, 2026) Live Score - ESP
- `get_market_context({'keyword': 'Wolverhampton'})` → No related markets found for 'Wolverhampton'
- `get_market_context({'keyword': 'Wolves'})` → No related markets found for 'Wolves'
- `search_web({'query': 'Burnley injury news May 2026 Premier League'})` → [Mon, 18 May 2026] Google News
[Sat, 16 May 2026] Arsenal vs Burnley: TV channel, kick-off time, liv

## Outcome
_Pending — will be updated when market resolves_

---
*Mode: LIVE | DRY_RUN: true*