# Market Analysis — 2026-05-21 10:27 UTC

## Market
- **Question:** Will Wolverhampton Wanderers FC win on 2026-05-24?
- **Category:** other
- **YES Price:** 36.0%
- **Days Left:** 3
- **Volume 24h:** $50,117
- **Liquidity:** $571,900

## Statistical Prior
- **p_base:** 28.8%
- **Source:** logistic:other
- **N (historical):** 7829
- **Raw gap:** 7.2%

## News Sources Fetched
### Macro Context
- Fear&Greed: 29/100 (Fear) | trend: improving
- BTC: $77,573 (+0.1% 24h) → neutral
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
- **Information Gap:** True
- **Crowd Bias:** False
- **Catalyst Type:** NONE
- **Catalyst Strength:** 0.20

### Reasoning
No verifiable edge found. While Wolves are confirmed to play Burnley away on May 24, critical information is missing: current league positions (especially regarding relegation status), injury reports, and recent form. The 7% gap above base rate (36% vs 29%) isn't enough to act on without confirming whether Wolves have any motivation (already relegated vs fighting for survival) or if there are lineup/fitness factors. The historical poor season context alone doesn't provide actionable intelligence for a specific match outcome.

## Gate Result
- **Passed:** ❌ NO
- **Reason:** low conf 45%<52%

## Tool Calls
- `get_sports_data({'sport': 'soccer', 'team': 'Wolverhampton Wanderers'})` → No injury data found for soccer Wolverhampton Wanderers
- `get_odds({'sport': 'soccer_epl', 'team': 'Wolverhampton Wanderers'})` → Odds API error: 401 {"message":"Usage quota has been reached. See usage plans at https://the-odds-ap
- `search_web({'query': 'Wolverhampton Wanderers FC match schedule May 2026'})` → [Thu, 21 May 2026] Google News
[Sun, 17 May 2026] Premier League 2025-26 fixtures: Dates, schedule, 
- `search_web({'query': 'Wolverhampton Wanderers 2025-26 season results form'})` → [Thu, 04 Dec 2025] Google News
[Thu, 19 Feb 2026] Could Wolves’ 2025-26 Side Become the Worst Premie
- `get_market_context({'keyword': 'Wolverhampton Wanderers'})` → No related markets found for 'Wolverhampton Wanderers'
- `search_web({'query': 'Wolverhampton Wanderers match May 24 2026 Premier League'})` → [Thu, 21 May 2026] Google News
[Mon, 18 May 2026] Premier League 2025-26 fixtures: Dates, schedule, 
- `search_web({'query': 'Wolves Premier League form 2025-26 season results'})` → [Thu, 19 Feb 2026] Google News
[Thu, 04 Dec 2025] Ten KEY questions for Matchweek 27's fixtures - Pr
- `search_web({'query': 'Burnley vs Wolves preview May 24 2026'})` → [Mon, 18 May 2026] Google News
[Wed, 20 May 2026] Burnley vs. Wolves (May 24, 2026) Live Score - ESP
- `search_web({'query': 'Wolverhampton Wanderers injuries team news May 2026'})` → [Sun, 17 May 2026] Google News
[Sun, 03 May 2026] Preview: Wolverhampton Wanderers vs Fulham - predi
- `search_web({'query': 'Premier League table 2025-26 standings Wolves Burnley'})` → [Thu, 21 May 2026] Google News
[Thu, 14 May 2026] Premier League 2025-26 table — Latest standings - 
- `search_web({'query': 'Burnley FC form 2025-26 season results'})` → [Thu, 21 May 2026] Google News
[Wed, 22 Apr 2026] Premier League 2025-26 fixtures: Dates, schedule, 
- `search_web({'query': '"Wolves" "Premier League" 2025-26 table position points'})` → [Thu, 19 Feb 2026] Google News
[Mon, 04 May 2026] Supercomputer Predicts Final 2025–26 Premier Leagu
- `search_web({'query': '"Burnley" "Premier League" 2025-26 table position points'})` → [Thu, 21 May 2026] Google News
[Mon, 18 May 2026] Premier League 2025-26 table — Latest standings - 
- `search_web({'query': '"Burnley vs Wolves" May 24 2026 prediction odds'})` → [Wed, 20 May 2026] Google News
[Wed, 18 Jun 2025] Burnley vs Wolves: Predictions, Picks, Odds &amp; 

## Outcome
_Pending — will be updated when market resolves_

---
*Mode: LIVE | DRY_RUN: true*