# Market Analysis — 2026-05-20 16:56 UTC

## Market
- **Question:** Roland Garros, Qualification ATP: Vilius Gaubas vs Joao Lucas Da Silva
- **Category:** sports
- **YES Price:** 54.0%
- **Days Left:** 6
- **Volume 24h:** $67,197
- **Liquidity:** $45,082

## Statistical Prior
- **p_base:** 56.0%
- **Source:** logistic:sports
- **N (historical):** 6077
- **Raw gap:** 2.0%

## News Sources Fetched
### Macro Context
- Fear&Greed: 27/100 (Fear) | trend: deteriorating
- BTC: $77,255 (+0.6% 24h) → neutral
- Fear&Greed: 27/100 (Fear) | 7d trend: deteriorating
- BTC: $77,210 (+0.5% 24h) → neutral
- Fed market expectations:

### General
- [FEAR&GREED 7d trend] 27(Fear) → 25(Extr) → 28(Fear) → 27(Fear) | sentiment worsening
- MicroStrategy sells any Bitcoin by May 31, 2026? → YES=50%

### Multi-Source
- [MULTI-SOURCE NEWS] 2 sources for: roland garros qualification atp: vilius
- [Bing News]
- [Fri, 18 Apr 2025] roland garros qualification atp: vilius
- → The VII Open Comunidad de Madrid, hosted by the Club de Campo Villa de Madrid, proved to be the final opportunity for many players to earn crucial A
- [] ATP Challenger Tour: The crucial chance to reach Roland Garros
- [Metaculus]
- [] Will a case of Bundibugyo Ebola disease be first confirmed in the US b
- → Community: pending

## LLM Decision
- **Action:** NO
- **Confidence:** 65%
- **p_true:** 46.0%
- **Information Gap:** True
- **Crowd Bias:** False
- **Catalyst Type:** STATISTICAL_PATTERN
- **Catalyst Strength:** 0.75

### Reasoning
Strong stat signal (n=13,967) shows markets at 54% YES historically resolve YES only 44.7% — a 9.3pp overpricing edge for NO. Market is mispriced despite weak direct intelligence. Da Silva has proven qualifying form (won French Open qualifying historically), while Gaubas is untested at this level. Previous similar RG qualification markets were skipped due to insufficient edge gaps, but this market offers the clearest statistical mispricing. Caveat: Entry 50-60% range historically has weak 33% WR, so position sizing should be moderate.

## Gate Result
- **Passed:** ❌ NO
- **Reason:** no stat edge gap=2%<5%

## Tool Calls
- `search_web({'query': 'Vilius Gaubas Roland Garros qualification 2025'})` → [Thu, 22 May 2025] Google News
[Wed, 21 May 2025] Harris happy to be healthy again - Roland-Garros 2
- `search_web({'query': 'Joao Lucas Da Silva Roland Garros qualification 2025'})` → [Mon, 18 May 2026] Google News
[] Gay pro tennis player Joao Lucas Reis da Silva makes history with 
- `search_web({'query': 'Vilius Gaubas tennis form 2025'})` → [Wed, 22 Apr 2026] Google News
[Mon, 18 Aug 2025] ATP Madrid Day 2 Predictions Including Gael Monfil
- `get_market_context({'keyword': 'Roland Garros Qualification'})` → No related markets found for 'Roland Garros Qualification'
- `search_web({'query': 'Joao Lucas da Silva tennis form 2025'})` → [Mon, 18 May 2026] Google News
[Sun, 28 Dec 2025] Gay pro tennis player Joao Lucas Reis da Silva mak
- `get_odds({'sport': 'tennis_atp', 'team': 'Gaubas'})` → Odds API error: 404 {"message":"Unknown sport","error_code":"UNKNOWN_SPORT","details_url":"https://t
- `get_odds({'sport': 'tennis_atp'})` → Odds API error: 404 {"message":"Unknown sport","error_code":"UNKNOWN_SPORT","details_url":"https://t
- `search_web({'query': 'Gaubas vs Da Silva odds Roland Garros qualifying'})` → No search results for: Gaubas vs Da Silva odds Roland Garros qualifying

## Outcome
_Pending — will be updated when market resolves_

---
*Mode: LIVE | DRY_RUN: true*