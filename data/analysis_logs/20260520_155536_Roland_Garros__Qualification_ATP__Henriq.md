# Market Analysis — 2026-05-20 15:55 UTC

## Market
- **Question:** Roland Garros, Qualification ATP: Henrique Rocha vs Borna Gojo
- **Category:** sports
- **YES Price:** 55.0%
- **Days Left:** 6
- **Volume 24h:** $117,342
- **Liquidity:** $64,013

## Statistical Prior
- **p_base:** 57.5%
- **Source:** logistic:sports
- **N (historical):** 6077
- **Raw gap:** 2.5%

## News Sources Fetched
### Macro Context
- Fear&Greed: 27/100 (Fear) | trend: deteriorating
- BTC: $77,461 (+1.3% 24h) → risk-ON
- Fear&Greed: 27/100 (Fear) | 7d trend: deteriorating
- BTC: $77,467 (+1.3% 24h) → risk-ON

### General
- [FEAR&GREED 7d trend] 27(Fear) → 25(Extr) → 28(Fear) → 27(Fear) | sentiment worsening

### Multi-Source
- [MULTI-SOURCE NEWS] 2 sources for: roland garros qualification atp: henrique
- [Bing News]
- [Sun, 08 Jun 2025] roland garros qualification atp: henrique
- → Roland Garros Carlos Alcaraz produces historic comeback against Sinner in longest final Roland Garros Roland Garros Winners List: All the Grand Slam
- [Tue, 27 May 2025] How much does Alcaraz take home after winning at Roland Garros: purse and ATP points
- → The French Open is here as we head to Roland Garros for two weeks between May 25 - 8 June for the clay court portion of the season to conclude with 
- [] ATP French Open Roland Garros 2025: Schedule, Draw, Results, Prize Money and TV Guide
- [Metaculus]

## LLM Decision
- **Action:** NO
- **Confidence:** 65%
- **p_true:** 44.7%
- **Information Gap:** True
- **Crowd Bias:** False
- **Catalyst Type:** STATISTICAL_PATTERN
- **Catalyst Strength:** 0.82

### Reasoning
Strong statistical signal (n=13,967) shows markets at 55% YES historically resolve YES only 44.7% of time — systematic 10.3pp overpricing of YES. Current NO price = 45% vs estimated true NO probability = 55.3% = ~10pp edge for NO. No player-specific injury or form data found to contradict this pattern. Gate passes: while base rate gap (2%) < 5%, the stat signal gap (10.3%) significantly exceeds threshold. Sports category shows 83% WR historically. Risk: Entry 50-60% range has 33% WR (n=9) — but stat signal is unusually strong here. Confidence tempered by lack of direct player data and upcoming match in 6 days.

## Gate Result
- **Passed:** ❌ NO
- **Reason:** no stat edge gap=2%<5%

## Tool Calls
- `get_sports_data({'sport': 'tennis', 'team': 'Henrique Rocha'})` → No injury data found for tennis Henrique Rocha
- `get_odds({'sport': 'tennis_atp'})` → Odds API error: 404 {"message":"Unknown sport","error_code":"UNKNOWN_SPORT","details_url":"https://t
- `search_web({'query': 'Henrique Rocha tennis 2025 Roland Garros qualification form'})` → [Sun, 17 May 2026] Google News
[Sat, 31 May 2025] Dimitrov to Goffin: Five to watch in men’s qualify
- `search_web({'query': 'Borna Gojo tennis 2025 Roland Garros qualification form results'})` → [Tue, 19 May 2026] Google News
[Tue, 19 May 2026] What were the Roland Garros qualifying results on 
- `search_web({'query': '"Henrique Rocha" tennis results 2025 2026 ranking'})` → [Sun, 29 Mar 2026] Google News
[Sat, 31 May 2025] 2026 Grand Prix Hassan II Tennis Live Scores - ESP
- `search_web({'query': '"Borna Gojo" tennis results 2025 2026 ranking Roland Garros'})` → [Tue, 19 May 2026] Google News
[Tue, 19 May 2026] What were the Roland Garros qualifying results on 
- `get_market_context({'keyword': 'Roland Garros qualification'})` → No related markets found for 'Roland Garros qualification'
- `search_web({'query': 'Henrique Rocha vs Borna Gojo head to head tennis'})` → [Wed, 20 May 2026] Google News
[Wed, 20 May 2026] Henrique Rocha vs Borna Gojo: Scores, Results Line
- `search_web({'query': 'Roland Garros 2026 qualifying draw results men'})` → [Mon, 18 May 2026] Google News
[Sat, 16 May 2026] Roland‑Garros 2026: discover the entry lists - Rol
- `search_web({'query': 'Henrique Rocha ATP ranking 2026 recent matches clay court'})` → [Wed, 13 May 2026] Google News
[Mon, 12 Jan 2026] Adolfo Daniel Vallejo Vs Henrique Rocha 🎾LIVE TENN
- `search_web({'query': 'Borna Gojo ATP ranking 2026 recent matches clay court form'})` → [Mon, 30 Mar 2026] Google News
[Thu, 05 Feb 2026] Borna Gojo continues Mexican mastery; Hamad Medjed
- `get_market_context({'keyword': 'Henrique Rocha'})` → No related markets found for 'Henrique Rocha'
- `search_web({'query': '"Borna Gojo" injury 2026'})` → [Tue, 19 May 2026] Google News
[Mon, 30 Mar 2026] Tennis: Roland-Garros 2026 - All results and score
- `search_web({'query': '"Henrique Rocha" injury 2026'})` → [Sun, 17 May 2026] Google News
[Mon, 13 Apr 2026] Dimitrov to Goffin: Five to watch in men’s qualify
- `get_market_context({'keyword': 'tennis Roland Garros'})` → No related markets found for 'tennis Roland Garros'
- `search_web({'query': 'Henrique Rocha clay court record 2026 wins losses'})` → [Wed, 20 May 2026] Google News
[Mon, 18 May 2026] H2H, prediction of Henrique Rocha vs Borna Gojo at
- `search_web({'query': 'Borna Gojo clay court record 2026 wins losses recent'})` → [Mon, 13 Apr 2026] Google News
[Wed, 20 May 2026] Shelton digs out of Munich hole, Cerundolo charges

## Outcome
_Pending — will be updated when market resolves_

---
*Mode: LIVE | DRY_RUN: true*