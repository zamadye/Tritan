// Shared UI primitives

export function Metric({ label, value, sub, color, badge }: {
  label: string; value: string; sub?: string; color?: string; badge?: string
}) {
  return (
    <div className="metric-card">
      <div style={{ display: 'flex', alignItems: 'flex-start', justifyContent: 'space-between', marginBottom: 6 }}>
        <div className="metric-label">{label}</div>
        {badge && <span className="badge" style={{ background: 'rgba(34,197,94,0.15)', color: '#22c55e', borderColor: 'rgba(34,197,94,0.3)', fontSize: 10 }}>{badge}</span>}
      </div>
      <div className="metric-value" style={{ color: color || '#f1f5f9' }}>{value}</div>
      {sub && <div className="metric-sub">{sub}</div>}
    </div>
  )
}

export function Card({ title, children, className = '' }: {
  title?: string; children: React.ReactNode; className?: string
}) {
  return (
    <div className={`card ${className}`}>
      {title && <div className="card-title">{title}</div>}
      {children}
    </div>
  )
}

export function Badge({ text, color }: {
  text: string; color: 'green' | 'red' | 'blue' | 'yellow' | 'purple' | 'gray'
}) {
  const styles: Record<string, string> = {
    green:  'bg-green-500/20 text-green-400 border-green-500/30',
    red:    'bg-red-500/20 text-red-400 border-red-500/30',
    blue:   'bg-blue-500/20 text-blue-400 border-blue-500/30',
    yellow: 'bg-yellow-500/20 text-yellow-400 border-yellow-500/30',
    purple: 'bg-purple-500/20 text-purple-400 border-purple-500/30',
    gray:   'bg-gray-500/20 text-gray-400 border-gray-500/30',
  }
  return (
    <span className={`text-[10px] px-2 py-0.5 rounded-full border font-semibold ${styles[color]}`}>{text}</span>
  )
}

export function Divider() {
  return <div className="h-px bg-[#1e1e3a] my-3" />
}

export function SectionTitle({ icon, title, sub }: { icon?: string; title: string; sub?: string }) {
  return (
    <div className="mb-4">
      <h2 className="text-base font-semibold text-[#e2e8f0] flex items-center gap-2">
        {icon && <span>{icon}</span>}{title}
      </h2>
      {sub && <p className="text-xs text-[#6b7280] mt-0.5">{sub}</p>}
    </div>
  )
}
