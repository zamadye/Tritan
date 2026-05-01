"""
Download semua resolved Polymarket markets dan build statistical prior per category.
Target: 10,000+ markets untuk base rate yang valid secara statistik.
"""
import requests
import json
import time
from pathlib import Path
from collections import defaultdict
from datetime import datetime

OUTPUT_FILE = Path("data/statistical_prior.json")
RAW_FILE    = Path("data/resolved_markets_raw.json")
BASE        = "https://gamma-api.polymarket.com"


def fetch_resolved_markets(limit_pages=50):
    """Fetch all resolved markets from Gamma API."""
    all_markets = []
    offset = 0
    page_size = 200

    print(f"Fetching resolved markets...")
    for page in range(limit_pages):
        try:
            r = requests.get(f"{BASE}/markets", params={
                "active": "false", "closed": "true",
                "limit": page_size, "offset": offset,
                "order": "volume24hr", "ascending": "false"
            }, timeout=15)
            markets = r.json()
            if not markets:
                break
            all_markets.extend(markets)
            offset += page_size
            print(f"  Page {page+1}: {len(markets)} markets (total: {len(all_markets)})")
            if len(markets) < page_size:
                break
            time.sleep(0.5)  # rate limit
        except Exception as e:
            print(f"  Error page {page+1}: {e}")
            break

    return all_markets


def infer_category(question: str, category: str = "") -> str:
    if category and category.strip() and category not in ("","unknown"):
        return category.lower()
    q = question.lower()
    if any(x in q for x in ["vs.", "vs ", "nba","nfl","mlb","nhl","ufc","tennis","open:","playoffs","series","match","game"]):
        return "sports"
    if any(x in q for x in ["bitcoin","btc","eth","crypto","solana"]):
        return "crypto"
    if any(x in q for x in ["iran","ceasefire","war","military","ukraine","russia","china","taiwan","nato"]):
        return "geopolitik"
    if any(x in q for x in ["election","president","congress","senate","vote","arrested","indicted"]):
        return "politics"
    if any(x in q for x in ["fed","rate","inflation","gdp","unemployment","fomc","cpi"]):
        return "economics"
    if any(x in q for x in ["openai","gpt","claude","gemini","ai model"]):
        return "ai"
    return "other"


def parse_outcome(m: dict):
    """Extract YES/NO outcome and entry price range."""
    op_raw = m.get("outcomePrices", [])
    if isinstance(op_raw, str):
        try: op = json.loads(op_raw)
        except: op = []
    else:
        op = op_raw

    outcome = None
    if len(op) >= 2:
        try:
            yes_p = float(op[0]); no_p = float(op[1])
            if yes_p >= 0.99: outcome = "YES"
            elif no_p >= 0.99: outcome = "NO"
        except: pass

    winner = m.get("winner","").lower()
    if not outcome:
        if winner in ("yes","true","1"): outcome = "YES"
        elif winner in ("no","false","0"): outcome = "NO"

    # Get last trade price as proxy for "market price before resolution"
    try:
        price = float(m.get("lastTradePrice") or 0.5)
    except:
        price = 0.5

    return outcome, price


def build_statistical_prior(markets: list) -> dict:
    """
    Build statistical prior: for each category and price bucket,
    what % of markets resolved YES?
    """
    # Buckets: 0-10%, 10-20%, ..., 90-100%
    stats = defaultdict(lambda: defaultdict(lambda: {"yes":0,"no":0,"total":0}))
    overall = defaultdict(lambda: {"yes":0,"no":0,"total":0})

    valid = 0
    for m in markets:
        outcome, price = parse_outcome(m)
        if outcome not in ("YES","NO"):
            continue
        if price <= 0 or price >= 1:
            continue

        cat = infer_category(m.get("question",""), m.get("category",""))
        bucket = f"{int(price*10)*10}-{int(price*10)*10+10}%"

        stats[cat][bucket]["total"] += 1
        stats[cat][bucket][outcome.lower()] += 1
        overall[bucket]["total"] += 1
        overall[bucket][outcome.lower()] += 1
        valid += 1

    # Calculate base rates
    prior = {"categories": {}, "overall": {}, "total_markets": valid,
             "generated_at": datetime.utcnow().isoformat()}

    for cat, buckets in stats.items():
        prior["categories"][cat] = {}
        for bucket, s in buckets.items():
            if s["total"] >= 5:  # min 5 samples
                yes_rate = s["yes"] / s["total"]
                prior["categories"][cat][bucket] = {
                    "yes_rate": round(yes_rate, 4),
                    "n": s["total"],
                    "calibration_error": round(abs(yes_rate - (int(bucket.split("-")[0])/100 + 0.05)), 4)
                }

    for bucket, s in overall.items():
        if s["total"] >= 10:
            yes_rate = s["yes"] / s["total"]
            prior["overall"][bucket] = {
                "yes_rate": round(yes_rate, 4),
                "n": s["total"],
                "market_implied": int(bucket.split("-")[0])/100 + 0.05,
                "calibration_error": round(abs(yes_rate - (int(bucket.split("-")[0])/100 + 0.05)), 4)
            }

    return prior


if __name__ == "__main__":
    print("=== TRITAN Statistical Prior Builder ===\n")

    # Fetch
    markets = fetch_resolved_markets(limit_pages=100)  # up to 20,000 markets
    print(f"\nTotal fetched: {len(markets)}")

    # Save raw
    RAW_FILE.parent.mkdir(parents=True, exist_ok=True)
    RAW_FILE.write_text(json.dumps(markets, indent=2))
    print(f"Raw data saved: {RAW_FILE}")

    # Build prior
    prior = build_statistical_prior(markets)
    OUTPUT_FILE.write_text(json.dumps(prior, indent=2))

    print(f"\n=== STATISTICAL PRIOR ===")
    print(f"Total valid markets: {prior['total_markets']}")
    print(f"\nOverall base rates (market price → actual YES rate):")
    for bucket, d in sorted(prior["overall"].items()):
        implied = d["market_implied"]
        actual  = d["yes_rate"]
        bias    = actual - implied
        flag    = "⚠️ BIASED" if abs(bias) > 0.05 else "✅"
        print(f"  {bucket:>10}: implied={implied:.0%} actual={actual:.0%} bias={bias:+.0%} n={d['n']:>5} {flag}")

    print(f"\nPer-category base rates:")
    for cat, buckets in sorted(prior["categories"].items()):
        n_total = sum(b["n"] for b in buckets.values())
        print(f"\n  [{cat}] ({n_total} markets)")
        for bucket, d in sorted(buckets.items()):
            print(f"    {bucket:>10}: actual={d['yes_rate']:.0%} n={d['n']:>4} cal_err={d['calibration_error']:.3f}")

    print(f"\nSaved to: {OUTPUT_FILE}")
