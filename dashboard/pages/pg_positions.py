import os, sys, json
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(__file__))))
from pathlib import Path
from datetime import datetime, timezone
import streamlit as st
from dashboard.components.shared import load_trades, get_live_price, get_current_mode

def render():
    mode    = get_current_mode()
    trades  = load_trades(mode)
    open_t  = [t for t in trades if not t.get("actual_outcome")]

    trail_pct = float(os.getenv("TRAILING_STOP_PCT", 0.25))
    tp_ret    = float(os.getenv("EXIT_TAKE_PROFIT",  1.0))
    sl_pct    = float(os.getenv("EXIT_STOP_LOSS",    0.33))

    st.subheader(f"📂 Open Positions ({len(open_t)})")

    if not open_t:
        st.info("No open positions."); return

    # ── summary row ───────────────────────────────────────────────────────────
    total_deployed = sum(t["size_usd"] for t in open_t)
    unreal_total   = 0
    prices_fetched = {}
    for t in open_t:
        nid = t.get("market_numeric_id","")
        if nid and nid not in prices_fetched:
            prices_fetched[nid] = get_live_price(nid)
        yes_p, no_p = prices_fetched.get(nid,(None,None))
        now_p = (yes_p if t["side"]=="YES" else no_p) if yes_p else None
        if now_p:
            shares = t["size_usd"]/t["price_at_entry"]
            unreal_total += shares*now_p - t["size_usd"]

    s1,s2,s3 = st.columns(3)
    s1.metric("Total Deployed",    f"${total_deployed:.2f}")
    s2.metric("Unrealized P&L",    f"${unreal_total:+.2f}")
    s3.metric("Positions",         str(len(open_t)))
    st.divider()

    # ── position cards ────────────────────────────────────────────────────────
    for t in open_t:
        nid   = t.get("market_numeric_id","")
        entry = t["price_at_entry"]
        side  = t["side"]
        size  = t["size_usd"]
        yes_p, no_p = prices_fetched.get(nid,(None,None))
        now_p  = (yes_p if side=="YES" else no_p) if yes_p else None
        shares = size/entry
        peak   = t.get("peak_price", entry)

        trail_sl  = peak*(1-trail_pct)
        init_sl   = entry*(1-sl_pct)
        eff_sl    = max(trail_sl, init_sl)
        tp_price  = min(entry*(1+tp_ret), 0.99)
        unreal    = round(shares*now_p - size, 2) if now_p else None
        pnl_pct   = (now_p-entry)/entry if now_p else 0
        trend     = ("📈" if pnl_pct>0.02 else "📉" if pnl_pct<-0.02 else "➡️") if now_p else "❓"
        partial   = " · PARTIAL" if t.get("partial_exited") else ""

        with st.expander(f"{trend} {side} ${size:.2f}{partial}  |  {t['market_question'][:58]}"):
            c1,c2,c3,c4 = st.columns(4)
            c1.metric("Entry",          f"{entry:.3f}")
            c2.metric("Current",        f"{now_p:.3f}" if now_p else "—",
                      delta=f"{pnl_pct:+.1%}" if now_p else None)
            c3.metric("Unrealized P&L", f"${unreal:+.2f}" if unreal is not None else "—")
            c4.metric("Peak",           f"{peak:.3f}")

            if now_p:
                rng = tp_price - eff_sl
                pos = max(0.0, min(1.0, (now_p-eff_sl)/rng)) if rng>0 else 0
                st.progress(pos, text=f"SL {eff_sl:.3f}  ←  now {now_p:.3f}  →  TP {tp_price:.3f}")

            st.caption(f"Trail SL: {eff_sl:.3f}  |  Init SL: {init_sl:.3f}  |  TP target: {tp_price:.3f}")
            if t.get("reasoning_summary"): st.info(t["reasoning_summary"])

            if st.button("🚪 Manual Exit", key=f"exit_{t['trade_id']}"):
                if now_p:
                    p = Path(f"data/{mode}_trades.json")
                    all_t = json.loads(p.read_text())
                    for tr in all_t:
                        if tr["trade_id"]==t["trade_id"]:
                            sh = tr["size_usd"]/tr["price_at_entry"]
                            tr.update({"actual_outcome":"EXIT","exit_price":now_p,"exit_reason":"MANUAL",
                                       "pnl":round(sh*now_p-tr["size_usd"],2),"prediction_correct":sh*now_p>tr["size_usd"],
                                       "resolved_at":datetime.now(timezone.utc).isoformat()})
                    p.write_text(json.dumps(all_t,indent=2))
                    st.cache_data.clear(); st.success(f"Exited at {now_p:.3f}"); st.rerun()
