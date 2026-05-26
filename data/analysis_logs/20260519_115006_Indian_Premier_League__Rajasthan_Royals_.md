# Market Analysis — 2026-05-19 11:50 UTC

## Market
- **Question:** Indian Premier League: Rajasthan Royals vs Lucknow Super Giants
- **Category:** sports
- **YES Price:** 57.0%
- **Days Left:** 7
- **Volume 24h:** $92,180
- **Liquidity:** $627,472

## Statistical Prior
- **p_base:** 60.4%
- **Source:** logistic:sports
- **N (historical):** 6077
- **Raw gap:** 3.4%

## News Sources Fetched
### Macro Context
- Fear&Greed: 25/100 (Extreme Fear) | trend: deteriorating
- BTC: $76,632 (-0.8% 24h) → neutral
- Fear&Greed: 25/100 (Extreme Fear) | 7d trend: deteriorating
- BTC: $76,822 (+0.0% 24h) → neutral

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
- → Read the full preview for IPL 2026 Match 64 between Rajasthan Royals and Lucknow Super Giants on May 19, featuring player form, team analysis, head-
- [Tue, 19 May 2026] Match Predictions: Indian Premier League 2026 - Match 64 - Rajasthan Royals vs Lucknow Super Giants - May 19th
- → RR vs LSG IPL 2026 preview featuring Rajasthan Royals’ playoff battle against eliminated Lucknow Super Giants in a crucial clash at Jaipur, know eve
- [Tue, 19 May 2026] RR Vs LSG Match Facts, IPL 2026: All You Need To Know About Today's Indian Premier League Match 64
- → Catch the updates and highlights from the IPL 2026 encounter between Rajasthan Royals and Lucknow Super Giants at the Sawai Mansingh Stadium in Jaip

## LLM Decision
- **Action:** SKIP
- **Confidence:** 58%
- **p_true:** 60.4%
- **Information Gap:** False
- **Crowd Bias:** False
- **Catalyst Type:** NONE
- **Catalyst Strength:** 0.30

### Reasoning
Stat signal (n=13,967) shows 57% YES historically resolves YES only 44.7% — clear ~12% overpricing bias. However, contextual factors are ambiguous: LSG eliminated (less motivation, possible spoiler) vs RR must-win (high motivation, home, Jadeja returning). Gate fails (gap=3%<5%). No concrete catalyst to resolve ambiguity. Crowd bias likely inflating YES on favorite/home team despite statistical edge. Skipping due to insufficient actionable edge despite stat signal.

## Gate Result
- **Passed:** ❌ NO
- **Reason:** no stat edge gap=3%<5%

## Tool Calls
- `get_sports_data({'team': 'Rajasthan Royals', 'sport': 'cricket'})` → No injury data found for cricket Rajasthan Royals
- `get_sports_data({'sport': 'cricket', 'team': 'Lucknow Super Giants'})` → No injury data found for cricket Lucknow Super Giants
- `search_web({'query': 'Rajasthan Royals vs Lucknow Super Giants IPL 2025 match preview prediction'})` → [Sun, 10 May 2026] Google News
[Tue, 21 Apr 2026] Rajasthan Royals Vs Lucknow Super Giants Today Dre
- `search_web({'query': 'IPL Rajasthan Royals Lucknow Super Giants team news injury report May 2025'})` → No search results for: IPL Rajasthan Royals Lucknow Super Giants team news injury report May 2025
- `search_web({'query': 'IPL 2026 Rajasthan Royals vs Lucknow Super Giants upcoming match preview'})` → [Tue, 19 May 2026] Google News
[Tue, 19 May 2026] RR vs LSG, IPL 2026 preview: Rajasthan Royals seek
- `search_web({'query': 'Rajasthan Royals current form IPL 2026 standings'})` → [Sun, 17 May 2026] Google News
[Tue, 28 Apr 2026] Vaibhav Sooryavanshi sets sights on breaking huge 
- `get_market_context({'keyword': 'IPL Rajasthan Lucknow'})` → No related markets found for 'IPL Rajasthan Lucknow'
- `search_web({'query': '"Rajasthan Royals" "Lucknow Super Giants" IPL 2026 match preview prediction odds'})` → [Tue, 19 May 2026] Google News
[Mon, 18 May 2026] RR vs LSG IPL 2026 64th Match Prediction &amp; Odd
- `search_web({'query': 'IPL 2026 Lucknow Super Giants eliminated eliminated from playoffs'})` → [Sun, 17 May 2026] Google News
[Tue, 19 May 2026] IPL 2026 playoffs: Qualified teams, standings and 
- `search_web({'query': 'IPL 2026 Lucknow Super Giants eliminated from playoffs motivation'})` → [Tue, 19 May 2026] Google News
[Tue, 19 May 2026] RR Vs LSG Match Prediction, IPL 2026: Who Will Win
- `search_web({'query': 'IPL 2026 Rajasthan Royals playoff chances must win matches remaining'})` → [Sun, 17 May 2026] Google News
[Tue, 19 May 2026] IPL 2026 playoffs: Qualified teams, standings and 
- `search_web({'query': 'RR vs LSG IPL 2026 who will win Rajasthan Royals Lucknow Super Giants head to head'})` → [Tue, 19 May 2026] Google News
[Mon, 18 May 2026] IPL Match Today, RR vs LSG: Predicted playing XI, 
- `search_web({'query': 'IPL 2026 Rajasthan Royals team news injuries Ravindra Jadeja Riyan Parag'})` → [Mon, 18 May 2026] Google News
[Tue, 19 May 2026] Riyan Parag reveals why Ravindra Jadeja is not pla
- `search_web({'query': 'RR vs LSG today match prediction May 19 2026 IPL who will win'})` → No search results for: RR vs LSG today match prediction May 19 2026 IPL who will win
- `search_web({'query': 'Lucknow Super Giants 2026 eliminated playoffs rest players motivation'})` → [Wed, 13 May 2026] Google News
[] LSG vs CSK IPL 2026 Match Preview &amp; Fantasy Prediction - Ai11

## Outcome
_Pending — will be updated when market resolves_

---
*Mode: LIVE | DRY_RUN: true*