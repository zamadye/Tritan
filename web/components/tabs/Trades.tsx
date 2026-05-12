'use client'
import { useState, useMemo } from 'react'
import { Search, ChevronDown, ChevronUp, Download } from 'lucide-react'
import type { DashboardData, Trade } from '@/types'

type Filter = 'All' | 'WIN' | 'LOSS' | 'EXIT'
type SortKey = 'date' | 'pnl' | 'edge' | 'brier'

export function Trades({ data }: { data: DashboardData }) {
  const { recent_full } = data
  const [filter, setFilter] = useState<Filter>('All')
  const [search, setSearch] = useState('')
  const [page, setPage] = useState(0)
  const [expanded, setExpanded] = useState<string | null>(null)
  const [sortBy, setSortBy] = useState<SortKey>('date')
  const [sortDir, setSortDir] = useState<'asc' | 'desc'>('desc')
  const [catFilter, setCatFilter] = useState<string>('all')
  const PAGE = 20

  const categories = useMemo(() => {
    const cats = new Set((recent_full || []).map(t => t.category || 'other'))
    return ['all', ...Array.from(cats).sort()]
  }, [recent_full])

  const filtered = (recent_full || []).filter(t => {
    if (filter === 'WIN' && !t.correct) return false
    if (filter === 'LOSS' && (t.correct || t.outcome === 'EXIT')) return false
    if (filter === 'EXIT' && t.outcome !== 'EXIT') return false
    if (search && !t.market?.toLowerCase().includes(search.toLowerCase())) return false
    if (catFilter !== 'all' && (t.category || 'other') !== catFilter) return false
    return true
  }).sort((a, b) => {
    const dir = sortDir === 'desc' ? -1 : 1
    if (sortBy === 'date') return dir * ((new Date(a.date).getTime() || 0) - (new Date(b.date).getTime() || 0))
    if (sortBy === 'pnl') return dir * ((a.pnl || 0) - (b.pnl || 0))
    if (sortBy === 'edge') return dir * ((a.edge || 0) - (b.edge || 0))
    if (sortBy === 'brier') return dir * ((a.brier || 0) - (b.brier || 0))
    return 0
  })

  const paged = filtered.slice(page * PAGE, (page + 1) * PAGE)
  const totalPages = Math.ceil(filtered.length / PAGE)

  const toggleSort = (key: SortKey) => {
    if (sortBy === key) setSortDir(d => d === 'desc' ? 'asc' : 'desc')
    else { setSortBy(key); setSortDir('desc') }
  }

  const exportCSV = () => {
    const headers = ['Date', 'Market', 'Side', 'Category', 'Entry', 'Edge', 'Confidence', 'P&L', 'Outcome', 'Brier', 'Exit Reason']
    const rows = filtered.map(t => [
      t.date?.slice(0, 10), t.market, t.side, t.category || 'other',
      ((t.entry || 0) * 100).toFixed(0) + '%', t.edge ? (t.edge * 100).toFixed(1) + '%' : '',
      t.confidence ? (t.confidence * 100).toFixed(0) + '%' : '',
      (t.pnl || 0).toFixed(2), t.correct ? 'WIN' : t.outcome === 'EXIT' ? 'EXIT' : 'LOSS',
      t.brier?.toFixed(3) || '', t.exit_reason || '',
    ])
    const csv = [headers, ...rows].map(r => r.map(c => `"${String(c).replace(/"/g, '""')}"`).join(',')).join('\n')
    const blob = new Blob([csv], { type: 'text/csv' })
    const url = URL.createObjectURL(blob)
    const a = document.createElement('a')
    a.href = url; a.download = `tritan-trades-${new Date().toISOString().slice(0, 10)}.csv`; a.click()
    URL.revokeObjectURL(url)
  }

  const wins = (recent_full || []).filter(t => t.correct).length
  const losses = (recent_full || []).filter(t => !t.correct && t.outcome !== 'EXIT').length
  const exits = (recent_full || []).filter(t => t.outcome === 'EXIT').length

  const filters: { id: Filter; label: string; color: string; bg: string; border: string }[] = [
    { id: 'All',  label: `All ${recent_full?.length || 0}`,  color: 'var(--muted)', bg: 'rgba(148,163,184,0.08)', border: 'rgba(148,163,184,0.2)' },
    { id: 'WIN',  label: `✓ ${wins}`,   color: 'var(--green)', bg: 'var(--green-bg)',  border: 'var(--green-border)' },
    { id: 'LOSS', label: `✗ ${losses}`, color: 'var(--red)',   bg: 'var(--red-bg)',    border: 'var(--red-border)' },
    { id: 'EXIT', label: `⇄ ${exits}`,  color: 'var(--yellow)', bg: 'var(--yellow-bg)', border: 'var(--yellow-border)' },
  ]

  return (
    <div className="flex flex-col gap-3 fade-in">
      {/* Header */}
      <div className="section-card">
        <div className="section-card-header">
          <div className="flex items-center justify-between">
            <div>
              <div className="text-[13px] font-semibold" style={{ color: 'var(--muted)' }}>Trade History</div>
              <div className="text-[11px] mt-0.5" style={{ color: 'var(--dim)' }}>
                {data.agent_mode === 'live' ? '💰 Live' : '📝 Demo'} · {filtered.length} trades
              </div>
            </div>
            <span className="status-pill" style={{
              borderColor: data.agent_mode === 'live' ? 'var(--green-border)' : 'var(--accent-border)',
              color: data.agent_mode === 'live' ? 'var(--green)' : 'var(--accent-light)',
              background: data.agent_mode === 'live' ? 'var(--green-bg)' : 'var(--accent-bg)',
              fontSize: 10,
              padding: '3px 8px',
            }}>
              {data.agent_mode === 'live' ? '💰 LIVE' : '📝 DEMO'}
            </span>
          </div>
        </div>
      </div>

      {/* Filter pills */}
      <div className="flex gap-2 flex-wrap">
        {filters.map(f => (
          <button key={f.id} onClick={() => { setFilter(f.id); setPage(0) }}
            className="btn btn-sm" style={{
              border: `1px solid ${filter === f.id ? f.border : 'var(--border)'}`,
              background: filter === f.id ? f.bg : 'transparent',
              color: filter === f.id ? f.color : 'var(--dim)',
            }}>
            {f.label}
          </button>
        ))}
      </div>

      {/* Search + Sort + Export */}
      <div className="relative">
        <Search size={14} className="absolute left-3 top-1/2 -translate-y-1/2" style={{ color: 'var(--dim)' }} />
        <input value={search} onChange={e => { setSearch(e.target.value); setPage(0) }}
          placeholder="Search market..." className="input" style={{ paddingLeft: 36 }} />
      </div>

      {/* Category filter + Sort + Export */}
      <div className="flex items-center gap-2 flex-wrap">
        <select value={catFilter} onChange={e => { setCatFilter(e.target.value); setPage(0) }}
          className="input" style={{ width: 'auto', padding: '6px 10px', fontSize: 11 }}>
          {categories.map(c => <option key={c} value={c}>{c === 'all' ? 'All categories' : c}</option>)}
        </select>
        <div className="flex gap-1">
          {([['date', 'Date'], ['pnl', 'P&L'], ['edge', 'Edge'], ['brier', 'Brier']] as [SortKey, string][]).map(([key, label]) => (
            <button key={key} onClick={() => toggleSort(key)}
              className="btn btn-sm" style={{
                padding: '4px 8px', fontSize: 10,
                background: sortBy === key ? 'var(--accent-bg)' : 'transparent',
                color: sortBy === key ? 'var(--accent-light)' : 'var(--dim)',
                border: `1px solid ${sortBy === key ? 'var(--accent-border)' : 'var(--border)'}`,
              }}>
              {label} {sortBy === key && (sortDir === 'desc' ? '↓' : '↑')}
            </button>
          ))}
        </div>
        <button onClick={exportCSV} className="btn btn-ghost btn-sm ml-auto" style={{ padding: '4px 8px', fontSize: 10 }}>
          <Download size={12} /> CSV
        </button>
      </div>

      {/* Trade cards */}
      <div className="flex flex-col gap-2">
        {paged.map((t) => {
          const isWin = t.correct
          const isExit = t.outcome === 'EXIT' && !t.correct
          const statusColor = isWin ? 'var(--green)' : isExit ? 'var(--yellow)' : 'var(--red)'
          const statusBg = isWin ? 'var(--green-bg)' : isExit ? 'var(--yellow-bg)' : 'var(--red-bg)'
          const statusBorder = isWin ? 'var(--green-border)' : isExit ? 'var(--yellow-border)' : 'var(--red-border)'

          return (
            <div key={t.market + t.date + t.side} className="section-card" style={{ borderLeft: `3px solid ${statusColor}` }}>
              <div className="section-card-body">
                {/* Row 1: status + market + pnl */}
                <div className="flex items-start gap-2.5 mb-2">
                  <span className="w-6 h-6 rounded-lg flex-shrink-0 flex items-center justify-center text-xs font-bold"
                    style={{ background: statusBg, color: statusColor }}>
                    {isWin ? '✓' : isExit ? '⇄' : '✗'}
                  </span>
                  <div className="flex-1 min-w-0">
                    <div className="text-xs font-semibold leading-snug mb-1" style={{ color: 'var(--text2)' }}>
                      {t.market?.slice(0, 65)}{(t.market?.length || 0) > 65 ? '…' : ''}
                    </div>
                    <div className="flex gap-1.5 flex-wrap">
                      <span className="badge" style={{
                        background: t.side === 'YES' ? 'var(--green-bg)' : 'var(--red-bg)',
                        color: t.side === 'YES' ? 'var(--green)' : 'var(--red)',
                        borderColor: t.side === 'YES' ? 'var(--green-border)' : 'var(--red-border)',
                      }}>{t.side}</span>
                      <span className="badge" style={{
                        background: 'rgba(107,114,128,0.08)', color: 'var(--dim)', borderColor: 'rgba(107,114,128,0.15)',
                      }}>{t.category || 'other'}</span>
                      {t.date && <span className="text-[10px]" style={{ color: 'var(--dim)' }}>{t.date.slice(0, 10)}</span>}
                    </div>
                  </div>
                  <div className="text-right flex-shrink-0">
                    <div className="text-sm font-bold mono" style={{ color: (t.pnl || 0) >= 0 ? 'var(--green)' : 'var(--red)' }}>
                      {(t.pnl || 0) >= 0 ? '+' : ''}${(t.pnl || 0).toFixed(2)}
                    </div>
                  </div>
                </div>

                {/* Row 2: stats */}
                <div className="flex gap-3 text-xs" style={{ color: 'var(--dim)' }}>
                  <span>Entry <span className="mono" style={{ color: 'var(--muted)' }}>{((t.entry || 0) * 100).toFixed(0)}%</span></span>
                  {t.edge != null && <span>Edge <span className="mono" style={{ color: 'var(--accent-light)' }}>{(t.edge * 100).toFixed(1)}%</span></span>}
                  {t.confidence != null && <span>Conf <span className="mono" style={{ color: 'var(--muted)' }}>{(t.confidence * 100).toFixed(0)}%</span></span>}
                  {t.brier != null && <span>Brier <span className="mono" style={{ color: 'var(--muted)' }}>{t.brier.toFixed(3)}</span></span>}
                </div>

                {/* Exit reason */}
                {t.exit_reason && (
                  <div className="mt-2 text-[10px] rounded-lg py-1.5 px-2.5" style={{ color: 'var(--dim)', background: 'var(--bg)' }}>
                    🚪 {t.exit_reason}
                  </div>
                )}

                {/* Expand toggle */}
                <button onClick={() => setExpanded(expanded === (t.market + t.date + t.side) ? null : (t.market + t.date + t.side))}
                  className="mt-2 flex items-center gap-1 text-[10px] cursor-pointer" style={{ color: 'var(--dim)', background: 'none', border: 'none' }}>
                  {expanded === (t.market + t.date + t.side) ? <ChevronUp size={12} /> : <ChevronDown size={12} />}
                  {expanded === (t.market + t.date + t.side) ? 'Less' : 'More details'}
                </button>

                {/* Expanded details */}
                {expanded === (t.market + t.date + t.side) && (
                  <div className="mt-2 pt-2 space-y-1.5 text-[10px]" style={{ borderTop: '1px solid var(--border2)', color: 'var(--dim)' }}>
                    {t.reasoning && (
                      <div><span style={{ color: 'var(--muted)' }}>Reasoning:</span> {t.reasoning}</div>
                    )}
                    {t.calibration && (
                      <div><span style={{ color: 'var(--muted)' }}>Calibration:</span> <span className="mono">{t.calibration}</span></div>
                    )}
                    {t.p_true != null && (
                      <div><span style={{ color: 'var(--muted)' }}>True Prob:</span> <span className="mono">{(t.p_true * 100).toFixed(1)}%</span></div>
                    )}
                    {t.base_rate != null && (
                      <div><span style={{ color: 'var(--muted)' }}>Base Rate:</span> <span className="mono">{(t.base_rate * 100).toFixed(1)}%</span></div>
                    )}
                    {t.catalyst && (
                      <div><span style={{ color: 'var(--muted)' }}>Catalyst:</span> {t.catalyst}</div>
                    )}
                    {t.tool_calls_log && (
                      <div><span style={{ color: 'var(--muted)' }}>Research:</span> {typeof t.tool_calls_log === 'string' ? t.tool_calls_log : JSON.stringify(t.tool_calls_log)}</div>
                    )}
                    {t.news_context && (
                      <div><span style={{ color: 'var(--muted)' }}>News:</span> {typeof t.news_context === 'string' ? t.news_context : JSON.stringify(t.news_context)}</div>
                    )}
                    {t.information_gap && (
                      <div><span style={{ color: 'var(--muted)' }}>Info Gap:</span> {t.information_gap} {t.information_gap_reason ? `— ${t.information_gap_reason}` : ''}</div>
                    )}
                  </div>
                )}
              </div>
            </div>
          )
        })}
      </div>

      {/* Pagination */}
      {totalPages > 1 && (
        <div className="flex justify-center items-center gap-3 pt-1">
          <button onClick={() => setPage(p => Math.max(0, p - 1))} disabled={page === 0}
            className="btn btn-secondary btn-sm" style={{ opacity: page === 0 ? 0.4 : 1 }}>
            ← Prev
          </button>
          <span className="text-xs mono" style={{ color: 'var(--dim)' }}>{page + 1} / {totalPages}</span>
          <button onClick={() => setPage(p => Math.min(totalPages - 1, p + 1))} disabled={page === totalPages - 1}
            className="btn btn-secondary btn-sm" style={{ opacity: page === totalPages - 1 ? 0.4 : 1 }}>
            Next →
          </button>
        </div>
      )}
    </div>
  )
}
