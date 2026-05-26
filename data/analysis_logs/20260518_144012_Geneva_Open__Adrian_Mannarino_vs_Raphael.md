# Market Analysis — 2026-05-18 14:40 UTC

## Market
- **Question:** Geneva Open: Adrian Mannarino vs Raphael Collignon
- **Category:** sports
- **YES Price:** 12.0%
- **Days Left:** 6
- **Volume 24h:** $91,194
- **Liquidity:** $28,964

## Statistical Prior
- **p_base:** 4.8%
- **Source:** logistic:sports
- **N (historical):** 6077
- **Raw gap:** 7.2%

## News Sources Fetched
### Macro Context
- Fear&Greed: 28/100 (Fear) | trend: deteriorating
- BTC: $76,630 (-1.7% 24h) → risk-OFF
- Fear&Greed: 28/100 (Fear) | 7d trend: deteriorating
- BTC: $76,668 (-1.6% 24h) → risk-OFF
- Fed market expectations:

### General
- [FEAR&GREED 7d trend] 28(Fear) → 27(Fear) → 31(Fear) → 43(Fear) | sentiment worsening
- Will the Fed increase interest rates by 25 bps after the Jun → YES=50%

### Multi-Source
- [MULTI-SOURCE NEWS] 2 sources for: geneva open: adrian mannarino raphael
- [Bing News]
- [Sat, 16 May 2026] geneva open: adrian mannarino raphael
- → May in Switzerland and sees Novak Djokovic as the defending champion but unlike previous years, he won't return to play in the tournament in ...
- [] Geneva Open 2026: Results, Draw, Schedule, Entry List, Prize Money and Predictions
- [Metaculus]
- [] Will the next IPC Sudan acute food insecurity analysis classify at lea
- → Community: pending

## LLM Decision
- **Action:** SKIP
- **Confidence:** 45%
- **p_true:** 5.0%
- **Information Gap:** False
- **Crowd Bias:** False
- **Catalyst Type:** NONE
- **Catalyst Strength:** 0.20

### Reasoning
Key finding: Mannarino got his 'first win of the season' at Houston Open in early May 2026, indicating a very poor 2026 season. Collignon appears to be an up-and-coming player competing against top-tier opponents (Paul, Fonseca, Cobolli) at major tournaments. However, critical data gaps remain: no head-to-head record found, no bookmaker odds obtained, no surface-specific stats (clay court form), and no injury reports. The YES price (12%) trades 7 points above the historical base rate (5%), but without concrete evidence of a specific catalyst or mispricing, there's no verifiable edge. Prior analyses also correctly identified this lack of edge. Need: (1) current ATP rankings and ELO for both players, (2) clay court win percentages, (3) head-to-head record, (4) bookmaker consensus odds to validate the 12% pricing.

## Gate Result
- **Passed:** ❌ NO
- **Reason:** low conf 45%<52%

## Tool Calls
- `get_odds({'sport': 'tennis_atp', 'team': 'Mannarino'})` → Odds API error: 404 {"message":"Unknown sport","error_code":"UNKNOWN_SPORT","details_url":"https://t
- `get_market_context({'keyword': 'Geneva Open Mannarino'})` → No related markets found for 'Geneva Open Mannarino'
- `search_web({'query': 'Adrian Mannarino vs Raphael Collignon Geneva Open 2025 odds'})` → [Sun, 17 May 2026] Google News
[Wed, 04 Mar 2026] Mannarino vs. Collignon Prediction at the Gonet Ge
- `search_web({'query': 'Raphael Collignon tennis 2025 form results'})` → [Fri, 29 Aug 2025] Google News
[Tue, 03 Mar 2026] Brain surgeon’s son Collignon on finding the menta
- `search_web({'query': 'Mannarino Geneva Open 2026 first round opponent Collignon prediction'})` → [Sun, 17 May 2026] Google News
[Thu, 15 Jan 2026] Mannarino vs. Collignon Prediction at the Gonet Ge
- `search_web({'query': 'Adrian Mannarino ATP ranking 2026 recent results form'})` → [Mon, 09 Feb 2026] Google News
[Tue, 17 Mar 2026] Biggest Movers in the ATP Top 100 this Week Includ
- `search_web({'query': 'Raphael Collignon ATP ranking 2026 recent form clay court'})` → [Tue, 20 Jan 2026] Google News
[Tue, 03 Mar 2026] Shelton wins ‘lefties on Laver’, sinks Humbert at 
- `search_web({'query': '"Mannarino" "Collignon" prediction odds winner Geneva 2026'})` → [Sat, 16 May 2026] Google News
[Sun, 17 May 2026] Adrian Mannarino vs. Raphael Collignon prediction,
- `search_web({'query': 'Raphael Collignon tennis player profile wins losses 2026'})` → [Wed, 11 Mar 2026] Google News
[Tue, 20 Jan 2026] Fonseca encouraged after Sinner defeat: 'The level
- `search_web({'query': 'dimers.com Mannarino Collignon prediction Geneva Open 2026 odds moneyline'})` → [Sat, 16 May 2026] Google News
[Sat, 16 May 2026] Adrian Mannarino vs. Raphael Collignon prediction,
- `search_web({'query': 'Mannarino clay court 2026 results Geneva Open form'})` → [Sat, 16 May 2026] Google News
[Fri, 15 May 2026] Geneva Open 2026: Draw, Schedule, Entry List, Priz
- `search_web({'query': 'site:dimers.com Mannarino Collignon Geneva Open prediction pick'})` → [Fri, 05 Feb 2021] Google News
[Mon, 09 Feb 2026] Tennis predictions for ATP and WTA matches on Sund
- `search_web({'query': 'Mannarino Collignon head to head tennis record'})` → [Thu, 19 Mar 2026] Google News
[Wed, 18 Mar 2026] ATP Miami Day 3 Predictions Including Tommy Paul v
- `search_web({'query': 'Tennis Tonic Collignon vs Mannarino head to head prediction March 2026'})` → [Sat, 21 Mar 2026] Google News
[Wed, 04 Mar 2026] H2H, prediction of Tommy Paul vs Raphael Collignon
- `search_web({'query': 'Mannarino tennis win loss record 2026 clay season'})` → [Tue, 05 May 2026] Google News
[Tue, 01 Apr 2025] ATP Rome Day 1 Predictions Including Hubert Hurkac
- `search_web({'query': 'Mannarino Houston Open first win season 2026 results'})` → [Mon, 06 Apr 2026] Google News
[Mon, 02 Feb 2026] “It's one none of the Americans want to miss”: Tom
- `search_web({'query': 'Raphael Collignon 2026 season results wins ranking'})` → [Tue, 03 Mar 2026] Google News
[Sun, 01 Feb 2026] Best Round 1 Matches at ATP Indian Wells Including

## Outcome
_Pending — will be updated when market resolves_

---
*Mode: LIVE | DRY_RUN: true*