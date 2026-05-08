'use client'
import { PnLChart, CategoryChart } from '@/components/charts'
import type { DashboardData } from '@/types'

function KpiCard({ label, value, sub, color, trend }: {
  label: string; value: string; sub?: string; color?: string; trend?: 'up' | 'down' | 'neutral'
}) {
  const trendColor = trend === 'up' ? '#22c55e' : trend === 'down' ? '#ef4444' : '#6b7280'
  return (
    <div style={{
      background: 'linear-gradient(135deg, #13132a, #16162e)',
      border: '1px solid #2a2a4a',
      borderRadius: 16,
      padding: '14px 16px',
    }}>
      <div style={{ fontSize: 10, fontWeight: 600, color: '#6b7280', textTransform: 'uppercase', letterSpacing: '0.6px', marginBottom: 8 }}>
        {label}
      </div>
      <div style={{ fontSize: 22, fontWeight: 700, color: color || '#f1f5f9', lineHeight: 1.1 }}>
        {value}
      </div>
      {sub && <div style={{ fontSize: 11, color: '#6b7280', marginTop: 4 }}>{sub}</div>}
    </div>
  )
}

function InfoRow({ label, value, color }: { label: string; value: string; color?: string }) {
  return (
    <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center', padding: '8px 0', borderBottom: '1px solid #1e1e3a' }}>
      <span style={{ fontSize: 12, color: '#94a3b8' }}>{label}</span>
      <span style={{ fontSize: 12, fontWeight: 600, color: color || '#e2e8f0', fontFamily: 'ui-monospace, monospace' }}>{value}</span>
    </div>
  )
}

function SectionCard({ title, children }: { title?: string; children: React.ReactNode }) {
  return (
    <div style={{ background: '#13132a', border: '1px solid #2a2a4a', borderRadius: 16, overflow: 'hidden' }}>
      {title && (
        <div style={{ padding: '14px 16px 0', fontSize: 13, fontWeight: 600, color: '#94a3b8' }}>
          {title}
        </div>
      )}
      <div style={{ padding: title ? '12px 16px 16px' : '16px' }}>
        {children}
      </div>
    </div>
  )
}

