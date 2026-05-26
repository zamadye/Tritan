# Market Analysis — 2026-05-18 11:13 UTC

## Market
- **Question:** Geneva Open: Stefanos Tsitsipas vs Giovanni Mpetshi Perricard
- **Category:** sports
- **YES Price:** 69.0%
- **Days Left:** 6
- **Volume 24h:** $100,267
- **Liquidity:** $50,952

## Statistical Prior
- **p_base:** 76.9%
- **Source:** logistic:sports
- **N (historical):** 6077
- **Raw gap:** 7.9%

## News Sources Fetched
### Macro Context
- Fear&Greed: 28/100 (Fear) | trend: deteriorating
- BTC: $76,783 (-2.1% 24h) → risk-OFF
- Fear&Greed: 28/100 (Fear) | 7d trend: deteriorating
- BTC: $76,695 (-2.1% 24h) → risk-OFF
- Fed market expectations:

### General
- [FEAR&GREED 7d trend] 28(Fear) → 27(Fear) → 31(Fear) → 43(Fear) | sentiment worsening
- Will the Fed increase interest rates by 25 bps after the Jun → YES=50%

### Multi-Source
- [MULTI-SOURCE NEWS] 2 sources for: geneva open: stefanos tsitsipas giovanni
- [Bing News]
- [Mon, 18 May 2026] geneva open: stefanos tsitsipas giovanni
- → Follow the Geneva Open as Wawrinka begins his farewell, with Tsitsipas, Rinderknech, and Mpetshi Perricard in action—crucial clay-court form ahead o
- [Fri, 15 May 2026] LIVE Geneva Open Day Two | Stan Wawrinka headlines on home soil, Tsitsipas-Mpetshi Perricard, Rinderknech in action
- → Just days before Roland-Garros, the Geneva tournament offers a final high-level rehearsal on clay. Taylor Fritz returns from injury, while several m
- [] Tsitsipas vs Mpetshi Perricard, Fritz Returns: Geneva ATP 250 Draw Revealed with Blockbuster First-Round Matches
- [Metaculus]

## LLM Decision
- **Action:** YES
- **Confidence:** 65%
- **p_true:** 82.9%
- **Information Gap:** True
- **Crowd Bias:** False
- **Catalyst Type:** STATISTICAL_VALUE
- **Catalyst Strength:** 0.65

### Reasoning
YES price (69%) is 8 points below the historical base rate (77%, n=6077), indicating systematic underpricing. Historical data shows when markets price YES at 69%, outcomes resolve YES 77% of the time. The 8% gap exceeds the 5% threshold for actionable edge. Tsitsipas has strong clay court pedigree (former Roland Garros finalist) despite recent form concerns. Mpetshi Perricard is primarily a hard-court big server less proven on clay. Entry price in the 60-70% range shows 67% historical win rate. However, confidence tempered by: (1) Tsitsipas's recent ranking decline and poor Monte Carlo result, (2) info gap trades historically showing lower 43% WR, and (3) Mpetshi Perricard's improving trajectory. Net edge exists but is moderate rather than strong.

## Gate Result
- **Passed:** ✅ YES
- **Reason:** BET YES $1.00

## Tool Calls
- `get_odds({'sport': 'tennis_atp', 'team': 'Tsitsipas'})` → Odds API error: 404 {"message":"Unknown sport","error_code":"UNKNOWN_SPORT","details_url":"https://t
- `get_odds({'sport': 'tennis_atp'})` → Odds API error: 404 {"message":"Unknown sport","error_code":"UNKNOWN_SPORT","details_url":"https://t
- `get_market_context({'keyword': 'Geneva Open Tsitsipas'})` → No related markets found for 'Geneva Open Tsitsipas'
- `search_web({'query': 'Stefanos Tsitsipas vs Giovanni Mpetshi Perricard Geneva Open 2025'})` → [Mon, 18 May 2026] Google News
[Sun, 17 May 2026] ATP Geneva Day 2 Predictions Including Stefanos Ts
- `search_web({'query': 'Tsitsipas recent form 2025 clay season results'})` → [Thu, 09 Apr 2026] Google News
[Tue, 07 Apr 2026] Clay power rankings: 2026 ATP Tour - Tennisnerd
[F
- `search_web({'query': 'Mpetshi Perricard 2025 form clay court results'})` → [Sat, 06 Dec 2025] Google News
[Wed, 06 May 2026] Fritz headlines 2025's best Grand Slam comebacks -
- `search_web({'query': 'Geneva Open 2025 draw predictions betting odds'})` → [Thu, 15 Jan 2026] Google News
[Sat, 28 Jun 2025] Australian Open tennis men's preview, picks, and b
- `get_market_context({'keyword': 'Tsitsipas tennis'})` → No related markets found for 'Tsitsipas tennis'
- `search_web({'query': '"Tsitsipas vs Mpetshi Perricard" Geneva 2026 prediction'})` → [Mon, 18 May 2026] Google News
[Sun, 17 May 2026] ATP Geneva Day 2 Predictions Including Stefanos Ts
- `search_web({'query': 'Mpetshi Perricard clay court ranking 2026'})` → [Sun, 17 May 2026] Google News
[Sat, 04 Apr 2026] ATP tennis Hamburg and Geneva previews, picks, and
- `search_web({'query': 'Tsitsipas ranking 2026 clay season form'})` → [Mon, 18 May 2026] Google News
[Thu, 09 Apr 2026] Geneva R1 previews and predictions: Michelsen vs. 
- `search_web({'query': 'Geneva Open 2026 Tsitsipas Mpetshi Perricard odds betting lines'})` → [Sat, 16 May 2026] Google News
[Mon, 18 May 2026] Tsitsipas vs. Mpetshi Perricard Prediction at the 
- `search_web({'query': 'Tsitsipas Mpetshi Perricard head to head record'})` → [Mon, 18 May 2026] Google News
[Mon, 18 May 2026] H2H, prediction of Giovanni Mpetshi Perricard vs S
- `search_web({'query': 'Mpetshi Perricard serve speed ranking 2026'})` → [Sun, 18 Jan 2026] Google News
[Mon, 30 Jun 2025] It All Adds Up: Mpetshi Perricard's serve sizzles 

## Outcome
_Pending — will be updated when market resolves_

---
*Mode: LIVE | DRY_RUN: true*