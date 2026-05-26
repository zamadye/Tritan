# Market Analysis — 2026-05-20 16:15 UTC

## Market
- **Question:** Roland Garros, Qualification ATP: Nicolai Budkov Kjaer vs Tom Gentzsch
- **Category:** sports
- **YES Price:** 56.0%
- **Days Left:** 6
- **Volume 24h:** $63,740
- **Liquidity:** $69,999

## Statistical Prior
- **p_base:** 59.0%
- **Source:** logistic:sports
- **N (historical):** 6077
- **Raw gap:** 2.9%

## News Sources Fetched
### Macro Context
- Fear&Greed: 27/100 (Fear) | trend: deteriorating
- BTC: $77,392 (+1.2% 24h) → risk-ON
- Fear&Greed: 27/100 (Fear) | 7d trend: deteriorating
- BTC: $77,471 (+1.4% 24h) → risk-ON

### General
- [FEAR&GREED 7d trend] 27(Fear) → 25(Extr) → 28(Fear) → 27(Fear) | sentiment worsening
- [CAUSAL CHAINS] Relevant cause-effect patterns:
- → Major AI model release → benchmark competition → sector excitement
- → AI regulation proposed → uncertainty → AI stocks fall short-term
- → AI chip shortage → NVIDIA revenue beats → AI infrastructure stocks rally
- → AI energy demand → data center power stocks rally

### Multi-Source
- [MULTI-SOURCE NEWS] 2 sources for: roland garros qualification atp: nicolai
- [Bing News]
- [Mon, 19 May 2025] roland garros qualification atp: nicolai
- → With the Entry Lists now confirmed for the 2025 French Open at Roland Garros between May 25 - June 8, the Prize Money has now been set with a record
- [Tue, 27 May 2025] Prize Money and points breakdown 2025 French Open | Roland Garros | ATP | WTA
- → The French Open is here as we head to Roland Garros for two weeks between May 25 - 8 June for the clay court portion of the season to conclude with 
- [Sun, 08 Jun 2025] ATP French Open Roland Garros 2025: Schedule, Draw, Results, Prize Money and TV Guide
- → Roland Garros Carlos Alcaraz produces historic comeback against Sinner in longest final Roland Garros Roland Garros Winners List: All the Grand Slam

## LLM Decision
- **Action:** SKIP
- **Confidence:** 62%
- **p_true:** 48.9%
- **Information Gap:** True
- **Crowd Bias:** False
- **Catalyst Type:** STATISTICAL_PATTERN
- **Catalyst Strength:** 0.75

### Reasoning
Stat signal (n=13,967) indicates markets at 56% YES resolve YES only 44.7% of the time — a ~11pp overpricing. No contradictory evidence found. Entry 50-60% WR=33% supports overpricing. Gap (+3%) below 5% gate, but stat edge is the primary catalyst.

## Gate Result
- **Passed:** ❌ NO
- **Reason:** no stat edge gap=3%<5%

## Tool Calls
- `get_odds({'sport': 'tennis_atp', 'team': 'Budkov Kjaer'})` → Odds API error: 404 {"message":"Unknown sport","error_code":"UNKNOWN_SPORT","details_url":"https://t
- `get_odds({'sport': 'tennis_atp', 'team': 'Gentzsch'})` → Odds API error: 404 {"message":"Unknown sport","error_code":"UNKNOWN_SPORT","details_url":"https://t
- `get_market_context({'keyword': 'Roland Garros qualification'})` → No related markets found for 'Roland Garros qualification'
- `search_web({'query': 'Nicolai Budkov Kjaer Roland Garros 2025 tennis form'})` → [Sun, 17 May 2026] Google News
[Tue, 28 Apr 2026] Dimitrov to Goffin: Five to watch in men’s qualify
- `search_web({'query': 'Tom Gentzsch tennis 2025 recent results ranking'})` → [Sun, 02 Jul 2023] Google News
[Fri, 03 Mar 2023] Tom Gentzsch | Rankings Breakdown | ATP Tour | Ten
- `search_web({'query': 'Nicolai Budkov Kjaer ATP ranking 2025 results statistics'})` → [Tue, 16 Dec 2025] Google News
[Fri, 26 Sep 2025] Scouting Report: Tien, Landaluce, Blockx eye succe
- `search_web({'query': 'Tom Gentzsch ATP ranking 2025 challenger results'})` → [Tue, 14 Apr 2026] Google News
[Mon, 30 Mar 2026] H2H, prediction of Henrique Rocha vs Tom Gentzsch 
- `search_web({'query': 'Budkov Kjaer vs Gentzsch head to head tennis'})` → [Wed, 20 May 2026] Google News
[Wed, 20 May 2026] H2H, prediction of Nicolai Budkov Kjaer vs Tom Gen
- `search_web({'query': 'Budkov Kjaer French Open 2026 qualifying draw'})` → [Sun, 17 May 2026] Google News
[Mon, 18 May 2026] Dimitrov to Goffin: Five to watch in men’s qualify
- `search_web({'query': '"Budkov Kjaer" "Gentzsch" prediction odds French Open 2026'})` → [Wed, 20 May 2026] Google News
[Wed, 20 May 2026] H2H, prediction of Nicolai Budkov Kjaer vs Tom Gen
- `search_web({'query': 'Wincomparator Budkov Kjaer Gentzsch odds prediction May 2026'})` → [Wed, 20 May 2026] Google News
[Tue, 19 May 2026] Nicolai Budkov Kjaer vs Tom Gentzsch prediction – 
- `search_web({'query': 'Nicolai Budkov Kjaer ranking ATP 2026 clay court form'})` → [Tue, 28 Apr 2026] Google News
[Wed, 22 Oct 2025] Dimitrov, #NextGenATP stars headline Roland Garros
- `search_web({'query': '"Nicolai Budkov Kjaer" ATP ranking current 2026'})` → [Fri, 28 Nov 2025] Google News
[Wed, 22 Oct 2025] Budkov Kjaer qualifies for the Next Gen ATP Finals
- `search_web({'query': '"Tom Gentzsch" ATP ranking current 2026'})` → [Wed, 11 Feb 2026] Google News
[Wed, 20 May 2026] Francesco Maestrelli Tom Gentzsch live score and H
- `search_web({'query': '"Budkov Kjaer" "Gentzsch" odds prediction French Open qualifying May 20 2026'})` → [Tue, 19 May 2026] Google News
[] Dalibor Svrcina vs. Federico Agustin Gomez 20 May 2026 | H2H, Bett

## Outcome
_Pending — will be updated when market resolves_

---
*Mode: LIVE | DRY_RUN: true*