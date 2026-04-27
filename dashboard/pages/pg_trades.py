import os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(__file__))))
import streamlit as st
from dashboard.components.shared import load_trades, get_current_mode

def render():
    mode = get_current_mode()
    trades   = load_trades(mode)
    resolved = [t for t in trades if t.get("actual_outcome")]

    st.subheader(f"📋 Trade History — {len(resolved)} resolved")

    # ── filters ───────────────────────────────────────────────────────────────
    f1,f2,f3,f4 = st.columns(4)
    f_res  = f1.selectbox("Result", ["All","WIN","LOSS","EXIT"])
    f_side = f2.selectbox("Side",   ["All","YES","NO"])
    cats   = sorted({t.get("category","") or "other" for t in resolved})
    f_cat  = f3.selectbox("Category", ["All"]+cats)
    f_q    = f4.text_input("Search", placeholder="keyword...")

    fil = resolved[:]
    if f_res == "WIN":  fil = [t for t in fil if t.get("prediction_correct")]
    elif f_res == "LOSS": fil = [t for t in fil if not t.get("prediction_correct") and t.get("actual_outcome")!="EXIT"]
    elif f_res == "EXIT": fil = [t for t in fil if t.get("actual_outcome")=="EXIT"]
    if f_side != "All": fil = [t for t in fil if t["side"]==f_side]
    if f_cat  != "All": fil = [t for t in fil if (t.get("category") or "other")==f_cat]
    if f_q:             fil = [t for t in fil if f_q.lower() in t.get("market_question","").lower()]

    fil = sorted(fil, key=lambda x: x.get("resolved_at",""), reverse=True)

    # ── pagination ────────────────────────────────────────────────────────────
    PAGE_SIZE = 20
    total_pages = max(1, (len(fil)-1)//PAGE_SIZE+1)
    pg = st.number_input("Page", 1, total_pages, 1, label_visibility="collapsed")
    st.caption(f"{len(fil)} trades · page {pg}/{total_pages}")
    page_trades = fil[(pg-1)*PAGE_SIZE : pg*PAGE_SIZE]

    # ── trade list ────────────────────────────────────────────────────────────
    for t in page_trades:
        icon = "✅" if t.get("prediction_correct") else ("🔄" if t.get("actual_outcome")=="EXIT" else "❌")
        conf = t.get("confidence_at_bet") or 0
        pnl  = t.get("pnl",0)
        with st.expander(f"{icon} {t['side']}→{t.get('actual_outcome','?')}  ${pnl:+.2f}  {conf:.0%} conf  |  {t['market_question'][:52]}"):
            c1,c2,c3,c4 = st.columns(4)
            c1.metric("P&L",        f"${pnl:+.2f}")
            c2.metric("Confidence", f"{conf:.0%}")
            c3.metric("Entry",      f"{t['price_at_entry']:.3f}")
            c4.metric("Brier",      f"{t.get('brier_score',0):.3f}")
            if t.get("exit_reason"):        st.caption(f"🚪 {t['exit_reason']}")
            if t.get("peak_price"):         st.caption(f"📈 Peak: {t['peak_price']:.3f}")
            if t.get("reasoning_summary"):  st.info(t["reasoning_summary"])
            if t.get("calibration_applied"):st.caption(f"⚙️ {t['calibration_applied']}")