export function Overview({ data, account }: { data: DashboardData; account?: any }) {
  const { stats, brier, pnl_series, cat_breakdown, bankroll_state, llm } = data
  const level = bankroll_state?.level || 0
  const today = llm?.daily || {}
  const isLive = account?.usdc_balance > 0

  return (
    <div style={{ display: 'flex', flexDirection: 'column', gap: 14 }}>

      {/* Mode banner */}
      <div style={{
        display: 'flex', alignItems: 'center', justifyContent: 'space-between',
        padding: '12px 16px', borderRadius: 14,
        background: isLive ? 'rgba(34,197,94,0.06)' : 'rgba(99,102,241,0.06)',
        border: `1px solid ${isLive ? 'rgba(34,197,94,0.2)' : 'rgba(99,102,241,0.2)'}`,
      }}>
        <div>
          <div style={{ fontSize: 13, fontWeight: 700, color: isLive ? '#22c55e' : '#a5b4fc' }}>
            {isLive ? '💰 Live Mode' : '📝 Demo Mode'}
          </div>
          <div style={{ fontSize: 11, color: '#6b7280', marginTop: 2 }}>
            Bankroll: <span style={{ color: '#e2e8f0', fontWeight: 600 }}>${stats.bankroll.toFixed(2)}</span>
            {' · '}Deployed: <span style={{ color: '#f59e0b' }}>${stats.deployed.toFixed(2)}</span>
          </div>
        </div>
        <div style={{ textAlign: 'right' }}>
          <div style={{ fontSize: 11, color: '#6b7280' }}>Level</div>
          <div style={{ fontSize: 20, fontWeight: 700, color: level > 0 ? '#22c55e' : level < 0 ? '#ef4444' : '#94a3b8' }}>
            {level >= 0 ? '+' : ''}{level}
          </div>
        </div>
      </div>

      {/* KPI grid — 2 col on mobile */}
      <div style={{ display: 'grid', gridTemplateColumns: '1fr 1fr', gap: 10 }}>
        <KpiCard label="Total P&L"
          value={`${stats.pnl >= 0 ? '+' : ''}$${stats.pnl.toFixed(2)}`}
          color={stats.pnl >= 0 ? '#22c55e' : '#ef4444'}
          trend={stats.pnl >= 0 ? 'up' : 'down'} />
        <KpiCard label="Win Rate"
          value={`${(stats.wr * 100).toFixed(1)}%`}
          sub={`${stats.wins}W · ${stats.losses}L`}
          color={stats.wr >= 0.55 ? '#22c55e' : stats.wr >= 0.50 ? '#f59e0b' : '#ef4444'} />
        <KpiCard label="Avg EV/Trade"
          value={`${stats.ev >= 0 ? '+' : ''}$${stats.ev.toFixed(3)}`}
          color={stats.ev >= 0 ? '#22c55e' : '#ef4444'} />
        <KpiCard label="R:R Ratio"
          value={`${stats.rr.toFixed(2)}x`}
          sub={`BE: ${stats.rr > 0 ? (1/(1+stats.rr)*100).toFixed(0) : '—'}%`} />
      </div>

      {/* P&L Chart */}
      {pnl_series?.length > 1 && (
        <SectionCard title="Portfolio Growth">
          <PnLChart data={pnl_series} />
        </SectionCard>
      )}

      {/* Stats detail */}
      <SectionCard title="Performance">
        <InfoRow label="Total Trades" value={`${stats.total}`} />
        <InfoRow label="Resolved" value={`${stats.resolved}`} />
        <InfoRow label="Open Positions" value={`${stats.open}`} color="#f59e0b" />
        <InfoRow label="Avg Win" value={`+$${stats.avg_win.toFixed(3)}`} color="#22c55e" />
        <InfoRow label="Avg Loss" value={`-$${stats.avg_loss.toFixed(3)}`} color="#ef4444" />
        <div style={{ borderBottom: 'none', display: 'flex', justifyContent: 'space-between', alignItems: 'center', padding: '8px 0 0' }}>
          <span style={{ fontSize: 12, color: '#94a3b8' }}>Brier Score</span>
          <span style={{ fontSize: 12, fontWeight: 600, color: '#a5b4fc', fontFamily: 'ui-monospace, monospace' }}>{stats.avg_brier.toFixed(3)}</span>
        </div>
      </SectionCard>

      {/* Model accuracy */}
      <SectionCard title="Model vs Market">
        <div style={{ display: 'flex', gap: 12, marginBottom: 12 }}>
          <div style={{ flex: 1, background: 'rgba(34,197,94,0.08)', border: '1px solid rgba(34,197,94,0.2)', borderRadius: 12, padding: '12px', textAlign: 'center' }}>
            <div style={{ fontSize: 10, color: '#6b7280', marginBottom: 4 }}>OUR MODEL</div>
            <div style={{ fontSize: 20, fontWeight: 700, color: '#22c55e' }}>{brier.model}</div>
          </div>
          <div style={{ flex: 1, background: 'rgba(107,114,128,0.08)', border: '1px solid rgba(107,114,128,0.2)', borderRadius: 12, padding: '12px', textAlign: 'center' }}>
            <div style={{ fontSize: 10, color: '#6b7280', marginBottom: 4 }}>MARKET</div>
            <div style={{ fontSize: 20, fontWeight: 700, color: '#6b7280' }}>{brier.naive}</div>
          </div>
        </div>
        <div style={{ fontSize: 12, color: '#22c55e', fontWeight: 600, textAlign: 'center' }}>
          +{brier.improvement}% better than market baseline
        </div>
        <div style={{ fontSize: 11, color: '#4b5563', textAlign: 'center', marginTop: 4 }}>
          Trained on 19,624 resolved markets
        </div>
      </SectionCard>

      {/* Category breakdown */}
      {Object.keys(cat_breakdown || {}).length > 0 && (
        <SectionCard title="By Category">
          <CategoryChart data={cat_breakdown} />
        </SectionCard>
      )}

      {/* LLM cost */}
      <SectionCard title="AI Cost Today">
        <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center', marginBottom: 10 }}>
          <div>
            <div style={{ fontSize: 22, fontWeight: 700, color: '#e2e8f0' }}>${(today.cost_usd || 0).toFixed(3)}</div>
            <div style={{ fontSize: 11, color: '#6b7280' }}>{today.calls || 0} calls · {((today.input || 0) / 1000).toFixed(0)}K tokens</div>
          </div>
          <div style={{ fontSize: 11, color: '#6b7280' }}>Limit $3.00</div>
        </div>
        <div style={{ height: 6, background: '#1e1e3a', borderRadius: 4, overflow: 'hidden' }}>
          <div style={{
            height: '100%', borderRadius: 4,
            width: `${Math.min(100, ((today.cost_usd || 0) / 3) * 100)}%`,
            background: (today.cost_usd || 0) > 2.5 ? '#ef4444' : '#6366f1',
            transition: 'width 0.4s',
          }} />
        </div>
      </SectionCard>

    </div>
  )
}
