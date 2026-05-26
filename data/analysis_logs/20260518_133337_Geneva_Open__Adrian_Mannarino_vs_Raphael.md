# Market Analysis — 2026-05-18 13:33 UTC

## Market
- **Question:** Geneva Open: Adrian Mannarino vs Raphael Collignon
- **Category:** sports
- **YES Price:** 13.0%
- **Days Left:** 6
- **Volume 24h:** $86,355
- **Liquidity:** $18,963

## Statistical Prior
- **p_base:** 5.5%
- **Source:** logistic:sports
- **N (historical):** 6077
- **Raw gap:** 7.5%

## News Sources Fetched
### Macro Context
- Fear&Greed: 28/100 (Fear) | trend: deteriorating
- BTC: $77,331 (-1.1% 24h) → risk-OFF
- Fear&Greed: 28/100 (Fear) | 7d trend: deteriorating
- BTC: $77,440 (-1.0% 24h) → risk-OFF
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
- **p_true:** 5.5%
- **Information Gap:** False
- **Crowd Bias:** False
- **Catalyst Type:** NONE
- **Catalyst Strength:** 0.00

### Reasoning
YES price (13%) trades 8 points ABOVE historical base rate (5%), indicating market has already incorporated information or is overvaluing YES. No verifiable catalyst or edge found - no injury news, no recent form changes, no breaking news affecting this specific match. Past similar decisions were SKIPPED at 40-45% confidence. Sports pattern strong (88% WR) but this appears to be a no-gap trade with no information advantage. Confidence well below 52% gate and 70% threshold for BET_YES.

## Gate Result
- **Passed:** ❌ NO
- **Reason:** low conf 45%<52%

## Tool Calls
- `search_web({'query': 'Geneva Open Adrian Mannarino vs Raphael Collignon odds'})` → [Sun, 17 May 2026] Google News
[Sat, 16 May 2026] Mannarino vs. Collignon Prediction at the Gonet Ge
- `search_web({'query': 'Adrian Mannarino injury update 2026'})` → [Sun, 22 Mar 2026] Google News
[Thu, 04 Sep 2025] Tommy Paul ankle injury sparks cold handshake talk
- `search_web({'query': 'Raphael Collignon recent form 2026'})` → [Fri, 15 May 2026] Google News
[Tue, 17 Mar 2026] Adrian Mannarino v Raphael Collignon (18/05/2026) 
- `get_market_context({'keyword': 'Geneva Open'})` → No related markets found for 'Geneva Open'
- `get_market_context({'keyword': 'Mannarino'})` → No related markets found for 'Mannarino'
- `get_odds({'sport': 'tennis_atp_italian_open', 'team': 'Mannarino'})` → Odds API error: 401 {"message":"Usage quota has been reached. See usage plans at https://the-odds-ap
- `search_web({'query': 'Mannarino vs Collignon betting odds prediction'})` → [Sun, 17 May 2026] Google News
[Sat, 16 May 2026] Mannarino vs. Collignon Prediction at the Gonet Ge

## Outcome
_Pending — will be updated when market resolves_

---
*Mode: LIVE | DRY_RUN: true*