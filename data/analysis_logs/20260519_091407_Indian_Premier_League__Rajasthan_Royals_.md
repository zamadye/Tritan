# Market Analysis — 2026-05-19 09:14 UTC

## Market
- **Question:** Indian Premier League: Rajasthan Royals vs Lucknow Super Giants
- **Category:** sports
- **YES Price:** 57.0%
- **Days Left:** 7
- **Volume 24h:** $82,174
- **Liquidity:** $299,288

## Statistical Prior
- **p_base:** 60.4%
- **Source:** logistic:sports
- **N (historical):** 6077
- **Raw gap:** 3.4%

## News Sources Fetched
### Macro Context
- Fear&Greed: 25/100 (Extreme Fear) | trend: deteriorating
- BTC: $76,988 (+0.1% 24h) → neutral
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
- **Catalyst Type:** STATISTICAL
- **Catalyst Strength:** 0.65

### Reasoning
Strong statistical signal shows markets at 57% YES historically resolve YES only 44.7% of time (n=13,967), indicating 12.3% market overpricing. However, the gap between market (57%) and base rate (60%) is only +3%, which FAILS the 5% minimum gate threshold required to place a bet. Past decisions on identical market also skipped/failed gate for same reason. While SPORTS pattern shows 80% WR (strong), entry at 50-60% has only 33% WR (weak), and without meeting the gap requirement, we cannot act despite the statistical edge. RR vs LSG match 64 has Jadeja returning and RR seeking revival, but no concrete evidence shifts true probability sufficiently to overcome gate failure.

## Gate Result
- **Passed:** ❌ NO
- **Reason:** no stat edge gap=3%<5%

## Tool Calls
- `get_market_context({'keyword': 'Rajasthan Royals Lucknow Super Giants'})` → No related markets found for 'Rajasthan Royals Lucknow Super Giants'
- `get_market_context({'keyword': 'Indian Premier League'})` → No related markets found for 'Indian Premier League'
- `search_web({'query': 'Rajasthan Royals vs Lucknow Super Giants match preview IPL 2024'})` → [Fri, 08 May 2026] Google News
[Mon, 18 May 2026] IPL RR VS LSG MATCH PREDICTION RAJASTHAN ROYALS VS
- `search_web({'query': 'IPL 2024 Rajasthan Royals vs Lucknow Super Giants odds predictions'})` → [Tue, 19 May 2026] Google News
[Mon, 18 May 2026] RR vs LSG IPL 2026 64th Match Prediction &amp; Odd
- `search_web({'query': 'Rajasthan Royals injury report IPL 2024'})` → [Tue, 22 Apr 2025] Google News
[Sat, 13 Apr 2024] Sanju Samson’s absence, captaincy gamble haunt Raj
- `search_web({'query': 'Lucknow Super Giants injury report IPL 2024'})` → [Wed, 15 Apr 2026] Google News
[Mon, 04 Nov 2024] RCB vs LSG, Match 23 Preview: Virat Kohli’s injury
- `search_web({'query': 'Rajasthan Royals recent results IPL 2024'})` → [Fri, 08 Aug 2025] Google News
[Fri, 07 Feb 2025] Sanju Samson’s IPL records with Rajasthan Royals -
- `search_web({'query': 'Lucknow Super Giants recent results IPL 2024'})` → [Fri, 15 May 2026] Google News
[Wed, 01 Apr 2026] CSK vs LSG Head to Head Records In IPL (2026 Stats
- `search_web({'query': 'RR vs LSG head to head IPL 2024'})` → [Wed, 22 Apr 2026] Google News
[Mon, 18 May 2026] LSG vs RR, IPL match 2026 today: Likely playing XI
- `search_web({'query': '"Rajasthan Royals vs Lucknow Super Giants" IPL 2024 preview'})` → [Fri, 08 May 2026] Google News
[Mon, 18 May 2026] IPL RR VS LSG MATCH PREDICTION RAJASTHAN ROYALS VS
- `search_web({'query': 'Rajasthan Royals form IPL 2024 wins losses'})` → [Mon, 13 Apr 2026] Google News
[Wed, 22 Apr 2026] SRH vs RR IPL 2026: Match 21 Odds, Head-to-Head &a
- `search_web({'query': 'RR vs LSG 2026 IPL'})` → [Tue, 19 May 2026] Google News
[Tue, 19 May 2026] IPL 2026 RR vs LSG Live Streaming: How to watch Ra
- `search_web({'query': 'Rajasthan Royals IPL 2026 form'})` → [Mon, 18 May 2026] Google News
[Sat, 16 May 2026] IPL 2026, RR vs LSG 64th Match Match Preview - RR 

## Outcome
_Pending — will be updated when market resolves_

---
*Mode: LIVE | DRY_RUN: true*