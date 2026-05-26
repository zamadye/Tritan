# Market Analysis — 2026-05-20 07:19 UTC

## Market
- **Question:** Bengaluru 3: Hamish Stewart vs Kriish Tyagi
- **Category:** geopolitik
- **YES Price:** 55.0%
- **Days Left:** 6
- **Volume 24h:** $84,843
- **Liquidity:** $14,941

## Statistical Prior
- **p_base:** 45.0%
- **Source:** logistic:geopolitik
- **N (historical):** 135
- **Raw gap:** 10.0%

## News Sources Fetched
### Macro Context
- Fear&Greed: 27/100 (Fear) | trend: deteriorating
- BTC: $77,275 (+0.2% 24h) → neutral
- Fear&Greed: 27/100 (Fear) | 7d trend: deteriorating
- BTC: $77,275 (+0.2% 24h) → neutral
- Fed market expectations:

### General
- [FEAR&GREED 7d trend] 27(Fear) → 25(Extr) → 28(Fear) → 27(Fear) | sentiment worsening
- MicroStrategy sells any Bitcoin by May 31, 2026? → YES=50%

### Multi-Source
- [MULTI-SOURCE NEWS] 2 sources for: bengaluru hamish stewart kriish tyagi
- [Bing News]
- [Thu, 14 May 2026] bengaluru hamish stewart kriish tyagi
- → Bengaluru, Local hero Kriish Tyagi produced the biggest win of his fledgling career as the 19-year-old wild card entrant knocked out second seed Ham
- [Thu, 14 May 2026] Bengaluru teen Kriish stuns 2nd seed Hamish to enter Karnataka Open semis
- → Bengaluru teenager Kriish Tyagi stunned second seed Hamish Stewart 7-6 5-7, 6-4 at the Karnataka Open ATP Challenger. The Indian wild card reached t
- [Fri, 15 May 2026] Karnataka Open: Kriish Tyagi fights his way into semifinals
- → Bengaluru teenager Kriish Tyagi's inspiring run at the Karnataka Open ATP Challenger men's singles event ended in the semifinals as he lost to Austr

## LLM Decision
- **Action:** NO
- **Confidence:** 65%
- **p_true:** 37.0%
- **Information Gap:** True
- **Crowd Bias:** False
- **Catalyst Type:** STATISTICAL_PATTERN
- **Catalyst Strength:** 0.70

### Reasoning
Markets at 55% historically resolve YES only 44.7% (n=13,967), showing systematic crowd overpricing. Market is 10% above base rate (45%). GEOPOLITIK category has extremely weak 14% WR. News confirms Kriish Tyagi already upset 2nd seed Hamish Stewart at Karnataka Open, providing direct evidence against YES outcome. Statistically significant edge combined with factual evidence supports NO bet.

## Gate Result
- **Passed:** ✅ YES
- **Reason:** BET NO $1.00

## Tool Calls
- `search_web({'query': 'Hamish Stewart vs Kriish Tyagi Bengaluru'})` → [Thu, 14 May 2026] Google News
[Thu, 14 May 2026] Tyagi, Kriish - Stewart, Hamish , COURT 1 - ATP To
- `search_web({'query': 'Kriish Tyagi Hamish Stewart Karnataka Open 2026'})` → [Thu, 14 May 2026] Google News
[Thu, 14 May 2026] Tyagi, Kriish - Stewart, Hamish , COURT 1 - ATP To
- `get_market_context({'keyword': 'Kriish Tyagi Hamish Stewart'})` → No related markets found for 'Kriish Tyagi Hamish Stewart'
- `get_market_context({'keyword': 'Bengaluru tennis'})` → No related markets found for 'Bengaluru tennis'
- `search_web({'query': 'Kriish Tyagi beats Hamish Stewart Karnataka Open score'})` → [Thu, 14 May 2026] Google News
[Thu, 14 May 2026] Kriish Tyagi Shocks 2nd Seed Hamish To Reach Karna
- `get_sports_data({'sport': 'tennis', 'team': 'Tyagi'})` → No injury data found for tennis Tyagi
- `get_odds({'sport': 'tennis_atp', 'team': 'Tyagi'})` → Odds API error: 404 {"message":"Unknown sport","error_code":"UNKNOWN_SPORT","details_url":"https://t

## Outcome
_Pending — will be updated when market resolves_

---
*Mode: LIVE | DRY_RUN: true*