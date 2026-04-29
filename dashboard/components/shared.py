"""Shared helpers, data loaders, and CSS for all pages."""
import sys, os, json, subprocess, re, requests
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(__file__))))
from pathlib import Path
from datetime import datetime, timezone
from dotenv import load_dotenv
import streamlit as st

load_dotenv(os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(__file__))), ".env"), override=True)

DARK_CSS = """<style>
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&display=swap');

html, body, [class*="css"] { font-family: 'Inter', system-ui, sans-serif !important; }
.main .block-container { padding: 0.5rem 2rem 2rem !important; max-width: 1440px !important; }

/* Metric cards */
[data-testid="metric-container"] {
  background: linear-gradient(135deg,#13132a,#16162e) !important;
  border: 1px solid #2a2a4a !important; border-radius: 12px !important;
  padding: 16px 20px !important; transition: border-color .2s !important;
}
[data-testid="metric-container"]:hover { border-color: #4a4a8a !important; }
[data-testid="metric-container"] label {
  font-size: 10px !important; font-weight: 600 !important; color: #6b7280 !important;
  text-transform: uppercase !important; letter-spacing: 1px !important;
}
[data-testid="metric-container"] [data-testid="stMetricValue"] {
  font-size: 26px !important; font-weight: 700 !important; color: #f1f5f9 !important;
}
[data-testid="metric-container"] [data-testid="stMetricDelta"] { font-size: 12px !important; }

/* Expanders */
[data-testid="stExpander"] {
  background: #0d0d1a !important; border: 1px solid #1e1e3a !important;
  border-radius: 10px !important; margin-bottom: 6px !important; transition: border-color .15s !important;
}
[data-testid="stExpander"]:hover { border-color: #3a3a6a !important; }
[data-testid="stExpander"] summary {
  font-size: 13px !important; font-weight: 500 !important;
  padding: 10px 16px !important; color: #cbd5e1 !important;
}

/* Hide chrome */
section[data-testid="stSidebar"], #MainMenu, footer, header[data-testid="stHeader"] { display: none !important; }

/* Buttons */
[data-testid="stButton"] > button {
  border-radius: 8px !important; font-size: 13px !important; font-weight: 500 !important;
  padding: 6px 14px !important; transition: all .15s !important; border-width: 1px !important;
}
[data-testid="stButton"] > button[kind="primary"] {
  background: linear-gradient(135deg,#4f46e5,#6366f1) !important;
  border-color: #4f46e5 !important; color: #fff !important;
}
[data-testid="stButton"] > button[kind="primary"]:hover {
  background: linear-gradient(135deg,#4338ca,#4f46e5) !important;
  box-shadow: 0 0 12px #4f46e540 !important;
}
[data-testid="stButton"] > button[kind="secondary"] {
  background: #0d0d1a !important; border-color: #2a2a4a !important; color: #94a3b8 !important;
}
[data-testid="stButton"] > button[kind="secondary"]:hover {
  background: #1a1a3a !important; color: #e2e8f0 !important; border-color: #4a4a8a !important;
}

/* Inputs */
[data-testid="stTextInput"] input, [data-testid="stNumberInput"] input {
  background: #0d0d1a !important; border: 1px solid #2a2a4a !important;
  border-radius: 8px !important; color: #e2e8f0 !important; font-size: 13px !important;
}
[data-testid="stSelectbox"] > div > div {
  background: #0d0d1a !important; border-color: #2a2a4a !important;
  border-radius: 8px !important; color: #e2e8f0 !important;
}

/* Tabs */
[data-testid="stTabs"] [role="tablist"] {
  background: #0a0a18 !important; border-radius: 10px !important;
  padding: 4px !important; border: 1px solid #1e1e3a !important;
}
[data-testid="stTabs"] [role="tab"] {
  font-size: 13px !important; font-weight: 500 !important;
  padding: 7px 16px !important; color: #6b7280 !important;
  border-radius: 7px !important; border: none !important;
}
[data-testid="stTabs"] [role="tab"][aria-selected="true"] {
  background: #1e1e3a !important; color: #a5b4fc !important; font-weight: 600 !important;
}

/* Alerts */
[data-testid="stInfo"]    { background: #0a1525 !important; border-left: 3px solid #3b82f6 !important; border-radius: 8px !important; font-size: 13px !important; }
[data-testid="stWarning"] { background: #150f00 !important; border-left: 3px solid #f59e0b !important; border-radius: 8px !important; font-size: 13px !important; }
[data-testid="stError"]   { background: #150000 !important; border-left: 3px solid #ef4444 !important; border-radius: 8px !important; font-size: 13px !important; }
[data-testid="stSuccess"] { background: #001510 !important; border-left: 3px solid #22c55e !important; border-radius: 8px !important; font-size: 13px !important; }

/* Progress */
[data-testid="stProgress"] > div { background: #1e1e3a !important; border-radius: 6px !important; height: 6px !important; }
[data-testid="stProgress"] > div > div { border-radius: 6px !important; }

/* Typography */
h1 { font-size: 20px !important; font-weight: 700 !important; color: #f1f5f9 !important; margin: 0 0 16px !important; }
h2 { font-size: 15px !important; font-weight: 600 !important; color: #e2e8f0 !important; margin: 14px 0 8px !important; }
h3 { font-size: 13px !important; font-weight: 600 !important; color: #94a3b8 !important; margin: 10px 0 6px !important; }
p, li { font-size: 13px !important; color: #cbd5e1 !important; line-height: 1.6 !important; }
[data-testid="stCaptionContainer"] { color: #4b5563 !important; font-size: 11px !important; }
[data-testid="stCode"] { background: #0a0a18 !important; border: 1px solid #1e1e3a !important; border-radius: 8px !important; font-size: 12px !important; }
hr { margin: 14px 0 !important; border-color: #1a1a3a !important; }

/* Slider */
[data-testid="stSlider"] [data-baseweb="slider"] div[role="slider"] { background: #6366f1 !important; border-color: #6366f1 !important; }

/* Scrollbar */
::-webkit-scrollbar { width: 5px; height: 5px; }
::-webkit-scrollbar-track { background: #0a0a18; }
::-webkit-scrollbar-thumb { background: #2a2a4a; border-radius: 3px; }
::-webkit-scrollbar-thumb:hover { background: #4a4a8a; }

/* Custom components */
.card { background: linear-gradient(135deg,#0d0d1a,#13132a); border: 1px solid #2a2a4a; border-radius: 12px; padding: 16px 20px; margin-bottom: 12px; }
.card-title { font-size: 10px; font-weight: 600; color: #6b7280; text-transform: uppercase; letter-spacing: 1px; margin-bottom: 10px; }
.card-value { font-size: 28px; font-weight: 700; line-height: 1.1; }
.card-sub { font-size: 12px; color: #6b7280; margin-top: 4px; }
.stat-row { display: flex; justify-content: space-between; align-items: center; padding: 8px 0; border-bottom: 1px solid #1a1a3a; font-size: 13px; }
.stat-row:last-child { border-bottom: none; }
.badge { display: inline-flex; align-items: center; gap: 4px; padding: 3px 10px; border-radius: 20px; font-size: 11px; font-weight: 600; }
.alert-banner { padding: 10px 16px; border-radius: 8px; font-size: 13px; font-weight: 500; margin-bottom: 12px; border-left: 3px solid #ef4444; background: #150000; }
</style>"""

