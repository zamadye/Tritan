'use client'
import { useEffect, useState } from 'react'
import { LineChart, Line, XAxis, YAxis, Tooltip, ResponsiveContainer, BarChart, Bar, Cell } from 'recharts'
import { Activity, TrendingUp, DollarSign, Target, Zap, Brain, Settings, RefreshCw, Play, Square, RotateCcw } from 'lucide-react'

type Stats = {
  stats: { pnl: number; wr: number; rr: number; ev: number; bankroll: number; deployed: number; total: number; resolved: number; open: number; wins: number; losses: number }
  bankroll_state: { level: number; win_streak: number; loss_streak: number }
  evolution: any
  pnl_series: { i: number; pnl: number; correct: boolean; date: string }[]
  cat_breakdown: Record<string, { w: number; l: number; pnl: number }>
  open_positions: any[]
  recent: any[]
  llm: { daily: { calls: number; cost_usd: number; input: number; output: number } }
  brier: { model: number; naive: number; improvement: number }
}

const TABS = ['Dashboard', 'Positions', 'Trades', 'Learning', 'Settings'] as const
type Tab = typeof TABS[number]

export default function Home() {
  const [data, setData] = useState<Stats | null>(null)
  const [agent, setAgent] = useState({ active: false, mode: 'demo' })
  const [tab, setTab] = useState<Tab>('Dashboard')
  const [loading, setLoading] = useState(false)

  const refresh = async () => {
    const [s, a] = await Promise.all([fetch('/api/stats').then(r => r.json()), fetch('/api/agent').then(r => r.json())])
    setData(s); setAgent(a)
  }

  useEffect(() => { refresh(); const t = setInterval(refresh, 30000); return () => clearInterval(t) }, [])

  const agentAction = async (action: string, mode?: string) => {
    setLoading(true)
    await fetch('/api/agent', { method: 'POST', headers: { 'Content-Type': 'application/json' }, body: JSON.stringify({ action, mode }) })
    setTimeout(() => { refresh(); setLoading(false) }, 2000)
  }

  if (!data) return <div className="min-h-screen bg-[#0a0a18] flex items-center justify-center text-white">Loading...</div>

  const { stats, bankroll_state, pnl_series, cat_breakdown, open_positions, recent, llm, brier, evolution } = data

  return (
    <div className="min-h-screen bg-[#0a0a18] text-white font-sans">
      {/* Navbar */}
      <nav className="border-b border-[#1e1e3a] px-6 py-3 flex items-center gap-6">
        <span className="text-[#7c7cff] font-bold text-lg">🤖 Tritan</span>
        <div className="flex gap-1">
          {TABS.map(t => (
            <button key={t} onClick={() => setTab(t)}
              className={`px-4 py-1.5 rounded-lg text-sm font-medium transition-all ${tab === t ? 'bg-[#2d2d5e] text-[#a5b4fc]' : 'text-[#6b7280] hover:text-white hover:bg-[#1e1e3a]'}`}>
              {t}
            </button>
          ))}
        </div>
        <div className="ml-auto flex items-center gap-3">
          <span className={`text-xs px-2 py-1 rounded-full border ${agent.active ? 'border-green-500 text-green-400 bg-green-500/10' : 'border-red-500 text-red-400 bg-red-500/10'}`}>
            {agent.active ? '● ON' : '● OFF'}
          </span>
          <span className={`text-xs px-2 py-1 rounded-full border ${agent.mode === 'demo' ? 'border-blue-400 text-blue-400 bg-blue-400/10' : 'border-yellow-400 text-yellow-400 bg-yellow-400/10'}`}>
            {agent.mode === 'demo' ? '📝 DEMO' : '💰 LIVE'}
          </span>
          <button onClick={() => agentAction('start')} disabled={loading} className="p-1.5 rounded-lg bg-green-500/20 hover:bg-green-500/30 text-green-400"><Play size={14} /></button>
          <button onClick={() => agentAction('stop')} disabled={loading} className="p-1.5 rounded-lg bg-red-500/20 hover:bg-red-500/30 text-red-400"><Square size={14} /></button>
          <button onClick={() => agentAction('restart')} disabled={loading} className="p-1.5 rounded-lg bg-blue-500/20 hover:bg-blue-500/30 text-blue-400"><RotateCcw size={14} /></button>
          <button onClick={refresh} className="p-1.5 rounded-lg bg-[#1e1e3a] hover:bg-[#2e2e4e] text-[#94a3b8]"><RefreshCw size={14} /></button>
        </div>
      </nav>

      <main className="p-6 max-w-7xl mx-auto">
        {tab === 'Dashboard' && <DashboardTab stats={stats} pnl_series={pnl_series} cat_breakdown={cat_breakdown} bankroll_state={bankroll_state} llm={llm} brier={brier} recent={recent} />}
        {tab === 'Positions' && <PositionsTab positions={open_positions} />}
        {tab === 'Trades' && <TradesTab trades={recent} />}
        {tab === 'Learning' && <LearningTab evolution={evolution} brier={brier} />}
        {tab === 'Settings' && <SettingsTab />}
      </main>
    </div>
  )
}

