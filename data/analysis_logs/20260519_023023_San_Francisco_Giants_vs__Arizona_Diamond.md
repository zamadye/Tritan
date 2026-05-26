# Market Analysis — 2026-05-19 02:30 UTC

## Market
- **Question:** San Francisco Giants vs. Arizona Diamondbacks
- **Category:** sports
- **YES Price:** 10.0%
- **Days Left:** 6
- **Volume 24h:** $71,608
- **Liquidity:** $60,504

## Statistical Prior
- **p_base:** 3.6%
- **Source:** logistic:sports
- **N (historical):** 6077
- **Raw gap:** 6.4%

## News Sources Fetched
### Macro Context
- Fear&Greed: 25/100 (Extreme Fear) | trend: deteriorating
- BTC: $76,710 (-0.4% 24h) → neutral
- Fear&Greed: 25/100 (Extreme Fear) | 7d trend: deteriorating
- BTC: $76,844 (-0.2% 24h) → neutral

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
- [MULTI-SOURCE NEWS] 2 sources for: francisco giants arizona diamondbacks
- [Bing News]
- [Mon, 18 May 2026] francisco giants arizona diamondbacks
- → The Arizona Diamondbacks (21-23) will compete against the San Francisco Giants (19-27) at Chase Field on Tuesday. The line on this contest has San F
- [Mon, 18 May 2026] San Francisco Giants vs Arizona Diamondbacks Prediction, 5/19/2026 MLB Picks, Best Bets &amp; Odds
- → The San Francisco Giants begin a three-game road series against the Arizona Diamondbacks tonight. Taking the mound for the Giants will be left-hande
- [Mon, 18 May 2026] How to watch San Francisco Giants vs. Arizona Diamondbacks
- → Here's how to watch Monday's Arizona Diamondbacks vs San Francisco Giants game, including start times, TV channels, scores and how to stream.

## LLM Decision
- **Action:** SKIP
- **Confidence:** 45%
- **p_true:** 5.0%
- **Information Gap:** False
- **Crowd Bias:** False
- **Catalyst Type:** NONE
- **Catalyst Strength:** 0.10

### Reasoning
Market at 10% with base rate 4% shows crowd overpricing YES by 2.5x. Negative gap (-6%) suggests market already reflects higher probability than historical base. No specific catalyst found in news to justify YES becoming more likely. Insufficient evidence of edge - market may be slightly overpriced but confidence too low for a bet. Similar past decisions were skipped for comparable reasons.

## Gate Result
- **Passed:** ❌ NO
- **Reason:** low conf 45%<52%

## Tool Calls
- `get_sports_data({'sport': 'mlb', 'team': 'San Francisco Giants'})` → INJURY [san francisco giants] Logan Webb (SP): 15-Day-IL
INJURY [san francisco giants] Heliot Ramos 
- `get_sports_data({'sport': 'mlb', 'team': 'Arizona Diamondbacks'})` → INJURY [arizona diamondbacks] A.J. Puk (RP): 60-Day-IL
INJURY [arizona diamondbacks] Jordan Lawlar (
- `search_web({'query': 'San Francisco Giants recent performance 2025'})` → [Mon, 18 May 2026] Google News
[Mon, 20 Oct 2025] Official San Francisco Giants Website - MLB.com
[M
- `search_web({'query': 'Arizona Diamondbacks recent performance 2025'})` → [Tue, 06 Jan 2026] Google News
[Sat, 24 Jan 2026] Faith &amp; Family Night | Arizona Diamondbacks - 
- `search_web({'query': 'Giants vs Diamondbacks May 2026 prediction'})` → [Mon, 18 May 2026] Google News
[Tue, 19 May 2026] San Francisco Giants vs. Arizona Diamondbacks pred
- `get_market_context({'keyword': 'San Francisco Giants Arizona Diamondbacks'})` → No related markets found for 'San Francisco Giants Arizona Diamondbacks'
- `get_odds({'sport': 'baseball_mlb', 'team': 'San Francisco Giants'})` → Odds API error: 401 {"message":"Usage quota has been reached. See usage plans at https://the-odds-ap
- `search_web({'query': 'San Francisco Giants vs Arizona Diamondbacks prediction May 18 2026 odds'})` → [Mon, 18 May 2026] Google News
[Tue, 19 May 2026] How to watch Giants vs. Diamondbacks: TV channel a
- `search_web({'query': 'San Francisco Giants starting pitcher May 18 2026'})` → [Mon, 18 May 2026] Google News
[Mon, 18 May 2026] Mike Krukow adamant Giants need to permanently add
- `search_web({'query': 'Arizona Diamondbacks starting pitcher May 18 2026'})` → [Tue, 19 May 2026] Google News
[Tue, 19 May 2026] Max Scherzer throws a bullpen session as he works 

## Outcome
_Pending — will be updated when market resolves_

---
*Mode: LIVE | DRY_RUN: true*