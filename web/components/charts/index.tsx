'use client'
import { LineChart, Line, XAxis, YAxis, Tooltip, ResponsiveContainer, BarChart, Bar, ReferenceLine } from 'recharts'

const CHART_COLORS = {
  accent: 'var(--accent)',
  green: 'var(--green)',
  red: 'var(--red)',
  yellow: 'var(--yellow)',
  dim: 'var(--dim)',
  muted: 'var(--muted)',
  border: 'var(--border)',
  border2: 'var(--border2)',
  bg3: 'var(--bg3)',
  accentLight: 'var(--accent-light)',
}

export function PnLChart({ data }: { data: { i: number; pnl: number; correct: boolean }[] }) {
  return (
    <ResponsiveContainer width="100%" height={220}>
      <LineChart data={data}>
        <XAxis dataKey="i" hide />
        <YAxis tick={{ fill: '#6b7280', fontSize: 11 }} tickFormatter={v => `$${v}`} />
        <Tooltip
          contentStyle={{ background: 'var(--bg3)', border: '1px solid var(--border)', borderRadius: 8, fontSize: 12 }}
          formatter={(v: any) => [`$${Number(v).toFixed(2)}`, 'Portfolio Growth']}
          labelFormatter={i => `Trade #${i}`}
        />
        <ReferenceLine y={0} stroke="var(--border2)" strokeDasharray="4 2" />
        <Line type="monotone" dataKey="pnl" stroke="var(--accent)" strokeWidth={2} dot={false} />
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
        <Tooltip contentStyle={{ background: 'var(--bg3)', border: '1px solid var(--border)', borderRadius: 8, fontSize: 12 }} />
        <Bar dataKey="wins" fill="var(--green)" radius={[3, 3, 0, 0]} name="Wins" />
        <Bar dataKey="losses" fill="var(--red)" radius={[3, 3, 0, 0]} name="Losses" />
      </BarChart>
    </ResponsiveContainer>
  )
}

export function ExitChart({ data }: { data: Record<string, number> }) {
  const colors: Record<string, string> = {
    TAKE_PROFIT: 'var(--green)', TRAILING_STOP: 'var(--accent-light)',
    STOP_LOSS: 'var(--red)', 'TIME/EVENT': 'var(--yellow)', RESOLVED: 'var(--dim)',
  }
  const total = Object.values(data).reduce((s, v) => s + v, 0)
  return (
    <div className="space-y-2">
      {Object.entries(data).sort((a, b) => b[1] - a[1]).map(([k, v]) => (
        <div key={k} className="flex items-center gap-3">
          <span className="text-xs w-28" style={{ color: 'var(--muted)' }}>{k}</span>
          <div className="flex-1 h-2 rounded-full overflow-hidden" style={{ background: 'var(--border2)' }}>
            <div className="h-full rounded-full transition-all" style={{ width: `${total ? (v/total)*100 : 0}%`, background: colors[k] || 'var(--dim)' }} />
          </div>
          <span className="text-xs w-12 text-right" style={{ color: 'var(--dim)' }}>{v} ({total ? Math.round(v/total*100) : 0}%)</span>
        </div>
      ))}
    </div>
  )
}
