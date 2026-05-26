# Market Analysis — 2026-05-21 11:08 UTC

## Market
- **Question:** Roland Garros, Qualification ATP: Toby Samuel vs Gonzalo Bueno
- **Category:** sports
- **YES Price:** 56.0%
- **Days Left:** 7
- **Volume 24h:** $56,111
- **Liquidity:** $49,059

## Statistical Prior
- **p_base:** 59.0%
- **Source:** logistic:sports
- **N (historical):** 6077
- **Raw gap:** 2.9%

## News Sources Fetched
### Macro Context
- Fear&Greed: 29/100 (Fear) | trend: improving
- BTC: $77,174 (-0.3% 24h) → neutral
- Fear&Greed: 29/100 (Fear) | 7d trend: improving
- BTC: $77,175 (-0.4% 24h) → neutral

### General
- [FEAR&GREED 7d trend] 29(Fear) → 27(Fear) → 25(Extr) → 28(Fear) | sentiment improving

### Multi-Source
- [MULTI-SOURCE NEWS] 2 sources for: roland garros qualification atp: toby
- [Bing News]
- [Mon, 19 May 2025] roland garros qualification atp: toby
- → With the Entry Lists now confirmed for the 2025 French Open at Roland Garros between May 25 - June 8, the Prize Money has now been set with a record
- [] Prize Money and points breakdown 2025 French Open | Roland Garros | ATP | WTA
- [Metaculus]
- [] Will a case of Bundibugyo Ebola disease be first confirmed in the US b
- → Community: pending

## LLM Decision
- **Action:** NO
- **Confidence:** 65%
- **p_true:** 47.8%
- **Information Gap:** True
- **Crowd Bias:** False
- **Catalyst Type:** STATISTICAL_SIGNAL
- **Catalyst Strength:** 0.78

### Reasoning
Strong statistical signal (n=13,967) shows markets at 56% YES historically resolve YES only 44.7% of the time — an 11.3pp edge for NO. Pattern data confirms 50-60% entry range has terrible WR=31%. While Toby Samuel is in strong form (2 recent Challenger titles, career-high ranking), the market appears to overprice his chances at 56%. The historical data is robust and consistent with prior Roland Garros qualification market overpricing patterns. No injury news or specific catalyst found to justify the YES premium.

## Gate Result
- **Passed:** ❌ NO
- **Reason:** no stat edge gap=3%<5%

## Tool Calls
- `get_odds({'sport': 'tennis_atp', 'team': 'Toby Samuel'})` → Odds API error: 404 {"message":"Unknown sport","error_code":"UNKNOWN_SPORT","details_url":"https://t
- `get_odds({'sport': 'tennis_atp'})` → Odds API error: 404 {"message":"Unknown sport","error_code":"UNKNOWN_SPORT","details_url":"https://t
- `search_web({'query': 'Toby Samuel vs Gonzalo Bueno Roland Garros 2025 qualification'})` → [Wed, 20 May 2026] Google News
[Wed, 20 May 2026] French Open qualifying 2026: British duo one win f
- `search_web({'query': 'Gonzalo Bueno tennis recent form 2025 clay court'})` → [Fri, 24 May 2019] Google News
[Mon, 25 Aug 2025] Roland Garros | Results | ATP Tour | Tennis - ATP 
- `get_market_context({'keyword': 'Roland Garros qualification tennis'})` → No related markets found for 'Roland Garros qualification tennis'
- `search_web({'query': 'Toby Samuel tennis ranking 2025 recent results'})` → [Wed, 18 Mar 2026] Google News
[Sun, 30 Nov 2025] Toby Samuel: Tennis player aiming for Grand Slams 
- `search_web({'query': 'Gonzalo Bueno tennis ranking 2025 clay court performance'})` → [Thu, 09 Apr 2026] Google News
[Fri, 13 Mar 2026] H2H, prediction of Gonzalo Bueno vs Lucio Ratti in
- `get_market_context({'keyword': 'Toby Samuel'})` → No related markets found for 'Toby Samuel'
- `search_web({'query': '"Toby Samuel" "Gonzalo Bueno" head to head tennis'})` → [Wed, 20 May 2026] Google News
[Wed, 20 May 2026] H2H, prediction of Toby Samuel vs Gonzalo Bueno at
- `search_web({'query': 'Roland Garros 2025 qualifying results first round tennis ATP'})` → [Thu, 21 May 2026] Google News
[Tue, 19 May 2026] Roland Garros: When is the draw &amp; how to watch
- `search_web({'query': 'Toby Samuel tennis 2025 ranking career high form clay court'})` → [Mon, 01 Dec 2025] Google News
[Mon, 05 May 2025] Elmer Moller closes out 2025 with third ATP Challe
- `search_web({'query': 'Gonzalo Bueno tennis 2025 ranking clay court results South America'})` → No search results for: Gonzalo Bueno tennis 2025 ranking clay court results South America
- `search_web({'query': 'Toby Samuel ATP ranking current 2026'})` → [Wed, 25 Mar 2026] Google News
[Wed, 18 Mar 2026] Toby Samuel’s Racquet – Player Profile - Tennisner
- `search_web({'query': 'Gonzalo Bueno ATP ranking current Peruvian tennis player'})` → [Tue, 18 Dec 2018] Google News
[Thu, 05 Feb 2026] Gonzalo Bueno - ATP Tour
[Mon, 13 Nov 2023] German

## Outcome
_Pending — will be updated when market resolves_

---
*Mode: LIVE | DRY_RUN: true*