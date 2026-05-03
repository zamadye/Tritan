'use client'
import { LineChart, Line, XAxis, YAxis, Tooltip, ResponsiveContainer, BarChart, Bar, ReferenceLine } from 'recharts'

export function PnLChart({ data }: { data: { i: number; pnl: number; correct: boolean }[] }) {
  return (
    <ResponsiveContainer width="100%" height={220}>
      <LineChart data={data}>
        <XAxis dataKey="i" hide />
        <YAxis tick={{ fill: '#6b7280', fontSize: 11 }} tickFormatter={v => `$${v}`} />
        <Tooltip
          contentStyle={{ background: '#16162a', border: '1px solid #2a2a4a', borderRadius: 8, fontSize: 12 }}
          formatter={(v: any) => [`$${Number(v).toFixed(2)}`, 'Cumulative P&L']}
          labelFormatter={i => `Trade #${i}`}
        />
        <ReferenceLine y={0} stroke="#2a2a4a" strokeDasharray="4 2" />
        <Line type="monotone" dataKey="pnl" stroke="#6366f1" strokeWidth={2} dot={false} />
      </LineChart>
    </ResponsiveContainer>
  )
}

export function CategoryChart({ data }: { data: Record<string, { w: number; l: number }> }) {
  const chartData = Object.entries(data).map(([cat, s]) => ({
    cat: cat.slice(0, 8), wins: s.w, losses: s.l,
  }))
  return (
    <ResponsiveContainer width="100%" height={180}>
      <BarChart data={chartData} barGap={2}>
        <XAxis dataKey="cat" tick={{ fill: '#6b7280', fontSize: 10 }} />
        <YAxis tick={{ fill: '#6b7280', fontSize: 10 }} />
        <Tooltip contentStyle={{ background: '#16162a', border: '1px solid #2a2a4a', borderRadius: 8, fontSize: 12 }} />
        <Bar dataKey="wins" fill="#22c55e" radius={[3, 3, 0, 0]} name="Wins" />
        <Bar dataKey="losses" fill="#ef4444" radius={[3, 3, 0, 0]} name="Losses" />
      </BarChart>
    </ResponsiveContainer>
  )
}

export function ExitChart({ data }: { data: Record<string, number> }) {
  const colors: Record<string, string> = {
    TAKE_PROFIT: '#22c55e', TRAILING_STOP: '#a5b4fc',
    STOP_LOSS: '#ef4444', 'TIME/EVENT': '#f59e0b', RESOLVED: '#6b7280',
  }
  const total = Object.values(data).reduce((s, v) => s + v, 0)
  return (
    <div className="space-y-2">
      {Object.entries(data).sort((a, b) => b[1] - a[1]).map(([k, v]) => (
        <div key={k} className="flex items-center gap-3">
          <span className="text-xs w-28 text-[#94a3b8]">{k}</span>
          <div className="flex-1 h-2 bg-[#1e1e3a] rounded-full overflow-hidden">
            <div className="h-full rounded-full transition-all" style={{ width: `${total ? (v/total)*100 : 0}%`, background: colors[k] || '#6b7280' }} />
          </div>
          <span className="text-xs text-[#6b7280] w-12 text-right">{v} ({total ? Math.round(v/total*100) : 0}%)</span>
        </div>
      ))}
    </div>
  )
}
