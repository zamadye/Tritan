# Market Analysis — 2026-05-19 11:52 UTC

## Market
- **Question:** Boston Red Sox vs. Kansas City Royals
- **Category:** sports
- **YES Price:** 55.0%
- **Days Left:** 7
- **Volume 24h:** $59,400
- **Liquidity:** $107,166

## Statistical Prior
- **p_base:** 57.5%
- **Source:** logistic:sports
- **N (historical):** 6077
- **Raw gap:** 2.5%

## News Sources Fetched
### Macro Context
- Fear&Greed: 25/100 (Extreme Fear) | trend: deteriorating
- BTC: $76,632 (-0.8% 24h) → neutral
- Fear&Greed: 25/100 (Extreme Fear) | 7d trend: deteriorating
- BTC: $76,815 (-0.1% 24h) → neutral

### General
- [FEAR&GREED 7d trend] 25(Extr) → 28(Fear) → 27(Fear) → 31(Fear) | sentiment worsening
- [SPORTS] Recent games:
- BOS @ KC | Final | Kansas City Royals(home) 20-28 score:1 vs Boston Red Sox(away) 20-27 score:3
- [SPORTS] Injuries:
- ?: James McCann — Out (Strain)
- ?: A.J. Puk — 60-Day-IL (Surgery)
- ?: Jordan Lawlar — 60-Day-IL (Fracture)
- ?: Jacob Wilson — 10-Day-IL (Dislocated)

### Multi-Source
- [MULTI-SOURCE NEWS] 2 sources for: boston kansas city royals
- [Bing News]
- [Tue, 19 May 2026] boston kansas city royals
- → On Monday, the Royals fell short in a 3-1 loss to the Boston Red Sox at Kauffman Stadium. It was their sixth loss in seven games. The Royals had the
- [Tue, 19 May 2026] Royals’ losing ways return in series-opening defeat against Red Sox: what happened
- → Boston Red Sox (20-27, fifth in the AL East) vs. Kansas City Royals (20-28, fifth in the AL Central) Kansas City, Missouri; Tuesday, 7:40 p.m. EDT. 
- [Tue, 19 May 2026] Red Sox face the Royals with 1-0 series lead
- → Here's how to watch Tuesday's Kansas City Royals vs Boston Red Sox game, including start times, TV channels, scores and how to stream.

## LLM Decision
- **Action:** SKIP
- **Confidence:** 62%
- **p_true:** 57.5%
- **Information Gap:** False
- **Crowd Bias:** False
- **Catalyst Type:** NONE
- **Catalyst Strength:** 0.10

### Reasoning
Stat signal (n=13,967) clearly indicates YES overpriced at 55% (true ~44.7%), but no concrete catalyst exists to drive resolution. Gap (+2%) fails the 5% gate threshold. Entry 50-60% zone has weak historical WR (33%). While the statistical edge is real, absence of a direct catalyst means we're betting against crowd bias without a specific trigger - too passive for high-confidence action.

## Gate Result
- **Passed:** ❌ NO
- **Reason:** no stat edge gap=2%<5%

## Tool Calls
- `get_sports_data({'sport': 'mlb', 'team': 'Red Sox'})` → INJURY [boston red sox] Ceddanne Rafaela (CF): Day-To-Day
INJURY [boston red sox] Carlos Narvaez (C)
- `get_odds({'sport': 'baseball_mlb', 'team': 'Red Sox'})` → Odds API error: 401 {"message":"Usage quota has been reached. See usage plans at https://the-odds-ap
- `get_market_context({'keyword': 'Boston Red Sox Kansas City Royals'})` → No related markets found for 'Boston Red Sox Kansas City Royals'
- `search_web({'query': 'Boston Red Sox vs Kansas City Royals 2025 series preview'})` → [Mon, 18 May 2026] Google News
[Mon, 18 May 2026] Series Preview: Red Sox at Royals - Over the Monst
- `search_web({'query': 'Boston Red Sox recent results May 2025 record'})` → [Tue, 05 May 2026] Google News
[Mon, 18 Aug 2025] 2026 MLB Standings and Records: Spring Training - 
- `search_web({'query': 'Kansas City Royals injury report May 2025'})` → [Wed, 18 Feb 2026] Google News
[Mon, 19 Jan 2026] Injured Royals righty represents bigger blow to pi
- `search_web({'query': 'MLB standings May 2025 American League East Central'})` → [Sun, 28 Sep 2025] Google News
[Mon, 01 Sep 2025] 2025 MLB playoff picture: Final baseball standings

## Outcome
_Pending — will be updated when market resolves_

---
*Mode: LIVE | DRY_RUN: true*