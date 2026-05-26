# Market Analysis — 2026-05-20 09:24 UTC

## Market
- **Question:** Geneva Open: Stefanos Tsitsipas vs Learner Tien
- **Category:** sports
- **YES Price:** 56.0%
- **Days Left:** 6
- **Volume 24h:** $126,269
- **Liquidity:** $55,209

## Statistical Prior
- **p_base:** 59.0%
- **Source:** logistic:sports
- **N (historical):** 6077
- **Raw gap:** 2.9%

## News Sources Fetched
### Macro Context
- Fear&Greed: 27/100 (Fear) | trend: deteriorating
- BTC: $77,331 (+0.6% 24h) → neutral
- Fear&Greed: 27/100 (Fear) | 7d trend: deteriorating
- BTC: $77,390 (+0.4% 24h) → neutral
- Fed market expectations:

### General
- [FEAR&GREED 7d trend] 27(Fear) → 25(Extr) → 28(Fear) → 27(Fear) | sentiment worsening
- MicroStrategy sells any Bitcoin by May 31, 2026? → YES=50%

### Multi-Source
- [MULTI-SOURCE NEWS] 2 sources for: geneva open: stefanos tsitsipas learner
- [Bing News]
- [Wed, 20 May 2026] geneva open: stefanos tsitsipas learner
- → Live Geneva Open coverage: follow Casper Ruud, Taylor Fritz and more with real-time scores, match updates, key results and expert talking points fro
- [Sat, 16 May 2026] LIVE Geneva Open Day Four | Fritz-Popyrin, Norrie, Tsitsipas-Tien, Ruud in action
- → May in Switzerland and sees Novak Djokovic as the defending champion but unlike previous years, he won't return to play in the tournament in ...
- [] Geneva Open 2026: Results, Draw, Schedule, Entry List, Prize Money and Predictions
- [Metaculus]

## LLM Decision
- **Action:** SKIP
- **Confidence:** 42%
- **p_true:** 59.0%
- **Information Gap:** False
- **Crowd Bias:** False
- **Catalyst Type:** FORM_DIVERGENCE
- **Catalyst Strength:** 0.35

### Reasoning
Stat signal (44.7% resolution at 56% price, n=13,967) and player form analysis both suggest Tsitsipas overpriced — Tien surging into Top 20 while Tsitsipas in freefall. However, gap is only 3% (below 5% gate), entry zone 50-60% has terrible 33% historical WR, no bookmaker odds available to verify, and previous decisions on identical market were SKIP. Directional lean toward NO but insufficient concrete edge to bet.

## Gate Result
- **Passed:** ❌ NO
- **Reason:** no stat edge gap=3%<5%

## Tool Calls
- `get_odds({'sport': 'tennis_atp', 'team': 'Tsitsipas'})` → Odds API error: 404 {"message":"Unknown sport","error_code":"UNKNOWN_SPORT","details_url":"https://t
- `get_sports_data({'sport': 'tennis', 'team': 'Tsitsipas'})` → No injury data found for tennis Tsitsipas
- `search_web({'query': 'Geneva Open 2025 Stefanos Tsitsipas vs Learner Tien odds'})` → [Wed, 20 May 2026] Google News
[Wed, 20 May 2026] Tennis Picks Today: 5 Best Bets &amp; Predictions 
- `get_market_context({'keyword': 'Geneva Open Tsitsipas'})` → No related markets found for 'Geneva Open Tsitsipas'
- `search_web({'query': 'Stefanos Tsitsipas recent form 2025 clay court results'})` → [Thu, 09 Apr 2026] Google News
[Thu, 31 Jul 2025] Clay power rankings: 2026 ATP Tour - Tennisnerd
[W
- `search_web({'query': 'Learner Tien ATP 2025 results form'})` → [Sat, 20 Dec 2025] Google News
[Sun, 21 Dec 2025] Tien &amp; Blockx reveal how the Next Gen ATP Fina
- `get_market_context({'keyword': 'Tsitsipas Tien'})` → No related markets found for 'Tsitsipas Tien'
- `search_web({'query': 'Tsitsipas vs Tien prediction Geneva Open 2025 head to head'})` → [Wed, 20 May 2026] Google News
[Wed, 04 Feb 2026] ATP Geneva Day 4 Predictions Including Taylor Frit
- `search_web({'query': 'Tsitsipas Tien odds tennis ATP 2025'})` → [Tue, 19 May 2026] Google News
[Sun, 17 May 2026] ATP Geneva Best Bets Including Taylor Fritz vs Ale
- `search_web({'query': '"Tsitsipas" "Tien" Geneva Open prediction'})` → [Wed, 20 May 2026] Google News
[Tue, 19 May 2026] ATP Geneva Day 4 Predictions Including Taylor Frit
- `search_web({'query': 'Learner Tien 2025 ATP ranking wins losses'})` → [Fri, 28 Nov 2025] Google News
[Mon, 27 Oct 2025] Learner Tien on the #NextGenATP surge: 'Everyone w
- `search_web({'query': 'site:thesgrandstand.com Tsitsipas Tien Geneva 2026 prediction'})` → No search results for: site:thesgrandstand.com Tsitsipas Tien Geneva 2026 prediction
- `search_web({'query': 'Tsitsipas Geneva Open 2026 clay record recent form'})` → [Mon, 18 May 2026] Google News
[Sun, 17 May 2026] Wawrinka survives final-set tie-break in Geneva, j
- `search_web({'query': 'Stefanos Tsitsipas ATP ranking May 2026'})` → [Wed, 20 May 2026] Google News
[Thu, 07 May 2026] Stefanos Tsitsipas vs Learner Tien Prediction &amp
- `search_web({'query': 'Learner Tien ATP ranking May 2026'})` → [Mon, 18 May 2026] Google News
[Wed, 20 May 2026] American Learner Tien breaks into Top 20 on ATP ra

## Outcome
_Pending — will be updated when market resolves_

---
*Mode: LIVE | DRY_RUN: true*