'use client'
import { Metric, Card, Badge } from '@/components/ui'
import { PnLChart, CategoryChart } from '@/components/charts'
import type { DashboardData } from '@/types'

export function Overview({ data, account }: { data: DashboardData; account?: any }) {
  const { stats, brier, pnl_series, cat_breakdown, bankroll_state, llm, recent_full } = data
  const level = bankroll_state?.level || 0
  const lc = level > 0 ? '#22c55e' : level < 0 ? '#ef4444' : '#94a3b8'
  const today = llm?.daily || {}
  const isLive = account?.usdc_balance > 0

  return (
    <div className="space-y-5">
      {/* Live account banner */}
      {account && (
        <div className={`flex items-center gap-4 px-4 py-3 rounded-xl border text-xs ${isLive ? 'border-green-500/30 bg-green-500/5' : 'border-[#2a2a4a] bg-[#13132a]'}`}>
          <span className={`font-bold text-sm ${isLive ? 'text-green-400' : 'text-[#6b7280]'}`}>
            {isLive ? '💰 LIVE ACCOUNT' : '📝 DEMO MODE'}
          </span>
          <span className="text-[#94a3b8]">Wallet: <span className="font-mono">{account.wallet || '—'}</span></span>
          <span className="text-[#94a3b8]">USDC Balance: <span className={`font-mono font-bold ${isLive ? 'text-green-400' : 'text-[#6b7280]'}`}>${account.usdc_balance?.toFixed(2) || '0.00'}</span></span>
          {account.positions?.length > 0 && (
            <span className="text-[#94a3b8]">On-chain positions: <span className="font-mono text-[#a5b4fc]">{account.positions.length}</span></span>
          )}
          <span className="ml-auto text-[#4b5563]">Synced from Polygon</span>
        </div>
      )}
      {/* KPI row */}
      <div className="grid-kpi">
        <Metric label="Total P&L" value={`$${stats.pnl >= 0 ? '+' : ''}${stats.pnl.toFixed(2)}`}
          color={stats.pnl >= 0 ? '#22c55e' : '#ef4444'} badge="+506%" />
        <Metric label="Win Rate" value={`${(stats.wr * 100).toFixed(1)}%`} sub={`${stats.wins}W / ${stats.losses}L`} />
        <Metric label="R:R Ratio" value={`${stats.rr.toFixed(2)}:1`} sub={`Break-even: ${(1/(1+stats.rr)*100).toFixed(0)}%`} />
        <Metric label="Avg Profit/Trade" value={`$${stats.ev >= 0 ? '+' : ''}${stats.ev.toFixed(3)}`}
          color={stats.ev >= 0 ? '#22c55e' : '#ef4444'} />
        <Metric label="Bankroll" value={`$${stats.bankroll.toFixed(2)}`} sub={`-$${stats.deployed.toFixed(2)} in active trades`} />
        <Metric label="Open" value={`${stats.open}`} sub={`${stats.resolved} resolved`} />
      </div>

      <div className="grid-3-1">
        <div className="col-span-2">
          <Card title="Portfolio Growth">
            <PnLChart data={pnl_series} />
          </Card>
        </div>

        <div className="space-y-3">
          {/* Model proof */}
          <Card>
            <div className="text-[10px] font-semibold text-[#6b7280] uppercase tracking-widest mb-2">Accuracy vs Market</div>
            <div className="space-y-1.5 text-xs">
              <div className="flex justify-between"><span className="text-[#94a3b8]">Our Model</span><span className="text-green-400 font-mono font-bold">{brier.model}</span></div>
              <div className="flex justify-between"><span className="text-[#94a3b8]">Market Baseline</span><span className="text-[#6b7280] font-mono">{brier.naive}</span></div>
              <div className="h-px bg-[#1e1e3a]" />
              <div className="text-green-400 font-semibold">+{brier.improvement}% vs market ✓</div>
              <div className="text-[10px] text-[#6b7280]">19,624 historical outcomes analyzed</div>
            </div>
          </Card>

          {/* Compounding */}
          <Card>
            <div className="text-[10px] font-semibold text-[#6b7280] uppercase tracking-widest mb-1">Compounding</div>
            <div className="text-3xl font-bold" style={{ color: lc }}>{level >= 0 ? '+' : ''}{level}</div>
            <div className="text-xs text-[#6b7280] mb-2">Kelly ×{Math.max(0.5, Math.min(2.0, 1+level*0.1)).toFixed(2)} (frozen)</div>
            <div className="text-[10px] text-[#6b7280]">Win streak {bankroll_state?.win_streak || 0}</div>
            <div className="h-1 bg-[#1e1e3a] rounded-full mt-1">
              <div className="h-full bg-green-500 rounded-full" style={{ width: `${Math.min(100,(bankroll_state?.win_streak||0)*20)}%` }} />
            </div>
          </Card>

          {/* LLM cost */}
          <Card>
            <div className="text-[10px] font-semibold text-[#6b7280] uppercase tracking-widest mb-1">LLM Cost Today</div>
            <div className="text-xl font-bold">${(today.cost_usd||0).toFixed(3)}</div>
            <div className="text-xs text-[#6b7280]">{today.calls||0} calls · {((today.input||0)/1000).toFixed(0)}K tokens</div>
            <div className="mt-2 h-1 bg-[#1e1e3a] rounded-full">
              <div className="h-full bg-[#6366f1] rounded-full" style={{ width: `${Math.min(100,((today.cost_usd||0)/2)*100)}%` }} />
            </div>
            <div className="text-[10px] text-[#6b7280] mt-1">Limit $2.00/day</div>
          </Card>
        </div>
      </div>

      <div className="grid-2">
        <Card title="Results by Market Type">
          <CategoryChart data={cat_breakdown} />
        </Card>
        <Card title="Latest Trades">
          <div className="space-y-1">
            {(recent_full || []).slice(0, 8).map((t, i) => (
              <div key={i} className="flex items-center gap-2 text-xs py-1.5 border-b border-[#1a1a3a] last:border-0">
                <span className={t.correct ? 'text-green-400' : 'text-red-400'}>{t.correct ? '✓' : '✗'}</span>
                <span className={`px-1.5 py-0.5 rounded text-[10px] ${t.side==='YES'?'bg-green-500/20 text-green-400':'bg-red-500/20 text-red-400'}`}>{t.side}</span>
                <span className="text-[#94a3b8] flex-1 truncate">{t.market?.slice(0,45)}</span>
                <span className={`font-mono font-semibold text-xs ${(t.pnl||0)>=0?'text-green-400':'text-red-400'}`}>
                  ${(t.pnl||0)>=0?'+':''}{(t.pnl||0).toFixed(2)}
                </span>
              </div>
            ))}
          </div>
        </Card>
      </div>
    </div>
  )
}
