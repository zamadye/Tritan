"""Shared helpers, data loaders, and CSS for all pages."""
import sys, os, json, subprocess, re, requests
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(__file__))))
from pathlib import Path
from datetime import datetime, timezone
from dotenv import load_dotenv
import streamlit as st

load_dotenv(os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(__file__))), ".env"), override=True)

DARK_CSS = """<style>
[data-testid="metric-container"]{background:#1e1e2e;border:1px solid #313155;border-radius:10px;padding:14px 18px!important}
[data-testid="metric-container"] label{font-size:11px!important;color:#888!important;text-transform:uppercase;letter-spacing:.5px}
[data-testid="metric-container"] [data-testid="stMetricValue"]{font-size:22px!important;font-weight:700!important}
[data-testid="stExpander"]{border:1px solid #2e2e4e!important;border-radius:8px!important;margin-bottom:4px!important}
[data-testid="stSidebar"]{background:#13131f!important}
[data-testid="stSidebar"] hr{border-color:#2e2e4e!important}
.nav-btn button{width:100%!important;text-align:left!important;background:transparent!important;border:none!important;
  padding:8px 12px!important;border-radius:6px!important;font-size:14px!important;color:#ccc!important}
.nav-btn button:hover{background:#2e2e4e!important;color:#fff!important}
.status-badge{padding:4px 10px;border-radius:20px;font-size:12px;font-weight:600;display:inline-block}
hr{margin:10px 0!important;border-color:#2e2e4e!important}
div[data-testid="stVerticalBlock"] > div:has(> [data-testid="stHorizontalBlock"]) {gap:8px!important}
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
