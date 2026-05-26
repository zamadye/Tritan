# Market Analysis — 2026-05-21 20:07 UTC

## Market
- **Question:** Geneva Open: Casper Ruud vs Mariano Navone
- **Category:** sports
- **YES Price:** 72.0%
- **Days Left:** 7
- **Volume 24h:** $60,374
- **Liquidity:** $22,641

## Statistical Prior
- **p_base:** 80.5%
- **Source:** logistic:sports
- **N (historical):** 6077
- **Raw gap:** 8.5%

## News Sources Fetched
### Macro Context
- Fear&Greed: 29/100 (Fear) | trend: improving
- BTC: $77,667 (+0.1% 24h) → neutral
- Fear&Greed: 29/100 (Fear) | 7d trend: improving
- BTC: $77,565 (+0.0% 24h) → neutral
- Fed market expectations:

### General
- [FEAR&GREED 7d trend] 29(Fear) → 27(Fear) → 25(Extr) → 28(Fear) | sentiment improving
- Will the Fed increase interest rates by 50+ bps after the Ju → YES=50%
- Pittsburgh Pirates vs. St. Louis Cardinals → YES=50%

### Multi-Source
- [MULTI-SOURCE NEWS] 2 sources for: geneva open: casper ruud mariano
- [Bing News]
- [Thu, 21 May 2026] geneva open: casper ruud mariano
- → Casper Ruud leads a star-studded clay lineup with Bublik, Tien, and Rinderknech chasing semifinal spots. Follow live tennis updates.
- [Wed, 20 May 2026] LIVE Geneva Open Quarter-Finals | Learner Tien advances in American clash as Bublik and Rinderknech close the day
- → Live Geneva Open coverage: follow Casper Ruud, Taylor Fritz and more with real-time scores, match updates, key results and expert talking points fro
- [Thu, 12 Mar 2026] Geneva Open Day Four Round-up | Taylor Fritz knocked out, Ruud advances, as Wawrinka loses tight tie-break contest
- → The field of participants at the Geneva Open (May 16 to 23) is taking shape. After Stan Wawrinka (ATP 92), another former winner, Casper Ruud (ATP 1

## LLM Decision
- **Action:** YES
- **Confidence:** 62%
- **p_true:** 86.5%
- **Information Gap:** True
- **Crowd Bias:** False
- **Catalyst Type:** BASE_RATE_DIVERGENCE
- **Catalyst Strength:** 0.65

### Reasoning
Base rate analysis (n=6077) shows 80% historical win rate for Ruud-like favorites, but market prices at only 72% - an 8% gap suggesting underpricing. Ruud has an 'impressive Geneva record' per ATP Tour and is in good form (beat Musetti at Italian Open). However, Navone's recent 'remarkable comeback in Geneva' and the weak 70-80% entry pattern (43% WR from 7 trades) temper confidence. The edge exists but is moderate due to Navone's competitive form and pattern warnings.

## Gate Result
- **Passed:** ✅ YES
- **Reason:** BET YES $1.00

## Tool Calls
- `get_odds({'sport': 'tennis_atp', 'team': 'Casper Ruud'})` → Odds API error: 404 {"message":"Unknown sport","error_code":"UNKNOWN_SPORT","details_url":"https://t
- `get_odds({'sport': 'tennis_atp', 'team': 'Mariano Navone'})` → Odds API error: 404 {"message":"Unknown sport","error_code":"UNKNOWN_SPORT","details_url":"https://t
- `search_web({'query': 'Casper Ruud vs Mariano Navone Geneva Open 2025'})` → [Mon, 18 May 2026] Google News
[Sun, 17 May 2026] Preview: Cameron Norrie vs. Mariano Navone - Genev
- `search_web({'query': 'Mariano Navone injury status 2025'})` → [Fri, 26 Dec 2025] Google News
[Thu, 02 Oct 2025] Draper to miss Australian Open due to injury - Reu
- `search_web({'query': 'Ruud Navone Geneva Open odds prediction 2026'})` → [Thu, 21 May 2026] Google News
[Mon, 18 May 2026] Mariano Navone vs. Jaume Munar prediction, odds, p
- `get_market_context({'keyword': 'Geneva Open'})` → No related markets found for 'Geneva Open'
- `search_web({'query': 'Casper Ruud injury 2026'})` → [Fri, 15 May 2026] Google News
[Tue, 19 May 2026] Rome Previews: Daniil Medvedev tries to derail Jan
- `search_web({'query': 'Mariano Navone form 2026'})` → [Sun, 17 May 2026] Google News
[Mon, 18 May 2026] ATP Geneva Day 1 Predictions Including Marco Trung
- `search_web({'query': 'Geneva Open 2026 draw Casper Ruud'})` → [Mon, 18 May 2026] Google News
[Wed, 13 May 2026] Casper Ruud has a clear decision he must make imme
- `get_market_context({'keyword': 'Ruud'})` → No related markets found for 'Ruud'
- `search_web({'query': 'Casper Ruud Geneva Open 2026 results form'})` → [Wed, 20 May 2026] Google News
[Tue, 19 May 2026] Popyrin spoils Fritz's return, Ruud continues impr
- `search_web({'query': 'Mariano Navone ranking form clay court 2026'})` → [Wed, 20 May 2026] Google News
[Wed, 20 May 2026] ATP Geneva Quarterfinal Predictions Including Casp
- `get_market_context({'keyword': 'Navone'})` → No related markets found for 'Navone'
- `search_web({'query': 'Ruud vs Navone head to head record'})` → [Sat, 25 Apr 2026] Google News
[Thu, 21 May 2026] Tennis Picks Today: 5 Best Bets &amp; Predictions 
- `search_web({'query': 'Mariano Navone clay court record 2026'})` → [Sun, 17 May 2026] Google News
[Thu, 21 May 2026] Navone makes remarkable comeback in Geneva - ATP T

## Outcome
_Pending — will be updated when market resolves_

---
*Mode: LIVE | DRY_RUN: true*