function Metric({ label, value, sub, color }: { label: string; value: string; sub?: string; color?: string }) {
  return (
    <div className="bg-gradient-to-br from-[#13132a] to-[#16162e] border border-[#2a2a4a] rounded-xl p-4 hover:border-[#4a4a8a] transition-colors">
      <div className="text-[10px] font-semibold text-[#6b7280] uppercase tracking-widest mb-1">{label}</div>
      <div className={`text-2xl font-bold ${color || 'text-[#f1f5f9]'}`}>{value}</div>
      {sub && <div className="text-xs text-[#6b7280] mt-1">{sub}</div>}
    </div>
  )
}

function DashboardTab({ stats, pnl_series, cat_breakdown, bankroll_state, llm, brier, recent }: any) {
  const level = bankroll_state?.level || 0
  const levelColor = level > 0 ? '#22c55e' : level < 0 ? '#ef4444' : '#94a3b8'

  return (
    <div className="space-y-6">
      {/* KPI row */}
      <div className="grid grid-cols-6 gap-4">
        <Metric label="Total P&L" value={`$${stats.pnl >= 0 ? '+' : ''}${stats.pnl.toFixed(2)}`} color={stats.pnl >= 0 ? '#22c55e' : '#ef4444'} />
        <Metric label="Win Rate" value={`${(stats.wr * 100).toFixed(1)}%`} sub={`${stats.wins}W / ${stats.losses}L`} />
        <Metric label="R:R Ratio" value={`${stats.rr.toFixed(2)}:1`} sub={`Break-even: ${(1/(1+stats.rr)*100).toFixed(0)}%`} />
        <Metric label="EV/Trade" value={`$${stats.ev >= 0 ? '+' : ''}${stats.ev.toFixed(3)}`} color={stats.ev >= 0 ? '#22c55e' : '#ef4444'} />
        <Metric label="Bankroll" value={`$${stats.bankroll.toFixed(2)}`} sub={`-$${stats.deployed.toFixed(2)} deployed`} />
        <Metric label="Open" value={`${stats.open}`} sub={`${stats.resolved} resolved`} />
      </div>

      <div className="grid grid-cols-3 gap-6">
        {/* P&L Chart */}
        <div className="col-span-2 bg-[#13132a] border border-[#2a2a4a] rounded-xl p-4">
          <h3 className="text-sm font-semibold text-[#e2e8f0] mb-4">Cumulative P&L</h3>
          <ResponsiveContainer width="100%" height={220}>
            <LineChart data={pnl_series}>
              <XAxis dataKey="i" hide />
              <YAxis tick={{ fill: '#6b7280', fontSize: 11 }} />
              <Tooltip contentStyle={{ background: '#16162a', border: '1px solid #2a2a4a', borderRadius: 8 }} labelStyle={{ color: '#94a3b8' }} formatter={(v: any) => [`$${v.toFixed(2)}`, 'P&L']} />
              <Line type="monotone" dataKey="pnl" stroke="#6366f1" strokeWidth={2} dot={false} />
            </LineChart>
          </ResponsiveContainer>
        </div>

        {/* Right panel */}
        <div className="space-y-4">
          {/* Compounding */}
          <div className="bg-[#13132a] border border-[#2a2a4a] rounded-xl p-4">
            <div className="text-[10px] font-semibold text-[#6b7280] uppercase tracking-widest mb-2">Compounding</div>
            <div className="text-3xl font-bold mb-1" style={{ color: levelColor }}>{level >= 0 ? '+' : ''}{level}</div>
            <div className="text-xs text-[#6b7280]">Kelly ×{Math.max(0.5, Math.min(2.0, 1 + level * 0.1)).toFixed(2)} (frozen)</div>
            <div className="mt-3 space-y-1.5">
              <div className="text-xs text-[#6b7280]">Win streak {bankroll_state?.win_streak || 0}</div>
              <div className="h-1.5 bg-[#1e1e3a] rounded-full"><div className="h-full bg-green-500 rounded-full" style={{ width: `${Math.min(100, (bankroll_state?.win_streak || 0) * 20)}%` }} /></div>
              <div className="text-xs text-[#6b7280]">Loss streak {bankroll_state?.loss_streak || 0}</div>
              <div className="h-1.5 bg-[#1e1e3a] rounded-full"><div className="h-full bg-red-500 rounded-full" style={{ width: `${Math.min(100, (bankroll_state?.loss_streak || 0) * 20)}%` }} /></div>
            </div>
          </div>

          {/* Brier score */}
          <div className="bg-[#13132a] border border-[#2a2a4a] rounded-xl p-4">
            <div className="text-[10px] font-semibold text-[#6b7280] uppercase tracking-widest mb-2">Model vs Naive</div>
            <div className="flex justify-between text-sm mb-1"><span className="text-[#94a3b8]">Model Brier</span><span className="text-green-400 font-mono">{brier.model}</span></div>
            <div className="flex justify-between text-sm mb-2"><span className="text-[#94a3b8]">Naive Brier</span><span className="text-[#6b7280] font-mono">{brier.naive}</span></div>
            <div className="text-xs text-green-400">+{brier.improvement}% improvement ✓</div>
          </div>

          {/* LLM cost */}
          <div className="bg-[#13132a] border border-[#2a2a4a] rounded-xl p-4">
            <div className="text-[10px] font-semibold text-[#6b7280] uppercase tracking-widest mb-2">LLM Today</div>
            <div className="text-xl font-bold text-[#f1f5f9]">${(llm?.daily?.cost_usd || 0).toFixed(3)}</div>
            <div className="text-xs text-[#6b7280]">{llm?.daily?.calls || 0} calls · limit $2.00</div>
            <div className="mt-2 h-1.5 bg-[#1e1e3a] rounded-full">
              <div className="h-full bg-[#6366f1] rounded-full" style={{ width: `${Math.min(100, ((llm?.daily?.cost_usd || 0) / 2) * 100)}%` }} />
            </div>
          </div>
        </div>
      </div>

      {/* Category + Recent */}
      <div className="grid grid-cols-2 gap-6">
        <div className="bg-[#13132a] border border-[#2a2a4a] rounded-xl p-4">
          <h3 className="text-sm font-semibold text-[#e2e8f0] mb-4">By Category</h3>
          <ResponsiveContainer width="100%" height={180}>
            <BarChart data={Object.entries(cat_breakdown).map(([cat, s]: any) => ({ cat, wins: s.w, losses: s.l }))}>
              <XAxis dataKey="cat" tick={{ fill: '#6b7280', fontSize: 11 }} />
              <YAxis tick={{ fill: '#6b7280', fontSize: 11 }} />
              <Tooltip contentStyle={{ background: '#16162a', border: '1px solid #2a2a4a', borderRadius: 8 }} />
              <Bar dataKey="wins" fill="#22c55e" radius={[3,3,0,0]} />
              <Bar dataKey="losses" fill="#ef4444" radius={[3,3,0,0]} />
            </BarChart>
          </ResponsiveContainer>
        </div>

        <div className="bg-[#13132a] border border-[#2a2a4a] rounded-xl p-4">
          <h3 className="text-sm font-semibold text-[#e2e8f0] mb-3">Recent Activity</h3>
          <div className="space-y-2">
            {recent.slice(0, 6).map((t: any, i: number) => (
              <div key={i} className="flex items-center gap-3 text-xs">
                <span className={t.prediction_correct ? 'text-green-400' : 'text-red-400'}>{t.prediction_correct ? '✓' : '✗'}</span>
                <span className="text-[#94a3b8] flex-1 truncate">{t.market_question?.slice(0, 45)}</span>
                <span className={`font-mono font-semibold ${(t.pnl || 0) >= 0 ? 'text-green-400' : 'text-red-400'}`}>${(t.pnl || 0) >= 0 ? '+' : ''}{(t.pnl || 0).toFixed(2)}</span>
              </div>
            ))}
          </div>
        </div>
      </div>
    </div>
  )
}

