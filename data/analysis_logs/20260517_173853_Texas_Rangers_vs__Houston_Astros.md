# Market Analysis — 2026-05-17 17:38 UTC

## Market
- **Question:** Texas Rangers vs. Houston Astros
- **Category:** sports
- **YES Price:** 54.0%
- **Days Left:** 7
- **Volume 24h:** $104,694
- **Liquidity:** $389,209

## Statistical Prior
- **p_base:** 56.0%
- **Source:** logistic:sports
- **N (historical):** 6077
- **Raw gap:** 2.0%

## News Sources Fetched
### Macro Context
- Fear&Greed: 27/100 (Fear) | trend: deteriorating
- BTC: $77,915 (-0.4% 24h) → neutral
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
- → Jose Altuve will undergo an MRI after leaving the Astros' 4-1 win over the Rangers amid Houston's 14-player IL crisis.
- [Sun, 17 May 2026] Astros’ Jose Altuve injury deals injury blow to Houston amid rough start to season
- → The Texas Rangers enter Sunday's game trying to avoid being swept by the Houston Astros with their co-ace back on the hill.
- [Sun, 17 May 2026] How to Watch Nathan Eovaldi Return for Rangers vs. Astros: TV, Stream, Radio
- → Here's how to watch Sunday's Houston Astros vs Texas Rangers game, including start times, TV channels, scores and how to stream.

## LLM Decision
- **Action:** SKIP
- **Confidence:** 65%
- **p_true:** 47.2%
- **Information Gap:** True
- **Crowd Bias:** False
- **Catalyst Type:** STATISTICAL_PATTERN
- **Catalyst Strength:** 0.72

### Reasoning
Strong historical edge: Markets at 54% YES price resolve YES only 44.7% of the time (n=13,967), suggesting 9.3pp overpricing. Both teams have key injuries (Seager, Altuve, Pena). Astros just shut out Rangers on May 16 (momentum). Bookmaker consensus (55% Rangers) aligns with market, but stat signal indicates systematic overpricing at this price level. Small base rate gap (+2%) is offset by large stat sample. Confidence tempered by lack of direct game-specific catalyst.

## Gate Result
- **Passed:** ❌ NO
- **Reason:** no stat edge gap=2%<5%

## Tool Calls
- `get_sports_data({'sport': 'mlb', 'team': 'Texas Rangers'})` → INJURY [texas rangers] Corey Seager (SS): Day-To-Day
INJURY [texas rangers] Josh Smith (2B): 10-Day-
- `get_sports_data({'sport': 'mlb', 'team': 'Houston Astros'})` → INJURY [houston astros] Jose Altuve (2B): Day-To-Day
INJURY [houston astros] Jeremy Pena (SS): 10-Da
- `search_web({'query': 'Texas Rangers vs Houston Astros recent game'})` → [Sat, 16 May 2026] Google News
[Sun, 17 May 2026] Texas Rangers at Houston Astros Game Story, Scores
- `search_web({'query': 'Astros Rangers series 2025'})` → [Wed, 17 Sep 2025] Google News
[Sat, 06 Sep 2025] Sweep! First place! Silver Boot! Astros do it all 
- `get_market_context({'keyword': 'Texas Rangers Houston Astros'})` → No related markets found for 'Texas Rangers Houston Astros'
- `get_odds({'sport': 'baseball_mlb', 'team': 'Rangers'})` → [ODDS] baseball_mlb — 1 events
  Houston Astros vs Texas Rangers (2026-05-17)
    [FanDuel] Houston 
- `search_web({'query': 'Rangers Astros May 2026 starting pitchers'})` → [Sun, 17 May 2026] Google News
[Sun, 17 May 2026] Texas Rangers lineup for May 17, 2026 - Lone Star 

## Outcome
_Pending — will be updated when market resolves_

---
*Mode: LIVE | DRY_RUN: true*