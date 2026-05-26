# Market Analysis — 2026-05-21 12:42 UTC

## Market
- **Question:** Roland Garros, Qualification ATP: Dalibor Svrcina vs Thomas Faurel
- **Category:** sports
- **YES Price:** 52.0%
- **Days Left:** 7
- **Volume 24h:** $72,562
- **Liquidity:** $43,616

## Statistical Prior
- **p_base:** 53.0%
- **Source:** logistic:sports
- **N (historical):** 6077
- **Raw gap:** 1.0%

## News Sources Fetched
### Macro Context
- Fear&Greed: 29/100 (Fear) | trend: improving
- BTC: $77,180 (-0.4% 24h) → neutral
- Fear&Greed: 29/100 (Fear) | 7d trend: improving
- BTC: $77,222 (-0.3% 24h) → neutral
- Fed market expectations:

### General
- [FEAR&GREED 7d trend] 29(Fear) → 27(Fear) → 25(Extr) → 28(Fear) | sentiment improving
- Will the Fed increase interest rates by 50+ bps after the Ju → YES=50%
- Will the Fed increase interest rates by 25 bps after the Jun → YES=50%

### Multi-Source
- [MULTI-SOURCE NEWS] 2 sources for: roland garros qualification atp: dalibor
- [Bing News]
- [] roland garros qualification atp: dalibor
- [Metaculus]
- [] Will a case of Bundibugyo Ebola disease be first confirmed in the US b
- → Community: pending
- [] Will the next IPC Sudan acute food insecurity analysis classify at lea
- → Community: pending

## LLM Decision
- **Action:** SKIP
- **Confidence:** 62%
- **p_true:** 53.0%
- **Information Gap:** False
- **Crowd Bias:** False
- **Catalyst Type:** STATISTICAL_ONLY
- **Catalyst Strength:** 0.40

### Reasoning
Despite statistical signal showing market at 52% historically resolves YES only 44.7% (n=13,967), this trade fails on multiple gates: (1) Gap is only +1%, well below the 5% minimum threshold required for action — consistent with prior RG qualification decisions that were all SKIPped; (2) Entry zone 50-60% has a terrible WR of just 38% from 16 trades, making this a high-risk entry point; (3) Svrcina appears to be the higher-ranked player based on news coverage (played Sinner at Indian Wells 2026), and Faurel received a wildcard, suggesting Svrcina should indeed be favored — the 52% market price may actually be fair or slightly underpriced; (4) No concrete catalyst found (no injury news, no recent form differential); (5) No related markets available for cross-validation. The statistical edge exists on paper but is too small, too unreliable at this price band, and potentially contradicted by fundamental player quality differences.

## Gate Result
- **Passed:** ❌ NO
- **Reason:** no stat edge gap=1%<5%

## Tool Calls
- `get_odds({'sport': 'tennis_atp', 'team': 'Dalibor Svrcina Thomas Faurel'})` → Odds API error: 404 {"message":"Unknown sport","error_code":"UNKNOWN_SPORT","details_url":"https://t
- `get_odds({'sport': 'tennis_atp'})` → Odds API error: 404 {"message":"Unknown sport","error_code":"UNKNOWN_SPORT","details_url":"https://t
- `get_odds({'sport': 'tennis_atp_italian_open', 'team': 'Svrcina'})` → Odds API error: 401 {"message":"Usage quota has been reached. See usage plans at https://the-odds-ap
- `search_web({'query': 'Dalibor Svrcina vs Thomas Faurel Roland Garros qualification 2025'})` → [Wed, 20 May 2026] Google News
[Tue, 12 May 2026] What were the Roland Garros qualifying results on 
- `search_web({'query': 'Dalibor Svrcina tennis ranking form 2025'})` → [Tue, 29 Jul 2025] Google News
[Mon, 18 Aug 2025] Lucky loser Svrcina, a Djokovic &amp; Nadal fan, l
- `search_web({'query': 'Thomas Faurel tennis ranking ATP 2025 2026'})` → [Wed, 20 May 2026] Google News
[Tue, 14 May 2024] What were the Roland Garros qualifying results on 
- `search_web({'query': 'Roland Garros 2026 qualifying draw ATP tennis'})` → [Thu, 21 May 2026] Google News
[Wed, 20 May 2026] Roland Garros: When is the draw &amp; how to watch
- `get_market_context({'keyword': 'Roland Garros qualification ATP'})` → No related markets found for 'Roland Garros qualification ATP'
- `search_web({'query': 'site:tennistonic.com Svrcina vs Faurel prediction odds preview'})` → [Tue, 04 Apr 2017] Google News
[Mon, 18 May 2026] Head to head statistics, previews, predictions and
- `search_web({'query': '"Dalibor Svrcina" "Thomas Faurel" head to head odds'})` → [Wed, 20 May 2026] Google News
[Tue, 19 May 2026] H2H, prediction of Dalibor Svrcina vs Thomas Faure
- `search_web({'query': 'Dalibor Svrcina ATP ranking 2026 recent results'})` → [Thu, 05 Mar 2026] Google News
[Sun, 01 Feb 2026] Schedule and where to watch Sinner's debut in Indi
- `search_web({'query': 'Thomas Faurel ATP ranking 2026 recent results'})` → [Wed, 20 May 2026] Google News
[Tue, 24 Mar 2026] What were the Roland Garros qualifying results on 
- `search_web({'query': 'Svrcina clay court form 2026 Roland Garros qualifying'})` → [Wed, 20 May 2026] Google News
[Wed, 06 May 2026] Hamburg Open 2026: All matches, live scores and ho
- `search_web({'query': 'Thomas Faurel clay court results 2026 French Open qualifying wildcard'})` → [Wed, 20 May 2026] Google News
[Tue, 12 May 2026] What were the Roland Garros qualifying results on 

## Outcome
_Pending — will be updated when market resolves_

---
*Mode: LIVE | DRY_RUN: true*