function PositionsTab({ positions }: { positions: any[] }) {
  if (!positions.length) return <div className="text-center text-[#6b7280] py-20">No open positions</div>
  return (
    <div className="space-y-3">
      <h2 className="text-lg font-semibold">Open Positions ({positions.length})</h2>
      {positions.map((t: any, i: number) => (
        <div key={i} className="bg-[#13132a] border border-[#2a2a4a] rounded-xl p-4">
          <div className="flex items-start justify-between mb-3">
            <div>
              <span className={`text-xs px-2 py-0.5 rounded-full mr-2 ${t.side === 'YES' ? 'bg-green-500/20 text-green-400' : 'bg-red-500/20 text-red-400'}`}>{t.side}</span>
              <span className="text-sm text-[#e2e8f0]">{t.market_question?.slice(0, 60)}</span>
            </div>
            <span className="text-xs text-[#6b7280]">{t.category || '?'}</span>
          </div>
          <div className="grid grid-cols-4 gap-4 text-xs">
            <div><div className="text-[#6b7280]">Entry</div><div className="font-mono text-[#e2e8f0]">{(t.price_at_entry * 100).toFixed(1)}%</div></div>
            <div><div className="text-[#6b7280]">Size</div><div className="font-mono text-[#e2e8f0]">${t.size_usd}</div></div>
            <div><div className="text-[#6b7280]">Peak</div><div className="font-mono text-[#e2e8f0]">{t.peak_price ? (t.peak_price * 100).toFixed(1) + '%' : '—'}</div></div>
            <div><div className="text-[#6b7280]">Confidence</div><div className="font-mono text-[#e2e8f0]">{((t.confidence_at_bet || 0) * 100).toFixed(0)}%</div></div>
          </div>
          {t.reasoning_summary && <div className="mt-2 text-xs text-[#6b7280] bg-[#0d0d1a] rounded-lg p-2">{t.reasoning_summary.slice(0, 120)}</div>}
        </div>
      ))}
    </div>
  )
}

