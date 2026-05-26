# Market Analysis — 2026-05-18 13:50 UTC

## Market
- **Question:** Geneva Open: Adrian Mannarino vs Raphael Collignon
- **Category:** sports
- **YES Price:** 13.0%
- **Days Left:** 6
- **Volume 24h:** $87,709
- **Liquidity:** $19,036

## Statistical Prior
- **p_base:** 5.5%
- **Source:** logistic:sports
- **N (historical):** 6077
- **Raw gap:** 7.5%

## News Sources Fetched
### Macro Context
- Fear&Greed: 28/100 (Fear) | trend: deteriorating
- BTC: $76,916 (-1.7% 24h) → risk-OFF
- Fear&Greed: 28/100 (Fear) | 7d trend: deteriorating
- BTC: $76,825 (-1.8% 24h) → risk-OFF
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
- **Confidence:** 42%
- **p_true:** 5.5%
- **Information Gap:** False
- **Crowd Bias:** False
- **Catalyst Type:** NONE_IDENTIFIED
- **Catalyst Strength:** 0.15

### Reasoning
The YES price (13%) already trades 8 points ABOVE the historical base rate (5%), indicating the market has already incorporated positive information for Collignon. No new catalyst (injury, withdrawal, or form spike) was discovered that would push YES higher. Past decisions on this same market correctly identified the same issue—market efficiency at these levels. Without a clear information edge or breaking news suggesting Collignon has an enhanced chance beyond what's priced, there's no profitable bet. The 90% WR sports pattern applies only when concrete evidence exists, which is absent here.

## Gate Result
- **Passed:** ❌ NO
- **Reason:** low conf 42%<52%

## Tool Calls
- `get_odds({'sport': 'tennis_atp', 'team': 'Mannarino'})` → Odds API error: 404 {"message":"Unknown sport","error_code":"UNKNOWN_SPORT","details_url":"https://t
- `get_odds({'sport': 'tennis'})` → Odds API error: 401 {"message":"Usage quota has been reached. See usage plans at https://the-odds-ap
- `search_web({'query': 'Adrian Mannarino vs Raphael Collignon Geneva Open 2025 odds'})` → [Sun, 17 May 2026] Google News
[Wed, 04 Mar 2026] Mannarino vs. Collignon Prediction at the Gonet Ge
- `search_web({'query': 'Raphael Collignon ATP ranking form 2025'})` → [Tue, 18 Nov 2025] Google News
[Tue, 03 Mar 2026] Bergs, Collignon fire Belgium to victory against F
- `search_web({'query': 'Adrian Mannarino recent results form 2025'})` → [Fri, 26 Sep 2025] Google News
[Sat, 06 Dec 2025] Highlights: Mannarino snaps in-form Bublik's strea
- `search_web({'query': 'Raphael Collignon Geneva Open 2025 draw opponent Mannarino'})` → No search results for: Raphael Collignon Geneva Open 2025 draw opponent Mannarino
- `search_web({'query': 'Adrian Mannarino clay court form 2025 results'})` → [Fri, 06 Feb 2026] Google News
[Sat, 30 Aug 2025] Tennis prop betting guide: Best stats for aces, ga
- `get_market_context({'keyword': 'Geneva Open tennis'})` → No related markets found for 'Geneva Open tennis'
- `search_web({'query': 'Geneva Open 2026 tennis draw first round'})` → [Sun, 17 May 2026] Google News
[Sat, 16 May 2026] Hamburg Open 2026: All matches, live scores and ho
- `search_web({'query': 'Mannarino Collignon head to head tennis'})` → [Sat, 16 May 2026] Google News
[Thu, 19 Mar 2026] Adrian Mannarino vs Raphael Collignon - Match ATP 
- `search_web({'query': 'Mannarino vs Collignon ATP Geneva Open 2026 prediction odds'})` → [Sat, 16 May 2026] Google News
[Sat, 16 May 2026] Adrian Mannarino vs. Raphael Collignon prediction,
- `get_market_context({'keyword': 'Collignon tennis'})` → No related markets found for 'Collignon tennis'
- `search_web({'query': 'dimers.com Mannarino Collignon Geneva Open prediction odds picks'})` → [Sat, 16 May 2026] Google News
[Sat, 16 May 2026] Adrian Mannarino vs. Raphael Collignon prediction,
- `search_web({'query': 'Raphael Collignon ATP ranking 2026 clay court record'})` → [Tue, 04 Nov 2025] Google News
[Tue, 03 Mar 2026] Young and the restless: Former junior champs Alexa

## Outcome
_Pending — will be updated when market resolves_

---
*Mode: LIVE | DRY_RUN: true*