# Market Analysis — 2026-05-21 13:14 UTC

## Market
- **Question:** Shenzhen Leopards vs. Zhejiang Lions
- **Category:** sports
- **YES Price:** 57.0%
- **Days Left:** 6
- **Volume 24h:** $104,443
- **Liquidity:** $24,894

## Statistical Prior
- **p_base:** 60.4%
- **Source:** logistic:sports
- **N (historical):** 6077
- **Raw gap:** 3.4%

## News Sources Fetched
### Macro Context
- Fear&Greed: 29/100 (Fear) | trend: improving
- BTC: $77,255 (-0.2% 24h) → neutral
- Fear&Greed: 29/100 (Fear) | 7d trend: improving
- BTC: $77,241 (-0.2% 24h) → neutral
- Fed market expectations:

### General
- [FEAR&GREED 7d trend] 29(Fear) → 27(Fear) → 25(Extr) → 28(Fear) | sentiment improving
- Will the Fed increase interest rates by 50+ bps after the Ju → YES=50%
- Will the Fed increase interest rates by 25 bps after the Jun → YES=50%

### Multi-Source
- [MULTI-SOURCE NEWS] 2 sources for: shenzhen leopards zhejiang lions
- [Bing News]
- [Thu, 27 Mar 2025] shenzhen leopards zhejiang lions
- → Barry Brown Jr. scored 25 points as the Zhejiang Lions routed the Ningbo Rockets 132-90 in a Chinese Basketball Association (CBA) regular-season gam
- [Wed, 26 Mar 2025] CBA: Zhejiang Lions crush Ningbo Rockets
- → XI'AN, China, March 27 (Xinhua) -- Barry Brown Jr. scored 25 points as the Zhejiang Lions routed the Ningbo Rockets 132-90 in a Chinese Basketball A
- [] CBA Review: Zhejiang Lions crush Ningbo Rockets
- [Metaculus]

## LLM Decision
- **Action:** SKIP
- **Confidence:** 62%
- **p_true:** 56.4%
- **Information Gap:** False
- **Crowd Bias:** False
- **Catalyst Type:** STATISTICAL_PATTERN
- **Catalyst Strength:** 0.60

### Reasoning
Markets at 57% YES price historically resolve YES only 44.7% of the time (n=13,967), suggesting a ~12.3% edge for NO bet. No specific match news found to counter this statistical pattern.

## Gate Result
- **Passed:** ❌ NO
- **Reason:** no stat edge gap=3%<5%

## Tool Calls
- `get_sports_data({'sport': 'nba', 'team': 'Shenzhen Leopards'})` → No injury data found for nba Shenzhen Leopards
- `get_odds({'sport': 'basketball_nba', 'team': 'Shenzhen Leopards'})` → Odds API error: 401 {"message":"Usage quota has been reached. See usage plans at https://the-odds-ap
- `search_web({'query': 'Shenzhen Leopards vs Zhejiang Lions CBA 2025'})` → [Mon, 12 Feb 2024] Google News
[Thu, 03 Apr 2025] Shenzhen Leopards vs Zhejiang Lions: Scores, Resul
- `search_web({'query': 'CBA playoffs 2025 Shenzhen Leopards injury report'})` → [Sat, 27 Dec 2025] Google News
[Sun, 21 Dec 2025] Zhejiang Lions vs Shenzhen Leopards Prediction, Be
- `get_market_context({'keyword': 'CBA basketball Shenzhen Leopards Zhejiang'})` → No related markets found for 'CBA basketball Shenzhen Leopards Zhejiang'
- `search_web({'query': 'CBA Shenzhen Leopards recent form 2025'})` → [Thu, 11 Dec 2025] Google News
[Mon, 12 Feb 2024] Preview: CBA shifts to FIBA timing rules as power 
- `search_web({'query': 'Zhejiang Lions CBA 2025 performance'})` → [Wed, 21 May 2025] Google News
[Wed, 21 May 2025] Zhejiang Lions’ triumph could herald shifting focu
- `search_web({'query': '"Shenzhen Leopards" "Zhejiang Lions" CBA June 2025'})` → [Tue, 10 Jun 2025] Google News
[Sun, 05 Feb 2023] Hu, Yang lead China men's basketball national team
- `search_web({'query': 'CBA semi-finals Shenzhen Leopards Zhejiang Lions 2025 playoffs'})` → [Fri, 15 May 2026] Google News
[] Zhejiang Lions vs Shenzhen Leopards prediction 16 May 2026 - TheTo

## Outcome
_Pending — will be updated when market resolves_

---
*Mode: LIVE | DRY_RUN: true*