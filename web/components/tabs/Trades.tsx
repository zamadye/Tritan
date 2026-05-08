'use client'
import { useState } from 'react'
import type { DashboardData, Trade } from '@/types'

type Filter = 'All' | 'WIN' | 'LOSS' | 'EXIT'

export function Trades({ data }: { data: DashboardData }) {
  const { recent_full } = data
  const [filter, setFilter] = useState<Filter>('All')
  const [search, setSearch] = useState('')
  const [page, setPage] = useState(0)
  const PAGE = 20

  const filtered = (recent_full || []).filter(t => {
    if (filter === 'WIN' && !t.correct) return false
    if (filter === 'LOSS' && (t.correct || t.outcome === 'EXIT')) return false
    if (filter === 'EXIT' && t.outcome !== 'EXIT') return false
    if (search && !t.market?.toLowerCase().includes(search.toLowerCase())) return false
    return true
  })

  const paged = filtered.slice(page * PAGE, (page + 1) * PAGE)
  const totalPages = Math.ceil(filtered.length / PAGE)

  const wins = (recent_full || []).filter(t => t.correct).length
  const losses = (recent_full || []).filter(t => !t.correct && t.outcome !== 'EXIT').length
  const exits = (recent_full || []).filter(t => t.outcome === 'EXIT').length

  return (
    <div style={{ display: 'flex', flexDirection: 'column', gap: 12 }}>
      {/* Summary pills */}
      <div style={{ display: 'flex', gap: 8, flexWrap: 'wrap' }}>
        {([
          { id: 'All',  label: `All ${recent_full?.length || 0}`,  color: '#94a3b8', bg: 'rgba(148,163,184,0.1)', border: 'rgba(148,163,184,0.2)' },
          { id: 'WIN',  label: `✓ ${wins}`,   color: '#22c55e', bg: 'rgba(34,197,94,0.1)',  border: 'rgba(34,197,94,0.25)' },
          { id: 'LOSS', label: `✗ ${losses}`, color: '#ef4444', bg: 'rgba(239,68,68,0.1)',  border: 'rgba(239,68,68,0.25)' },
          { id: 'EXIT', label: `⇄ ${exits}`,  color: '#f59e0b', bg: 'rgba(245,158,11,0.1)', border: 'rgba(245,158,11,0.25)' },
        ] as const).map(f => (
          <button key={f.id} onClick={() => { setFilter(f.id); setPage(0) }}
            style={{
              padding: '6px 14px', borderRadius: 20, fontSize: 12, fontWeight: 600,
              border: `1px solid ${filter === f.id ? f.border : '#2a2a4a'}`,
              background: filter === f.id ? f.bg : 'transparent',
              color: filter === f.id ? f.color : '#6b7280',
              cursor: 'pointer', transition: 'all 0.15s',
            }}>
            {f.label}
          </button>
        ))}
      </div>

      {/* Search */}
      <input value={search} onChange={e => { setSearch(e.target.value); setPage(0) }}
        placeholder="Search market..."
        style={{
          width: '100%', background: '#0d0d1a', border: '1px solid #2a2a4a',
          borderRadius: 12, padding: '10px 14px', fontSize: 13, color: '#e2e8f0',
          outline: 'none',
        }} />

      {/* Count */}
      <div style={{ fontSize: 11, color: '#6b7280' }}>{filtered.length} trades</div>

      {/* Trade cards */}
      <div style={{ display: 'flex', flexDirection: 'column', gap: 8 }}>
        {paged.map((t, i) => {
          const isWin = t.correct
          const isExit = t.outcome === 'EXIT' && !t.correct
          const statusColor = isWin ? '#22c55e' : isExit ? '#f59e0b' : '#ef4444'
          const statusBg = isWin ? 'rgba(34,197,94,0.06)' : isExit ? 'rgba(245,158,11,0.06)' : 'rgba(239,68,68,0.06)'
          const statusBorder = isWin ? 'rgba(34,197,94,0.2)' : isExit ? 'rgba(245,158,11,0.2)' : 'rgba(239,68,68,0.2)'

          return (
            <div key={i} style={{
              background: '#13132a', border: `1px solid ${statusBorder}`,
              borderRadius: 14, padding: '12px 14px',
            }}>
              {/* Row 1: status + market + pnl */}
              <div style={{ display: 'flex', alignItems: 'flex-start', gap: 10, marginBottom: 8 }}>
                <span style={{
                  width: 24, height: 24, borderRadius: 8, flexShrink: 0,
                  background: statusBg, color: statusColor,
                  display: 'flex', alignItems: 'center', justifyContent: 'center',
                  fontSize: 12, fontWeight: 700,
                }}>
                  {isWin ? '✓' : isExit ? '⇄' : '✗'}
                </span>
                <div style={{ flex: 1, minWidth: 0 }}>
                  <div style={{ fontSize: 12, fontWeight: 600, color: '#e2e8f0', lineHeight: 1.4, marginBottom: 4 }}>
                    {t.market?.slice(0, 65)}{(t.market?.length || 0) > 65 ? '…' : ''}
                  </div>
                  <div style={{ display: 'flex', gap: 6, flexWrap: 'wrap' }}>
                    <span style={{ fontSize: 10, fontWeight: 600, padding: '1px 7px', borderRadius: 20, background: t.side === 'YES' ? 'rgba(34,197,94,0.15)' : 'rgba(239,68,68,0.15)', color: t.side === 'YES' ? '#22c55e' : '#ef4444', border: `1px solid ${t.side === 'YES' ? 'rgba(34,197,94,0.3)' : 'rgba(239,68,68,0.3)'}` }}>
                      {t.side}
                    </span>
                    <span style={{ fontSize: 10, color: '#6b7280', padding: '1px 7px', borderRadius: 20, background: 'rgba(107,114,128,0.1)', border: '1px solid rgba(107,114,128,0.2)' }}>
                      {t.category || 'other'}
                    </span>
                    {t.date && <span style={{ fontSize: 10, color: '#4b5563' }}>{t.date.slice(0, 10)}</span>}
                  </div>
                </div>
                <div style={{ textAlign: 'right', flexShrink: 0 }}>
                  <div style={{ fontSize: 15, fontWeight: 700, color: (t.pnl || 0) >= 0 ? '#22c55e' : '#ef4444', fontFamily: 'ui-monospace, monospace' }}>
                    {(t.pnl || 0) >= 0 ? '+' : ''}${(t.pnl || 0).toFixed(2)}
                  </div>
                </div>
              </div>

              {/* Row 2: stats */}
              <div style={{ display: 'flex', gap: 12, fontSize: 11, color: '#6b7280' }}>
                <span>Entry <span style={{ color: '#94a3b8', fontFamily: 'ui-monospace, monospace' }}>{((t.entry || 0) * 100).toFixed(0)}%</span></span>
                {t.edge != null && <span>Edge <span style={{ color: '#a5b4fc', fontFamily: 'ui-monospace, monospace' }}>{(t.edge * 100).toFixed(1)}%</span></span>}
                {t.confidence != null && <span>Conf <span style={{ color: '#94a3b8', fontFamily: 'ui-monospace, monospace' }}>{(t.confidence * 100).toFixed(0)}%</span></span>}
                {t.brier != null && <span>Brier <span style={{ color: '#94a3b8', fontFamily: 'ui-monospace, monospace' }}>{t.brier.toFixed(3)}</span></span>}
              </div>

              {/* Exit reason */}
              {t.exit_reason && (
                <div style={{ marginTop: 6, fontSize: 10, color: '#6b7280', background: '#0d0d1a', borderRadius: 8, padding: '5px 10px' }}>
                  🚪 {t.exit_reason}
                </div>
              )}
            </div>
          )
        })}
      </div>

      {/* Pagination */}
      {totalPages > 1 && (
        <div style={{ display: 'flex', justifyContent: 'center', alignItems: 'center', gap: 12, paddingTop: 4 }}>
          <button onClick={() => setPage(p => Math.max(0, p - 1))} disabled={page === 0}
            style={{ padding: '8px 16px', borderRadius: 10, fontSize: 12, background: '#13132a', border: '1px solid #2a2a4a', color: '#94a3b8', cursor: 'pointer', opacity: page === 0 ? 0.4 : 1 }}>
            ← Prev
          </button>
          <span style={{ fontSize: 12, color: '#6b7280' }}>{page + 1} / {totalPages}</span>
          <button onClick={() => setPage(p => Math.min(totalPages - 1, p + 1))} disabled={page === totalPages - 1}
            style={{ padding: '8px 16px', borderRadius: 10, fontSize: 12, background: '#13132a', border: '1px solid #2a2a4a', color: '#94a3b8', cursor: 'pointer', opacity: page === totalPages - 1 ? 0.4 : 1 }}>
            Next →
          </button>
        </div>
      )}
    </div>
  )
}
