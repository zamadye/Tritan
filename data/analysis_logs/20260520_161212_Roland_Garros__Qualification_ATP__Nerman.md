# Market Analysis — 2026-05-20 16:12 UTC

## Market
- **Question:** Roland Garros, Qualification ATP: Nerman Fatic vs Kyrian Jacquet
- **Category:** sports
- **YES Price:** 53.0%
- **Days Left:** 6
- **Volume 24h:** $99,349
- **Liquidity:** $13,406

## Statistical Prior
- **p_base:** 54.5%
- **Source:** logistic:sports
- **N (historical):** 6077
- **Raw gap:** 1.5%

## News Sources Fetched
### Macro Context
- Fear&Greed: 27/100 (Fear) | trend: deteriorating
- BTC: $77,392 (+1.2% 24h) → risk-ON
- Fear&Greed: 27/100 (Fear) | 7d trend: deteriorating
- BTC: $77,446 (+1.4% 24h) → risk-ON

### General
- [FEAR&GREED 7d trend] 27(Fear) → 25(Extr) → 28(Fear) → 27(Fear) | sentiment worsening

### Multi-Source
- [MULTI-SOURCE NEWS] 2 sources for: roland garros qualification atp: nerman
- [Bing News]
- [Tue, 27 May 2025] roland garros qualification atp: nerman
- → The French Open is here as we head to Roland Garros for two weeks between May 25 - 8 June for the clay court portion of the season to conclude with 
- [] ATP French Open Roland Garros 2025: Schedule, Draw, Results, Prize Money and TV Guide
- [Metaculus]
- [] Will a case of Bundibugyo Ebola disease be first confirmed in the US b
- → Community: pending

## LLM Decision
- **Action:** SKIP
- **Confidence:** 55%
- **p_true:** 54.5%
- **Information Gap:** False
- **Crowd Bias:** False
- **Catalyst Type:** STATISTICAL_OVERPRICING
- **Catalyst Strength:** 0.50

### Reasoning
Stat signal (n=13,967) suggests market overprices YES (44.7% true vs 53% market), but gap analysis shows only +1% (below 5% threshold), entry range 50-60% has poor 33% WR historically, and similar past decisions were SKIPped. Moderate confidence SKIP due to conflicting signals and low gap despite strong statistical evidence.

## Gate Result
- **Passed:** ❌ NO
- **Reason:** no stat edge gap=1%<5%

## Tool Calls
- `search_web({'query': 'Nerman Fatic tennis 2025 recent results'})` → [Fri, 17 Oct 2025] Google News
[Mon, 01 Dec 2025] Nerman Fatić Hugo Grenier live score and H2H resul
- `search_web({'query': 'Kyrian Jacquet tennis 2025 recent results Roland Garros qualification'})` → [Tue, 19 May 2026] Google News
[Tue, 19 May 2026] Rodionov vs Jacquet • Q 3rd round • French Open 20
- `get_market_context({'keyword': 'Roland Garros qualification tennis'})` → No related markets found for 'Roland Garros qualification tennis'
- `search_web({'query': 'Nerman Fatic vs Kyrian Jacquet head to head'})` → [Wed, 20 May 2026] Google News
[Wed, 20 May 2026] H2H, prediction of Kyrian Jacquet vs Nerman Fatic 
- `search_web({'query': '"Nerman Fatic" OR "Kyrian Jacquet" Roland Garros 2025 qualifying'})` → [Tue, 19 May 2026] Google News
[Mon, 27 Oct 2025] Rodionov vs Jacquet • Q 3rd round • French Open 20
- `search_web({'query': 'Kyrian Jacquet vs Nerman Fatic prediction odds French Open 2026'})` → [Wed, 20 May 2026] Google News
[Wed, 20 May 2026] H2H, prediction of Kyrian Jacquet vs Nerman Fatic 
- `search_web({'query': 'Nerman Fatic ranking ITF 2025 2026 clay court record'})` → [Thu, 16 Dec 2021] Google News
[Mon, 30 Mar 2026] Jay Clarke | Player stats, ranking, bio &amp; news
- `search_web({'query': 'Kyrian Jacquet ranking ITF 2025 2026 clay court record'})` → [Wed, 17 Dec 2025] Google News
[] Two more players receive Australian Open wildcards including WTA t
- `get_odds({'sport': 'tennis_atp_italian_open', 'team': 'Fatic'})` → Odds API error: 401 {"message":"Usage quota has been reached. See usage plans at https://the-odds-ap

## Outcome
_Pending — will be updated when market resolves_

---
*Mode: LIVE | DRY_RUN: true*