function TradesTab({ trades }: { trades: any[] }) {
  return (
    <div className="space-y-2">
      <h2 className="text-lg font-semibold mb-4">Recent Trades</h2>
      {trades.map((t: any, i: number) => (
        <div key={i} className={`bg-[#13132a] border rounded-xl p-3 flex items-center gap-4 ${t.prediction_correct ? 'border-green-500/20' : 'border-red-500/20'}`}>
          <span className={`text-lg ${t.prediction_correct ? 'text-green-400' : 'text-red-400'}`}>{t.prediction_correct ? '✓' : '✗'}</span>
          <div className="flex-1 min-w-0">
            <div className="text-sm text-[#e2e8f0] truncate">{t.market_question?.slice(0, 60)}</div>
            <div className="text-xs text-[#6b7280] mt-0.5">{t.side} · {t.category || '?'} · {(t.resolved_at || '').slice(0, 10)}</div>
          </div>
          <div className="text-right">
            <div className={`font-mono font-semibold ${(t.pnl || 0) >= 0 ? 'text-green-400' : 'text-red-400'}`}>${(t.pnl || 0) >= 0 ? '+' : ''}{(t.pnl || 0).toFixed(2)}</div>
            <div className="text-xs text-[#6b7280]">{t.exit_reason?.slice(0, 20) || 'RESOLVED'}</div>
          </div>
        </div>
      ))}
    </div>
  )
}