def inject_css():
    st.markdown(DARK_CSS, unsafe_allow_html=True)

def badge(text, color):
    return f"<span class='status-badge' style='background:{color}22;border:1px solid {color};color:{color}'>{text}</span>"

# ── service helpers ───────────────────────────────────────────────────────────
def service_active():
    r = subprocess.run(["systemctl","is-active","polymarket-agent"], capture_output=True, text=True)
    return r.stdout.strip() == "active"

def get_current_mode():
    try:
        svc = Path("/etc/systemd/system/polymarket-agent.service").read_text()
        return "live" if "--mode live" in svc else "demo"
    except: return "demo"

def switch_mode(new_mode):
    svc_path = Path("/etc/systemd/system/polymarket-agent.service")
    svc = re.sub(r"--mode (demo|live)", f"--mode {new_mode}", svc_path.read_text())
    svc_path.write_text(svc)
    subprocess.run(["systemctl","daemon-reload"])
    subprocess.run(["systemctl","restart","polymarket-agent"])

def save_env(updates: dict):
    p = Path(".env"); txt = p.read_text()
    for k, v in updates.items():
        if re.search(f"^{k}=", txt, re.MULTILINE):
            txt = re.sub(f"^{k}=.*", f"{k}={v}", txt, flags=re.MULTILINE)
        else:
            txt += f"\n{k}={v}"
    p.write_text(txt)

