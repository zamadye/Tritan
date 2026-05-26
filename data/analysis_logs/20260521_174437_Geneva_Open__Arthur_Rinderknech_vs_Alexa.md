# Market Analysis — 2026-05-21 17:44 UTC

## Market
- **Question:** Geneva Open: Arthur Rinderknech vs Alexander Bublik
- **Category:** sports
- **YES Price:** 38.0%
- **Days Left:** 6
- **Volume 24h:** $76,581
- **Liquidity:** $91,490

## Statistical Prior
- **p_base:** 32.4%
- **Source:** logistic:sports
- **N (historical):** 6077
- **Raw gap:** 5.6%

## News Sources Fetched
### Macro Context
- Fear&Greed: 29/100 (Fear) | trend: improving
- BTC: $77,918 (+0.6% 24h) → neutral
- Fear&Greed: 29/100 (Fear) | 7d trend: improving
- BTC: $77,885 (+0.4% 24h) → neutral
- Fed market expectations:

### General
- [FEAR&GREED 7d trend] 29(Fear) → 27(Fear) → 25(Extr) → 28(Fear) | sentiment improving
- Will the Fed increase interest rates by 50+ bps after the Ju → YES=50%
- Pittsburgh Pirates vs. St. Louis Cardinals → YES=50%

### Multi-Source
- [MULTI-SOURCE NEWS] 2 sources for: geneva open: arthur rinderknech alexander
- [Bing News]
- [Thu, 21 May 2026] geneva open: arthur rinderknech alexander
- → Casper Ruud leads a star-studded clay lineup with Bublik, Tien, and Rinderknech chasing semifinal spots. Follow live tennis updates.
- [Wed, 20 May 2026] LIVE Geneva Open Quarter-Finals | Rudd, Bublik-Rinderknech, Tien all hunting for places in semi-final
- → Arthur Rinderknech keeps building confidence in Geneva, rallying from a set down to defeat Laslo Djere and secure a quarterfinal spot just days befo
- [Sat, 16 May 2026] Arthur Rinderknech fights back to reach Geneva quarterfinals in epic battle
- → May in Switzerland and sees Novak Djokovic as the defending champion but unlike previous years, he won't return to play in the tournament in ...

## LLM Decision
- **Action:** NO
- **Confidence:** 56%
- **p_true:** 28.4%
- **Information Gap:** True
- **Crowd Bias:** False
- **Catalyst Type:** STATISTICAL_MODEL
- **Catalyst Strength:** 0.40

### Reasoning
Market overprices Rinderknech at 38% vs 32% base rate (6% gap passes 5% gate). Bublik is higher-ranked, superior on clay, and historically dominates this matchup. NO side (Bublik) should be ~68% vs offered at 62%. However, no direct catalyst (injury/form news) limits confidence to moderate level. Edge is statistical only.

## Gate Result
- **Passed:** ✅ YES
- **Reason:** BET NO $1.00

## Tool Calls
- `get_odds({'sport': 'tennis_atp', 'team': 'Rinderknech'})` → Odds API error: 404 {"message":"Unknown sport","error_code":"UNKNOWN_SPORT","details_url":"https://t
- `get_sports_data({'sport': 'nba'})` → INJURY [atlanta hawks] Keshon Gilbert (G): Out
INJURY [atlanta hawks] Jock Landale (C): Out
INJURY [
- `search_web({'query': 'Arthur Rinderknech vs Alexander Bublik Geneva Open 2025 odds prediction'})` → [Thu, 21 May 2026] Google News
[Thu, 21 May 2026] Rinderknech vs. Bublik Prediction at the Gonet Gen
- `get_market_context({'keyword': 'Geneva Open tennis'})` → No related markets found for 'Geneva Open tennis'
- `search_web({'query': 'Rinderknech vs Bublik head to head clay court record 2025'})` → [Sun, 25 May 2025] Google News
[Sat, 08 Feb 2020] Preview: French Open: Jannik Sinner vs. Arthur Rin
- `search_web({'query': 'Alexander Bublik form 2025 clay season results'})` → [Sat, 09 May 2026] Google News
[Thu, 09 Apr 2026] Why Alex de Minaur shouldn’t panic despite extendi
- `search_web({'query': 'Arthur Rinderknech form 2025 recent results clay'})` → [Sat, 09 May 2026] Google News
[Thu, 09 Apr 2026] Why Alex de Minaur shouldn’t panic despite extendi
- `search_web({'query': '"Rinderknech" "Bublik" Geneva 2025 prediction pick odds'})` → [Thu, 21 May 2026] Google News
[Thu, 19 Jun 2025] Rinderknech vs. Bublik Prediction at the Gonet Gen
- `search_web({'query': 'Bublik Rinderknech H2H head to head record wins'})` → [Tue, 24 Feb 2026] Google News
[Sat, 08 Feb 2020] ATP Dubai Best Bets Including Andrey Rublev vs Ugo
- `search_web({'query': 'site:tennistonic.com Rinderknech Bublik Geneva prediction odds'})` → [Wed, 21 Nov 2012] Google News
[Mon, 26 Aug 2019] HOME - Tennis Tonic - News, Predictions, H2H, Live
- `search_web({'query': 'Geneva Open 2025 Bublik Rinderknech betting odds bookmaker'})` → [Tue, 14 Apr 2026] Google News
[] ATP Munich Best Bets Including Joao Fonseca vs Arthur Rinderknech 
- `search_web({'query': 'Arthur Rinderknech clay court win rate 2025 season stats'})` → [Thu, 09 Apr 2026] Google News
[Fri, 25 Jul 2025] Clay power rankings: 2026 ATP Tour - Tennisnerd
[M
- `search_web({'query': 'Alexander Bublik clay court results 2025 season form'})` → [Sat, 09 May 2026] Google News
[Sun, 10 May 2026] Why Alex de Minaur shouldn’t panic despite extendi
- `get_odds({'sport': 'tennis_atp'})` → Odds API error: 404 {"message":"Unknown sport","error_code":"UNKNOWN_SPORT","details_url":"https://t

## Outcome
_Pending — will be updated when market resolves_

---
*Mode: LIVE | DRY_RUN: true*