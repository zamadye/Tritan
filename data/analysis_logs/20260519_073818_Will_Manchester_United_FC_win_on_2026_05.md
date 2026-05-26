# Market Analysis — 2026-05-19 07:38 UTC

## Market
- **Question:** Will Manchester United FC win on 2026-05-24?
- **Category:** other
- **YES Price:** 29.0%
- **Days Left:** 5
- **Volume 24h:** $63,559
- **Liquidity:** $568,662

## Statistical Prior
- **p_base:** 24.5%
- **Source:** logistic:other
- **N (historical):** 7829
- **Raw gap:** 4.5%

## News Sources Fetched
### Macro Context
- Fear&Greed: 25/100 (Extreme Fear) | trend: deteriorating
- BTC: $77,067 (+0.1% 24h) → neutral
- Fear&Greed: 25/100 (Extreme Fear) | 7d trend: deteriorating
- BTC: $76,936 (+0.0% 24h) → neutral

### General
- [FEAR&GREED 7d trend] 25(Extr) → 28(Fear) → 27(Fear) → 31(Fear) | sentiment worsening

### Multi-Source
- [MULTI-SOURCE NEWS] 2 sources for: manchester united 2026-05-24
- [Bing News]
- [Thu, 14 May 2026] manchester united 2026-05-24
- → Carrick, closer than ever to being confirmed as United's permanent manager.
- [Tue, 12 May 2026] Manchester United Is Determined to Negotiate for Michael Carrick to Be Their Permanent Manager
- → Manchester United will reportedly look to sign 24-year-old AC Milan centre-back Strahinja Pavlovic in the summer transfer window.
- [Sat, 16 May 2026] Manchester United front-runners to sign Strahinja Pavlovic
- → The Premier League's packed Sunday slate begins with Manchester United hosting Nottingham Forest in a meeting at Old Trafford.

## LLM Decision
- **Action:** SKIP
- **Confidence:** 55%
- **p_true:** 24.5%
- **Information Gap:** False
- **Crowd Bias:** False
- **Catalyst Type:** NONE
- **Catalyst Strength:** 0.00

### Reasoning
Market at 29% YES is 5% above base rate of 24%, indicating crowd overconfidence without verifiable justification. Unable to confirm opponent, match context, or any concrete catalyst through multiple search attempts. Odds API unavailable. Previous analyses (2 prior decisions) also found no edge and correctly skipped. The gap of exactly 5% doesn't clearly exceed the 5% threshold required for statistical edge. No independent evidence found to contradict the base rate or support the market premium.

## Gate Result
- **Passed:** ❌ NO
- **Reason:** no stat edge gap=5%<5%

## Tool Calls
- `get_odds({'sport': 'soccer_epl', 'team': 'Manchester United'})` → Odds API error: 401 {"message":"Usage quota has been reached. See usage plans at https://the-odds-ap
- `search_web({'query': 'Manchester United match 2026-05-24 opponent'})` → [Fri, 27 Mar 2026] Google News
[Sun, 12 Apr 2026] Man Utd willing to sell Marcus Rashford to Premier
- `search_web({'query': 'Manchester United Premier League schedule May 2026'})` → [Mon, 18 May 2026] Google News
[Tue, 19 May 2026] Premier League 2025-26 table — Latest standings - 
- `search_web({'query': 'Manchester United fixture 24 May 2026 Premier League'})` → [Tue, 05 May 2026] Google News
[Wed, 18 Jun 2025] Long list: United's 2025/26 Premier League fixture
- `search_web({'query': '"Manchester United" "24 May 2026" Premier League'})` → [Fri, 15 May 2026] Google News
[Fri, 01 May 2026] Spurs vs. Everton (24 May, 2026) Live Score - ESPN
- `get_market_context({'keyword': 'Manchester United win Premier League'})` → No related markets found for 'Manchester United win Premier League'
- `search_web({'query': 'Manchester United next match May 2026 final day Premier League'})` → [Mon, 18 May 2026] Google News
[Sun, 17 May 2026] Premier League and FA Cup final: 10 talking points
- `get_sports_data({'sport': 'nba', 'team': 'Manchester United'})` → No injury data found for nba Manchester United
- `get_market_context({'keyword': 'Manchester United'})` → No related markets found for 'Manchester United'
- `search_web({'query': 'Premier League final day 24 May 2026 fixtures schedule'})` → [Thu, 09 Apr 2026] Google News
[Wed, 18 Jun 2025] Premier League 2025-26 fixtures: Dates, schedule, 
- `search_web({'query': 'Manchester United form 2025-26 season results'})` → [Fri, 26 Dec 2025] Google News
[Fri, 07 Nov 2025] Man Utd 1 Newcastle 0: Has Amorim embraced the bac

## Outcome
_Pending — will be updated when market resolves_

---
*Mode: LIVE | DRY_RUN: true*