# Market Analysis — 2026-05-18 12:54 UTC

## Market
- **Question:** Geneva Open: Adrian Mannarino vs Raphael Collignon
- **Category:** sports
- **YES Price:** 12.0%
- **Days Left:** 6
- **Volume 24h:** $84,773
- **Liquidity:** $14,633

## Statistical Prior
- **p_base:** 4.8%
- **Source:** logistic:sports
- **N (historical):** 6077
- **Raw gap:** 7.2%

## News Sources Fetched
### Macro Context
- Fear&Greed: 28/100 (Fear) | trend: deteriorating
- BTC: $77,601 (-1.1% 24h) → risk-OFF
- Fear&Greed: 28/100 (Fear) | 7d trend: deteriorating
- BTC: $77,290 (-1.4% 24h) → risk-OFF
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
No verifiable edge found. YES price (12%) trades 7 points ABOVE historical base rate (5%), suggesting market has already incorporated information about this specific matchup. Mannarino is established ATP veteran with strong clay court credentials; Collignon is lower-ranked Belgian without clear upset indicators. No injury reports, form changes, or situational catalysts discovered to justify the premium pricing. Market appears efficient - cannot identify what the crowd is missing.

## Gate Result
- **Passed:** ❌ NO
- **Reason:** low conf 45%<52%

## Tool Calls
- `get_sports_data({'sport': 'tennis_atp', 'team': 'Mannarino Collignon'})` → No injury data found for tennis_atp Mannarino Collignon
- `search_web({'query': 'Adrian Mannarino vs Raphael Collignon Geneva Open 2024 recent form'})` → [Sun, 17 May 2026] Google News
[Sat, 22 Oct 2016] Mannarino vs. Collignon Prediction at the Gonet Ge
- `search_web({'query': 'Raphael Collignon tennis results 2024'})` → [Tue, 18 Nov 2025] Google News
[Wed, 22 Apr 2026] Tennis: Davis Cup Final 8 2025: Belgium scores 2–0
- `get_market_context({'keyword': 'Geneva Open tennis'})` → No related markets found for 'Geneva Open tennis'
- `get_odds({'sport': 'tennis_atp', 'team': 'Mannarino'})` → Odds API error: 404 {"message":"Unknown sport","error_code":"UNKNOWN_SPORT","details_url":"https://t
- `search_web({'query': 'Geneva Open 2024 draw Mannarino Collignon'})` → [Sat, 18 May 2019] Google News
[Sun, 19 Apr 2026] Geneva | Draws | ATP Tour | Tennis - ATP Tour
[Tue
- `search_web({'query': 'Adrian Mannarino 2024 season results ATP'})` → [Wed, 30 Jul 2025] Google News
[Sun, 08 Feb 2026] Shelton serves up Mannarino revenge in Toronto, Ru
- `search_web({'query': 'Raphael Collignon ATP ranking 2024 clay court results'})` → [Sun, 30 Nov 2025] Google News
[Fri, 10 Apr 2026] #NextGenATP stars Tien &amp; Fonseca spring bigges
- `search_web({'query': 'Adrian Mannarino clay court 2024 results recent form'})` → [Wed, 01 Apr 2026] Google News
[Mon, 13 Apr 2026] ATP Bucharest Day 3 Predictions Including Sebastia
- `search_web({'query': 'Mannarino vs Collignon head to head tennis'})` → [Sat, 16 May 2026] Google News
[Thu, 19 Mar 2026] Adrian Mannarino vs Raphael Collignon - Match ATP 
- `search_web({'query': 'Mannarino Collignon Geneva Open 2026 third round'})` → [Sat, 16 May 2026] Google News
[Sun, 17 May 2026] Adrian Mannarino vs Raphael Collignon - Match ATP 
- `search_web({'query': 'Adrian Mannarino form 2026 clay court season'})` → [Tue, 05 May 2026] Google News
[Tue, 10 Mar 2026] ATP Rome Best Bets Including Jenson Brooksby vs Se
- `search_web({'query': 'Raphael Collignon 2026 results form'})` → [Sat, 16 May 2026] Google News
[Thu, 14 May 2026] Adrian Mannarino v Raphael Collignon 18/05/2026, O
- `search_web({'query': '"Mannarino vs Collignon" prediction odds 2026'})` → [Sat, 16 May 2026] Google News
[Sun, 17 May 2026] Adrian Mannarino vs. Raphael Collignon prediction,
- `search_web({'query': 'Adrian Mannarino ATP ranking May 2026'})` → [Tue, 12 Aug 2025] Google News
[Mon, 08 Jan 2024] ATP: Unseeded trio bring French flair to Cincy - R
- `search_web({'query': 'Raphael Collignon ATP ranking May 2026'})` → [Mon, 23 Feb 2026] Google News
[Tue, 20 Jan 2026] Resurgent Luca Van Assche rides Play In Challenger
- `search_web({'query': 'dimers.com Mannarino Collignon prediction odds picks ATP Geneva Open 2026'})` → [Sat, 16 May 2026] Google News
[Sat, 16 May 2026] Adrian Mannarino vs. Raphael Collignon prediction,
- `search_web({'query': 'Bleacher Nation Mannarino Collignon prediction Gonet Geneva Open'})` → [Sun, 17 May 2026] Google News
[] Mannarino vs. Collignon Prediction at the Gonet Geneva Open – Mond
- `search_web({'query': '"Adrian Mannarino vs Raphael Collignon" prediction market polymarket'})` → [Sat, 16 May 2026] Google News
[] Adrian Mannarino vs. Raphael Collignon prediction, odds, picks for
- `search_web({'query': 'Geneva Open 2026 Mannarino Collignon match preview analysis'})` → [Sat, 16 May 2026] Google News
[Sun, 17 May 2026] Adrian Mannarino vs. Raphael Collignon prediction,

## Outcome
_Pending — will be updated when market resolves_

---
*Mode: LIVE | DRY_RUN: true*