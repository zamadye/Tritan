# Market Analysis — 2026-05-19 12:46 UTC

## Market
- **Question:** Indian Premier League: Rajasthan Royals vs Lucknow Super Giants
- **Category:** sports
- **YES Price:** 58.0%
- **Days Left:** 7
- **Volume 24h:** $96,245
- **Liquidity:** $115,047

## Statistical Prior
- **p_base:** 61.9%
- **Source:** logistic:sports
- **N (historical):** 6077
- **Raw gap:** 3.9%

## News Sources Fetched
### Macro Context
- Fear&Greed: 25/100 (Extreme Fear) | trend: deteriorating
- BTC: $76,847 (-1.1% 24h) → risk-OFF
- Fear&Greed: 25/100 (Extreme Fear) | 7d trend: deteriorating
- BTC: $76,863 (-1.0% 24h) → risk-OFF

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
- [MULTI-SOURCE NEWS] 2 sources for: indian premier league: rajasthan royals
- [Bing News]
- [Tue, 19 May 2026] indian premier league: rajasthan royals
- → Rajasthan Royals have 12 points from 12 games, while Lucknow Super Giants have eight points from 12 matches and are out of playoff contention. Follo
- [Mon, 18 May 2026] RR Vs LSG Live Cricket Score, IPL 2026: Playoffs-Seeking Royals Desperate For First Win In Jaipur
- → Read the full preview for IPL 2026 Match 64 between Rajasthan Royals and Lucknow Super Giants on May 19, featuring player form, team analysis, head-
- [Tue, 19 May 2026] Match Predictions: Indian Premier League 2026 - Match 64 - Rajasthan Royals vs Lucknow Super Giants - May 19th
- → RR vs LSG IPL 2026 preview featuring Rajasthan Royals’ playoff battle against eliminated Lucknow Super Giants in a crucial clash at Jaipur, know eve

## LLM Decision
- **Action:** SKIP
- **Confidence:** 65%
- **p_true:** 51.9%
- **Information Gap:** True
- **Crowd Bias:** False
- **Catalyst Type:** STAT_SIGNAL
- **Catalyst Strength:** 0.75

### Reasoning
Strong statistical signal (n=13,967) shows markets at 58% YES resolve YES only 44.7% of the time - market overprices YES by 13.3 percentage points. No contradictory team news or form indicators found in searches.

## Gate Result
- **Passed:** ❌ NO
- **Reason:** no stat edge gap=4%<5%

## Tool Calls
- `search_web({'query': 'Rajasthan Royals vs Lucknow Super Giants IPL 2025 match preview'})` → [Mon, 18 May 2026] Google News
[Tue, 12 May 2026] IPL 2026, RR vs LSG 64th Match Match Preview - RR 
- `search_web({'query': 'Rajasthan Royals Lucknow Super Giants head to head 2026'})` → [Tue, 19 May 2026] Google News
[Tue, 19 May 2026] RR vs LSG Playing 11: Check probable XIs, head-to-
- `search_web({'query': 'Rajasthan Royals vs Lucknow Super Giants team news injuries 2026'})` → [Mon, 18 May 2026] Google News
[Tue, 19 May 2026] IPL 2026, RR vs LSG 64th Match Match Preview - RR 
- `get_market_context({'keyword': 'IPL Rajasthan Royals Lucknow Super Giants'})` → No related markets found for 'IPL Rajasthan Royals Lucknow Super Giants'
- `search_web({'query': 'RR vs LSG match 64 IPL 2026 preview ESPNcricinfo'})` → [Mon, 18 May 2026] Google News
[Mon, 18 May 2026] IPL 2026, RR vs LSG 64th Match Match Preview - RR 
- `search_web({'query': 'RR vs LSG betting odds IPL 2026'})` → [Tue, 19 May 2026] Google News
[Tue, 19 May 2026] RR vs LSG IPL 2026 64th Match Prediction &amp; Odd
- `search_web({'query': 'Betfred RR vs LSG IPL 2026 odds prediction'})` → [Tue, 19 May 2026] Google News
[Mon, 13 Apr 2026] RR vs LSG Prediction &amp; 2026 IPL Cricket Previe

## Outcome
_Pending — will be updated when market resolves_

---
*Mode: LIVE | DRY_RUN: true*