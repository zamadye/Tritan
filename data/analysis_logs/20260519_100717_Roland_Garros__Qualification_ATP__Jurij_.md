# Market Analysis — 2026-05-19 10:07 UTC

## Market
- **Question:** Roland Garros, Qualification ATP: Jurij Rodionov vs Dusan Lajovic
- **Category:** sports
- **YES Price:** 56.0%
- **Days Left:** 6
- **Volume 24h:** $118,313
- **Liquidity:** $18,159

## Statistical Prior
- **p_base:** 59.0%
- **Source:** logistic:sports
- **N (historical):** 6077
- **Raw gap:** 2.9%

## News Sources Fetched
### Macro Context
- Fear&Greed: 25/100 (Extreme Fear) | trend: deteriorating
- BTC: $76,733 (-0.1% 24h) → neutral
- Fear&Greed: 25/100 (Extreme Fear) | 7d trend: deteriorating
- BTC: $76,733 (-0.1% 24h) → neutral

### General
- [FEAR&GREED 7d trend] 25(Extr) → 28(Fear) → 27(Fear) → 31(Fear) | sentiment worsening

### Multi-Source
- [MULTI-SOURCE NEWS] 2 sources for: roland garros qualification atp: jurij
- [Bing News]
- [Sun, 08 Jun 2025] roland garros qualification atp: jurij
- → Roland Garros Carlos Alcaraz produces historic comeback against Sinner in longest final Roland Garros Roland Garros Winners List: All the Grand Slam
- [Sat, 25 Apr 2026] How much does Alcaraz take home after winning at Roland Garros: purse and ATP points
- → Jakarta (ANTARA) - Carlos Alcaraz mengumumkan akan absen pada ajang ATP Masters 1000 Internazionali BNL d'Italia di Roma dan Grand Slam lapangan tan
- [Tue, 27 May 2025] Cedera, Alcaraz absen di ATP Masters 1000 Roma dan Roland Garros
- → The French Open is here as we head to Roland Garros for two weeks between May 25 - 8 June for the clay court portion of the season to conclude with 

## LLM Decision
- **Action:** SKIP
- **Confidence:** 62%
- **p_true:** 50.9%
- **Information Gap:** False
- **Crowd Bias:** False
- **Catalyst Type:** STATISTICAL_PATTERN
- **Catalyst Strength:** 0.70

### Reasoning
Strong statistical signal (n=13,967) shows markets at 56% YES historically resolve YES only 44.7% of time, indicating significant overpricing. The +3% gap between market price (56%) and base rate (59%) is misleading—the stat signal reveals the TRUE probability is ~11.3% lower than market price. Entry range 50-60% shows poor 33% WR historically. Unable to find concrete player-specific information (form, injuries, H2H) through search or odds API. Without evidence of Lajovic weakness or Rodionov upside to justify the YES price, the statistical edge favors NO. Crowd appears overconfident in YES outcome.

## Gate Result
- **Passed:** ❌ NO
- **Reason:** no stat edge gap=3%<5%

## Tool Calls
- `search_web({'query': 'Jurij Rodionov vs Dusan Lajovic Roland Garros qualification 2025'})` → [Tue, 19 May 2026] Google News
[] Tennis: Roland-Garros 2026 - All results and scores from the Frenc
- `search_web({'query': 'Dusan Lajovic recent results 2026'})` → [Wed, 14 Jan 2026] Google News
[Wed, 22 Apr 2026] What were the Australian Open qualifying results o
- `get_odds({'sport': 'tennis_atp_italian_open', 'team': 'Lajovic'})` → Odds API error: 401 {"message":"Usage quota has been reached. See usage plans at https://the-odds-ap
- `get_market_context({'keyword': 'Roland Garros'})` → No related markets found for 'Roland Garros'
- `search_web({'query': 'Jurij Rodionov Roland Garros qualifying 2026'})` → [Fri, 25 Sep 2020] Google News
[Sun, 01 Oct 2023] Thiem helps Rodionov realise main draw dream - Rol
- `search_web({'query': 'Dusan Lajovic Roland Garros qualifying 2026'})` → [Wed, 24 Dec 2025] Google News
[Tue, 21 May 2024] Qualifying entry lists released for Australian Ope
- `get_market_context({'keyword': 'ATP qualification'})` → No related markets found for 'ATP qualification'
- `search_web({'query': 'Rodionov vs Lajovic odds Roland Garros qualifying 2026'})` → No search results for: Rodionov vs Lajovic odds Roland Garros qualifying 2026
- `search_web({'query': 'Roland Garros 2026 qualifying draw schedule'})` → [Sat, 16 May 2026] Google News
[Mon, 18 May 2026] Roland-Garros 2026: the full tournament schedule -

## Outcome
_Pending — will be updated when market resolves_

---
*Mode: LIVE | DRY_RUN: true*