# Market Analysis — 2026-05-20 14:57 UTC

## Market
- **Question:** Hamburg European Open: Ugo Humbert vs Karen Khachanov
- **Category:** sports
- **YES Price:** 51.0%
- **Days Left:** 6
- **Volume 24h:** $227,043
- **Liquidity:** $64,567

## Statistical Prior
- **p_base:** 51.5%
- **Source:** logistic:sports
- **N (historical):** 6077
- **Raw gap:** 0.5%

## News Sources Fetched
### Macro Context
- Fear&Greed: 27/100 (Fear) | trend: deteriorating
- BTC: $77,468 (+1.5% 24h) → risk-ON
- Fear&Greed: 27/100 (Fear) | 7d trend: deteriorating
- BTC: $77,468 (+1.5% 24h) → risk-ON

### General
- [FEAR&GREED 7d trend] 27(Fear) → 25(Extr) → 28(Fear) → 27(Fear) | sentiment worsening
- [CAUSAL CHAINS] Relevant cause-effect patterns:
- → ECB rate cut → EUR weakens vs USD → EUR/USD falls
- → EU GDP beats expectations → EUR strengthens
- → EU political crisis (elections) → EUR uncertainty → falls
- → EUR/USD above 1.10 → European exports competitive → EU stocks rally

### Multi-Source
- [MULTI-SOURCE NEWS] 2 sources for: hamburg european open: humbert karen
- [Bing News]
- [Fri, 15 May 2026] hamburg european open: humbert karen
- → Hamburg Open 2026 (ATP 500): stacked clay-field before Roland Garros. Defending champ Flavio Cobolli, Zverev, Auger-Aliassime, Shelton, Fonseca, Men
- [Wed, 13 May 2026] Hamburg Open 2026: Results, Draw, Schedule, Entry List, Prize Money and Predictions
- → Terence Atmane capitalizes on a flurry of last-minute withdrawals to secure a spot in the ATP 500 Hamburg main draw, joining fellow Frenchmen Ugo Hu
- [] Mass Withdrawals at Hamburg Open: Atmane Gains Direct Entry into Main Draw
- [Metaculus]

## LLM Decision
- **Action:** SKIP
- **Confidence:** 55%
- **p_true:** 51.5%
- **Information Gap:** True
- **Crowd Bias:** False
- **Catalyst Type:** STATISTICAL_EDGE
- **Catalyst Strength:** 0.45

### Reasoning
Stat signal shows markets at 51% resolve YES only 44.7% of the time (n=13,967), suggesting ~6.3% edge for NO. However, multiple decision gates fail: (1) Gap is only +1% (<5% threshold), (2) Pattern for 50-60% entry shows poor WR=33% from 9 trades, (3) No direct catalyst or injury information found for this specific match, (4) Days left=6 suggests match may not be imminent. While the statistical edge exists, the combination of small gap, weak subcategory pattern, and lack of direct evidence makes this insufficient for a bet.

## Gate Result
- **Passed:** ❌ NO
- **Reason:** no stat edge gap=1%<5%

## Tool Calls
- `get_odds({'sport': 'tennis_atp', 'team': 'Humbert'})` → Odds API error: 404 {"message":"Unknown sport","error_code":"UNKNOWN_SPORT","details_url":"https://t
- `search_web({'query': 'Ugo Humbert vs Karen Khachanov Hamburg European Open 2025 odds'})` → [Wed, 20 May 2026] Google News
[] Humbert vs. Khachanov Prediction at the Hamburg European Open – We
- `search_web({'query': 'Humbert Khachanov match prediction Hamburg 2025'})` → [Wed, 20 May 2026] Google News
[Tue, 19 May 2026] Humbert vs. Khachanov Prediction at the Hamburg Eu
- `get_market_context({'keyword': 'Hamburg European Open'})` → No related markets found for 'Hamburg European Open'
- `search_web({'query': 'Ugo Humbert recent results 2025'})` → [Sun, 07 Dec 2025] Google News
[Thu, 16 Oct 2025] Rublev, De Minaur, Humbert, and Ruud reach the Fin
- `search_web({'query': 'Karen Khachanov recent results 2025'})` → [Mon, 05 Jan 2026] Google News
[Wed, 06 Aug 2025] Karen Khachanov Tournament Results - ESPN
[Wed, 29
- `get_market_context({'keyword': 'Humbert'})` → No related markets found for 'Humbert'
- `search_web({'query': 'Humbert Khachanov Polymarket prediction market'})` → No search results for: Humbert Khachanov Polymarket prediction market
- `search_web({'query': 'Hamburg European Open 2025 tennis odds bookmakers'})` → [Mon, 21 Jul 2025] Google News
[Tue, 24 Jun 2025] The 2025 tennis calendar: Every tournament, dates 
- `search_web({'query': 'Humbert vs Khachanov head to head record'})` → [Mon, 16 Feb 2026] Google News
[Sat, 02 Nov 2024] ATP Doha Day 2 Predictions Including Andrey Rublev
- `search_web({'query': 'Ugo Humbert clay court record 2025'})` → [Tue, 07 Apr 2026] Google News
[Sun, 14 Dec 2025] Monte-Carlo Masters: Carlos Alcaraz and Jannik Sin
- `search_web({'query': 'Karen Khachanov clay court 2025 form'})` → [Fri, 16 Jan 2026] Google News
[Tue, 12 May 2026] Ranking the 2026 Australian Open top contenders - 
- `search_web({'query': '"Humbert vs. Khachanov Prediction at the Hamburg European Open" Bleacher Nation'})` → [Wed, 20 May 2026] Google News
[Wed, 19 Jul 2023] Humbert vs. Khachanov Prediction at the Hamburg Eu
- `search_web({'query': 'Hamburg European Open 2026 results today'})` → [Tue, 19 May 2026] Google News
[Wed, 20 May 2026] Hamburg Open 2026: All matches, live scores and ho
- `search_web({'query': 'Hamburg Open 2026 Humbert Khachanov result'})` → [Wed, 20 May 2026] Google News
[Wed, 20 May 2026] Ugo Humbert vs. Karen Khachanov prediction, odds, 
- `search_web({'query': 'Ugo Humbert form Hamburg 2026'})` → [Tue, 19 May 2026] Google News
[Tue, 19 May 2026] Highlights: Humbert outlasts home hope Engel in Ha

## Outcome
_Pending — will be updated when market resolves_

---
*Mode: LIVE | DRY_RUN: true*