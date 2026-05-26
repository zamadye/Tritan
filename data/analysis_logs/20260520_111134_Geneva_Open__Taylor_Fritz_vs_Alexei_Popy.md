# Market Analysis — 2026-05-20 11:11 UTC

## Market
- **Question:** Geneva Open: Taylor Fritz vs Alexei Popyrin
- **Category:** sports
- **YES Price:** 55.0%
- **Days Left:** 6
- **Volume 24h:** $84,562
- **Liquidity:** $91,191

## Statistical Prior
- **p_base:** 57.5%
- **Source:** logistic:sports
- **N (historical):** 6077
- **Raw gap:** 2.5%

## News Sources Fetched
### Macro Context
- Fear&Greed: 27/100 (Fear) | trend: deteriorating
- BTC: $77,443 (+0.6% 24h) → neutral
- Fear&Greed: 27/100 (Fear) | 7d trend: deteriorating
- BTC: $77,464 (+0.6% 24h) → neutral
- Fed market expectations:

### General
- [FEAR&GREED 7d trend] 27(Fear) → 25(Extr) → 28(Fear) → 27(Fear) | sentiment worsening
- MicroStrategy sells any Bitcoin by May 31, 2026? → YES=50%

### Multi-Source
- [MULTI-SOURCE NEWS] 2 sources for: geneva open: taylor fritz alexei
- [Bing News]
- [Tue, 19 May 2026] geneva open: taylor fritz alexei
- → After 57 days without competition, Taylor Fritz (No. 8) takes on Alexei Popyrin (No. 61) in the second round of the Geneva Open. Tied 1-1, first mee
- [Wed, 20 May 2026] Fritz vs Popyrin • 2nd round • Geneva 2026
- → Live Geneva Open coverage: follow Casper Ruud, Taylor Fritz and more with real-time scores, match updates, key results and expert talking points fro
- [Sat, 16 May 2026] LIVE Geneva Open Day Four | Fritz-Popyrin, Norrie, Tsitsipas-Tien, Ruud in action
- → May in Switzerland and sees Novak Djokovic as the defending champion but unlike previous years, he won't return to play in the tournament in ...

## LLM Decision
- **Action:** SKIP
- **Confidence:** 58%
- **p_true:** 51.5%
- **Information Gap:** True
- **Crowd Bias:** False
- **Catalyst Type:** STAT_SIGNAL + FITNESS_CONCERN
- **Catalyst Strength:** 0.65

### Reasoning
Strong statistical signal (n=13,967) shows markets at 55% YES resolve YES only 44.7% of time — systematic ~10% overpricing of YES. Fundamental catalyst supports this: Fritz returning after 2 months away from clay, admits fitness concerns ('not perfect', 'I can play without pain, I just need time'). Popyrin is in active form, recently beat Tabur 2:1, and is specifically hunting top 10 scalps (14th top 10 scalp). Market at 55% overprices Fritz's chances given his rust and Popyrin's current form. Previous decision was SKIP due to small gap (2%), but the stat signal provides independent quantitative evidence of overpricing not captured by the gap metric.

## Gate Result
- **Passed:** ❌ NO
- **Reason:** no stat edge gap=2%<5%

## Tool Calls
- `get_odds({'sport': 'tennis_atp', 'team': 'Fritz'})` → Odds API error: 404 {"message":"Unknown sport","error_code":"UNKNOWN_SPORT","details_url":"https://t
- `get_odds({'sport': 'tennis_atp'})` → Odds API error: 404 {"message":"Unknown sport","error_code":"UNKNOWN_SPORT","details_url":"https://t
- `search_web({'query': 'Taylor Fritz vs Alexei Popyrin Geneva Open 2025 prediction'})` → [Wed, 20 May 2026] Google News
[Tue, 19 May 2026] ATP Geneva Day 4 Predictions Including Taylor Frit
- `search_web({'query': 'Taylor Fritz injury status Geneva Open 2025'})` → [Mon, 18 May 2026] Google News
[Sun, 17 May 2026] “Two months is long”: Taylor Fritz admits concerns
- `search_web({'query': 'Alexei Popyrin recent form clay court 2025'})` → [Thu, 28 Aug 2025] Google News
[Sun, 26 Oct 2025] Alexei Popyrin’s profile: Age, height, family, gir
- `get_market_context({'keyword': 'Geneva Open Fritz Popyrin'})` → No related markets found for 'Geneva Open Fritz Popyrin'
- `search_web({'query': '"Taylor Fritz" "Geneva" clay court return 2026 concerns'})` → [Mon, 18 May 2026] Google News
[Mon, 18 May 2026] “Two months is long”: Taylor Fritz admits concerns
- `search_web({'query': '"Alexei Popyrin" "Geneva Open" 2026 form results'})` → [Tue, 19 May 2026] Google News
[Tue, 19 May 2026] Ruud bounces back from Rome final defeat, advances
- `search_web({'query': 'Taylor Fritz Geneva Open 2026 round result'})` → [Tue, 19 May 2026] Google News
[Mon, 18 May 2026] Geneva Open 2026: Results, Draw, Schedule, Entry L
- `search_web({'query': 'Alexei Popyrin Geneva Open 2026 result'})` → [Tue, 19 May 2026] Google News
[Wed, 20 May 2026] Ruud bounces back from Rome final defeat, advances
- `search_web({'query': 'Popyrin Tabur Geneva Open 2026 score result'})` → [Wed, 20 May 2026] Google News
[Mon, 18 May 2026] Alexei Popyrin - Clement Tabur 2:1 - Flashscore.co
- `search_web({'query': '"Fritz" "Popyrin" head to head record clay'})` → [Wed, 20 May 2026] Google News
[Mon, 29 Jul 2024] Taylor Fritz vs Alexei Popyrin Tips, Prediction &a
- `get_crypto_price({'coin': 'bitcoin'})` → bitcoin: $77,449.00 | 24h: +0.68%
- `search_web({'query': 'Taylor Fritz clay court results 2026 season'})` → [Wed, 13 May 2026] Google News
[Tue, 24 Mar 2026] Gonet Geneva Open 2026: Draws, dates, history &amp

## Outcome
_Pending — will be updated when market resolves_

---
*Mode: LIVE | DRY_RUN: true*