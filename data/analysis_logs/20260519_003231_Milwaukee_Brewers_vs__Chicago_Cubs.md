# Market Analysis — 2026-05-19 00:32 UTC

## Market
- **Question:** Milwaukee Brewers vs. Chicago Cubs
- **Category:** sports
- **YES Price:** 59.0%
- **Days Left:** 6
- **Volume 24h:** $92,119
- **Liquidity:** $38,623

## Statistical Prior
- **p_base:** 63.3%
- **Source:** logistic:sports
- **N (historical):** 6077
- **Raw gap:** 4.3%

## News Sources Fetched
### Macro Context
- Fear&Greed: 25/100 (Extreme Fear) | trend: deteriorating
- BTC: $77,194 (+0.1% 24h) → neutral
- Fear&Greed: 25/100 (Extreme Fear) | 7d trend: deteriorating
- BTC: $77,054 (-0.2% 24h) → neutral

### General
- [FEAR&GREED 7d trend] 25(Extr) → 28(Fear) → 27(Fear) → 31(Fear) | sentiment worsening
- [SPORTS] Recent games:
- MIL @ CHC | In Progress | Chicago Cubs(home) 29-18 score:0 vs Milwaukee Brewers(away) 26-18 score:1
- [SPORTS] Injuries:
- ?: A.J. Puk — 60-Day-IL (Surgery)
- ?: Jordan Lawlar — 60-Day-IL (Fracture)
- ?: Pavin Smith — 60-Day-IL (Surgery)
- ?: Jacob Wilson — 10-Day-IL (Dislocated)

### Multi-Source
- [MULTI-SOURCE NEWS] 2 sources for: milwaukee brewers chicago cubs
- [Bing News]
- [Mon, 18 May 2026] milwaukee brewers chicago cubs
- → The Brewers and Cubs square off for the first time in 2026 on Monday night at Wrigley Field.
- [Mon, 18 May 2026] Brewers 1, Cubs 0: Christian Yelich crushes one
- → The Cubs open a three-game set against their I-94 rivals.
- [Mon, 18 May 2026] Chicago Cubs vs. Milwaukee Brewers preview, Monday 5/18, 6:40 CT
- → The Milwaukee Brewers visit the Chicago Cubs Monday at 7:40 p.m. ET as the NL Central rivals swing into a 3-game series in Chicago, Illinois.

## LLM Decision
- **Action:** SKIP
- **Confidence:** 0%
- **p_true:** 63.3%
- **Information Gap:** False
- **Crowd Bias:** False
- **Catalyst Type:** NONE
- **Catalyst Strength:** 0.00

### Reasoning


## Gate Result
- **Passed:** ❌ NO
- **Reason:** no stat edge gap=4%<5%

## Tool Calls
- `get_sports_data({'sport': 'mlb', 'team': 'Milwaukee Brewers'})` → INJURY [milwaukee brewers] Brandon Woodruff (SP): 15-Day-IL
INJURY [milwaukee brewers] Akil Baddoo (
- `get_sports_data({'sport': 'mlb', 'team': 'Chicago Cubs'})` → INJURY [chicago cubs] Hunter Harvey (RP): 60-Day-IL
INJURY [chicago cubs] Matthew Boyd (SP): 15-Day-
- `search_web({'query': 'Milwaukee Brewers vs Chicago Cubs 2025 series schedule'})` → [Wed, 08 Oct 2025] Google News
[Fri, 03 Oct 2025] Milwaukee Brewers at Chicago Cubs Preview - 10/08/
- `search_web({'query': 'Cubs Brewers head to head 2025'})` → [Mon, 18 May 2026] Google News
[Mon, 13 Oct 2025] Not to worry, there are more rivalries on tap this
- `get_market_context({'keyword': 'Milwaukee Brewers Chicago Cubs'})` → No related markets found for 'Milwaukee Brewers Chicago Cubs'
- `get_market_context({'keyword': 'Brewers Cubs'})` → No related markets found for 'Brewers Cubs'
- `get_odds({'sport': 'baseball_mlb', 'team': 'Brewers'})` → Odds API error: 401 {"message":"Usage quota has been reached. See usage plans at https://the-odds-ap
- `search_web({'query': 'Milwaukee Brewers vs Chicago Cubs NLDS odds 2025'})` → [Sat, 11 Oct 2025] Google News
[Fri, 03 Oct 2025] Brewers vs. Cubs NLDS Game 5 Prediction, Odds, Pic
- `search_web({'query': 'Brewers Cubs series odds betting lines October 2025'})` → [Sat, 11 Oct 2025] Google News
[Sat, 11 Oct 2025] Brewers vs. Cubs NLDS Game 5 Prediction, Odds, Pic

## Outcome
_Pending — will be updated when market resolves_

---
*Mode: LIVE | DRY_RUN: true*