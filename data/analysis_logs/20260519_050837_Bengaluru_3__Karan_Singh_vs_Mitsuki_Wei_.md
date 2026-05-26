# Market Analysis — 2026-05-19 05:08 UTC

## Market
- **Question:** Bengaluru 3: Karan Singh vs Mitsuki Wei Kang Leong
- **Category:** sports
- **YES Price:** 55.0%
- **Days Left:** 6
- **Volume 24h:** $50,598
- **Liquidity:** $68,998

## Statistical Prior
- **p_base:** 57.5%
- **Source:** logistic:sports
- **N (historical):** 6077
- **Raw gap:** 2.5%

## News Sources Fetched
### Macro Context
- Fear&Greed: 25/100 (Extreme Fear) | trend: deteriorating
- BTC: $76,837 (-0.2% 24h) → neutral
- Fear&Greed: 25/100 (Extreme Fear) | 7d trend: deteriorating
- BTC: $76,837 (-0.2% 24h) → neutral

### General
- [FEAR&GREED 7d trend] 25(Extr) → 28(Fear) → 27(Fear) → 31(Fear) | sentiment worsening

### Multi-Source
- [MULTI-SOURCE NEWS] 2 sources for: bengaluru karan singh mitsuki kang
- [Bing News]
- [Tue, 06 Jan 2026] bengaluru karan singh mitsuki kang
- → Dhakshineswar Suresh came up with a power-packed performance to oust Croatia’s Duje Ajdukovic 6-4, 6-4 in the opening round of the Dafa News Bengalu
- [] Bengaluru Open: Dhakshineswar packs off Ajdukovic; Karan, Aryan bow out
- [Metaculus]
- [] Will the next IPC Sudan acute food insecurity analysis classify at lea
- → Community: pending

## LLM Decision
- **Action:** SKIP
- **Confidence:** 50%
- **p_true:** 57.5%
- **Information Gap:** False
- **Crowd Bias:** False
- **Catalyst Type:** NONE
- **Catalyst Strength:** 0.00

### Reasoning
Market at 55% shows historical overpricing pattern (resolves YES only 44.7%), but edge is insufficient for bet: (1) Gap from base rate is only +2%, below the 5% threshold required for action. (2) No concrete catalyst found - Karan Singh is India's No. 2 player and likely favored, but no injury/form/news suggesting a clear edge. (3) Entry zone 50-60% has poor historical WR (33% from 6 trades). (4) Previous SKIP decisions on same market were correct. (5) Without verifiable information advantage or strong catalyst, statistical edge alone is too thin given the small gap. Tennis Challenger events have high variance and limited public information.

## Gate Result
- **Passed:** ❌ NO
- **Reason:** no stat edge gap=2%<5%

## Tool Calls
- `search_web({'query': 'Karan Singh vs Mitsuki Wei Kang Leong tennis Bengaluru 3 2025'})` → [Sun, 23 Feb 2025] Google News
[Mon, 24 Feb 2025] Bengaluru Open 2025 tennis: Rising teen star Manas
- `search_web({'query': '"Karan Singh" "Mitsuki Wei Kang Leong" tennis 2025'})` → [Sun, 23 Feb 2025] Google News
[Mon, 24 Feb 2025] Bengaluru Open 2025 tennis: Rising teen star Manas
- `get_market_context({'keyword': 'Karan Singh tennis'})` → No related markets found for 'Karan Singh tennis'
- `get_odds({'sport': 'tennis_atp_italian_open', 'team': 'Karan Singh'})` → Odds API error: 401 {"message":"Usage quota has been reached. See usage plans at https://the-odds-ap
- `search_web({'query': 'Karan Singh tennis player recent results 2025'})` → [Wed, 09 Jul 2025] Google News
[Fri, 25 Jul 2025] Tennis: Karan Singh becomes India’s No. 2 ranked p
- `search_web({'query': 'Mitsuki Wei Kang Leong tennis recent results 2025'})` → [Wed, 19 Nov 2025] Google News
[Thu, 18 Dec 2025] Alcantara F C / Ferguson C Koay H S / Leong M W K 
- `search_web({'query': '"Karan Singh" "Mitsuki" tennis head to head'})` → [Mon, 18 May 2026] Google News
[Mon, 18 May 2026] H2H, prediction of Karan Singh vs Mitsuki Wei Kang

## Outcome
_Pending — will be updated when market resolves_

---
*Mode: LIVE | DRY_RUN: true*