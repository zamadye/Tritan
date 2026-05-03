'use client'
import { useState } from 'react'
import { Card, Badge } from '@/components/ui'
import type { DashboardData, Trade } from '@/types'

type Filter = { result: string; side: string; cat: string; q: string }

export function Trades({ data }: { data: DashboardData }) {
  const { recent_full } = data
  const [filter, setFilter] = useState<Filter>({ result: 'All', side: 'All', cat: 'All', q: '' })
  const [page, setPage] = useState(0)
  const PAGE = 15

  const cats = ['All', ...Array.from(new Set((recent_full||[]).map(t => t.category||'other')))]

  const filtered = (recent_full||[]).filter(t => {
    if (filter.result === 'WIN' && !t.correct) return false
    if (filter.result === 'LOSS' && (t.correct || t.outcome === 'EXIT')) return false
    if (filter.result === 'EXIT' && t.outcome !== 'EXIT') return false
    if (filter.side !== 'All' && t.side !== filter.side) return false
    if (filter.cat !== 'All' && (t.category||'other') !== filter.cat) return false
    if (filter.q && !t.market?.toLowerCase().includes(filter.q.toLowerCase())) return false
    return true
  })

  const paged = filtered.slice(page * PAGE, (page + 1) * PAGE)
  const totalPages = Math.ceil(filtered.length / PAGE)

  return (
    <div className="space-y-4">
      {/* Filters */}
      <div className="flex gap-2 flex-wrap">
        {(['All','WIN','LOSS','EXIT'] as const).map(r => (
          <button key={r} onClick={() => { setFilter(f => ({...f, result: r})); setPage(0) }}
            className={`px-3 py-1 rounded-lg text-xs font-medium transition-all ${filter.result===r ? 'bg-[#2d2d5e] text-[#a5b4fc]' : 'bg-[#13132a] text-[#6b7280] hover:text-white border border-[#2a2a4a]'}`}>
            {r}
          </button>
        ))}
        <select value={filter.side} onChange={e => { setFilter(f => ({...f, side: e.target.value})); setPage(0) }}
          className="px-3 py-1 rounded-lg text-xs bg-[#13132a] text-[#94a3b8] border border-[#2a2a4a]">
          {['All','YES','NO'].map(s => <option key={s}>{s}</option>)}
        </select>
        <select value={filter.cat} onChange={e => { setFilter(f => ({...f, cat: e.target.value})); setPage(0) }}
          className="px-3 py-1 rounded-lg text-xs bg-[#13132a] text-[#94a3b8] border border-[#2a2a4a]">
          {cats.map(c => <option key={c}>{c}</option>)}
        </select>
        <input value={filter.q} onChange={e => { setFilter(f => ({...f, q: e.target.value})); setPage(0) }}
          placeholder="Search market..." className="px-3 py-1 rounded-lg text-xs bg-[#13132a] text-[#94a3b8] border border-[#2a2a4a] flex-1 min-w-32" />
        <span className="text-xs text-[#6b7280] self-center">{filtered.length} trades</span>
      </div>

      {/* Trade list */}
      <div className="space-y-2">
        {paged.map((t, i) => (
          <div key={i} className={`p-3 rounded-xl border text-xs transition-colors hover:border-[#3a3a6a] ${
            t.correct ? 'border-green-500/20 bg-green-500/5' : t.outcome==='EXIT' ? 'border-yellow-500/20 bg-yellow-500/5' : 'border-red-500/20 bg-red-500/5'
          }`}>
            <div className="flex items-start gap-3">
              <span className={`text-base mt-0.5 ${t.correct ? 'text-green-400' : t.outcome==='EXIT' ? 'text-yellow-400' : 'text-red-400'}`}>
                {t.correct ? '✓' : t.outcome==='EXIT' ? '⇄' : '✗'}
              </span>
              <div className="flex-1 min-w-0">
                <div className="flex items-center gap-2 mb-1 flex-wrap">
                  <Badge text={t.side} color={t.side==='YES'?'green':'red'} />
                  <Badge text={t.category||'other'} color="purple" />
                  {t.calibration?.includes('logistic') && <Badge text="STAT EDGE" color="blue" />}
                  <span className="text-[#94a3b8] truncate flex-1">{t.market?.slice(0,60)}</span>
                </div>
                <div className="grid grid-cols-5 gap-2 text-[10px] text-[#6b7280]">
                  <span>Entry <span className="text-[#94a3b8] font-mono">{((t.entry||0)*100).toFixed(0)}%</span></span>
                  <span>p_base <span className="text-[#a5b4fc] font-mono">{t.p_base||'—'}</span></span>
                  <span>Edge <span className="text-[#94a3b8] font-mono">{t.edge?`${(t.edge*100).toFixed(1)}%`:'—'}</span></span>
                  <span>Conf <span className="text-[#94a3b8] font-mono">{t.confidence?`${(t.confidence*100).toFixed(0)}%`:'—'}</span></span>
                  <span>Brier <span className="text-[#94a3b8] font-mono">{t.brier?.toFixed(3)||'—'}</span></span>
                </div>
                {t.exit_reason && <div className="text-[10px] text-[#6b7280] mt-1">🚪 {t.exit_reason}</div>}
              </div>
              <div className="text-right shrink-0">
                <div className={`font-mono font-semibold text-sm ${(t.pnl||0)>=0?'text-green-400':'text-red-400'}`}>
                  ${(t.pnl||0)>=0?'+':''}{(t.pnl||0).toFixed(2)}
                </div>
                <div className="text-[10px] text-[#4b5563]">{t.date?.slice(0,10)}</div>
              </div>
            </div>
          </div>
        ))}
      </div>

      {/* Pagination */}
      {totalPages > 1 && (
        <div className="flex items-center justify-center gap-2">
          <button onClick={() => setPage(p => Math.max(0, p-1))} disabled={page===0}
            className="px-3 py-1 rounded-lg text-xs bg-[#13132a] border border-[#2a2a4a] text-[#94a3b8] disabled:opacity-40">← Prev</button>
          <span className="text-xs text-[#6b7280]">{page+1} / {totalPages}</span>
          <button onClick={() => setPage(p => Math.min(totalPages-1, p+1))} disabled={page===totalPages-1}
            className="px-3 py-1 rounded-lg text-xs bg-[#13132a] border border-[#2a2a4a] text-[#94a3b8] disabled:opacity-40">Next →</button>
        </div>
      )}
    </div>
  )
}
