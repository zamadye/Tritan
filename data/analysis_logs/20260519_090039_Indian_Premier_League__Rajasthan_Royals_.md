# Market Analysis — 2026-05-19 09:00 UTC

## Market
- **Question:** Indian Premier League: Rajasthan Royals vs Lucknow Super Giants
- **Category:** sports
- **YES Price:** 57.0%
- **Days Left:** 7
- **Volume 24h:** $81,137
- **Liquidity:** $287,173

## Statistical Prior
- **p_base:** 60.4%
- **Source:** logistic:sports
- **N (historical):** 6077
- **Raw gap:** 3.4%

## News Sources Fetched
### Macro Context
- Fear&Greed: 25/100 (Extreme Fear) | trend: deteriorating
- BTC: $77,032 (+0.1% 24h) → neutral
- Fear&Greed: 25/100 (Extreme Fear) | 7d trend: deteriorating
- BTC: $77,118 (+0.3% 24h) → neutral

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
- → Rajasthan Royals face Lucknow Super Giants in IPL 2026 Match 64 on Tuesday. Check RR’s playoff qualification scenarios ahead of the big match tonigh

## LLM Decision
- **Action:** SKIP
- **Confidence:** 52%
- **p_true:** 60.4%
- **Information Gap:** False
- **Crowd Bias:** False
- **Catalyst Type:** NONE
- **Catalyst Strength:** 0.10

### Reasoning
Strong stat signal (n=13,967) suggests markets at 57% resolve YES only 44.7% of time, indicating potential NO edge. However: (1) base rate gap only +3%, below 5% gate threshold — same market skipped twice before for same reason; (2) 50-60% entry range has weak 33% WR historically; (3) No concrete catalysts found in news searches regarding team form, injuries, or match conditions; (4) Macro fear/greed environment is extreme fear but likely irrelevant to cricket match outcome. Pattern shows info gap trades outperform, but no verified information edge exists here. Stat edge alone insufficient without catalyst or clear information asymmetry.

## Gate Result
- **Passed:** ❌ NO
- **Reason:** no stat edge gap=3%<5%

## Tool Calls
- `search_web({'query': 'Rajasthan Royals vs Lucknow Super Giants recent results IPL 2025'})` → [Wed, 22 Apr 2026] Google News
[Tue, 21 Apr 2026] LSG vs RR IPL 2026: Players, standings, stats and 
- `search_web({'query': 'Rajasthan Royals injury news IPL 2026'})` → [Mon, 18 May 2026] Google News
[Sun, 17 May 2026] IPL 2026, RR vs LSG 64th Match Match Preview - RR 
- `search_web({'query': 'RR vs LSG 2026 match preview ESPNcricinfo'})` → [Mon, 18 May 2026] Google News
[Tue, 21 Apr 2026] IPL 2026, RR vs LSG 64th Match Match Preview - RR 
- `search_web({'query': 'Rajasthan Royals form IPL 2026 results'})` → [Mon, 16 Mar 2026] Google News
[Fri, 01 May 2026] IPL 2026 schedule: Fixtures, start times, scorecar
- `search_web({'query': 'Lucknow Super Giants form IPL 2026 results'})` → [Tue, 05 May 2026] Google News
[Mon, 16 Mar 2026] IPL 2026: What’s gone wrong for LSG? Pant’s form, 
- `get_market_context({'keyword': 'IPL'})` → No related markets found for 'IPL'
- `get_market_context({'keyword': 'Rajasthan Royals'})` → No related markets found for 'Rajasthan Royals'

## Outcome
_Pending — will be updated when market resolves_

---
*Mode: LIVE | DRY_RUN: true*