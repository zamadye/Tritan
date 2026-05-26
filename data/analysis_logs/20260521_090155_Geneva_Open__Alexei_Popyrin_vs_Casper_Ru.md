# Market Analysis — 2026-05-21 09:01 UTC

## Market
- **Question:** Geneva Open: Alexei Popyrin vs Casper Ruud
- **Category:** sports
- **YES Price:** 27.0%
- **Days Left:** 7
- **Volume 24h:** $52,788
- **Liquidity:** $53,032

## Statistical Prior
- **p_base:** 18.4%
- **Source:** logistic:sports
- **N (historical):** 6077
- **Raw gap:** 8.6%

## News Sources Fetched
### Macro Context
- Fear&Greed: 29/100 (Fear) | trend: improving
- BTC: $77,832 (+0.5% 24h) → neutral
- Fear&Greed: 29/100 (Fear) | 7d trend: improving
- BTC: $77,853 (+0.6% 24h) → neutral

### General
- [FEAR&GREED 7d trend] 29(Fear) → 27(Fear) → 25(Extr) → 28(Fear) | sentiment improving

### Multi-Source
- [MULTI-SOURCE NEWS] 2 sources for: geneva open: alexei popyrin casper
- [Bing News]
- [Wed, 20 May 2026] geneva open: alexei popyrin casper
- → Live Geneva Open coverage: follow Casper Ruud, Taylor Fritz and more with real-time scores, match updates, key results and expert talking points fro
- [Wed, 20 May 2026] Geneva Open Day Four Round-up | Taylor Fritz knocked out, Ruud advances, as Wawrinka loses tight tie-break contest
- → Alexei Popyrin memastikan Taylor Fritz mendapatkan hasil yang tidak memuaskan saat kembali beraksi di turnamen ATP ketika mereka bertemu di Geneva O
- [Thu, 21 May 2026] Alexei Popyrin Kacaukan Rencana Taylor Fritz Di Jenewa
- → This week’s tennis action continues with raging speed, and today, Australia’s Alex de Minaur is scheduled to face Italy’s Luciano Darderi at the qua

## LLM Decision
- **Action:** NO
- **Confidence:** 65%
- **p_true:** 12.4%
- **Information Gap:** True
- **Crowd Bias:** False
- **Catalyst Type:** STATISTICAL
- **Catalyst Strength:** 0.65

### Reasoning
Market overpricing Popyrin's chances against Ruud. Base rate analysis (n=6,077) shows YES resolves only 18% of time when priced at 27%, creating -9% gap favoring NO. Past similar markets (Fritz vs Popyrin) showed same pattern of ~10% overpricing. Pattern data: sports WR=76%, 20-30% entry WR=80%. Ruud is clay court specialist (Geneva is clay) and typically ranked higher. News indicates Ruud 'rampant' in Geneva form. No injury news found for Ruud. Statistical edge passes 5% gap gate.

## Gate Result
- **Passed:** ✅ YES
- **Reason:** BET NO $1.00

## Tool Calls
- `get_odds({'sport': 'tennis_atp', 'team': 'Popyrin'})` → Odds API error: 404 {"message":"Unknown sport","error_code":"UNKNOWN_SPORT","details_url":"https://t
- `get_odds({'sport': 'tennis_atp'})` → Odds API error: 404 {"message":"Unknown sport","error_code":"UNKNOWN_SPORT","details_url":"https://t
- `search_web({'query': 'Geneva Open 2025 Alexei Popyrin vs Casper Ruud odds'})` → [Thu, 21 May 2026] Google News
[Mon, 18 May 2026] Tennis Picks Today: 5 Best Bets &amp; Predictions 
- `search_web({'query': 'Alexei Popyrin vs Casper Ruud Geneva Open prediction 2025'})` → [Mon, 18 May 2026] Google News
[Thu, 21 May 2026] ATP Geneva Day 3 Predictions Including Casper Ruud
- `get_market_context({'keyword': 'Geneva Open tennis'})` → No related markets found for 'Geneva Open tennis'
- `get_market_context({'keyword': 'Popyrin Ruud'})` → No related markets found for 'Popyrin Ruud'
- `search_web({'query': 'Casper Ruud recent form 2025 injury'})` → [Thu, 25 Sep 2025] Google News
[Wed, 27 Aug 2025] 'Warrior' Alcaraz survives injury scare in Tokyo d

## Outcome
_Pending — will be updated when market resolves_

---
*Mode: LIVE | DRY_RUN: true*