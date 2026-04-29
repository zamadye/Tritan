import os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(__file__))))
import streamlit as st
from dashboard.components.shared import load_trades, get_current_mode

def render():
    mode     = get_current_mode()
    trades   = load_trades(mode)
    resolved = [t for t in trades if t.get("actual_outcome")]

    st.markdown(f"<h2>📋 Trade History <span style='font-size:13px;font-weight:400;color:#6b7280'>({len(resolved)} resolved)</span></h2>", unsafe_allow_html=True)

    # ── filters ───────────────────────────────────────────────────────────────
    f1,f2,f3,f4 = st.columns([1,1,1.2,2.5])
    f_res  = f1.selectbox("Result",   ["All","WIN","LOSS","EXIT"], label_visibility="collapsed")
    f_side = f2.selectbox("Side",     ["All","YES","NO"],          label_visibility="collapsed")
    cats   = sorted({t.get("category","") or "other" for t in resolved})
    f_cat  = f3.selectbox("Category", ["All"]+cats,                label_visibility="collapsed")
    f_q    = f4.text_input("",        placeholder="🔍 Search market...", label_visibility="collapsed")

    fil = resolved[:]
    if f_res == "WIN":    fil = [t for t in fil if t.get("prediction_correct")]
    elif f_res == "LOSS": fil = [t for t in fil if not t.get("prediction_correct") and t.get("actual_outcome")!="EXIT"]
    elif f_res == "EXIT": fil = [t for t in fil if t.get("actual_outcome")=="EXIT"]
    if f_side != "All":   fil = [t for t in fil if t["side"]==f_side]
    if f_cat  != "All":   fil = [t for t in fil if (t.get("category") or "other")==f_cat]
    if f_q:               fil = [t for t in fil if f_q.lower() in t.get("market_question","").lower()]
    fil = sorted(fil, key=lambda x: x.get("resolved_at",""), reverse=True)

    # ── pagination ────────────────────────────────────────────────────────────
    PAGE_SIZE   = 20
    total_pages = max(1, (len(fil)-1)//PAGE_SIZE+1)
    pa, pb = st.columns([5,1])
    pa.markdown(f"<div style='font-size:12px;color:#6b7280;padding-top:8px'>{len(fil)} trades · page {1}/{total_pages}</div>", unsafe_allow_html=True)
    pg = pb.number_input("pg", 1, total_pages, 1, label_visibility="collapsed")
    page_trades = fil[(pg-1)*PAGE_SIZE : pg*PAGE_SIZE]

    st.markdown("<div style='height:6px'></div>", unsafe_allow_html=True)

    # ── trade rows ────────────────────────────────────────────────────────────
    for t in page_trades:
        correct = t.get("prediction_correct")
        outcome = t.get("actual_outcome","?")
        pnl     = t.get("pnl",0) or 0
        conf    = t.get("confidence_at_bet") or 0
        entry   = t.get("price_at_entry",0)
        brier   = t.get("brier_score",0) or 0
        icon    = "✓" if correct else ("⇄" if outcome=="EXIT" else "✗")

        with st.expander(f"{icon}  {t['side']} → {outcome}   ${pnl:+.2f}   {conf:.0%} conf   ·   {t['market_question'][:55]}"):
            c1,c2,c3,c4 = st.columns(4)
            c1.metric("P&L",        f"${pnl:+.2f}")
            c2.metric("Confidence", f"{conf:.0%}")
            c3.metric("Entry",      f"{entry:.3f}")
            c4.metric("Brier",      f"{brier:.3f}")
            if t.get("exit_reason"):
                st.markdown(f"<div style='font-size:12px;color:#94a3b8;margin-top:4px'>🚪 {t['exit_reason']}</div>", unsafe_allow_html=True)
            if t.get("peak_price"):
                st.markdown(f"<div style='font-size:12px;color:#94a3b8'>📈 Peak: {t['peak_price']:.3f}</div>", unsafe_allow_html=True)
            if t.get("reasoning_summary"):
                st.info(t["reasoning_summary"])
            if t.get("calibration_applied"):
                st.markdown(f"<div style='font-size:11px;color:#6b7280;margin-top:4px'>⚙️ {t['calibration_applied']}</div>", unsafe_allow_html=True)
