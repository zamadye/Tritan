# Market Analysis — 2026-05-17 17:03 UTC

## Market
- **Question:** Texas Rangers vs. Houston Astros
- **Category:** sports
- **YES Price:** 54.0%
- **Days Left:** 7
- **Volume 24h:** $98,970
- **Liquidity:** $391,063

## Statistical Prior
- **p_base:** 56.0%
- **Source:** logistic:sports
- **N (historical):** 6077
- **Raw gap:** 2.0%

## News Sources Fetched
### Macro Context
- Fear&Greed: 27/100 (Fear) | trend: deteriorating
- BTC: $78,015 (-0.2% 24h) → neutral
- Fear&Greed: 27/100 (Fear) | 7d trend: deteriorating
- BTC: $78,071 (-0.1% 24h) → neutral

### General
- [FEAR&GREED 7d trend] 27(Fear) → 31(Fear) → 43(Fear) → 34(Fear) | sentiment worsening
- [SPORTS] Recent games:
- TEX @ HOU | Scheduled | Houston Astros(home) 19-28 score:0 vs Texas Rangers(away) 21-24 score:0
- [SPORTS] Injuries:
- ?: Pavin Smith — 60-Day-IL (Surgery)
- ?: Carlos Santana — 10-Day-IL (Strain)
- ?: Jordan Lawlar — 60-Day-IL (Fracture)
- ?: Denzel Clarke — 10-Day-IL (Bruise)

### Multi-Source
- [MULTI-SOURCE NEWS] 2 sources for: texas rangers houston astros
- [Bing News]
- [Sun, 17 May 2026] texas rangers houston astros
- → Jose Altuve will undergo an MRI after leaving the Astros' 4-1 win over the Rangers amid Houston's 14-player IL crisis.
- [Sun, 17 May 2026] Astros’ Jose Altuve injury deals injury blow to Houston amid rough start to season
- → Here's how to watch Sunday's Houston Astros vs Texas Rangers game, including start times, TV channels, scores and how to stream.
- [Sun, 17 May 2026] Where to watch Texas Rangers vs Houston Astros: TV channel, start time, streaming for May 17
- → View the Texas Rangers vs. Houston Astros game played on May 17, 2026. Box score, stats, play-by-play timeline, highlights, odds &amp; more ...

## LLM Decision
- **Action:** SKIP
- **Confidence:** 65%
- **p_true:** 48.0%
- **Information Gap:** True
- **Crowd Bias:** False
- **Catalyst Type:** STATISTICAL_HISTORICAL_PATTERN
- **Catalyst Strength:** 0.70

### Reasoning
Stat signal with large sample (n=13,967) shows markets at 54% YES historically resolve YES only 44.7% of time, creating ~9.3% edge for NO. Both teams have significant injuries (Seager D2D for Rangers; Altuve D2D, Pena IL for Astros) — roughly neutral impact. No bookmaker odds available to cross-reference, but the systematic overpricing pattern is strong. Market is pricing Rangers at 54% but historical resolution suggests true probability is ~45%.

## Gate Result
- **Passed:** ❌ NO
- **Reason:** no stat edge gap=2%<5%

## Tool Calls
- `get_sports_data({'sport': 'mlb', 'team': 'Texas Rangers'})` → INJURY [texas rangers] Corey Seager (SS): Day-To-Day
INJURY [texas rangers] Josh Smith (2B): 10-Day-
- `get_sports_data({'sport': 'mlb', 'team': 'Houston Astros'})` → INJURY [houston astros] Jose Altuve (2B): Day-To-Day
INJURY [houston astros] Jeremy Pena (SS): 10-Da
- `get_odds({'sport': 'baseball_mlb', 'team': 'Rangers Astros'})` → [ODDS] baseball_mlb — 0 events
- `search_web({'query': 'Texas Rangers vs Houston Astros 2025 MLB matchup preview'})` → [Sat, 16 May 2026] Google News
[Sun, 10 May 2026] Rangers vs Astros Prediction, Odds, Moneyline, Spr
- `search_web({'query': 'Houston Astros Texas Rangers recent game results May 2025'})` → [Wed, 18 Mar 2026] Google News
[Tue, 16 Sep 2025] Houston Astros vs. Texas Rangers: Upcoming Series 
- `get_market_context({'keyword': 'Texas Rangers Houston Astros'})` → No related markets found for 'Texas Rangers Houston Astros'
- `search_web({'query': '"Texas Rangers" win probability starting pitcher May 2025'})` → [Sun, 17 May 2026] Google News
[Tue, 05 May 2026] Texas Rangers Odds &amp; Betting Lines - Action Ne

## Outcome
_Pending — will be updated when market resolves_

---
*Mode: LIVE | DRY_RUN: true*