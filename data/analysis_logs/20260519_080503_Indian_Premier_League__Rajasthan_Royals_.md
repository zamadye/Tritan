# Market Analysis — 2026-05-19 08:05 UTC

## Market
- **Question:** Indian Premier League: Rajasthan Royals vs Lucknow Super Giants
- **Category:** sports
- **YES Price:** 55.0%
- **Days Left:** 7
- **Volume 24h:** $54,910
- **Liquidity:** $689,971

## Statistical Prior
- **p_base:** 57.5%
- **Source:** logistic:sports
- **N (historical):** 6077
- **Raw gap:** 2.5%

## News Sources Fetched
### Macro Context
- Fear&Greed: 25/100 (Extreme Fear) | trend: deteriorating
- BTC: $77,168 (+0.2% 24h) → neutral
- Fear&Greed: 25/100 (Extreme Fear) | 7d trend: deteriorating
- BTC: $77,147 (+0.1% 24h) → neutral

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
- [Mon, 18 May 2026] Match Predictions: Indian Premier League 2026 - Match 64 - Rajasthan Royals vs Lucknow Super Giants - May 19th
- → IPL 2026 Playing 11 Today Match, Squad, Players List: The Indian Express looks at predicted line-ups for both sides for the clash on Tuesday in Jaip

## LLM Decision
- **Action:** SKIP
- **Confidence:** 52%
- **p_true:** 57.5%
- **Information Gap:** False
- **Crowd Bias:** False
- **Catalyst Type:** NONE
- **Catalyst Strength:** 0.10

### Reasoning
Strong statistical signal indicates market overprices YES (44.7% historical resolution vs 55% price), but I cannot identify which team is the YES side. Without knowing if YES = RR or YES = LSG, I cannot determine if a BET_NO is warranted. Research found: RR at home in Jaipur with Riyan Parag as captain, Jadeja returning; LSG led by Rishabh Pant who had a Super Over loss to KKR recently. No specific injury news or form catalysts discovered that would create a clear edge. Gap is only 2% (<5% gate threshold). Per past decision pattern, similar IPL markets with small gaps were skipped correctly. Would need: (1) clear YES team identification, or (2) major breaking news (key player injury/withdrawal) to take position.

## Gate Result
- **Passed:** ❌ NO
- **Reason:** no stat edge gap=2%<5%

## Tool Calls
- `get_sports_data({'sport': 'cricket', 'team': 'Rajasthan Royals'})` → No injury data found for cricket Rajasthan Royals
- `get_sports_data({'sport': 'cricket', 'team': 'Lucknow Super Giants'})` → No injury data found for cricket Lucknow Super Giants
- `search_web({'query': 'Rajasthan Royals vs Lucknow Super Giants IPL 2025 match preview'})` → [Tue, 12 May 2026] Google News
[Tue, 21 Apr 2026] RR VS LSG IPL 2025 HIGHLIGHTS | LIVE MATCH | RAJAS
- `search_web({'query': 'Rajasthan Royals Lucknow Super Giants team news injury update 2025'})` → [Wed, 22 Apr 2026] Google News
[Sat, 19 Apr 2025] LSG vs RR Dream11 Prediction, Match 32, IPL Fantas
- `get_market_context({'keyword': 'IPL Rajasthan Lucknow'})` → No related markets found for 'IPL Rajasthan Lucknow'
- `search_web({'query': 'Rajasthan Royals IPL 2025 current form standings results'})` → [Tue, 07 Apr 2026] Google News
[Mon, 13 Apr 2026] RR vs MI IPL 2026: Players, standings, stats and k
- `search_web({'query': 'Lucknow Super Giants IPL 2025 current form standings results'})` → [Mon, 18 May 2026] Google News
[Tue, 27 May 2025] IPL 2026 playoffs: Qualified teams, standings and 
- `search_web({'query': '"Rajasthan Royals" "Lucknow Super Giants" IPL 2026 head to head recent'})` → [Mon, 18 May 2026] Google News
[Mon, 18 May 2026] IPL 2026: Here's all you need to know about RR vs 
- `search_web({'query': 'Sanju Samson injury status RR captain 2026'})` → [Sun, 29 Mar 2026] Google News
[Sat, 28 Mar 2026] IPL 2026, RR vs CSK 3rd Match Match Preview - Reva
- `search_web({'query': 'Riyan Parag Rajasthan Royals captain IPL 2026 Sanju Samson'})` → [Tue, 12 May 2026] Google News
[Sat, 16 May 2026] IPL BREAKING: NOT JADEJA! RIYAN PARAG REPLACES SAN
- `search_web({'query': 'Rajasthan Royals vs Lucknow Super Giants IPL 2026 match preview prediction today'})` → [Tue, 19 May 2026] Google News
[Tue, 19 May 2026] RR Vs LSG Match Prediction, IPL 2026: Who Will Win
- `search_web({'query': 'Rajasthan Royals playing XI IPL 2026 May 19 Lucknow Super Giants'})` → [Tue, 19 May 2026] Google News
[Mon, 18 May 2026] RR vs LSG IPL 2026 Playing 11 Today Match: Ravindr
- `search_web({'query': 'Lucknow Super Giants recent form results IPL 2026'})` → [Mon, 27 Apr 2026] Google News
[Fri, 15 May 2026] IPL 2026 | 'Criminal decision': Rishabh Pant faces
- `search_web({'query': 'RR vs LSG IPL 2026 match 64 preview pitch report Jaipur'})` → [Mon, 18 May 2026] Google News
[Tue, 19 May 2026] IPL 2026: RR vs. LSG prediction, lineups, pitch re
- `search_web({'query': 'Rajasthan Royals wins losses IPL 2026 standings points'})` → [Wed, 22 Apr 2026] Google News
[Thu, 14 May 2026] IPL 2026 Points Table after Match 32: Rajasthan Ro

## Outcome
_Pending — will be updated when market resolves_

---
*Mode: LIVE | DRY_RUN: true*