function LearningTab({ evolution, brier }: any) {
  const ep = evolution?.exit_patterns || {}
  const total_ep = Object.values(ep).reduce((s: any, v: any) => s + v, 0) as number
  return (
    <div className="space-y-6">
      <h2 className="text-lg font-semibold">Evolution Learning</h2>
      <div className="grid grid-cols-3 gap-4">
        <Metric label="Resolved Trades" value={String(evolution?.total_resolved || 0)} />
        <Metric label="Win Rate" value={`${((evolution?.overall_win_rate || 0) * 100).toFixed(0)}%`} />
        <Metric label="Model Improvement" value={`+${brier.improvement}%`} color="#22c55e" sub="vs naive baseline" />
      </div>

      <div className="grid grid-cols-2 gap-6">
        <div className="bg-[#13132a] border border-[#2a2a4a] rounded-xl p-4">
          <h3 className="text-sm font-semibold text-[#e2e8f0] mb-3">Exit Breakdown</h3>
          {Object.entries(ep).map(([k, v]: any) => (
            <div key={k} className="flex items-center gap-3 mb-2">
              <span className="text-xs text-[#94a3b8] w-32">{k}</span>
              <div className="flex-1 h-2 bg-[#1e1e3a] rounded-full">
                <div className="h-full rounded-full bg-[#6366f1]" style={{ width: `${total_ep ? (v / total_ep) * 100 : 0}%` }} />
              </div>
              <span className="text-xs text-[#6b7280] w-8 text-right">{v}</span>
            </div>
          ))}
        </div>

        <div className="bg-[#13132a] border border-[#2a2a4a] rounded-xl p-4">
          <h3 className="text-sm font-semibold text-[#e2e8f0] mb-3">Recent Losses</h3>
          {(evolution?.recent_mistakes || []).map((m: any, i: number) => (
            <div key={i} className="mb-3 p-2 bg-[#0d0d1a] rounded-lg">
              <div className="text-xs text-[#94a3b8] truncate">{m.question?.slice(0, 55)}</div>
              <div className="text-xs text-red-400 mt-1">{m.lesson?.slice(0, 80)}</div>
            </div>
          ))}
        </div>
      </div>
    </div>
  )
}

