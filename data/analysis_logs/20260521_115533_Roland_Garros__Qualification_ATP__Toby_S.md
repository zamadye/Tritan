# Market Analysis — 2026-05-21 11:55 UTC

## Market
- **Question:** Roland Garros, Qualification ATP: Toby Samuel vs Gonzalo Bueno
- **Category:** sports
- **YES Price:** 51.0%
- **Days Left:** 7
- **Volume 24h:** $124,781
- **Liquidity:** $64,457

## Statistical Prior
- **p_base:** 51.5%
- **Source:** logistic:sports
- **N (historical):** 6077
- **Raw gap:** 0.5%

## News Sources Fetched
### Macro Context
- Fear&Greed: 29/100 (Fear) | trend: improving
- BTC: $77,174 (-0.2% 24h) → neutral
- Fear&Greed: 29/100 (Fear) | 7d trend: improving
- BTC: $77,174 (-0.2% 24h) → neutral

### General
- [FEAR&GREED 7d trend] 29(Fear) → 27(Fear) → 25(Extr) → 28(Fear) | sentiment improving

### Multi-Source
- [MULTI-SOURCE NEWS] 2 sources for: roland garros qualification atp: toby
- [Bing News]
- [Wed, 20 May 2026] roland garros qualification atp: toby
- → Britain's Toby Samuel and Felix Gill are both one win away from a lucrative first Grand Slam singles appearance as they reach the final round of Fre
- [Mon, 19 May 2025] British duo one win from French Open breakthroughs
- → With the Entry Lists now confirmed for the 2025 French Open at Roland Garros between May 25 - June 8, the Prize Money has now been set with a record
- [] Prize Money and points breakdown 2025 French Open | Roland Garros | ATP | WTA
- [Metaculus]

## LLM Decision
- **Action:** SKIP
- **Confidence:** 65%
- **p_true:** 43.5%
- **Information Gap:** False
- **Crowd Bias:** False
- **Catalyst Type:** STATISTICAL_OVERPRICING
- **Catalyst Strength:** 0.70

### Reasoning
Strong statistical signal (n=13,967) shows markets at 51% YES historically resolve YES only 44.7% of the time, creating a ~6% edge for NO. Samuel's recent win over Goffin likely inflated YES price, but the crowd overprices momentum. Base rate (52%) vs market (51%) shows minimal gap (+1%), yet historical resolution data confirms systematic overpricing at this price point. Pattern data confirms Entry 50-60% range has only 38% WR for YES trades. Bueno is competitive at ATP qualifying level and the market is underestimating his chances.

## Gate Result
- **Passed:** ❌ NO
- **Reason:** no stat edge gap=1%<5%

## Tool Calls
- `get_sports_data({'sport': 'atp', 'team': 'Samuel'})` → No injury data found for atp Samuel
- `get_odds({'sport': 'tennis_atp', 'team': 'Samuel'})` → Odds API error: 404 {"message":"Unknown sport","error_code":"UNKNOWN_SPORT","details_url":"https://t
- `search_web({'query': 'Toby Samuel vs Gonzalo Bueno Roland Garros qualification 2025'})` → [Wed, 20 May 2026] Google News
[Wed, 20 May 2026] French Open qualifying 2026: British duo one win f
- `search_web({'query': 'Toby Samuel tennis form results 2025'})` → [Wed, 18 Mar 2026] Google News
[Mon, 01 Dec 2025] Toby Samuel: Tennis player aiming for Grand Slams 
- `get_market_context({'keyword': 'Roland Garros Qualification'})` → No related markets found for 'Roland Garros Qualification'
- `search_web({'query': 'Gonzalo Bueno tennis results 2026'})` → [Wed, 14 Jan 2026] Google News
[Thu, 05 Feb 2026] What were the Australian Open qualifying results o
- `search_web({'query': 'Roland Garros 2026 qualifying results Samuel Bueno'})` → [Wed, 20 May 2026] Google News
[Mon, 18 May 2026] David Goffin's Roland-Garros Farewell: Emotional R
- `search_web({'query': '"Toby Samuel" "Gonzalo Bueno" 2026'})` → [Wed, 20 May 2026] Google News
[Wed, 20 May 2026] French Open qualifying 2026: British duo one win f
- `search_web({'query': 'Toby Samuel Roland Garros 2026 qualifying final round opponent'})` → [Wed, 20 May 2026] Google News
[Wed, 20 May 2026] What were the Roland Garros qualifying results on 
- `search_web({'query': 'Roland Garros qualifying results Wednesday Samuel Bueno'})` → [Wed, 20 May 2026] Google News
[] David Goffin's Roland-Garros Farewell: Emotional Run Ends with Qua
- `search_web({'query': 'Gonzalo Bueno tennis ranking form 2026'})` → [Wed, 20 May 2026] Google News
[Wed, 14 Jan 2026] Costa Rica Tennis Fans Get a Latin American Showca
- `search_web({'query': 'Toby Samuel head to head Bueno tennis'})` → [Wed, 20 May 2026] Google News
[Wed, 20 May 2026] H2H, prediction of Toby Samuel vs Gonzalo Bueno at

## Outcome
_Pending — will be updated when market resolves_

---
*Mode: LIVE | DRY_RUN: true*