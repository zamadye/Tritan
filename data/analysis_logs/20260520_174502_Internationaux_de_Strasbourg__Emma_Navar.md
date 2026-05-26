# Market Analysis — 2026-05-20 17:45 UTC

## Market
- **Question:** Internationaux de Strasbourg: Emma Navarro vs Iva Jovic
- **Category:** sports
- **YES Price:** 53.0%
- **Days Left:** 6
- **Volume 24h:** $403,264
- **Liquidity:** $97,039

## Statistical Prior
- **p_base:** 54.5%
- **Source:** logistic:sports
- **N (historical):** 6077
- **Raw gap:** 1.5%

## News Sources Fetched
### Macro Context
- Fear&Greed: 27/100 (Fear) | trend: deteriorating
- BTC: $77,523 (+0.9% 24h) → neutral
- Fear&Greed: 27/100 (Fear) | 7d trend: deteriorating
- BTC: $77,512 (+0.9% 24h) → neutral

### General
- [FEAR&GREED 7d trend] 27(Fear) → 25(Extr) → 28(Fear) → 27(Fear) | sentiment worsening

### Multi-Source
- [MULTI-SOURCE NEWS] 2 sources for: internationaux strasbourg: emma navarro jovic
- [Bing News]
- [Wed, 20 May 2026] internationaux strasbourg: emma navarro jovic
- → Emma Navarro seeks to rediscover form vs rising American Iva Jovic. Get draw, schedule, entry list, prize money and expert predictions.
- [Wed, 20 May 2026] LIVE Internationaux de Strasbourg Day Four | Navarro-Jovic headlines line-up in all American clash
- → Elite tennis action continues in full swing as Emma Navarro is set to go up against Iva Jovic in an all-American clash in the Round of 16 match at t
- [Fri, 15 May 2026] Tennis Picks Today: 5 Best Bets &amp; Predictions Ft. Emma Navarro vs Iva Jovic, Stan Wawrinka vs Alex Michelsen | May 20, 2026
- → The Internationaux de Strasbourg takes place between 17-23 May in a WTA 500 tournament prior to the French Open. Elena Rybakina is defending champio

## LLM Decision
- **Action:** SKIP
- **Confidence:** 45%
- **p_true:** 54.5%
- **Information Gap:** False
- **Crowd Bias:** False
- **Catalyst Type:** STATISTICAL_OVERPRICING
- **Catalyst Strength:** 0.35

### Reasoning
While statistical signal indicates market overprices YES (53% price vs 44.7% historical resolution rate, n=13,967), the gap between market price (53%) and base rate (54%) is only +1%, well below the 5% threshold required for action. Additionally, the 50-60% entry zone has historically performed poorly (33% win rate from 9 trades). No specific catalyst, injury, or head-to-head data found to support a clear edge. Similar Strasbourg markets (Navarro vs Raducanu) were previously skipped for same reason - insufficient gap despite statistical signal.

## Gate Result
- **Passed:** ❌ NO
- **Reason:** no stat edge gap=1%<5%

## Tool Calls
- `get_odds({'sport': 'tennis_atp', 'team': 'Navarro'})` → Odds API error: 404 {"message":"Unknown sport","error_code":"UNKNOWN_SPORT","details_url":"https://t
- `get_sports_data({'sport': 'nba'})` → INJURY [atlanta hawks] Keshon Gilbert (G): Out
INJURY [atlanta hawks] Jock Landale (C): Out
INJURY [
- `get_market_context({'keyword': 'tennis WTA Strasbourg'})` → No related markets found for 'tennis WTA Strasbourg'
- `search_web({'query': 'Emma Navarro vs Iva Jovic 2025 tennis match preview'})` → [Wed, 20 May 2026] Google News
[Wed, 20 May 2026] Tennis Picks Today: 5 Best Bets &amp; Predictions 
- `search_web({'query': 'Internationaux de Strasbourg 2025 tennis draw results'})` → [Wed, 20 May 2026] Google News
[Mon, 18 May 2026] The Official Home of the Women's Tennis Associatio
- `search_web({'query': 'Emma Navarro current form ranking 2025 results'})` → [Fri, 27 Feb 2026] Google News
[Fri, 27 Feb 2026] Emma Navarro’s 2026 season goes from bad to worse 
- `search_web({'query': 'Iva Jovic tennis 2025 season results ranking'})` → [Mon, 26 Jan 2026] Google News
[Fri, 26 Sep 2025] Australian Open 2026: Meet Iva Jovic the 'future n
- `search_web({'query': '"Emma Navarro" vs "Iva Jovic" head to head tennis 2026'})` → [Tue, 19 May 2026] Google News
[Sun, 04 Jan 2026] WTA Strasbourg Day 4 Predictions Including Emma Na
- `search_web({'query': 'WTA Strasbourg 2026 results round predictions'})` → [Wed, 20 May 2026] Google News
[Sun, 17 May 2026] Internationaux de Strasbourg 2026: Results, Draw, 
- `search_web({'query': 'Emma Navarro tennis 2026 season record form clay court'})` → [Tue, 19 May 2026] Google News
[Mon, 04 May 2026] WTA Strasbourg Day 4 Predictions Including Emma Na
- `search_web({'query': 'Iva Jovic tennis 2026 season record form results age'})` → [Sat, 24 Jan 2026] Google News
[Fri, 06 Mar 2026] Australian Open Day 8 order of play: Teenagers tak
- `search_web({'query': 'Emma Navarro WTA ranking May 2026 clay court results'})` → [Sun, 17 May 2026] Google News
[Thu, 30 Apr 2026] WTA Strasbourg Day 1 Predictions Including Sara Be
- `search_web({'query': 'Iva Jovic WTA ranking May 2026 Strasbourg'})` → [Wed, 20 May 2026] Google News
[Fri, 15 May 2026] WTA Strasbourg Best Bets Including Emma Navarro vs
- `search_web({'query': 'Emma Navarro ranking 2026 current position tennis'})` → [Mon, 05 Jan 2026] Google News
[Thu, 26 Mar 2026] Ranking the best American tennis players as 2026 b
- `search_web({'query': 'Iva Jovic ranking 2026 current position tennis teenager'})` → [Tue, 10 Mar 2026] Google News
[Sun, 18 Jan 2026] Interview: Ambitious Iva Jovic keen to cement her 
- `search_web({'query': '"Emma Navarro" vs "Iva Jovic" head to head record all matches'})` → [Tue, 19 May 2026] Google News
[Mon, 16 Feb 2026] WTA Strasbourg Day 4 Predictions Including Emma Na
- `search_web({'query': 'Navarro Jovic Strasbourg 2026 preview prediction odds'})` → [Wed, 20 May 2026] Google News
[Wed, 20 May 2026] Tennis Picks Today: 5 Best Bets &amp; Predictions 

## Outcome
**✅ WIN** | P&L: $+0.49 | Resolved: YES

---
*Mode: LIVE | DRY_RUN: true*