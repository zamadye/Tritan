# Market Analysis — 2026-05-19 01:19 UTC

## Market
- **Question:** Los Angeles Dodgers vs. San Diego Padres
- **Category:** sports
- **YES Price:** 57.0%
- **Days Left:** 7
- **Volume 24h:** $146,762
- **Liquidity:** $483,562

## Statistical Prior
- **p_base:** 60.4%
- **Source:** logistic:sports
- **N (historical):** 6077
- **Raw gap:** 3.4%

## News Sources Fetched
### Macro Context
- Fear&Greed: 25/100 (Extreme Fear) | trend: deteriorating
- BTC: $77,024 (+0.1% 24h) → neutral
- Fear&Greed: 25/100 (Extreme Fear) | 7d trend: deteriorating
- BTC: $77,024 (+0.1% 24h) → neutral

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
- [MULTI-SOURCE NEWS] 2 sources for: angeles dodgers diego padres
- [Bing News]
- [Mon, 18 May 2026] angeles dodgers diego padres
- → The Los Angeles Dodgers and the San Diego Padres open a 3-game series Monday at Petco Park in San Diego, California. First pitch is set for 9:40 p.m
- [Mon, 18 May 2026] LA Dodgers at San Diego Padres odds, picks and predictions
- → The Los Angeles Dodgers (29-18) meet the San Diego Padres( 28-18) to start a three-game series between the NL West rivals. The Dodgers have won five
- [Mon, 18 May 2026] Where to watch Los Angeles Dodgers vs. San Diego Padres: Live stream, TV channel, odds for Monday, May 18
- → The Los Angeles Dodgers (29-18) take a five-game winning streak down the coast on Monday night to open a three-game series for the National League W

## LLM Decision
- **Action:** SKIP
- **Confidence:** 62%
- **p_true:** 58.4%
- **Information Gap:** True
- **Crowd Bias:** False
- **Catalyst Type:** INJURIES + STAT SIGNAL
- **Catalyst Strength:** 0.55

### Reasoning
Strong statistical signal indicates markets at 57% resolve YES only 44.7% of the time (n=13,967), suggesting 12% overpricing of YES. Dodgers missing two key starting pitchers (Snell and Glasnow) on IL weakens their chances, providing direct catalyst aligning with stat signal. Despite gap=3% below 5% gate threshold, the 12.3% gap between market price (57%) and historical resolution rate (44.7%) represents meaningful edge. SPORTS pattern strong (WR=81%), though entry 50-60% bracket weaker (WR=40%). Moderate confidence due to limited independent verification of injury impact on pricing.

## Gate Result
- **Passed:** ❌ NO
- **Reason:** no stat edge gap=3%<5%

## Tool Calls
- `get_sports_data({'sport': 'mlb', 'team': 'Dodgers'})` → INJURY [los angeles dodgers] Blake Snell (SP): 15-Day-IL
INJURY [los angeles dodgers] Tyler Glasnow 
- `get_sports_data({'sport': 'mlb', 'team': 'Padres'})` → INJURY [san diego padres] German Marquez (SP): 15-Day-IL
INJURY [san diego padres] Jhony Brito (RP):
- `search_web({'query': 'Dodgers vs Padres 2025 series injuries'})` → [Mon, 18 May 2026] Google News
[Mon, 18 May 2026] Dodgers Preview: Dodgers–Padres Showdown: Yamamoto
- `search_web({'query': 'Los Angeles Dodgers San Diego Padres 2025 standings'})` → [Mon, 18 May 2026] Google News
[Tue, 05 May 2026] MLB power rankings: Renewing a rivalry - San Diego
- `get_market_context({'keyword': 'Dodgers Padres'})` → No related markets found for 'Dodgers Padres'
- `search_web({'query': 'Dodgers Padres series May 2026 injuries'})` → [Tue, 19 May 2026] Google News
[Sun, 17 May 2026] Dodgers @ Padres May 18, 2026: Yamamoto opens thre
- `search_web({'query': '"Dodgers vs. Padres Series Injured List" May 18 2026'})` → [Sun, 17 May 2026] Google News
[Sun, 18 Dec 2016] Dodgers vs. Padres Series Injured List - May 18-20

## Outcome
_Pending — will be updated when market resolves_

---
*Mode: LIVE | DRY_RUN: true*