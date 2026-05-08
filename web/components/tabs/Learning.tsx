'use client'
import { ExitChart } from '@/components/charts'
import type { DashboardData } from '@/types'

function SCard({ title, children }: { title?: string; children: React.ReactNode }) {
  return (
    <div style={{ background: '#13132a', border: '1px solid #2a2a4a', borderRadius: 16, overflow: 'hidden' }}>
      {title && <div style={{ padding: '14px 16px 0', fontSize: 13, fontWeight: 600, color: '#94a3b8' }}>{title}</div>}
      <div style={{ padding: title ? '12px 16px 16px' : '16px' }}>{children}</div>
    </div>
  )
}

export function Learning({ data }: { data: DashboardData }) {
  const { evolution, brier, exit_breakdown, stats } = data

  return (
    <div style={{ display: 'flex', flexDirection: 'column', gap: 14 }}>
      <div>
        <div style={{ fontSize: 15, fontWeight: 700, color: '#e2e8f0' }}>🧠 AI Learning</div>
        <div style={{ fontSize: 12, color: '#6b7280', marginTop: 3 }}>System improves automatically after every resolved trade</div>
      </div>

      {/* KPI row */}
      <div style={{ display: 'grid', gridTemplateColumns: 'repeat(2, 1fr)', gap: 10 }}>
        {[
          { label: 'Resolved', value: String(evolution?.total_resolved || 0) },
          { label: 'Overall WR', value: `${((evolution?.overall_win_rate || 0) * 100).toFixed(0)}%`, color: (evolution?.overall_win_rate || 0) >= 0.55 ? '#22c55e' : '#f59e0b' },
          { label: 'Accuracy Gain', value: `+${brier.improvement}%`, color: '#22c55e' },
          { label: 'New Arch WR', value: `${((stats.new_arch?.wr || 0) * 100).toFixed(0)}%`, color: (stats.new_arch?.wr || 0) >= 0.54 ? '#22c55e' : '#f59e0b' },
        ].map((k, i) => (
          <div key={i} style={{ background: 'linear-gradient(135deg,#13132a,#16162e)', border: '1px solid #2a2a4a', borderRadius: 14, padding: '12px 14px' }}>
            <div style={{ fontSize: 10, fontWeight: 600, color: '#6b7280', textTransform: 'uppercase', letterSpacing: '0.6px', marginBottom: 6 }}>{k.label}</div>
            <div style={{ fontSize: 22, fontWeight: 700, color: k.color || '#f1f5f9' }}>{k.value}</div>
          </div>
        ))}
      </div>

      {/* Exit breakdown */}
      <SCard title="How Trades Close">
        <ExitChart data={exit_breakdown || {}} />
      </SCard>

      {/* Best entry zones */}
      {Object.keys(evolution?.price_movement_patterns || {}).length > 0 && (
        <SCard title="Best Entry Price Zones">
          <div style={{ display: 'flex', flexDirection: 'column', gap: 8 }}>
            {Object.entries(evolution.price_movement_patterns || {}).map(([b, d]: any) => (
              <div key={b} style={{ display: 'flex', alignItems: 'center', gap: 10 }}>
                <span style={{ fontSize: 11, color: '#94a3b8', width: 60, flexShrink: 0 }}>{b}</span>
                <div style={{ flex: 1, height: 6, background: '#1e1e3a', borderRadius: 4, overflow: 'hidden' }}>
                  <div style={{ height: '100%', borderRadius: 4, background: '#6366f1', width: `${(d.win_rate || 0) * 100}%` }} />
                </div>
                <span style={{ fontSize: 11, color: '#94a3b8', width: 36, textAlign: 'right', flexShrink: 0 }}>{((d.win_rate || 0) * 100).toFixed(0)}%</span>
                <span style={{ fontSize: 11, fontFamily: 'ui-monospace,monospace', color: (d.avg_pnl || 0) >= 0 ? '#22c55e' : '#ef4444', width: 44, textAlign: 'right', flexShrink: 0 }}>
                  {(d.avg_pnl || 0) >= 0 ? '+' : ''}${(d.avg_pnl || 0).toFixed(2)}
                </span>
              </div>
            ))}
          </div>
        </SCard>
      )}

      {/* Winning patterns */}
      <SCard title="✅ What's Working">
        {!(evolution?.momentum_lessons?.length) ? (
          <div style={{ fontSize: 12, color: '#6b7280', textAlign: 'center', padding: '12px 0' }}>Collecting data...</div>
        ) : (
          <div style={{ display: 'flex', flexDirection: 'column', gap: 8 }}>
            {(evolution.momentum_lessons || []).map((m: any, i: number) => (
              <div key={i} style={{ padding: '10px 12px', background: '#0d0d1a', borderRadius: 12, border: '1px solid rgba(34,197,94,0.2)' }}>
                <div style={{ display: 'flex', gap: 8, marginBottom: 4 }}>
                  <span style={{ fontSize: 12, fontWeight: 700, color: '#22c55e' }}>${(m.pnl || 0).toFixed(2)}</span>
                  <span style={{ fontSize: 11, color: '#6b7280' }}>{m.exit_reason}</span>
                  <span style={{ fontSize: 10, color: '#4b5563', marginLeft: 'auto' }}>[{m.category}]</span>
                </div>
                <div style={{ fontSize: 11, color: '#6b7280', lineHeight: 1.4 }}>{m.catalyst?.slice(0, 100)}</div>
              </div>
            ))}
          </div>
        )}
      </SCard>

      {/* Mistakes */}
      <SCard title="❌ Learning from Losses">
        {!(evolution?.recent_mistakes?.length) ? (
          <div style={{ fontSize: 12, color: '#6b7280', textAlign: 'center', padding: '12px 0' }}>No mistakes yet 🎉</div>
        ) : (
          <div style={{ display: 'flex', flexDirection: 'column', gap: 8 }}>
            {(evolution.recent_mistakes || []).map((m: any, i: number) => (
              <div key={i} style={{ padding: '10px 12px', background: '#0d0d1a', borderRadius: 12, border: '1px solid rgba(239,68,68,0.2)' }}>
                <div style={{ fontSize: 11, color: '#94a3b8', marginBottom: 4, overflow: 'hidden', textOverflow: 'ellipsis', whiteSpace: 'nowrap' }}>{m.question?.slice(0, 55)}</div>
                <div style={{ fontSize: 11, color: '#ef4444', lineHeight: 1.4 }}>{m.lesson?.slice(0, 100)}</div>
              </div>
            ))}
          </div>
        )}
      </SCard>
    </div>
  )
}
