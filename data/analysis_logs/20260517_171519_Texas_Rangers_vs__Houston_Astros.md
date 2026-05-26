# Market Analysis — 2026-05-17 17:15 UTC

## Market
- **Question:** Texas Rangers vs. Houston Astros
- **Category:** sports
- **YES Price:** 54.0%
- **Days Left:** 7
- **Volume 24h:** $100,227
- **Liquidity:** $394,578

## Statistical Prior
- **p_base:** 56.0%
- **Source:** logistic:sports
- **N (historical):** 6077
- **Raw gap:** 2.0%

## News Sources Fetched
### Macro Context
- Fear&Greed: 27/100 (Fear) | trend: deteriorating
- BTC: $77,984 (-0.3% 24h) → neutral
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
- **Confidence:** 62%
- **p_true:** 56.0%
- **Information Gap:** False
- **Crowd Bias:** False
- **Catalyst Type:** SYSTEMATIC_MARKET_INEFFICIENCY
- **Catalyst Strength:** 0.40

### Reasoning
Stat signal with large sample (n=13,967) suggests markets at 54% overprice YES historically (44.7% resolution), but gap vs base rate is only +2% (below 5% gate threshold). Bookmaker odds align with market (~55% Rangers). No concrete catalyst or new injury information. Previous decisions for same market were SKIP. Systematic inefficiency exists but lacks actionable edge without catalyst or larger gap.

## Gate Result
- **Passed:** ❌ NO
- **Reason:** no stat edge gap=2%<5%

## Tool Calls
- `get_sports_data({'sport': 'mlb', 'team': 'Texas Rangers'})` → INJURY [texas rangers] Corey Seager (SS): Day-To-Day
INJURY [texas rangers] Josh Smith (2B): 10-Day-
- `search_web({'query': 'Texas Rangers vs Houston Astros recent game results 2025'})` → [Sat, 06 Sep 2025] Google News
[Tue, 16 Sep 2025] Houston Astros at Texas Rangers Game Story, Scores
- `search_web({'query': 'Texas Rangers Houston Astros series preview 2025'})` → [Sat, 06 Sep 2025] Google News
[Fri, 05 Sep 2025] Houston Astros at Texas Rangers Preview - 09/07/20
- `get_market_context({'keyword': 'Texas Rangers Houston Astros'})` → No related markets found for 'Texas Rangers Houston Astros'
- `get_market_context({'keyword': 'Rangers Astros MLB'})` → No related markets found for 'Rangers Astros MLB'
- `get_odds({'sport': 'baseball_mlb', 'team': 'Rangers'})` → [ODDS] baseball_mlb — 1 events
  Houston Astros vs Texas Rangers (2026-05-17)
    [FanDuel] Houston 
- `get_market_context({'keyword': 'MLB Texas'})` → No related markets found for 'MLB Texas'

## Outcome
_Pending — will be updated when market resolves_

---
*Mode: LIVE | DRY_RUN: true*