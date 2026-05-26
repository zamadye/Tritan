# Market Analysis — 2026-05-18 13:14 UTC

## Market
- **Question:** Geneva Open: Adrian Mannarino vs Raphael Collignon
- **Category:** sports
- **YES Price:** 11.0%
- **Days Left:** 6
- **Volume 24h:** $84,205
- **Liquidity:** $15,546

## Statistical Prior
- **p_base:** 4.2%
- **Source:** logistic:sports
- **N (historical):** 6077
- **Raw gap:** 6.8%

## News Sources Fetched
### Macro Context
- Fear&Greed: 28/100 (Fear) | trend: deteriorating
- BTC: $77,574 (-1.0% 24h) → neutral
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
- **Confidence:** 40%
- **p_true:** 5.0%
- **Information Gap:** False
- **Crowd Bias:** False
- **Catalyst Type:** NONE
- **Catalyst Strength:** 0.10

### Reasoning
YES price (11%) already trades 7 points ABOVE historical base rate (4%), suggesting market has incorporated available information. Previous decisions on identical market also correctly identified overpricing. Mannarino is historically poor on clay, but no fresh catalyst found to justify the elevated YES price. Market appears efficiently priced with no verifiable edge.

## Gate Result
- **Passed:** ❌ NO
- **Reason:** low conf 40%<52%

## Tool Calls
- `get_sports_data({'sport': 'tennis', 'team': 'Mannarino'})` → No injury data found for tennis Mannarino
- `get_odds({'sport': 'tennis_atp_italian_open', 'team': 'Mannarino'})` → Odds API error: 401 {"message":"Usage quota has been reached. See usage plans at https://the-odds-ap
- `search_web({'query': 'Geneva Open 2025 Adrian Mannarino vs Raphael Collignon odds'})` → [Sun, 17 May 2026] Google News
[Sun, 17 May 2026] Mannarino vs. Collignon Prediction at the Gonet Ge
- `search_web({'query': 'Adrian Mannarino recent results 2025 form tennis'})` → [Fri, 26 Sep 2025] Google News
[Tue, 17 Mar 2026] Zverev, De Minaur among Turin contenders to advanc
- `search_web({'query': 'Raphael Collignon tennis ranking form 2025'})` → [Tue, 18 Nov 2025] Google News
[Fri, 21 Nov 2025] Bergs, Collignon fire Belgium to victory against F
- `get_market_context({'keyword': 'Mannarino'})` → No related markets found for 'Mannarino'
- `search_web({'query': 'Mannarino vs Collignon head to head record ATP'})` → [Thu, 19 Mar 2026] Google News
[Tue, 03 Mar 2026] ATP Miami Day 3 Predictions Including Tommy Paul v
- `search_web({'query': 'Mannarino ranking 2025 clay court record'})` → [Fri, 29 Aug 2025] Google News
[Mon, 07 Apr 2025] Tennis, ATP – US Open 2025: Mannarino eliminates S
- `search_web({'query': '"Geneva Open" "Mannarino vs Collignon" prediction odds 2025'})` → [Sun, 17 May 2026] Google News
[] Mannarino vs. Collignon Prediction at the Gonet Geneva Open – Mond
- `search_web({'query': 'Raphael Collignon Geneva Open 2025 draw'})` → [Sun, 17 May 2026] Google News
[Sat, 16 May 2026] ATP tennis Hamburg and Geneva previews, picks, and
- `search_web({'query': 'Mannarino ATP ranking May 2026'})` → [Tue, 12 Aug 2025] Google News
[Wed, 04 Feb 2026] ATP: Unseeded trio bring French flair to Cincy - R
- `search_web({'query': 'Collignon ATP ranking May 2026'})` → [Tue, 20 Jan 2026] Google News
[Mon, 23 Feb 2026] Tennis, ATP – Australian Open 2026: Musetti downs 
- `search_web({'query': 'Geneva Open 2026 first round results today'})` → [Sun, 17 May 2026] Google News
[Mon, 18 May 2026] Hamburg Open 2026: All matches, live scores and ho
- `search_web({'query': '"Mannarino" "Collignon" Geneva Open 2026 prediction'})` → [Sun, 17 May 2026] Google News
[Sat, 16 May 2026] Mannarino vs. Collignon Prediction at the Gonet Ge
- `search_web({'query': 'Mannarino clay court 2026 win loss record'})` → [Mon, 06 Apr 2026] Google News
[Wed, 04 Feb 2026] The fact that confirms the total divorce between M

## Outcome
_Pending — will be updated when market resolves_

---
*Mode: LIVE | DRY_RUN: true*