# Market Analysis — 2026-05-19 00:46 UTC

## Market
- **Question:** Los Angeles Dodgers vs. San Diego Padres
- **Category:** sports
- **YES Price:** 57.0%
- **Days Left:** 7
- **Volume 24h:** $137,251
- **Liquidity:** $472,806

## Statistical Prior
- **p_base:** 60.4%
- **Source:** logistic:sports
- **N (historical):** 6077
- **Raw gap:** 3.4%

## News Sources Fetched
### Macro Context
- Fear&Greed: 25/100 (Extreme Fear) | trend: deteriorating
- BTC: $77,092 (+0.1% 24h) → neutral
- Fear&Greed: 25/100 (Extreme Fear) | 7d trend: deteriorating
- BTC: $77,117 (+0.1% 24h) → neutral

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
- → The Los Angeles Dodgers (29-18) take a five-game winning streak down the coast on Monday night to open a three-game series for the National League W
- [Mon, 18 May 2026] How to live stream Dodgers vs Padres: MLB, TV channel
- → The Los Angeles Dodgers and the San Diego Padres open a 3-game series Monday at Petco Park in San Diego, California. First pitch is set for 9:40 p.m
- [Mon, 18 May 2026] LA Dodgers at San Diego Padres odds, picks and predictions
- → The Los Angeles Dodgers (29-18) meet the San Diego Padres( 28-18) to start a three-game series between the NL West rivals. The Dodgers have won five

## LLM Decision
- **Action:** SKIP
- **Confidence:** 35%
- **p_true:** 60.4%
- **Information Gap:** False
- **Crowd Bias:** False
- **Catalyst Type:** NONE
- **Catalyst Strength:** 0.10

### Reasoning
Contradictory signals prevent confident action: stat signal (44.7% YES at 57%) suggests NO edge, but base rate (60%) suggests YES is underpriced. The 3% gap is below the 5% threshold. Past two decisions on this exact market were also SKIP for the same reasons. Yamamoto/Ohtani pitching is strong for Dodgers but Glasnow IL hurts. No verifiable edge or new catalyst to break the tie.

## Gate Result
- **Passed:** ❌ NO
- **Reason:** no stat edge gap=3%<5%

## Tool Calls
- `get_sports_data({'sport': 'mlb', 'team': 'Dodgers'})` → INJURY [los angeles dodgers] Tyler Glasnow (SP): 15-Day-IL
INJURY [los angeles dodgers] Ben Caspariu
- `get_sports_data({'sport': 'mlb', 'team': 'Padres'})` → INJURY [san diego padres] German Marquez (SP): 15-Day-IL
INJURY [san diego padres] Jhony Brito (RP):
- `get_odds({'sport': 'baseball_mlb', 'team': 'Dodgers'})` → Odds API error: 401 {"message":"Usage quota has been reached. See usage plans at https://the-odds-ap
- `search_web({'query': 'Los Angeles Dodgers vs San Diego Padres upcoming series 2025'})` → [Mon, 18 May 2026] Google News
[Mon, 18 May 2026] Padres Lineup vs Dodgers: Fernando Tatis Leading O
- `search_web({'query': 'Dodgers Padres injuries roster news May 2025'})` → [Mon, 18 May 2026] Google News
[Sun, 17 May 2026] Dodgers Preview: Dodgers–Padres Showdown: Yamamoto
- `get_market_context({'keyword': 'Dodgers Padres'})` → No related markets found for 'Dodgers Padres'
- `search_web({'query': 'Padres vs Dodgers series May 2025 schedule pitchers'})` → [Mon, 18 May 2026] Google News
[Sun, 17 May 2026] Padres vs Dodgers Series Preview: Pitching Probabl
- `search_web({'query': 'Dodgers recent form results May 2025'})` → [Tue, 16 Sep 2025] Google News
[Fri, 30 May 2025] Dodgers may have fix for leaky bullpen: MLB's best
- `search_web({'query': 'Padres recent form results May 2025'})` → [Thu, 02 Oct 2025] Google News
[Fri, 30 May 2025] How to watch Chicago Cubs vs. San Diego Padres Gam

## Outcome
_Pending — will be updated when market resolves_

---
*Mode: LIVE | DRY_RUN: true*