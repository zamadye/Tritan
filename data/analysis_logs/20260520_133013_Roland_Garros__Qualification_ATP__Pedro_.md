# Market Analysis — 2026-05-20 13:30 UTC

## Market
- **Question:** Roland Garros, Qualification ATP: Pedro Boscardin Dias vs Alexis Galarneau
- **Category:** sports
- **YES Price:** 59.0%
- **Days Left:** 6
- **Volume 24h:** $53,045
- **Liquidity:** $99,957

## Statistical Prior
- **p_base:** 63.3%
- **Source:** logistic:sports
- **N (historical):** 6077
- **Raw gap:** 4.3%

## News Sources Fetched
### Macro Context
- Fear&Greed: 27/100 (Fear) | trend: deteriorating
- BTC: $77,407 (+0.9% 24h) → neutral
- Fear&Greed: 27/100 (Fear) | 7d trend: deteriorating
- BTC: $77,275 (+1.0% 24h) → neutral
- Fed market expectations:

### General
- [FEAR&GREED 7d trend] 27(Fear) → 25(Extr) → 28(Fear) → 27(Fear) | sentiment worsening
- MicroStrategy sells any Bitcoin by May 31, 2026? → YES=50%

### Multi-Source
- [MULTI-SOURCE NEWS] 2 sources for: roland garros qualification atp: pedro
- [Bing News]
- [Tue, 19 May 2026] roland garros qualification atp: pedro
- → Pedro Mart&#237;nez’s victory over Rei Sakamoto was overshadowed by a fiery confrontation at the net, forcing the umpire to step in and separate the
- [Sat, 25 Apr 2026] ‘It almost got out of hand’: Tense scene erupts after Mart&#237;nez’s win at Roland-Garros
- → Jakarta (ANTARA) - Carlos Alcaraz mengumumkan akan absen pada ajang ATP Masters 1000 Internazionali BNL d'Italia di Roma dan Grand Slam lapangan tan
- [Fri, 06 Jun 2025] Cedera, Alcaraz absen di ATP Masters 1000 Roma dan Roland Garros
- → The French Open has wrapped in incredible style and the memories of the 2025 edition will live long in the memory of fans. US star Coco Gauff became

## LLM Decision
- **Action:** SKIP
- **Confidence:** 65%
- **p_true:** 53.3%
- **Information Gap:** False
- **Crowd Bias:** False
- **Catalyst Type:** STATISTICAL_PATTERN
- **Catalyst Strength:** 0.75

### Reasoning
Strong statistical signal (n=13,967) shows markets at 59% YES resolve YES only 44.7% of time historically — indicating systematic 14.3% overpricing of YES. No player-specific catalyst found to explain the 59% market price vs 63% base rate. The pattern suggests qualifying markets at this level consistently overvalue the favorite. Confidence tempered by weak 50-60% entry win rate (33%, n=9) and lack of direct player context.

## Gate Result
- **Passed:** ❌ NO
- **Reason:** no stat edge gap=4%<5%

## Tool Calls
- `get_odds({'sport': 'tennis_atp', 'team': 'Boscardin Dias'})` → Odds API error: 404 {"message":"Unknown sport","error_code":"UNKNOWN_SPORT","details_url":"https://t
- `search_web({'query': 'Pedro Boscardin Dias tennis 2025 recent results form'})` → [Mon, 14 Nov 2016] Google News
[Wed, 09 Oct 2019] Nikoloz Basilashvili Tournament Results - ESPN
[Sa
- `search_web({'query': 'Alexis Galarneau tennis 2025 recent results Roland Garros qualification'})` → [Mon, 18 May 2026] Google News
[Tue, 20 May 2025] Canada's Galarneau, Draxl win first matches in Fre
- `get_market_context({'keyword': 'Roland Garros qualification tennis'})` → No related markets found for 'Roland Garros qualification tennis'
- `search_web({'query': 'Pedro Boscardin Dias ATP ranking 2025 clay court record'})` → [Wed, 28 Jan 2026] Google News
[Mon, 13 Apr 2026] H2H, prediction of Adolfo Daniel Vallejo vs Pedro 
- `search_web({'query': 'Alexis Galarneau ATP ranking 2025 clay court performance'})` → [Mon, 17 Nov 2025] Google News
[Mon, 14 Jul 2025] Monday Digest: Auger-Aliassime Cracks Top 5 with A
- `search_web({'query': 'Boscardin Dias vs Galarneau head to head tennis'})` → [Tue, 19 May 2026] Google News
[Tue, 19 May 2026] H2H, prediction of Alexis Galarneau vs Pedro Bosca
- `search_web({'query': '"Pedro Boscardin Dias" tennis ranking profile'})` → [Tue, 05 Mar 2024] Google News
[Mon, 18 May 2026] Pedro Boscardin Dias - ATP Tour
[Tue, 13 May 2025]
- `search_web({'query': '"Alexis Galarneau" tennis ranking profile 2025'})` → [Wed, 31 Dec 2025] Google News
[Wed, 30 Jul 2025] Who is competing in the 2026 United Cup? - ATP Tou
- `get_market_context({'keyword': 'Boscardin Dias Galarneau tennis'})` → No related markets found for 'Boscardin Dias Galarneau tennis'
- `search_web({'query': 'Pedro Boscardin Dias ATP profile ranking points 2025'})` → [Mon, 20 Oct 2025] Google News
[] #NextGenATP alum Van Assche beats Carreno Busta to win Olbia Chall
- `search_web({'query': 'Alexis Galarneau ATP profile ranking points clay court 2025'})` → [Wed, 30 Jul 2025] Google News
[Wed, 12 Dec 2018] Alexis Galarneau feels relief and motivation after
- `search_web({'query': 'Roland Garros 2025 qualifying draw first round results'})` → [Tue, 19 May 2026] Google News
[Mon, 18 May 2026] What were the Roland Garros qualifying results on 
- `search_web({'query': 'French Open 2025 qualifying tennis players seeds'})` → [Mon, 18 May 2026] Google News
[Sun, 17 May 2026] Roland‑Garros 2026: discover the entry lists - Rol
- `search_web({'query': 'Pedro Boscardin Dias French Open qualifying 2025 results'})` → [Fri, 24 May 2019] Google News
[Mon, 18 May 2026] Roland Garros | Results | ATP Tour | Tennis - ATP 
- `search_web({'query': 'Alexis Galarneau French Open qualifying 2025 results first round'})` → [Mon, 18 May 2026] Google News
[Mon, 26 May 2025] Canada's Galarneau, Draxl win first matches in Fre
- `search_web({'query': 'Boscardin Dias ATP ranking clay court stats 2025'})` → [Mon, 18 May 2026] Google News
[Wed, 28 Jan 2026] H2H, prediction of Emilio Nava vs Bu Yunchaokete a
- `search_web({'query': 'Galarneau ATP ranking clay court stats 2025 Canada'})` → [Wed, 12 Dec 2018] Google News
[Sun, 29 Mar 2026] Alexis Galarneau - ATP Tour
[Mon, 10 Nov 2025] H2H

## Outcome
_Pending — will be updated when market resolves_

---
*Mode: LIVE | DRY_RUN: true*