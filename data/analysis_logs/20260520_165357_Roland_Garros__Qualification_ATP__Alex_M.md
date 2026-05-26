# Market Analysis — 2026-05-20 16:53 UTC

## Market
- **Question:** Roland Garros, Qualification ATP: Alex Molcan vs Felix Gill
- **Category:** sports
- **YES Price:** 55.0%
- **Days Left:** 6
- **Volume 24h:** $108,793
- **Liquidity:** $46,415

## Statistical Prior
- **p_base:** 57.5%
- **Source:** logistic:sports
- **N (historical):** 6077
- **Raw gap:** 2.5%

## News Sources Fetched
### Macro Context
- Fear&Greed: 27/100 (Fear) | trend: deteriorating
- BTC: $77,255 (+0.6% 24h) → neutral
- Fear&Greed: 27/100 (Fear) | 7d trend: deteriorating
- BTC: $77,255 (+0.6% 24h) → neutral
- Fed market expectations:

### General
- [FEAR&GREED 7d trend] 27(Fear) → 25(Extr) → 28(Fear) → 27(Fear) | sentiment worsening
- MicroStrategy sells any Bitcoin by May 31, 2026? → YES=50%

### Multi-Source
- [MULTI-SOURCE NEWS] 2 sources for: roland garros qualification atp: alex
- [Bing News]
- [Fri, 31 Oct 2025] roland garros qualification atp: alex
- → Alex de Minaur has coughed up a lead to lose to Alexander Bublik again, this time at the Paris Masters. Earlier this year, de Minaur lost from two s
- [Fri, 15 May 2026] Alex de Minaur upset by Alexander Bublik again in Paris in repeat of Roland Garros heartbreak
- → The second Grand Slam of the year is approaching rapidly. Roland Garros (also known as the French Open) will host the best players in the world with
- [Sun, 26 Apr 2026] Roland Garros 2026: Dates, Tickets, and How to Attend the French Open
- → The tennis world was rocked late last week as Carlos Alcaraz announced his withdrawal from Rome and Roland Garros, both of which he won last year, d

## LLM Decision
- **Action:** SKIP
- **Confidence:** 58%
- **p_true:** 57.5%
- **Information Gap:** False
- **Crowd Bias:** False
- **Catalyst Type:** NONE
- **Catalyst Strength:** 0.20

### Reasoning
Stat signal (n=13,967) indicates market overprices YES at 55% (true ~44.7%), but gap between base rate and market is only 2%, below 5% gate threshold. No specific injury/form catalyst found for Molcan vs Gill. Consistent with past similar Roland Garros qualification decisions that were SKIP'd.

## Gate Result
- **Passed:** ❌ NO
- **Reason:** no stat edge gap=2%<5%

## Tool Calls
- `get_sports_data({'sport': 'tennis', 'team': 'Molcan'})` → No injury data found for tennis Molcan
- `get_odds({'sport': 'tennis_atp', 'team': 'Molcan'})` → Odds API error: 404 {"message":"Unknown sport","error_code":"UNKNOWN_SPORT","details_url":"https://t
- `search_web({'query': 'Alex Molcan vs Felix Gill Roland Garros qualification 2025'})` → [Tue, 19 May 2026] Google News
[Mon, 18 May 2026] Emma Raducanu: British number one suffers first-ro
- `search_web({'query': 'Alex Molcan recent form tennis 2025'})` → [Sun, 24 Aug 2025] Google News
[Mon, 13 Apr 2026] Challenger Tour Weekly Recap: Alex Molcan Back to 
- `get_market_context({'keyword': 'Roland Garros qualification'})` → No related markets found for 'Roland Garros qualification'
- `search_web({'query': 'Felix Gill tennis player ranking 2025'})` → [Mon, 18 May 2026] Google News
[Tue, 19 May 2026] Who's playing in Roland Garros 2026? | Britwatch -
- `search_web({'query': 'Alex Molcan ATP ranking 2025 clay court record'})` → [Mon, 08 Sep 2025] Google News
[Wed, 12 Dec 2018] "All the sacrifices paid off!": Ignacio Buse wins 
- `get_market_context({'keyword': 'tennis ATP Roland Garros'})` → No related markets found for 'tennis ATP Roland Garros'
- `search_web({'query': '"Alex Molcan" vs "Felix Gill" tennis head to head'})` → [Wed, 20 May 2026] Google News
[Mon, 18 May 2026] H2H, prediction of Alex Molcan vs Felix Gill at th
- `search_web({'query': '"Felix Gill" ATP ranking clay court 2025 2026'})` → [Wed, 19 Jun 2024] Google News
[Wed, 20 May 2026] Broady, Willis headline initial Wimbledon wild car
- `search_web({'query': 'Alex Molcan vs Felix Gill French Open 2026 odds prediction Tennis Tonic'})` → [Wed, 20 May 2026] Google News
[Tue, 19 May 2026] H2H, prediction of Alex Molcan vs Felix Gill at th
- `search_web({'query': '"Alex Molcan" 2026 form clay court results'})` → [Wed, 01 Apr 2026] Google News
[Tue, 14 Apr 2026] World No. 189 Molcan stuns top seed Diallo in Buch
- `search_web({'query': '"Felix Gill" ATP ranking 2026 recent results'})` → [Sat, 28 Feb 2026] Google News
[Sat, 04 Apr 2026] Pune ATP Challenger 2026: Niki Poonacha-Pruchya Is
- `search_web({'query': '"Alex Molcan" "Felix Gill" head to head record tennis'})` → [Wed, 20 May 2026] Google News
[Mon, 18 May 2026] H2H, prediction of Alex Molcan vs Felix Gill at th

## Outcome
_Pending — will be updated when market resolves_

---
*Mode: LIVE | DRY_RUN: true*