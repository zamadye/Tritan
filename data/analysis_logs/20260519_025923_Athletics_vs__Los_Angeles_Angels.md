# Market Analysis — 2026-05-19 02:59 UTC

## Market
- **Question:** Athletics vs. Los Angeles Angels
- **Category:** sports
- **YES Price:** 53.0%
- **Days Left:** 6
- **Volume 24h:** $175,278
- **Liquidity:** $113,174

## Statistical Prior
- **p_base:** 54.5%
- **Source:** logistic:sports
- **N (historical):** 6077
- **Raw gap:** 1.5%

## News Sources Fetched
### Macro Context
- Fear&Greed: 25/100 (Extreme Fear) | trend: deteriorating
- BTC: $76,579 (-0.2% 24h) → neutral
- Fear&Greed: 25/100 (Extreme Fear) | 7d trend: deteriorating
- BTC: $76,579 (-0.2% 24h) → neutral

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
- → Angels: Walbert Urena (1-4, 3.29 ERA, 1.43 WHIP, 26 strikeouts) LINE: Athletics -129, Angels +109; over/under is 9 runs BOTTOM LINE: The Los Angeles
- [Mon, 18 May 2026] Angels host the Athletics to begin 4-game series
- → The Sacramento Athletics (23-22) are headed to Angel Stadium on Monday where they will go up against the Los Angeles Angels (16-30). The moneyline o

## LLM Decision
- **Action:** NO
- **Confidence:** 62%
- **p_true:** 44.5%
- **Information Gap:** True
- **Crowd Bias:** False
- **Catalyst Type:** STATISTICAL_CALIBRATION
- **Catalyst Strength:** 0.75

### Reasoning
Strong statistical signal (n=13,967) shows markets at 53% resolve YES only 44.7% of time, indicating YES overpriced by ~8.3%. Athletics have key injuries (Max Muncy, Jacob Wilson on IL) weakening their lineup. NO at 47% offers value vs true probability of 55.3%. Moderate confidence due to entry range pattern (50-60%) showing poor WR historically (40%), but large sample calibration edge is compelling.

## Gate Result
- **Passed:** ❌ NO
- **Reason:** no stat edge gap=1%<5%

## Tool Calls
- `get_sports_data({'sport': 'mlb', 'team': 'Athletics'})` → INJURY [athletics] Jacob Wilson (SS): 10-Day-IL
INJURY [athletics] Max Muncy (3B): 10-Day-IL
INJURY 
- `search_web({'query': 'Athletics vs Angels upcoming game June 2025'})` → [Sat, 16 Aug 2025] Google News
[Fri, 06 Mar 2026] Los Angeles Angels at Athletics Game Story, Scores
- `search_web({'query': 'Athletics Angels prediction analysis 2025'})` → [Thu, 23 Oct 2025] Google News
[Mon, 01 Dec 2025] World Series predictions: Our experts pick whether
- `get_market_context({'query': 'Athletics Angels MLB'})` → [YES=50% vol=$10,847,271] Spurs vs. Thunder
[YES=50% vol=$5,821,653] Will Bitcoin hit $150k by June 
- `get_odds({'sport': 'baseball_mlb', 'team': 'Athletics'})` → Odds API error: 401 {"message":"Usage quota has been reached. See usage plans at https://the-odds-ap
- `search_web({'query': 'Oakland Athletics vs Los Angeles Angels odds June 2025 MLB'})` → [Sun, 02 Nov 2025] Google News
[Wed, 17 Sep 2025] Early MLB 2026 power rankings based on World Serie
- `search_web({'query': 'Athletics Angels head to head 2025 season record'})` → [Fri, 15 May 2026] Google News
[Sun, 17 May 2026] Diving into all 15 Rivalry Weekend matchups - MLB.
- `search_web({'query': '"Athletics" "Angels" "June 2025" MLB game odds'})` → [Tue, 01 Jul 2025] Google News
[Wed, 28 May 2025] MLB Power Rankings: Mets, Guardians end June with 
- `get_crypto_price({'coin': 'bitcoin'})` → bitcoin: $76,592.00 | 24h: -0.23%

## Outcome
**❌ LOSS** | P&L: $-1.00 | Resolved: YES

---
*Mode: LIVE | DRY_RUN: true*