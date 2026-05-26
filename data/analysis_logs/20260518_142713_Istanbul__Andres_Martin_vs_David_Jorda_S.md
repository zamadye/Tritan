# Market Analysis — 2026-05-18 14:27 UTC

## Market
- **Question:** Istanbul: Andres Martin vs David Jorda Sanchis
- **Category:** sports
- **YES Price:** 32.0%
- **Days Left:** 6
- **Volume 24h:** $62,498
- **Liquidity:** $12,847

## Statistical Prior
- **p_base:** 24.4%
- **Source:** logistic:sports
- **N (historical):** 6077
- **Raw gap:** 7.6%

## News Sources Fetched
### Macro Context
- Fear&Greed: 28/100 (Fear) | trend: deteriorating
- BTC: $76,677 (-1.8% 24h) → risk-OFF
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
- **Confidence:** 45%
- **p_true:** 24.4%
- **Information Gap:** False
- **Crowd Bias:** False
- **Catalyst Type:** NONE
- **Catalyst Strength:** 0.10

### Reasoning
Negative gap (-8%) suggests crowd overpricing YES (32% vs 24% base rate), which would theoretically favor NO. However, concrete evidence is insufficient: (1) No current form/ranking data retrieved for either player, (2) No injury reports available, (3) No related market consensus found, (4) Odds API unavailable. Pattern shows Entry 30-40% has poor WR=33% from 3 trades, making this price zone historically unprofitable. Previous decision on same market was SKIP with only 2% gap; now gap is larger but still lacks direct catalyst to exploit the overpricing. Confidence below 0.55 threshold - skip until verifiable player form data becomes available.

## Gate Result
- **Passed:** ❌ NO
- **Reason:** low conf 45%<52%

## Tool Calls
- `get_sports_data({'sport': 'tennis', 'team': 'Martin'})` → No injury data found for tennis Martin
- `search_web({'query': 'Andres Martin vs David Jorda Sanchis Istanbul 2025 tennis'})` → [Mon, 18 May 2026] Google News
[Mon, 11 May 2026] H2H, prediction of Andres Martin vs David Jorda Sa
- `search_web({'query': 'Andres Martin David Jorda Sanchis tennis match result 2025'})` → [Fri, 29 Jul 2022] Google News
[Mon, 18 May 2026] Tennis Scores &amp; Schedule - Sky Sports
[Mon, 11
- `get_odds({'sport': 'tennis', 'team': 'Martin'})` → Odds API error: 401 {"message":"Usage quota has been reached. See usage plans at https://the-odds-ap
- `get_market_context({'keyword': 'Istanbul tennis Martin Sanchis'})` → No related markets found for 'Istanbul tennis Martin Sanchis'
- `search_web({'query': 'Andres Martin ATP ranking 2025 form results'})` → [Fri, 19 Dec 2025] Google News
[Wed, 13 Aug 2025] Chris Rodesch - virginiasports.com
[Mon, 28 Jul 20
- `search_web({'query': '"David Jorda Sanchis" tennis 2025'})` → [Wed, 30 Apr 2025] Google News
[Wed, 19 Nov 2025] David Jorda Sanchis Philip Hjorth live score and H
- `search_web({'query': '"Andres Martin" tennis Challenger 2025 results'})` → [Mon, 14 Jul 2025] Google News
[Wed, 13 Aug 2025] Draxl Shines in Winnipeg to Earn First Title of 20
- `get_market_context({'keyword': 'Istanbul Challenger tennis'})` → No related markets found for 'Istanbul Challenger tennis'
- `search_web({'query': '"Andres Martin" tennis ATP ranking Challenger 2026'})` → [Mon, 18 May 2026] Google News
[Tue, 21 Apr 2026] H2H, prediction of Andres Martin vs David Jorda Sa
- `search_web({'query': '"David Jorda Sanchis" ATP ranking Challenger 2026'})` → [Tue, 17 Feb 2026] Google News
[Tue, 17 Feb 2026] Delhi Open 2026 tennis: Sumit Nagal advances to se
- `search_web({'query': 'Tennis Tonic Andres Martin vs David Jorda Sanchis Istanbul prediction odds pick'})` → [Mon, 18 May 2026] Google News
[Sat, 11 Nov 2023] H2H, prediction of Andres Martin vs David Jorda Sa
- `search_web({'query': 'Andres Martin tennis Challenger results wins losses 2026'})` → [Mon, 18 May 2026] Google News
[Mon, 11 May 2026] H2H, prediction of Andres Martin vs David Jorda Sa

## Outcome
_Pending — will be updated when market resolves_

---
*Mode: LIVE | DRY_RUN: true*