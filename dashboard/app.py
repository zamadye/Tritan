"""Poly-Agent Admin — Entry point with top navbar."""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.dirname(__file__)))
import subprocess
import streamlit as st
from pathlib import Path

st.set_page_config(page_title="Poly-Agent", page_icon="🤖", layout="wide", initial_sidebar_state="collapsed")

from dashboard.components.shared import (
    inject_css, badge, service_active, get_current_mode,
    switch_mode, restart_agent, load_trades, load_evolution,
    load_bankroll, compute_stats, get_usdc_balance
)

inject_css()

# ── top navbar ────────────────────────────────────────────────────────────────
mode   = get_current_mode()
active = service_active()

st.markdown("""<style>
section[data-testid="stSidebar"]{display:none}
#MainMenu{visibility:hidden}
header[data-testid="stHeader"]{background:#0d0d1a;border-bottom:1px solid #2e2e4e}
.topbar{display:flex;align-items:center;gap:16px;padding:0 8px;flex-wrap:wrap}
.topbar-title{font-size:18px;font-weight:700;color:#fff;margin-right:8px}
.nav-link{padding:6px 14px;border-radius:6px;font-size:13px;font-weight:500;
  cursor:pointer;border:1px solid transparent;color:#aaa;text-decoration:none;white-space:nowrap}
.nav-link:hover,.nav-link.active{background:#2e2e4e;color:#fff;border-color:#3e3e6e}
.nav-link.active{color:#7c7cff}
</style>""", unsafe_allow_html=True)

# Nav state
if "page" not in st.session_state:
    st.session_state.page = "dashboard"

# Top bar: logo + nav + status + controls
col_nav, col_ctrl = st.columns([5, 1])

with col_nav:
    pages = [
        ("dashboard",  "📊 Dashboard"),
        ("trades",     "📋 Trades"),
        ("positions",  "📂 Positions"),
        ("scanner",    "🔍 Scanner"),
        ("learning",   "🧠 Learning"),
        ("settings",   "⚙️ Settings"),
    ]
    cols = st.columns([1.2] + [1]*len(pages))
    cols[0].markdown("**🤖 Poly-Agent**")
    for i, (key, label) in enumerate(pages):
        if cols[i+1].button(label, key=f"nav_{key}",
                            type="primary" if st.session_state.page==key else "secondary",
                            use_container_width=True):
            st.session_state.page = key
            st.rerun()

with col_ctrl:
    mc = "#00cc88" if mode=="demo" else "#ff9900"
    ac = "#00cc88" if active else "#ff4444"
    st.markdown(
        f"{badge('🟢 ON' if active else '🔴 OFF', ac)} "
        f"{badge('📝 DEMO' if mode=='demo' else '💰 LIVE', mc)}",
        unsafe_allow_html=True
    )

st.divider()

# ── auto-refresh ──────────────────────────────────────────────────────────────
try:
    from streamlit_autorefresh import st_autorefresh
    st_autorefresh(interval=30000, key="ar")
except ImportError:
    pass

# ── route to page ─────────────────────────────────────────────────────────────
page = st.session_state.page

if page == "dashboard":
    from dashboard.pages.pg_dashboard import render
elif page == "trades":
    from dashboard.pages.pg_trades import render
elif page == "positions":
    from dashboard.pages.pg_positions import render
elif page == "scanner":
    from dashboard.pages.pg_scanner import render
elif page == "learning":
    from dashboard.pages.pg_learning import render
elif page == "settings":
    from dashboard.pages.pg_settings import render
else:
    from dashboard.pages.pg_dashboard import render

render()

st.markdown(f"<div style='text-align:right;color:#555;font-size:11px;margin-top:20px'>Poly-Agent Admin v3.1 · {__import__('datetime').datetime.utcnow().strftime('%H:%M UTC')}</div>", unsafe_allow_html=True)
