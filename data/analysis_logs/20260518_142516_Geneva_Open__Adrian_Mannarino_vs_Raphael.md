# Market Analysis — 2026-05-18 14:25 UTC

## Market
- **Question:** Geneva Open: Adrian Mannarino vs Raphael Collignon
- **Category:** sports
- **YES Price:** 12.0%
- **Days Left:** 6
- **Volume 24h:** $91,202
- **Liquidity:** $29,073

## Statistical Prior
- **p_base:** 4.8%
- **Source:** logistic:sports
- **N (historical):** 6077
- **Raw gap:** 7.2%

## News Sources Fetched
### Macro Context
- Fear&Greed: 28/100 (Fear) | trend: deteriorating
- BTC: $76,677 (-1.8% 24h) → risk-OFF
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
- **Catalyst Strength:** 0.10

### Reasoning
No concrete evidence found to support a profitable bet. The YES price (12%) already trades 7 points above the historical base rate (5%), indicating the market has likely incorporated available information. Search results provided general match predictions but no verifiable edge (injury news, form slumps, or head-to-head data) to overcome the pre-existing premium. Past decisions for this same market also correctly skipped due to low confidence. Without a clear catalyst or unpriced information, there is insufficient evidence to meet the 0.70 confidence threshold for a BET_YES.

## Gate Result
- **Passed:** ❌ NO
- **Reason:** low conf 45%<52%

## Tool Calls
- `get_odds({'sport': 'tennis_atp', 'team': 'Adrian Mannarino'})` → Odds API error: 404 {"message":"Unknown sport","error_code":"UNKNOWN_SPORT","details_url":"https://t
- `get_odds({'sport': 'tennis_atp'})` → Odds API error: 404 {"message":"Unknown sport","error_code":"UNKNOWN_SPORT","details_url":"https://t
- `get_market_context({'keyword': 'Geneva Open Mannarino Collignon'})` → No related markets found for 'Geneva Open Mannarino Collignon'
- `search_web({'query': 'Adrian Mannarino vs Raphael Collignon Geneva Open 2025 odds'})` → [Sun, 17 May 2026] Google News
[Wed, 04 Mar 2026] Mannarino vs. Collignon Prediction at the Gonet Ge
- `search_web({'query': 'Mannarino Collignon head to head 2025 2026'})` → [Thu, 19 Mar 2026] Google News
[Tue, 02 Sep 2025] ATP Miami Day 3 Predictions Including Tommy Paul v
- `search_web({'query': 'Geneva Open tennis 2025 draw results'})` → [Wed, 13 May 2026] Google News
[Tue, 18 Nov 2025] Gonet Geneva Open 2026: Draws, dates, history &amp
- `search_web({'query': 'Adrian Mannarino ranking 2026 ATP'})` → [Mon, 09 Feb 2026] Google News
[Mon, 09 Feb 2026] Biggest Movers in the ATP Top 100 this Week Includ
- `search_web({'query': 'Raphael Collignon ranking 2026 ATP'})` → [Mon, 16 Feb 2026] Google News
[Tue, 20 Jan 2026] De Minaur jumps after Rotterdam triumph, Mover of 
- `search_web({'query': 'Mannarino form 2026 clay court season results'})` → [Sun, 29 Mar 2026] Google News
[Sun, 08 Feb 2026] Shelton, Darderi, Diallo headline fields in Housto
- `search_web({'query': 'Collignon form 2026 clay court results'})` → [Tue, 03 Mar 2026] Google News
[Fri, 01 May 2026] ATP Indian Wells 2026 men’s draw: Djokovic and def
- `search_web({'query': 'Bleacher Nation Mannarino vs Collignon prediction Geneva Open'})` → [Sun, 17 May 2026] Google News
[] Mannarino vs. Collignon Prediction at the Gonet Geneva Open – Mond

## Outcome
_Pending — will be updated when market resolves_

---
*Mode: LIVE | DRY_RUN: true*