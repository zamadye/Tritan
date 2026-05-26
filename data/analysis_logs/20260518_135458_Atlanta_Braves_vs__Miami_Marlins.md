# Market Analysis — 2026-05-18 13:54 UTC

## Market
- **Question:** Atlanta Braves vs. Miami Marlins
- **Category:** sports
- **YES Price:** 49.5%
- **Days Left:** 7
- **Volume 24h:** $110,729
- **Liquidity:** $221,442

## Statistical Prior
- **p_base:** 49.2%
- **Source:** logistic:sports
- **N (historical):** 6077
- **Raw gap:** 0.3%

## News Sources Fetched
### Macro Context
- Fear&Greed: 28/100 (Fear) | trend: deteriorating
- BTC: $76,916 (-1.7% 24h) → risk-OFF
- Fear&Greed: 28/100 (Fear) | 7d trend: deteriorating
- BTC: $77,304 (-1.2% 24h) → risk-OFF
- Fed market expectations:

### General
- [FEAR&GREED 7d trend] 28(Fear) → 27(Fear) → 31(Fear) → 43(Fear) | sentiment worsening
- Will the Fed increase interest rates by 25 bps after the Jun → YES=50%
- [SPORTS] Recent games:
- MIA @ TB | Final | Tampa Bay Rays(home) 30-15 score:6 vs Miami Marlins(away) 21-26 score:3
- BOS @ ATL | Final | Atlanta Braves(home) 32-15 score:8 vs Boston Red Sox(away) 19-27 score:1
- [SPORTS] Injuries:
- ?: Pavin Smith — 60-Day-IL (Surgery)
- ?: Carlos Santana — 10-Day-IL (Strain)

### Multi-Source
- [MULTI-SOURCE NEWS] 2 sources for: atlanta braves miami marlins
- [Bing News]
- [Mon, 18 May 2026] atlanta braves miami marlins
- → Here's how to watch Monday's Miami Marlins vs Atlanta Braves game, including start times, TV channels, scores and how to stream.
- [Mon, 18 May 2026] Where to watch Atlanta Braves vs Miami Marlins: TV channel, start time, streaming for May 18
- → The Miami Marlins are in need of a momentum boost against the Atlanta Braves.
- [Mon, 18 May 2026] Marlins announce pitching probables for crucial series vs. Braves
- → Here is your TV guide for the upcoming NL East slate between the Atlanta Braves and the Miami Marlins ...

## LLM Decision
- **Action:** SKIP
- **Confidence:** 50%
- **p_true:** 49.2%
- **Information Gap:** False
- **Crowd Bias:** False
- **Catalyst Type:** NONE
- **Catalyst Strength:** 0.00

### Reasoning
No statistical edge exists. The gap is -0% (market 50% vs base rate 49%), falling far below the required 5% threshold. Both teams have significant injuries (Braves missing Acuna Jr.; Marlins missing pitching depth) that roughly cancel each other out. Historical data shows YES at 51% resolves YES only 44.7% of the time (n=13,967), suggesting slight YES overpricing, but the 0% gap is insufficient to act. Past decisions on this exact market were SKIP for the same reason. Pattern data confirms no-gap trades have only 50% WR and entry at 40-50% has poor 33% WR. No breaking news or direct catalyst identified. Macro fear environment doesn't affect sports outcomes.

## Gate Result
- **Passed:** ❌ NO
- **Reason:** no stat edge gap=0%<5%

## Tool Calls
- `get_sports_data({'sport': 'mlb', 'team': 'Atlanta Braves'})` → INJURY [atlanta braves] Eli White (CF): 7-Day IL
INJURY [atlanta braves] Ronald Acuna Jr. (RF): 10-D
- `get_sports_data({'sport': 'mlb', 'team': 'Miami Marlins'})` → INJURY [miami marlins] Robby Snelling (SP): 15-Day-IL
INJURY [miami marlins] Ronny Henriquez (RP): 6
- `search_web({'query': 'Atlanta Braves vs Miami Marlins May 2025 series preview'})` → [Mon, 18 May 2026] Google News
[Sat, 16 May 2026] Reason Ronald Acuña Jr. Likely Won't Play vs. Marl
- `search_web({'query': 'Braves Marlins injuries news 2025'})` → [Mon, 18 May 2026] Google News
[Fri, 15 May 2026] Marlins vs. Braves: Injury Report, Updates &amp; P
- `get_market_context({'keyword': 'Braves'})` → No related markets found for 'Braves'
- `get_market_context({'keyword': 'Marlins'})` → No related markets found for 'Marlins'
- `get_market_context({'keyword': 'baseball'})` → No related markets found for 'baseball'

## Outcome
_Pending — will be updated when market resolves_

---
*Mode: LIVE | DRY_RUN: true*