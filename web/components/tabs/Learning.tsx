'use client'
import { ExitChart } from '@/components/charts'
import { Metric, SectionCard, ModeBadge } from '@/components/ui'
import type { DashboardData } from '@/types'

export function Learning({ data }: { data: DashboardData }) {
  const { evolution, brier, exit_breakdown, stats } = data

  return (
    <div className="flex flex-col gap-4 fade-in">
      <div className="flex items-start justify-between">
        <div>
          <div className="text-base font-bold" style={{ color: 'var(--text)' }}>🧠 AI Learning</div>
          <div className="text-xs mt-0.5" style={{ color: 'var(--dim)' }}>System improves automatically after every resolved trade</div>
        </div>
        <ModeBadge mode={data.agent_mode || 'demo'} />
      </div>

      {/* KPI row */}
      <div className="grid-kpi" style={{ gridTemplateColumns: 'repeat(2, 1fr)' }}>
        <Metric label="Resolved" value={String(evolution?.total_resolved || 0)} />
        <Metric label="Overall WR" value={`${((evolution?.overall_win_rate || 0) * 100).toFixed(0)}%`}
          color={(evolution?.overall_win_rate || 0) >= 0.55 ? 'var(--green)' : 'var(--yellow)'} />
        <Metric label="Accuracy Gain" value={`+${brier.improvement}%`} color="var(--green)" />
        <Metric label="New Arch WR" value={`${((stats.new_arch?.wr || 0) * 100).toFixed(0)}%`}
          color={(stats.new_arch?.wr || 0) >= 0.54 ? 'var(--green)' : 'var(--yellow)'} />
      </div>

      {/* Exit breakdown */}
      <SectionCard title="How Trades Close">
        <ExitChart data={exit_breakdown || {}} />
      </SectionCard>

      {/* Category performance */}
      {data.cat_breakdown && Object.keys(data.cat_breakdown).length > 0 && (
        <SectionCard title="Performance by Category">
          <div className="flex flex-col gap-0">
            {Object.entries(data.cat_breakdown)
              .sort(([,a]: any, [,b]: any) => (b.w/(b.w+b.l||1)) - (a.w/(a.w+a.l||1)))
              .map(([cat, s]: any) => {
                const total = s.w + s.l
                const wr = total ? s.w / total : 0
                return (
                  <div key={cat} className="flex items-center gap-3 py-2.5" style={{ borderBottom: '1px solid var(--border2)' }}>
                    <div className="w-20 flex-shrink-0">
                      <div className="text-xs font-semibold capitalize" style={{ color: 'var(--text2)' }}>{cat}</div>
                      <div className="text-[10px]" style={{ color: 'var(--dim)' }}>{s.w}W/{s.l}L</div>
                    </div>
                    <div className="flex-1 h-1.5 rounded-full overflow-hidden" style={{ background: 'var(--border2)' }}>
                      <div className="h-full rounded-full" style={{ background: wr >= 0.6 ? 'var(--green)' : wr >= 0.5 ? 'var(--yellow)' : 'var(--red)', width: `${wr * 100}%` }} />
                    </div>
                    <span className="text-xs mono w-10 text-right flex-shrink-0" style={{ color: wr >= 0.6 ? 'var(--green)' : wr >= 0.5 ? 'var(--yellow)' : 'var(--red)' }}>
                      {(wr * 100).toFixed(0)}%
                    </span>
                    <span className="text-xs mono w-14 text-right flex-shrink-0" style={{ color: s.pnl >= 0 ? 'var(--green)' : 'var(--red)' }}>
                      {s.pnl >= 0 ? '+' : ''}${s.pnl.toFixed(2)}
                    </span>
                  </div>
                )
              })}
          </div>
        </SectionCard>
      )}

      {/* Best entry zones */}
      {Object.keys(evolution?.price_movement_patterns || {}).length > 0 && (
        <SectionCard title="Best Entry Price Zones">
          <div className="flex flex-col gap-2">
            {Object.entries(evolution.price_movement_patterns || {}).map(([b, d]: any) => (
              <div key={b} className="flex items-center gap-2.5">
                <span className="text-xs w-14 flex-shrink-0" style={{ color: 'var(--muted)' }}>{b}</span>
                <div className="flex-1 h-1.5 rounded-full overflow-hidden" style={{ background: 'var(--border2)' }}>
                  <div className="h-full rounded-full transition-all" style={{ background: 'var(--accent)', width: `${(d.win_rate || 0) * 100}%` }} />
                </div>
                <span className="text-xs w-8 text-right flex-shrink-0" style={{ color: 'var(--muted)' }}>{((d.win_rate || 0) * 100).toFixed(0)}%</span>
                <span className="text-xs mono w-12 text-right flex-shrink-0" style={{ color: (d.avg_pnl || 0) >= 0 ? 'var(--green)' : 'var(--red)' }}>
                  {(d.avg_pnl || 0) >= 0 ? '+' : ''}${(d.avg_pnl || 0).toFixed(2)}
                </span>
              </div>
            ))}
          </div>
        </SectionCard>
      )}

      {/* Winning patterns */}
      <SectionCard title="✅ What's Working">
        {!(evolution?.momentum_lessons?.length) ? (
          <div className="text-xs text-center py-3" style={{ color: 'var(--dim)' }}>Collecting data...</div>
        ) : (
          <div className="flex flex-col gap-2">
            {(evolution.momentum_lessons || []).map((m: any, i: number) => (
              <div key={m.catalyst || i} className="p-3 rounded-xl" style={{ background: 'var(--bg)', border: '1px solid var(--green-border)' }}>
                <div className="flex gap-2 mb-1">
                  <span className="text-xs font-bold" style={{ color: 'var(--green)' }}>${(m.pnl || 0).toFixed(2)}</span>
                  <span className="text-xs" style={{ color: 'var(--dim)' }}>{m.exit_reason}</span>
                  <span className="text-[10px] ml-auto" style={{ color: 'var(--dim)' }}>[{m.category}]</span>
                </div>
                <div className="text-xs leading-relaxed" style={{ color: 'var(--dim)' }}>{m.catalyst?.slice(0, 100)}</div>
              </div>
            ))}
          </div>
        )}
      </SectionCard>

      {/* Mistakes */}
      <SectionCard title="❌ Learning from Losses">
        {!(evolution?.recent_mistakes?.length) ? (
          <div className="text-xs text-center py-3" style={{ color: 'var(--dim)' }}>No mistakes yet</div>
        ) : (
          <div className="flex flex-col gap-2">
            {(evolution.recent_mistakes || []).map((m: any, i: number) => (
              <div key={i} className="p-3 rounded-xl" style={{ background: 'var(--bg)', border: '1px solid var(--red-border)' }}>
                <div className="text-xs mb-1 truncate" style={{ color: 'var(--muted)' }}>{m.question?.slice(0, 55)}</div>
                <div className="text-xs leading-relaxed" style={{ color: 'var(--red)' }}>{m.lesson?.slice(0, 100)}</div>
              </div>
            ))}
          </div>
        )}
      </SectionCard>

      {/* Edge Reality Check */}
      {evolution?.edge_reality && Object.keys(evolution.edge_reality).length > 0 && (
        <SectionCard title="Edge Reality Check" sub="Claimed edge vs actual win rate">
          <div className="flex flex-col gap-2">
            {Object.entries(evolution.edge_reality).sort(([a], [b]) => Number(a) - Number(b)).map(([bucket, d]: any) => (
              <div key={bucket} className="flex items-center gap-2.5">
                <span className="text-xs w-14 flex-shrink-0 mono" style={{ color: 'var(--muted)' }}>{bucket}%</span>
                <div className="flex-1 h-1.5 rounded-full overflow-hidden" style={{ background: 'var(--border2)' }}>
                  <div className="h-full rounded-full transition-all" style={{
                    background: (d.actual_wr || 0) >= (Number(bucket) / 100) ? 'var(--green)' : 'var(--red)',
                    width: `${(d.actual_wr || 0) * 100}%`,
                  }} />
                </div>
                <span className="text-xs w-10 text-right flex-shrink-0 mono" style={{
                  color: (d.actual_wr || 0) >= (Number(bucket) / 100) ? 'var(--green)' : 'var(--red)',
                }}>
                  {((d.actual_wr || 0) * 100).toFixed(0)}%
                </span>
                <span className="text-[10px] w-8 text-right flex-shrink-0" style={{ color: 'var(--dim)' }}>n={d.n || 0}</span>
              </div>
            ))}
          </div>
          <div className="text-[10px] mt-2" style={{ color: 'var(--dim)' }}>
            Green = actual WR meets claimed edge · Red = underperforming
          </div>
        </SectionCard>
      )}
    </div>
  )
}