def restart_agent():
    subprocess.run(["systemctl","restart","polymarket-agent"])

# ── data loaders ──────────────────────────────────────────────────────────────
@st.cache_data(ttl=30)
def load_trades(mode="demo"):
    p = Path(f"data/{mode}_trades.json")
    return json.loads(p.read_text()) if p.exists() else []

@st.cache_data(ttl=30)
def load_evolution():
    p = Path("data/evolution_lessons.json")
    return json.loads(p.read_text()) if p.exists() else {}

@st.cache_data(ttl=30)
def load_bankroll():
    p = Path("data/bankroll_state.json")
    return json.loads(p.read_text()) if p.exists() else {"level":0,"win_streak":0,"loss_streak":0}

@st.cache_data(ttl=60)
def get_live_price(nid):
    try:
        base = os.getenv("POLYMARKET_GAMMA_API","https://gamma-api.polymarket.com")
        m = requests.get(f"{base}/markets/{nid}", timeout=5).json()
        op = m.get("outcomePrices",[])
        op = json.loads(op) if isinstance(op,str) else op
        return float(op[0]) if op else None, float(op[1]) if len(op)>1 else None
    except: return None, None

@st.cache_data(ttl=120)
def get_usdc_balance():
    try:
        wallet = os.getenv("POLYGON_WALLET_ADDRESS","")
        if not wallet: return 0.0
        rpc = "https://polygon-mainnet.g.alchemy.com/v2/-LJWrAuXvUC8QszJzGzs0"
        USDC = "0x2791Bca1f2de4661ED88A30C99A7a9449Aa84174"
        data = "0x70a08231000000000000000000000000" + wallet[2:].zfill(64)
        r = requests.post(rpc, json={"jsonrpc":"2.0","method":"eth_call","params":[{"to":USDC,"data":data},"latest"],"id":1}, timeout=5)
        return int(r.json().get("result","0x0"),16)/1e6
    except: return 0.0

def compute_stats(mode="demo"):
    trades   = load_trades(mode)
    resolved = [t for t in trades if t.get("actual_outcome")]
    wins     = [t for t in resolved if t.get("prediction_correct")]
    losses   = [t for t in resolved if not t.get("prediction_correct")]
    open_t   = [t for t in trades if not t.get("actual_outcome")]
    pnl      = sum(t.get("pnl",0) for t in resolved)
    base_br  = float(os.getenv("DEMO_BANKROLL",20))
    deployed = sum(t["size_usd"] for t in open_t)
    bankroll = round(max(base_br - deployed + pnl, 0), 2)
    avg_win  = sum(t["pnl"] for t in wins)/len(wins) if wins else 0
    avg_loss = abs(sum(t["pnl"] for t in losses)/len(losses)) if losses else 0
    wr       = len(wins)/len(resolved) if resolved else 0
    rr       = avg_win/avg_loss if avg_loss else 0
    ev       = wr*avg_win - (1-wr)*avg_loss if resolved else 0
    return dict(trades=trades, resolved=resolved, wins=wins, losses=losses,
                open_t=open_t, pnl=pnl, bankroll=bankroll, deployed=deployed,
                avg_win=avg_win, avg_loss=avg_loss, wr=wr, rr=rr, ev=ev)
