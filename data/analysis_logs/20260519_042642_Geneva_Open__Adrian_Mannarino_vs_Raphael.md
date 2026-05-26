# Market Analysis — 2026-05-19 04:26 UTC

## Market
- **Question:** Geneva Open: Adrian Mannarino vs Raphael Collignon
- **Category:** sports
- **YES Price:** 12.0%
- **Days Left:** 6
- **Volume 24h:** $68,508
- **Liquidity:** $29,764

## Statistical Prior
- **p_base:** 4.8%
- **Source:** logistic:sports
- **N (historical):** 6077
- **Raw gap:** 7.2%

## News Sources Fetched
### Macro Context
- Fear&Greed: 25/100 (Extreme Fear) | trend: deteriorating
- BTC: $76,784 (-0.2% 24h) → neutral
- Fear&Greed: 25/100 (Extreme Fear) | 7d trend: deteriorating
- BTC: $76,709 (-0.1% 24h) → neutral

### General
- [FEAR&GREED 7d trend] 25(Extr) → 28(Fear) → 27(Fear) → 31(Fear) | sentiment worsening

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
- **Confidence:** 35%
- **p_true:** 5.0%
- **Information Gap:** False
- **Crowd Bias:** False
- **Catalyst Type:** NONE
- **Catalyst Strength:** 0.00

### Reasoning
Unresolved timing discrepancy and insufficient verifiable edge. Critical issues: (1) Market states '6 days left' but match is scheduled for May 18 per multiple sources - same discrepancy flagged in prior SKIP decisions remains unresolved; (2) Prediction articles exist from dimers.com and Bleacher Nation but content inaccessible to verify specific odds/analysis; (3) Mannarino ranked ~#43, Collignon is rising talent (beat Ruud recently) but form data unavailable; (4) Market YES at 12% is 7% ABOVE base rate of 5%, suggesting crowd may be overpricing YES rather than offering value; (5) Two prior analyses of this exact market resulted in SKIP (conf 38%, 25%) with same low-information assessment. Pattern data shows 80% WR on sports bets overall, but this specific market lacks the verifiable catalyst needed for a confident position. Wait for clearer information or better pricing.

## Gate Result
- **Passed:** ❌ NO
- **Reason:** low conf 35%<52%

## Tool Calls
- `get_odds({'sport': 'tennis_atp', 'team': 'Mannarino'})` → Odds API error: 404 {"message":"Unknown sport","error_code":"UNKNOWN_SPORT","details_url":"https://t
- `get_sports_data({'sport': 'nba', 'team': 'Mannarino'})` → No injury data found for nba Mannarino
- `search_web({'query': 'Adrian Mannarino Geneva Open 2025 match preview'})` → [Sun, 17 May 2026] Google News
[Thu, 28 Aug 2025] ATP tennis Hamburg and Geneva previews, picks, and
- `search_web({'query': 'Raphael Collignon tennis 2025 results form'})` → [Fri, 29 Aug 2025] Google News
[Tue, 03 Mar 2026] Brain surgeon’s son Collignon on finding the menta
- `get_market_context({'keyword': 'Geneva Open tennis Mannarino'})` → No related markets found for 'Geneva Open tennis Mannarino'
- `search_web({'query': 'Mannarino vs Collignon Geneva Open 2025 head to head'})` → [Mon, 18 May 2026] Google News
[Mon, 18 May 2026] ATP Geneva Day 3 Predictions Including Casper Ruud
- `search_web({'query': 'ATP Geneva Open 2025 draw schedule first round'})` → [Wed, 13 May 2026] Google News
[Sat, 16 May 2026] Gonet Geneva Open 2026: Draws, dates, history &amp
- `get_market_context({'keyword': 'ATP tennis prediction market'})` → No related markets found for 'ATP tennis prediction market'
- `search_web({'query': '"Mannarino" "Collignon" Geneva tennis prediction 2026'})` → [Mon, 18 May 2026] Google News
[Sat, 16 May 2026] ATP Geneva Day 3 Predictions Including Casper Ruud
- `search_web({'query': 'Raphael Collignon ATP ranking 2026 clay court results'})` → [Wed, 22 Apr 2026] Google News
[Sat, 02 May 2026] The 2026 Madrid Open is here. These are the Argent
- `search_web({'query': 'Adrian Mannarino 2026 season form ranking clay court'})` → [Mon, 18 May 2026] Google News
[Sun, 29 Mar 2026] ATP Geneva Day 3 Predictions Including Casper Ruud
- `search_web({'query': 'Raphael Collignon 2026 season form ranking clay court'})` → [Mon, 18 May 2026] Google News
[Tue, 03 Mar 2026] ATP Geneva Day 3 Predictions Including Casper Ruud
- `search_web({'query': 'dimers.com Mannarino Collignon Geneva Open 2026 prediction'})` → [Sat, 16 May 2026] Google News
[Sat, 16 May 2026] Adrian Mannarino vs. Raphael Collignon prediction,
- `search_web({'query': '"Bleacher Nation" Mannarino Collignon odds picks 2026'})` → [Sun, 17 May 2026] Google News
[Sat, 16 May 2026] Mannarino vs. Collignon Prediction at the Gonet Ge
- `search_web({'query': 'site:dimers.com Mannarino Collignon Geneva Open'})` → [Fri, 05 Feb 2021] Google News
[Mon, 09 Feb 2026] Tennis predictions for ATP and WTA matches on Mond
- `search_web({'query': 'Mannarino Collignon odds tennis Geneva Open May 18 2026'})` → [Sun, 17 May 2026] Google News
[Sat, 16 May 2026] Mannarino vs. Collignon Prediction at the Gonet Ge

## Outcome
_Pending — will be updated when market resolves_

---
*Mode: LIVE | DRY_RUN: true*