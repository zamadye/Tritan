# Market Analysis — 2026-05-17 17:26 UTC

## Market
- **Question:** Texas Rangers vs. Houston Astros
- **Category:** sports
- **YES Price:** 54.0%
- **Days Left:** 7
- **Volume 24h:** $104,300
- **Liquidity:** $399,074

## Statistical Prior
- **p_base:** 56.0%
- **Source:** logistic:sports
- **N (historical):** 6077
- **Raw gap:** 2.0%

## News Sources Fetched
### Macro Context
- Fear&Greed: 27/100 (Fear) | trend: deteriorating
- BTC: $77,924 (-0.4% 24h) → neutral
- Fear&Greed: 27/100 (Fear) | 7d trend: deteriorating
- BTC: $77,943 (-0.4% 24h) → neutral

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
- → Here's how to watch Sunday's Houston Astros vs Texas Rangers game, including start times, TV channels, scores and how to stream.
- [Sun, 17 May 2026] Where to watch Texas Rangers vs Houston Astros: TV channel, start time, streaming for May 17
- → Jose Altuve will undergo an MRI after leaving the Astros' 4-1 win over the Rangers amid Houston's 14-player IL crisis.
- [Sun, 17 May 2026] Astros’ Jose Altuve injury deals injury blow to Houston amid rough start to season
- → View the Texas Rangers vs. Houston Astros game played on May 17, 2026. Box score, stats, play-by-play timeline, highlights, odds &amp; more ...

## LLM Decision
- **Action:** SKIP
- **Confidence:** 62%
- **p_true:** 56.0%
- **Information Gap:** False
- **Crowd Bias:** False
- **Catalyst Type:** INJURY_NEWS
- **Catalyst Strength:** 0.45

### Reasoning
Mixed signals: Stat signal (n=13,967) suggests markets at 54% overprice YES (44.7% historical resolution), but concrete injury information favors Rangers (Altuve left game injured today, Pena/Hader also out). Bookmakers have Rangers at 55-56%, slightly above market price. Gap too small (+2%) for confident action. Injury catalyst partially priced in, generic stat pattern may not apply to this specific sports context. Past decisions on same market also skipped.

## Gate Result
- **Passed:** ❌ NO
- **Reason:** no stat edge gap=2%<5%

## Tool Calls
- `get_sports_data({'sport': 'mlb', 'team': 'Texas Rangers'})` → INJURY [texas rangers] Corey Seager (SS): Day-To-Day
INJURY [texas rangers] Josh Smith (2B): 10-Day-
- `get_sports_data({'sport': 'mlb', 'team': 'Houston Astros'})` → INJURY [houston astros] Jose Altuve (2B): Day-To-Day
INJURY [houston astros] Jeremy Pena (SS): 10-Da
- `search_web({'query': 'Texas Rangers vs Houston Astros game today injury report'})` → [Sun, 17 May 2026] Google News
[Sun, 17 May 2026] Rangers vs. Astros (May 17, 2026) Live Score - ESP
- `search_web({'query': 'MLB Texas Rangers Houston Astros recent results May 2025'})` → [Sat, 16 May 2026] Google News
[Wed, 18 Mar 2026] Texas Rangers at Houston Astros Game Story, Scores
- `get_odds({'sport': 'baseball_mlb', 'team': 'Rangers'})` → [ODDS] baseball_mlb — 1 events
  Houston Astros vs Texas Rangers (2026-05-17)
    [FanDuel] Houston 
- `get_market_context({'keyword': 'Texas Rangers'})` → No related markets found for 'Texas Rangers'
- `search_web({'query': 'Jose Altuve injury update Astros May 2026'})` → [Sun, 17 May 2026] Google News
[Sun, 17 May 2026] Jose Altuve's injury may not be as disastrous as s
- `get_market_context({'keyword': 'Astros Rangers'})` → No related markets found for 'Astros Rangers'

## Outcome
_Pending — will be updated when market resolves_

---
*Mode: LIVE | DRY_RUN: true*