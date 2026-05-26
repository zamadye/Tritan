# Market Analysis — 2026-05-19 09:27 UTC

## Market
- **Question:** Indian Premier League: Rajasthan Royals vs Lucknow Super Giants
- **Category:** sports
- **YES Price:** 57.0%
- **Days Left:** 7
- **Volume 24h:** $83,163
- **Liquidity:** $578,681

## Statistical Prior
- **p_base:** 60.4%
- **Source:** logistic:sports
- **N (historical):** 6077
- **Raw gap:** 3.4%

## News Sources Fetched
### Macro Context
- Fear&Greed: 25/100 (Extreme Fear) | trend: deteriorating
- BTC: $76,848 (-0.1% 24h) → neutral
- Fear&Greed: 25/100 (Extreme Fear) | 7d trend: deteriorating
- BTC: $76,848 (-0.1% 24h) → neutral

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
- [Mon, 18 May 2026] indian premier league: rajasthan royals
- → Rajasthan Royals face Lucknow Super Giants in a crucial IPL 2026 clash at the Sawai Mansingh Stadium as playoff pressure mounts. Here’s match previe
- [Mon, 18 May 2026] RR Vs LSG Match Prediction, IPL 2026: Who Will Win Today's Indian Premier League Match In Jaipur?
- → Read the full preview for IPL 2026 Match 64 between Rajasthan Royals and Lucknow Super Giants on May 19, featuring player form, team analysis, head-
- [Tue, 19 May 2026] Match Predictions: Indian Premier League 2026 - Match 64 - Rajasthan Royals vs Lucknow Super Giants - May 19th
- → Lucknow Super Giants pose a big challenge to Rajasthan Royals in the IPL playoff race after rediscovering their form, but the Riyan Parag-led side h

## LLM Decision
- **Action:** SKIP
- **Confidence:** 58%
- **p_true:** 54.4%
- **Information Gap:** True
- **Crowd Bias:** False
- **Catalyst Type:** STATISTICAL
- **Catalyst Strength:** 0.65

### Reasoning
Strong statistical signal (n=13,967) shows markets at 57% YES historically resolve YES only 44.7% of the time, indicating the market overprices YES by ~12%. Despite the 3% gap between market (57%) and base rate (60%) not meeting the 5% threshold for a clear edge gate, the stat signal provides concrete evidence of a mispricing. No specific match catalyst (injuries, form) was found, but the historical pattern is robust. Conf=0.58 reflects moderate evidence from statistical data without match-specific confirmation.

## Gate Result
- **Passed:** ❌ NO
- **Reason:** no stat edge gap=3%<5%

## Tool Calls
- `get_sports_data({'sport': 'cricket', 'team': 'Rajasthan Royals'})` → No injury data found for cricket Rajasthan Royals
- `search_web({'query': 'Rajasthan Royals vs Lucknow Super Giants IPL 2025 match preview'})` → [Tue, 12 May 2026] Google News
[Tue, 21 Apr 2026] RR VS LSG IPL 2025 HIGHLIGHTS | LIVE MATCH | RAJAS
- `search_web({'query': 'Rajasthan Royals form IPL 2025 recent results'})` → [Tue, 06 Jan 2026] Google News
[Sat, 25 Apr 2026] Vaibhav Sooryavanshi Profile - Cricket Player Indi
- `search_web({'query': 'Lucknow Super Giants form IPL 2025 recent results'})` → [Tue, 03 Jun 2025] Google News
[Mon, 26 May 2025] IPL 2025 schedule: The complete match list - olymp
- `search_web({'query': '"Rajasthan Royals vs Lucknow Super Giants" 2025 match date'})` → [Sun, 29 Mar 2026] Google News
[Tue, 03 Jun 2025] 2026 IPL Schedule, Standings &amp; Next Match Coun
- `get_sports_data({'sport': 'cricket', 'team': 'Lucknow Super Giants'})` → No injury data found for cricket Lucknow Super Giants
- `get_market_context({'keyword': 'Rajasthan Royals Lucknow Super Giants IPL'})` → No related markets found for 'Rajasthan Royals Lucknow Super Giants IPL'

## Outcome
_Pending — will be updated when market resolves_

---
*Mode: LIVE | DRY_RUN: true*