function SettingsTab() {
  const [env, setEnv] = useState<Record<string, string>>({})
  const [saved, setSaved] = useState(false)

  useEffect(() => { fetch('/api/settings').then(r => r.json()).then(setEnv) }, [])

  const save = async (updates: Record<string, string>) => {
    await fetch('/api/settings', { method: 'POST', headers: { 'Content-Type': 'application/json' }, body: JSON.stringify(updates) })
    setSaved(true); setTimeout(() => setSaved(false), 2000)
  }

  const Field = ({ k, label }: { k: string; label: string }) => (
    <div>
      <label className="text-xs text-[#6b7280] block mb-1">{label}</label>
      <input value={env[k] || ''} onChange={e => setEnv(prev => ({ ...prev, [k]: e.target.value }))}
        className="w-full bg-[#0d0d1a] border border-[#2a2a4a] rounded-lg px-3 py-2 text-sm text-[#e2e8f0] focus:border-[#6366f1] outline-none" />
    </div>
  )

  return (
    <div className="space-y-6 max-w-2xl">
      <h2 className="text-lg font-semibold">Settings</h2>
      {saved && <div className="bg-green-500/20 border border-green-500/40 text-green-400 text-sm px-4 py-2 rounded-lg">✓ Saved & agent restarted</div>}

      <div className="bg-[#13132a] border border-[#2a2a4a] rounded-xl p-5 space-y-4">
        <h3 className="text-sm font-semibold text-[#e2e8f0]">Strategy</h3>
        <div className="grid grid-cols-2 gap-4">
          <Field k="MIN_CONFIDENCE" label="Min Confidence" />
          <Field k="EDGE_THRESHOLD" label="Edge Threshold" />
          <Field k="MIN_BET_SIZE" label="Min Bet ($)" />
          <Field k="MAX_BET_SIZE" label="Max Bet ($)" />
        </div>
        <button onClick={() => save({ MIN_CONFIDENCE: env.MIN_CONFIDENCE, EDGE_THRESHOLD: env.EDGE_THRESHOLD, MIN_BET_SIZE: env.MIN_BET_SIZE, MAX_BET_SIZE: env.MAX_BET_SIZE })}
          className="bg-[#4f46e5] hover:bg-[#4338ca] text-white text-sm px-4 py-2 rounded-lg transition-colors">Save Strategy</button>
      </div>

      <div className="bg-[#13132a] border border-[#2a2a4a] rounded-xl p-5 space-y-4">
        <h3 className="text-sm font-semibold text-[#e2e8f0]">Exit Rules</h3>
        <div className="grid grid-cols-2 gap-4">
          <Field k="EXIT_TAKE_PROFIT" label="Take Profit (%)" />
          <Field k="TRAILING_STOP_PCT" label="Trailing Stop (%)" />
          <Field k="EXIT_STOP_LOSS" label="Stop Loss (%)" />
          <Field k="EXIT_MAX_HOURS" label="Max Hold (hours)" />
        </div>
        <button onClick={() => save({ EXIT_TAKE_PROFIT: env.EXIT_TAKE_PROFIT, TRAILING_STOP_PCT: env.TRAILING_STOP_PCT, EXIT_STOP_LOSS: env.EXIT_STOP_LOSS, EXIT_MAX_HOURS: env.EXIT_MAX_HOURS })}
          className="bg-[#4f46e5] hover:bg-[#4338ca] text-white text-sm px-4 py-2 rounded-lg transition-colors">Save Exit Rules</button>
      </div>

      <div className="bg-[#13132a] border border-[#2a2a4a] rounded-xl p-5 space-y-4">
        <h3 className="text-sm font-semibold text-[#e2e8f0]">Scan</h3>
        <div className="grid grid-cols-2 gap-4">
          <Field k="SCAN_INTERVAL_MINUTES" label="Off-peak interval (min)" />
          <Field k="SCAN_INTERVAL_ACTIVE_MINUTES" label="Active interval (min)" />
          <Field k="MAX_LLM_CALLS_PER_CYCLE" label="Max LLM calls/cycle" />
          <Field k="LLM_DAILY_COST_LIMIT_USD" label="Daily LLM limit ($)" />
        </div>
        <button onClick={() => save({ SCAN_INTERVAL_MINUTES: env.SCAN_INTERVAL_MINUTES, SCAN_INTERVAL_ACTIVE_MINUTES: env.SCAN_INTERVAL_ACTIVE_MINUTES, MAX_LLM_CALLS_PER_CYCLE: env.MAX_LLM_CALLS_PER_CYCLE, LLM_DAILY_COST_LIMIT_USD: env.LLM_DAILY_COST_LIMIT_USD })}
          className="bg-[#4f46e5] hover:bg-[#4338ca] text-white text-sm px-4 py-2 rounded-lg transition-colors">Save Scan Settings</button>
      </div>
    </div>
  )
}
