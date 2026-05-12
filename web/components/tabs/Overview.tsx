'use client'
import { PnLChart, CategoryChart } from '@/components/charts'
import { Metric, SectionCard, InfoRow } from '@/components/ui'
import type { DashboardData } from '@/types'

export function Overview({ data, account }: { data: DashboardData; account?: any }) {
  const { stats, brier, pnl_series, cat_breakdown, bankroll_state, llm } = data
  const level = bankroll_state?.level || 0
  const today = llm?.daily || {}

  return (
    <div className="flex flex-col gap-4 fade-in">

      {/* ═══ PERFORMANCE METRICS ═══ */}
      <div className="section-card">
        <div className="section-card-header">
          <div className="text-[13px] font-semibold" style={{ color: 'var(--muted)' }}>Performance</div>
        </div>
        <div className="section-card-body">
          <div className="grid-kpi">
            <Metric label="Total P&L" value={`${stats.pnl >= 0 ? '+' : ''}$${stats.pnl.toFixed(2)}`}
              color={stats.pnl >= 0 ? 'var(--green)' : 'var(--red)'} trend={stats.pnl >= 0 ? 'up' : 'down'} />
            <Metric label="Win Rate" value={`${(stats.wr * 100).toFixed(1)}%`}
              sub={`${stats.wins}W · ${stats.losses}L`}
              color={stats.wr >= 0.55 ? 'var(--green)' : stats.wr >= 0.50 ? 'var(--yellow)' : 'var(--red)'} />
            <Metric label="Avg EV/Trade" value={`${stats.ev >= 0 ? '+' : ''}$${stats.ev.toFixed(3)}`}
              color={stats.ev >= 0 ? 'var(--green)' : 'var(--red)'} />
            <Metric label="R:R Ratio" value={`${stats.rr.toFixed(2)}x`}
              sub={`BE: ${stats.rr > 0 ? (1/(1+stats.rr)*100).toFixed(0) : '—'}%`} />
            {stats.max_drawdown != null && (
              <Metric label="Max Drawdown" value={`$${stats.max_drawdown.toFixed(2)}`}
                color="var(--red)" />
            )}
            {stats.sharpe != null && (
              <Metric label="Sharpe Ratio" value={stats.sharpe.toFixed(2)}
                color={stats.sharpe > 1 ? 'var(--green)' : stats.sharpe > 0 ? 'var(--yellow)' : 'var(--red)'} />
            )}
          </div>
        </div>
      </div>

      {/* ═══ P&L CHART ═══ */}
      {pnl_series?.length > 1 && (
        <SectionCard title="Portfolio Growth">
          <PnLChart data={pnl_series} />
        </SectionCard>
      )}

      {/* ═══ TRADE SUMMARY ═══ */}
      <div className="section-card">
        <div className="section-card-header">
          <div className="text-[13px] font-semibold" style={{ color: 'var(--muted)' }}>Trade Summary</div>
        </div>
        <div className="section-card-body">
          <InfoRow label="Total Trades" value={`${stats.total}`} />
          <InfoRow label="Resolved" value={`${stats.resolved}`} />
          <InfoRow label="Open Positions" value={`${stats.open}`} color="var(--yellow)" />
          <InfoRow label="Avg Win" value={`+$${stats.avg_win.toFixed(3)}`} color="var(--green)" />
          <InfoRow label="Avg Loss" value={`-$${stats.avg_loss.toFixed(3)}`} color="var(--red)" />
          <InfoRow label="Brier Score" value={stats.avg_brier.toFixed(3)} color="var(--accent-light)" />
        </div>
      </div>

      {/* ═══ MODEL VS MARKET ═══ */}
      <div className="section-card">
        <div className="section-card-header">
          <div className="text-[13px] font-semibold" style={{ color: 'var(--muted)' }}>Model vs Market Accuracy</div>
        </div>
        <div className="section-card-body">
          <div className="flex gap-3 mb-3">
            <div className="flex-1 text-center p-3 rounded-xl" style={{ background: 'var(--green-bg)', border: '1px solid var(--green-border)' }}>
              <div className="text-[10px] font-semibold mb-1" style={{ color: 'var(--dim)' }}>OUR MODEL</div>
              <div className="text-xl font-bold" style={{ color: 'var(--green)' }}>{brier.model}</div>
            </div>
            <div className="flex-1 text-center p-3 rounded-xl" style={{ background: 'rgba(107,114,128,0.06)', border: '1px solid rgba(107,114,128,0.15)' }}>
              <div className="text-[10px] font-semibold mb-1" style={{ color: 'var(--dim)' }}>MARKET</div>
              <div className="text-xl font-bold" style={{ color: 'var(--dim)' }}>{brier.naive}</div>
            </div>
          </div>
          <div className="text-xs font-semibold text-center" style={{ color: 'var(--green)' }}>
            +{brier.improvement}% better than market baseline
          </div>
          <div className="text-[11px] text-center mt-1" style={{ color: 'var(--dim)' }}>
            Trained on 19,624 resolved markets
          </div>
        </div>
      </div>

      {/* ═══ CATEGORY BREAKDOWN ═══ */}
      {Object.keys(cat_breakdown || {}).length > 0 && (
        <SectionCard title="By Category">
          <CategoryChart data={cat_breakdown} />
        </SectionCard>
      )}

      {/* ═══ AI COST ═══ */}
      <div className="section-card">
        <div className="section-card-header">
          <div className="text-[13px] font-semibold" style={{ color: 'var(--muted)' }}>AI Cost Today</div>
        </div>
        <div className="section-card-body">
          <div className="flex justify-between items-center mb-3">
            <div>
              <div className="text-xl font-bold mono" style={{ color: 'var(--text2)' }}>${(today.cost_usd || 0).toFixed(3)}</div>
              <div className="text-xs" style={{ color: 'var(--dim)' }}>{today.calls || 0} calls · {((today.input || 0) / 1000).toFixed(0)}K tokens</div>
            </div>
            <div className="text-xs" style={{ color: 'var(--dim)' }}>Limit ${(data.llm?.daily_limit || 3).toFixed(2)}</div>
          </div>
          <div className="progress-bar">
            <div className="progress-fill" style={{
              width: `${Math.min(100, ((today.cost_usd || 0) / (data.llm?.daily_limit || 3)) * 100)}%`,
              background: (today.cost_usd || 0) > (data.llm?.daily_limit || 3) * 0.85 ? 'var(--red)' : 'var(--accent)',
            }} />
          </div>
        </div>
      </div>
    </div>
  )
}
