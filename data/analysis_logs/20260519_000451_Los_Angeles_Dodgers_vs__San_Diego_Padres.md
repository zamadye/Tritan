# Market Analysis — 2026-05-19 00:04 UTC

## Market
- **Question:** Los Angeles Dodgers vs. San Diego Padres
- **Category:** sports
- **YES Price:** 57.0%
- **Days Left:** 7
- **Volume 24h:** $131,391
- **Liquidity:** $499,935

## Statistical Prior
- **p_base:** 60.4%
- **Source:** logistic:sports
- **N (historical):** 6077
- **Raw gap:** 3.4%

## News Sources Fetched
### Macro Context
- Fear&Greed: 25/100 (Extreme Fear) | trend: deteriorating
- BTC: $76,966 (-0.6% 24h) → neutral
- Fear&Greed: 25/100 (Extreme Fear) | 7d trend: deteriorating
- BTC: $76,946 (-0.6% 24h) → neutral

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
- → Siani only spent three months with the Dodgers organization after being claimed in February. The 26-year-old outfielder never appeared in a Major Le
- [Mon, 18 May 2026] Dodgers Lose Player to Orioles Before Padres Game
- → Petco Park is the location where the San Diego Padres (27-18) will take on the Los Angeles Dodgers (28-18) on Tuesday. The moneyline on this game ha
- [Mon, 18 May 2026] Los Angeles Dodgers vs San Diego Padres Prediction, 5/19/2026 MLB Picks, Best Bets &amp; Odds
- → The Los Angeles Dodgers (29-18) meet the San Diego Padres( 28-18) to start a three-game series between the NL West rivals. The Dodgers have won five

## LLM Decision
- **Action:** SKIP
- **Confidence:** 52%
- **p_true:** 60.4%
- **Information Gap:** True
- **Crowd Bias:** False
- **Catalyst Type:** STATISTICAL
- **Catalyst Strength:** 0.40

### Reasoning
Contradictory signals prevent confident action. Stat signal (n=13,967) is strong: markets at 57% resolve YES only 44.7%, suggesting YES overpriced by ~12pts. However, base rate (60%, n=6077) suggests YES underpriced by 3pts — direct contradiction. Gap (3%) below 5% gate threshold. Pattern data shows 50-60% entry range has weak 40% WR (n=5). Two prior SKIPs on same market for identical reasons. Context slightly favors Padres (won Aug 22, now lead NL West; Dodgers' Blake Snell on IL), but no new breaking catalyst to resolve signal conflict. Information gap exists but too ambiguous to exploit profitably.

## Gate Result
- **Passed:** ❌ NO
- **Reason:** no stat edge gap=3%<5%

## Tool Calls
- `get_sports_data({'sport': 'mlb', 'team': 'Los Angeles Dodgers'})` → INJURY [los angeles dodgers] Brusdar Graterol (RP): 60-Day-IL
INJURY [los angeles dodgers] Jack Drey
- `get_sports_data({'sport': 'mlb', 'team': 'San Diego Padres'})` → INJURY [san diego padres] German Marquez (SP): 15-Day-IL
INJURY [san diego padres] Jhony Brito (RP):
- `search_web({'query': 'Los Angeles Dodgers vs San Diego Padres recent results 2025'})` → [Fri, 22 Aug 2025] Google News
[Wed, 18 Mar 2026] Los Angeles Dodgers at San Diego Padres Game Story
- `search_web({'query': 'Dodgers Padres head to head 2025 series'})` → [Mon, 18 May 2026] Google News
[Mon, 18 May 2026] Not to worry, there are more rivalries on tap this
- `search_web({'query': 'Dodgers Padres next game August 2025 series schedule'})` → [Wed, 13 Aug 2025] Google News
[Fri, 06 Mar 2026] San Diego Padres at Los Angeles Dodgers Preview - 
- `search_web({'query': '"Dodgers" "Padres" game today August 23 2025 starting pitchers'})` → [Mon, 18 May 2026] Google News
[Sat, 23 Aug 2025] Rivalry Returns: Padres, Dodgers Clash For First T
- `get_market_context({'keyword': 'Dodgers Padres'})` → No related markets found for 'Dodgers Padres'
- `search_web({'query': 'Polymarket Dodgers Padres baseball prediction market'})` → [Mon, 18 May 2026] Google News
[Sun, 17 May 2026] Memorial Day Week Polymarket promo code “SILIVE” u
- `get_odds({'sport': 'baseball_mlb', 'team': 'Dodgers'})` → Odds API error: 401 {"message":"Usage quota has been reached. See usage plans at https://the-odds-ap
- `search_web({'query': '"Los Angeles Dodgers" "San Diego Padres" August 2025 starting pitcher'})` → [Mon, 18 May 2026] Google News
[Sat, 24 Jan 2026] Rivalry Returns: Padres, Dodgers Clash For First T

## Outcome
_Pending — will be updated when market resolves_

---
*Mode: LIVE | DRY_RUN: true*