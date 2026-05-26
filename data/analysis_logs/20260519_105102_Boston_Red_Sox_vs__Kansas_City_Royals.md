# Market Analysis — 2026-05-19 10:51 UTC

## Market
- **Question:** Boston Red Sox vs. Kansas City Royals
- **Category:** sports
- **YES Price:** 54.0%
- **Days Left:** 7
- **Volume 24h:** $56,756
- **Liquidity:** $50,989

## Statistical Prior
- **p_base:** 56.0%
- **Source:** logistic:sports
- **N (historical):** 6077
- **Raw gap:** 2.0%

## News Sources Fetched
### Macro Context
- Fear&Greed: 25/100 (Extreme Fear) | trend: deteriorating
- BTC: $76,710 (-0.2% 24h) → neutral
- Fear&Greed: 25/100 (Extreme Fear) | 7d trend: deteriorating
- BTC: $76,710 (-0.0% 24h) → neutral

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
- → Here's how to watch Tuesday's Kansas City Royals vs Boston Red Sox game, including start times, TV channels, scores and how to stream.
- [Tue, 19 May 2026] Where to watch Boston Red Sox vs Kansas City Royals: TV channel, start time, streaming for May 19
- → On Monday, the Royals fell short in a 3-1 loss to the Boston Red Sox at Kauffman Stadium. It was their sixth loss in seven games. The Royals had the
- [Tue, 19 May 2026] Royals’ losing ways return in series-opening defeat against Red Sox: what happened
- → Boston Red Sox (20-27, fifth in the AL East) vs. Kansas City Royals (20-28, fifth in the AL Central) Kansas City, Missouri; Tuesday, 7:40 p.m. EDT P

## LLM Decision
- **Action:** SKIP
- **Confidence:** 55%
- **p_true:** 56.0%
- **Information Gap:** True
- **Crowd Bias:** False
- **Catalyst Type:** INJURY_NEWS
- **Catalyst Strength:** 0.60

### Reasoning
Conflicting signals: Stat signal (n=13,967) suggests YES overpriced at 54% (resolves YES only 44.7% historically), but Royals losing All-Star pitcher Bubic to IL should favor Red Sox. Gap only 2% (below 5% threshold), entry point 50-60% has weak 33% WR, and past decisions on this market were SKIP. Cannot determine clear edge.

## Gate Result
- **Passed:** ❌ NO
- **Reason:** no stat edge gap=2%<5%

## Tool Calls
- `get_sports_data({'sport': 'mlb', 'team': 'Red Sox'})` → INJURY [boston red sox] Ceddanne Rafaela (CF): Day-To-Day
INJURY [boston red sox] Carlos Narvaez (C)
- `get_odds({'sport': 'baseball_mlb', 'team': 'Red Sox'})` → Odds API error: 401 {"message":"Usage quota has been reached. See usage plans at https://the-odds-ap
- `get_market_context({'keyword': 'Red Sox Royals baseball'})` → No related markets found for 'Red Sox Royals baseball'
- `search_web({'query': 'Boston Red Sox Kansas City Royals game today lineup injuries'})` → [Mon, 18 May 2026] Google News
[Mon, 18 May 2026] Red Sox lineup: Recent call-up again starts over C
- `search_web({'query': 'MLB Red Sox vs Royals preview May 2025'})` → [Mon, 18 May 2026] Google News
[Mon, 18 May 2026] Red Sox vs Royals Prediction, Odds &amp; Player Pr
- `search_web({'query': 'Kansas City Royals All-Star pitcher injured list Red Sox series'})` → [Mon, 18 May 2026] Google News
[Mon, 18 May 2026] Royals place All-Star pitcher on injured list ahea
- `search_web({'query': 'Royals starting pitcher injury May 2025 rotation'})` → [Mon, 18 May 2026] Google News
[Wed, 13 May 2026] Royals' Kris Bubic placed on 15-day injured list w

## Outcome
_Pending — will be updated when market resolves_

---
*Mode: LIVE | DRY_RUN: true*