# Market Analysis — 2026-05-19 01:28 UTC

## Market
- **Question:** Geneva Open: Adrian Mannarino vs Raphael Collignon
- **Category:** sports
- **YES Price:** 12.0%
- **Days Left:** 6
- **Volume 24h:** $69,237
- **Liquidity:** $26,045

## Statistical Prior
- **p_base:** 4.8%
- **Source:** logistic:sports
- **N (historical):** 6077
- **Raw gap:** 7.2%

## News Sources Fetched
### Macro Context
- Fear&Greed: 25/100 (Extreme Fear) | trend: deteriorating
- BTC: $77,024 (+0.1% 24h) → neutral
- Fear&Greed: 25/100 (Extreme Fear) | 7d trend: deteriorating
- BTC: $76,830 (-0.1% 24h) → neutral

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
- **Confidence:** 38%
- **p_true:** 5.0%
- **Information Gap:** False
- **Crowd Bias:** False
- **Catalyst Type:** NONE
- **Catalyst Strength:** 0.10

### Reasoning
No actionable edge found. Mannarino had a disastrous 2026 season (first win only in May at Houston) and faces clay court disadvantage against rising Belgian Collignon who recently beat Ruud. YES at 12% already trades 7 points ABOVE the 5% base rate, suggesting crowd is overpricing YES, not underpricing. No injury news, no form catalyst, no concrete evidence to justify a bet. Previous two analyses on this exact market both concluded SKIP. Confirmed SKIP: insufficient information and no verifiable catalyst.

## Gate Result
- **Passed:** ❌ NO
- **Reason:** low conf 38%<52%

## Tool Calls
- `get_sports_data({'sport': 'tennis', 'team': 'Mannarino'})` → No injury data found for tennis Mannarino
- `get_sports_data({'sport': 'tennis', 'team': 'Collignon'})` → No injury data found for tennis Collignon
- `get_market_context({'keyword': 'Geneva Open Mannarino'})` → No related markets found for 'Geneva Open Mannarino'
- `search_web({'query': 'Adrian Mannarino 2025 form results tennis'})` → [Fri, 26 Sep 2025] Google News
[Fri, 29 Aug 2025] Highlights: Mannarino snaps in-form Bublik's strea
- `search_web({'query': 'Raphael Collignon tennis 2025 results form'})` → [Fri, 29 Aug 2025] Google News
[Tue, 03 Mar 2026] Brain surgeon’s son Collignon on finding the menta
- `search_web({'query': 'Geneva Open 2025 tennis draw predictions'})` → [Sat, 16 May 2026] Google News
[Sun, 17 May 2026] Geneva Open 2026: Draw, Schedule, Entry List, Priz
- `search_web({'query': 'Mannarino Collignon head to head tennis record'})` → [Mon, 18 May 2026] Google News
[Thu, 19 Mar 2026] ATP Geneva Day 3 Predictions Including Casper Ruud
- `search_web({'query': 'Mannarino ranking 2026 recent losses clay court'})` → [Sat, 04 Apr 2026] Google News
[Wed, 09 Jul 2025] 2026 Rolex Monte-Carlo Masters: Bergs [46th] vs. M
- `search_web({'query': 'Tennis Tonic Mannarino vs Collignon Geneva 2026 prediction odds'})` → [Mon, 18 May 2026] Google News
[Mon, 18 May 2026] H2H, prediction of Adrian Mannarino vs Raphael Col
- `search_web({'query': 'Raphael Collignon ATP ranking 2026 clay court form'})` → [Mon, 18 May 2026] Google News
[Sun, 17 May 2026] ATP Geneva Day 3 Predictions Including Casper Ruud
- `get_odds({'sport': 'tennis_atp', 'team': 'Mannarino'})` → Odds API error: 404 {"message":"Unknown sport","error_code":"UNKNOWN_SPORT","details_url":"https://t
- `search_web({'query': 'Mannarino vs Collignon Geneva Open odds betting lines May 2026'})` → [Sat, 16 May 2026] Google News
[Sun, 17 May 2026] Adrian Mannarino vs. Raphael Collignon prediction,
- `search_web({'query': 'dimers.com Mannarino Collignon odds Geneva Open prediction pick'})` → [Sat, 16 May 2026] Google News
[Sat, 16 May 2026] Adrian Mannarino vs. Raphael Collignon prediction,

## Outcome
_Pending — will be updated when market resolves_

---
*Mode: LIVE | DRY_RUN: true*