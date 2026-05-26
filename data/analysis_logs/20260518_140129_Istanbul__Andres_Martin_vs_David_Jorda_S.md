# Market Analysis — 2026-05-18 14:01 UTC

## Market
- **Question:** Istanbul: Andres Martin vs David Jorda Sanchis
- **Category:** sports
- **YES Price:** 55.0%
- **Days Left:** 6
- **Volume 24h:** $54,321
- **Liquidity:** $17,304

## Statistical Prior
- **p_base:** 57.5%
- **Source:** logistic:sports
- **N (historical):** 6077
- **Raw gap:** 2.5%

## News Sources Fetched
### Macro Context
- Fear&Greed: 28/100 (Fear) | trend: deteriorating
- BTC: $76,915 (-1.6% 24h) → risk-OFF
- Fear&Greed: 28/100 (Fear) | 7d trend: deteriorating
- BTC: $76,915 (-1.6% 24h) → risk-OFF
- Fed market expectations:

### General
- [FEAR&GREED 7d trend] 28(Fear) → 27(Fear) → 31(Fear) → 43(Fear) | sentiment worsening
- Will the Fed increase interest rates by 25 bps after the Jun → YES=50%

### Multi-Source
- [MULTI-SOURCE NEWS] 2 sources for: istanbul: andres martin david jorda
- [Bing News]
- [] istanbul: andres martin david jorda
- [Metaculus]
- [] Will the next IPC Sudan acute food insecurity analysis classify at lea
- → Community: pending
- [] Will Bitcoin trade above $120,000 before August 1, 2026?
- → Community: pending

## LLM Decision
- **Action:** SKIP
- **Confidence:** 62%
- **p_true:** 51.5%
- **Information Gap:** True
- **Crowd Bias:** False
- **Catalyst Type:** STATISTICAL_PATTERN
- **Catalyst Strength:** 0.65

### Reasoning
Strong historical evidence (n=13,967) shows markets at 55% YES resolve YES only 44.7% of time, indicating ~10% overpricing. Entry 50-60% has only 25% win rate. No specific match information found to support YES outcome. Market appears systematically overpriced at this level.

## Gate Result
- **Passed:** ❌ NO
- **Reason:** no stat edge gap=2%<5%

## Tool Calls
- `search_web({'query': 'Andres Martin vs David Jorda Sanchis Istanbul tennis 2025'})` → [Mon, 11 May 2026] Google News
[Mon, 18 May 2026] H2H Andres Martin Vs David Jorda Sanchis stats, pr
- `search_web({'query': 'Andres Martin tennis injury 2026'})` → [Thu, 26 Mar 2026] Google News
[Tue, 10 Mar 2026] (VIDEO) American tennis player draws criticism onl
- `search_web({'query': 'David Jorda Sanchis recent results 2026'})` → [Thu, 30 Apr 2026] Google News
[Sun, 29 Mar 2026] David Jorda Sanchis vs Roman Safiullin: Live Score
- `get_odds({'sport': 'tennis_atp_italian_open', 'team': 'Martin'})` → Odds API error: 401 {"message":"Usage quota has been reached. See usage plans at https://the-odds-ap
- `get_market_context({'keyword': 'Andres Martin'})` → No related markets found for 'Andres Martin'
- `get_market_context({'keyword': 'Istanbul tennis'})` → No related markets found for 'Istanbul tennis'
- `search_web({'query': 'Andres Martin vs David Jorda Sanchis prediction Istanbul Challenger 2026'})` → [Mon, 18 May 2026] Google News
[Mon, 11 May 2026] H2H, prediction of Andres Martin vs David Jorda Sa

## Outcome
_Pending — will be updated when market resolves_

---
*Mode: LIVE | DRY_RUN: true*