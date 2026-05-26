# Market Analysis — 2026-05-21 09:33 UTC

## Market
- **Question:** Internationaux de Strasbourg: Marie Bouzkova vs Ann Li
- **Category:** sports
- **YES Price:** 30.0%
- **Days Left:** 6
- **Volume 24h:** $182,238
- **Liquidity:** $87,935

## Statistical Prior
- **p_base:** 21.9%
- **Source:** logistic:sports
- **N (historical):** 6077
- **Raw gap:** 8.1%

## News Sources Fetched
### Macro Context
- Fear&Greed: 29/100 (Fear) | trend: improving
- BTC: $77,871 (+0.7% 24h) → neutral
- Fear&Greed: 29/100 (Fear) | 7d trend: improving
- BTC: $77,822 (+0.6% 24h) → neutral

### General
- [FEAR&GREED 7d trend] 29(Fear) → 27(Fear) → 25(Extr) → 28(Fear) | sentiment improving

### Multi-Source
- [MULTI-SOURCE NEWS] 2 sources for: internationaux strasbourg: marie bouzkova
- [Bing News]
- [Tue, 20 May 2025] internationaux strasbourg: marie bouzkova
- → After a first-round bye, third seed Paula Badosa will take on lucky loser Marie Bouzkova in the second round of the Internationaux de Strasbourg 202
- [Mon, 19 May 2025] Strasbourg 2025: Paula Badosa vs Marie Bouzkova preview, head-to-head, prediction, odds and pick | Internationaux de Strasbourg
- → Day 3 at the 2025 Internationaux de Strasbourg will feature four second-round matches in the singles event. Some of the biggest seeds at the event, 
- [Mon, 19 May 2025] Strasbourg 2025 Day 3: Women's singles predictions ft. Paula Badosa vs Marie Bouzkova, Elena Rybakina vs Wang Xinyu | Internationau
- → No. 10-ranked Paula Badosa will meet No. 50 Marie Bouzkova in the Internationaux de Strasbourg Round of 16 on Tuesday, May 20. Badosa retired and wa

## LLM Decision
- **Action:** NO
- **Confidence:** 60%
- **p_true:** 17.9%
- **Information Gap:** True
- **Crowd Bias:** False
- **Catalyst Type:** STATISTICAL_ARBITRAGE
- **Catalyst Strength:** 0.40

### Reasoning
YES price at 30% is 8% above base rate of 22%. Historical pattern from n=13,967 markets shows YES at 57% resolves YES only 44.7%, indicating consistent overpricing of YES in this category. Sports category has strong WR=73% from 26 trades. No direct catalyst found (injury, form change) to justify premium over base rate. Market appears to be overpricing the underdog outcome without supporting evidence.

## Gate Result
- **Passed:** ✅ YES
- **Reason:** BET NO $1.00

## Tool Calls
- `search_web({'query': 'Marie Bouzkova Ann Li Internationaux de Strasbourg 2025 match preview'})` → [Wed, 20 May 2026] Google News
[Thu, 21 May 2026] H2H, prediction of Marie Bouzkova vs Ann Li in Str
- `search_web({'query': 'Bouzkova recent form 2026 results'})` → [Wed, 20 May 2026] Google News
[Thu, 09 Apr 2026] WTA Strasbourg Quarterfinal Predictions Including 
- `search_web({'query': 'Ann Li tennis 2026 results recent form'})` → [Wed, 20 May 2026] Google News
[Mon, 08 Dec 2025] WTA Strasbourg Quarterfinal Predictions Including 
- `get_market_context({'keyword': 'Strasbourg tennis'})` → No related markets found for 'Strasbourg tennis'
- `get_odds({'sport': 'tennis_atp', 'team': 'Bouzkova'})` → Odds API error: 404 {"message":"Unknown sport","error_code":"UNKNOWN_SPORT","details_url":"https://t
- `get_odds({'sport': 'tennis_atp_italian_open', 'team': 'Bouzkova'})` → Odds API error: 401 {"message":"Usage quota has been reached. See usage plans at https://the-odds-ap
- `search_web({'query': 'Bouzkova vs Ann Li odds Strasbourg 2026'})` → [Wed, 20 May 2026] Google News
[Wed, 20 May 2026] Marie Bouzkova vs Ann Li: Scores, Results Lineups,

## Outcome
**✅ WIN** | P&L: $+0.49 | Resolved: YES

---
*Mode: LIVE | DRY_RUN: true*