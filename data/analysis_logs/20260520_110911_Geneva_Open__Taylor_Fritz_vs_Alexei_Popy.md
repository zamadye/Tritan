# Market Analysis — 2026-05-20 11:09 UTC

## Market
- **Question:** Geneva Open: Taylor Fritz vs Alexei Popyrin
- **Category:** sports
- **YES Price:** 55.0%
- **Days Left:** 6
- **Volume 24h:** $99,739
- **Liquidity:** $44,333

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
- **Confidence:** 52%
- **p_true:** 57.5%
- **Information Gap:** True
- **Crowd Bias:** False
- **Catalyst Type:** STATISTICAL_MEAN_REVERSION
- **Catalyst Strength:** 0.35

### Reasoning
Strong stat signal (44.7% resolution at 55% price, n=13,967) indicates ~10% overpricing of YES. However, no verifiable match-specific catalyst found (no injury data, H2H unclear, form data unavailable). Market-base gap only 2% (below 5% gate). Historical WR for 50-60% entry zone is poor (33%). Without direct catalyst or information advantage, the statistical edge alone is insufficient for high-confidence bet.

## Gate Result
- **Passed:** ❌ NO
- **Reason:** no stat edge gap=2%<5%

## Tool Calls
- `get_sports_data({'team': 'fritz popyrin', 'sport': 'tennis'})` → No injury data found for tennis fritz popyrin
- `search_web({'query': 'Taylor Fritz vs Alexei Popyrin Geneva Open 2024 head to head record'})` → [Wed, 20 May 2026] Google News
[Tue, 19 May 2026] PREDICTION, PREVIEW, H2H: Fritz, Ruud, Wawrinka an
- `search_web({'query': 'Taylor Fritz recent form injury status 2024'})` → [Mon, 10 Nov 2025] Google News
[Fri, 16 Jan 2026] Tennis, ATP Finals 2025: Taylor Fritz breezes thro
- `get_market_context({'keyword': 'Geneva Open Fritz Popyrin'})` → No related markets found for 'Geneva Open Fritz Popyrin'
- `search_web({'query': 'Geneva Open 2026 Taylor Fritz Alexei Popyrin odds prediction'})` → [Wed, 20 May 2026] Google News
[Tue, 19 May 2026] Taylor Fritz vs. Alexei Popyrin prediction, odds, 
- `search_web({'query': 'Taylor Fritz Alexei Popyrin head to head record ATP'})` → [Tue, 19 May 2026] Google News
[Wed, 20 May 2026] ATP Hamburg Best Bets Including Alex de Minaur vs 
- `get_odds({'sport': 'tennis_atp', 'team': 'fritz popyrin'})` → Odds API error: 404 {"message":"Unknown sport","error_code":"UNKNOWN_SPORT","details_url":"https://t
- `search_web({'query': 'Taylor Fritz vs Alexei Popyrin Geneva Open betting odds bookmaker consensus'})` → No search results for: Taylor Fritz vs Alexei Popyrin Geneva Open betting odds bookmaker consensus
- `search_web({'query': 'Alexei Popyrin 2026 clay court results form'})` → [Tue, 19 May 2026] Google News
[Wed, 01 Apr 2026] Geneva Open 2026: Results, Draw, Schedule, Entry L
- `search_web({'query': 'Popyrin Fritz 2026 head to head record tennis results'})` → [Mon, 04 Aug 2025] Google News
[Sun, 08 Sep 2024] PREVIEW Canadian Open ATP Quarter-Finals: Alexande
- `search_web({'query': 'Geneva Open 2026 draw predictions Fritz Popyrin round 2'})` → [Sun, 17 May 2026] Google News
[Tue, 19 May 2026] ATP tennis Hamburg and Geneva previews, picks, and
- `search_web({'query': '"Taylor Fritz" "Alexei Popyrin" Geneva H2H prediction 2026 site:tennistonic.com OR site:bets.com.au'})` → [Wed, 20 May 2026] Google News
[Wed, 20 May 2026] Taylor Fritz vs Alexei Popyrin Tips, Prediction &a
- `search_web({'query': 'Fritz Popyrin Geneva 2026 clay court prediction head to head'})` → [Wed, 20 May 2026] Google News
[Wed, 20 May 2026] ATP Geneva Day 4 Predictions Including Taylor Frit

## Outcome
_Pending — will be updated when market resolves_

---
*Mode: LIVE | DRY_RUN: true*