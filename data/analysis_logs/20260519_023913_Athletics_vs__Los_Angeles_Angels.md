# Market Analysis — 2026-05-19 02:39 UTC

## Market
- **Question:** Athletics vs. Los Angeles Angels
- **Category:** sports
- **YES Price:** 51.0%
- **Days Left:** 6
- **Volume 24h:** $169,631
- **Liquidity:** $19,659

## Statistical Prior
- **p_base:** 51.5%
- **Source:** logistic:sports
- **N (historical):** 6077
- **Raw gap:** 0.5%

## News Sources Fetched
### Macro Context
- Fear&Greed: 25/100 (Extreme Fear) | trend: deteriorating
- BTC: $76,735 (-0.1% 24h) → neutral
- Fear&Greed: 25/100 (Extreme Fear) | 7d trend: deteriorating
- BTC: $76,744 (-0.3% 24h) → neutral

### General
- [FEAR&GREED 7d trend] 25(Extr) → 28(Fear) → 27(Fear) → 31(Fear) | sentiment worsening
- [SPORTS] Injuries:
- ?: A.J. Puk — 60-Day-IL (Surgery)
- ?: Jordan Lawlar — 60-Day-IL (Fracture)
- ?: Pavin Smith — 60-Day-IL (Surgery)
- ?: Jacob Wilson — 10-Day-IL (Dislocated)
- ?: Max Muncy — 10-Day-IL (Fracture)
- ?: Brooks Kriske — 15-Day-IL (Pinched Nerve)

### Multi-Source
- [MULTI-SOURCE NEWS] 2 sources for: athletics angeles angels
- [Bing News]
- [Mon, 18 May 2026] athletics angeles angels
- → New Series Begins Tonight ...
- [Mon, 18 May 2026] Game #47: Athletics at Angels game thread
- → Athletics (23-23, first in the AL West) vs. Los Angeles Angels (16-31, fifth in the AL West) Anaheim, California; Monday, 9:38 p.m. EDT PITCHING PRO
- [Mon, 18 May 2026] Angels host the Athletics to begin 4-game series
- → The Sacramento Athletics (23-22) are headed to Angel Stadium on Monday where they will go up against the Los Angeles Angels (16-30). The moneyline o

## LLM Decision
- **Action:** SKIP
- **Confidence:** 45%
- **p_true:** 51.5%
- **Information Gap:** True
- **Crowd Bias:** False
- **Catalyst Type:** STATISTICAL_PATTERN
- **Catalyst Strength:** 0.40

### Reasoning
Strong stat signal (n=13,967) suggests YES overpricing at 51% (true ~44.7%), implying NO value. However, SKIP because: (1) Entry 50-60% pattern shows only 40% WR — worst price range historically, (2) no specific game-level catalyst confirms the stat pattern applies here, (3) gap vs base rate is only +1% (below 5% threshold), (4) cannot cross-verify with bookmaker odds (API down) or related markets (none found), (5) injuries roughly balanced. The statistical edge is contradicted by poor historical performance in this exact range, making risk too high.

## Gate Result
- **Passed:** ❌ NO
- **Reason:** no stat edge gap=1%<5%

## Tool Calls
- `get_sports_data({'sport': 'mlb', 'team': 'Athletics'})` → INJURY [athletics] Jacob Wilson (SS): 10-Day-IL
INJURY [athletics] Max Muncy (3B): 10-Day-IL
INJURY 
- `get_sports_data({'sport': 'mlb', 'team': 'Angels'})` → INJURY [los angeles angels] Travis d'Arnaud (C): 10-Day-IL
INJURY [los angeles angels] Ben Joyce (RP
- `search_web({'query': 'Athletics vs Los Angeles Angels 2025 recent results'})` → [Sun, 07 Sep 2025] Google News
[Fri, 15 Aug 2025] Athletics at Los Angeles Angels Game Story, Scores
- `search_web({'query': 'Oakland Athletics recent form MLB 2025'})` → [Wed, 13 May 2026] Google News
[Tue, 05 May 2026] World Series | History, Winners, &amp; Facts - Bri
- `get_odds({'sport': 'baseball_mlb', 'team': 'Athletics'})` → Odds API error: 401 {"message":"Usage quota has been reached. See usage plans at https://the-odds-ap
- `get_market_context({'keyword': 'Athletics Angels'})` → No related markets found for 'Athletics Angels'
- `search_web({'query': 'Athletics Angels September 2025 pitching matchup preview'})` → [Mon, 04 May 2026] Google News
[Tue, 30 Sep 2025] Los Angeles Angels vs Athletics | September 23, 20
- `search_web({'query': 'Oakland Athletics Angels head to head 2025 season series'})` → [Mon, 18 May 2026] Google News
[Wed, 18 Mar 2026] Los Angeles Angels vs Athletics Prediction &amp; P
- `search_web({'query': '"Athletics" "Angels" September 7 2025 starter pitcher'})` → [Mon, 18 May 2026] Google News
[Sun, 07 Sep 2025] Los Angeles Angels vs Athletics Prediction &amp; P
- `get_market_context({'keyword': 'MLB baseball'})` → No related markets found for 'MLB baseball'

## Outcome
_Pending — will be updated when market resolves_

---
*Mode: LIVE | DRY_RUN: true*