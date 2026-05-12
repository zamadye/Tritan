'use client'
import { useState, useEffect } from 'react'
import { useRouter } from 'next/navigation'
import Link from 'next/link'
import { useAuth } from '@/lib/auth'
import { Navbar, Tab } from '@/components/Navbar'
import { Overview } from '@/components/tabs/Overview'
import { Proof } from '@/components/tabs/Proof'
import { Positions } from '@/components/tabs/Positions'
import { Trades as History } from '@/components/tabs/Trades'
import { Learning } from '@/components/tabs/Learning'
import { Config } from '@/components/tabs/Config'
import { AssistantChat } from '@/components/AssistantChat'
import { OnboardingGuide } from '@/components/OnboardingGuide'
import { SkeletonPage } from '@/components/ui'
import { useData } from '@/hooks/useData'
import { Wallet, TrendingUp, TrendingDown, Activity, BarChart3, BookOpen, User, RefreshCw, ToggleLeft, ToggleRight } from 'lucide-react'

export default function Home() {
  const { user, loading: authLoading } = useAuth()
  const router = useRouter()
  const { data, agent, account, loading, error, refresh, agentAction } = useData()
  const [tab, setTab] = useState<Tab>('Overview')
  const [syncing, setSyncing] = useState(false)
  const [switching, setSwitching] = useState(false)

  useEffect(() => {
    if (!authLoading && !user) router.push('/login')
  }, [user, authLoading, router])

  const handleApplySuggestion = async (key: string, value: string) => {
    await fetch('/api/settings', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ [key]: value }),
    })
    setTab('Config')
  }

  const handleSync = async () => {
    setSyncing(true)
    try {
      await fetch('/api/sync', { method: 'POST' })
      await refresh()
    } catch (e) {
      console.error('Sync failed:', e)
    }
    setSyncing(false)
  }

  const handleSwitchMode = async () => {
    const newMode = isLive ? 'demo' : 'live'
    setSwitching(true)
    try {
      await agentAction('switch_mode', newMode)
      // Wait for restart
      await new Promise(r => setTimeout(r, 3000))
      await refresh()
    } catch (e) {
      console.error('Switch failed:', e)
    }
    setSwitching(false)
  }

  if (authLoading || !user) {
    return (
      <div className="min-h-screen flex items-center justify-center" style={{ background: 'var(--bg)' }}>
        <div className="text-center">
          <div className="text-2xl mb-2">⚡</div>
          <div className="text-sm" style={{ color: 'var(--dim)' }}>Loading Tritan...</div>
        </div>
      </div>
    )
  }

  const isLive = data?.agent_mode === 'live'
  const stats = data?.stats

  return (
    <div className="min-h-screen" style={{ background: 'var(--bg)', color: 'var(--text)', fontFamily: 'var(--font-sans)' }}>
      <Navbar tab={tab} setTab={setTab} agent={agent} loading={loading} onAction={agentAction} onRefresh={refresh} />

      <main className="main-content">
        {/* ═══ MODE SWITCH & SYNC BAR ═══ */}
        <div className="flex items-center justify-between mb-4 p-3 rounded-xl" style={{
          background: isLive ? 'var(--green-bg)' : 'var(--accent-bg)',
          border: `1px solid ${isLive ? 'var(--green-border)' : 'var(--accent-border)'}`,
        }}>
          <div className="flex items-center gap-3">
            <button
              onClick={handleSwitchMode}
              disabled={switching}
              className="flex items-center gap-2 px-3 py-2 rounded-lg text-sm font-semibold"
              style={{
                background: isLive ? 'var(--green)' : 'var(--accent)',
                color: 'white',
                opacity: switching ? 0.6 : 1,
                cursor: switching ? 'not-allowed' : 'pointer',
                border: 'none',
              }}
            >
              {switching ? (
                <RefreshCw size={14} className="animate-spin" />
              ) : isLive ? (
                <ToggleRight size={14} />
              ) : (
                <ToggleLeft size={14} />
              )}
              {switching ? 'Switching...' : isLive ? 'LIVE' : 'DEMO'}
            </button>
            <div className="text-xs" style={{ color: 'var(--dim)' }}>
              {isLive ? 'Real money trading' : 'Simulation mode'}
            </div>
          </div>
          {isLive && (
            <button
              onClick={handleSync}
              disabled={syncing}
              className="flex items-center gap-2 px-3 py-2 rounded-lg text-xs font-semibold"
              style={{
                background: 'var(--bg)',
                color: 'var(--green)',
                border: '1px solid var(--green-border)',
                opacity: syncing ? 0.6 : 1,
                cursor: syncing ? 'not-allowed' : 'pointer',
              }}
            >
              <RefreshCw size={12} className={syncing ? 'animate-spin' : ''} />
              {syncing ? 'Syncing...' : 'Sync Polymarket'}
            </button>
          )}
        </div>

        {/* ═══ WALLET HEADER (LIVE MODE ONLY) ═══ */}
        {isLive && account && (
          <div className="wallet-header mb-4">
            <div className="wallet-header-inner">
              <div className="flex items-center gap-3 mb-3">
                <div className="wallet-icon">
                  <Wallet size={20} />
                </div>
                <div>
                  <div className="text-[10px] uppercase tracking-wider" style={{ color: 'var(--dim)' }}>Wallet Balance</div>
                  <div className="wallet-balance">${account.usdc_balance?.toFixed(2) || '0.00'}</div>
                </div>
              </div>
              <div className="wallet-stats">
                <div className="wallet-stat">
                  <div className="wallet-stat-label">Deployed</div>
                  <div className="wallet-stat-value" style={{ color: 'var(--yellow)' }}>
                    ${stats?.deployed?.toFixed(2) || '0.00'}
                  </div>
                </div>
                <div className="wallet-stat">
                  <div className="wallet-stat-label">Available</div>
                  <div className="wallet-stat-value" style={{ color: 'var(--green)' }}>
                    ${((account.usdc_balance || 0) - (stats?.deployed || 0)).toFixed(2)}
                  </div>
                </div>
                <div className="wallet-stat">
                  <div className="wallet-stat-label">P&L</div>
                  <div className="wallet-stat-value" style={{ color: (stats?.pnl || 0) >= 0 ? 'var(--green)' : 'var(--red)' }}>
                    {(stats?.pnl || 0) >= 0 ? '+' : ''}${stats?.pnl?.toFixed(2) || '0.00'}
                  </div>
                </div>
              </div>
              <div className="wallet-address">
                {account.wallet || '—'}
              </div>
            </div>
          </div>
        )}

        {/* ═══ DEMO HEADER (DEMO MODE ONLY) ═══ */}
        {!isLive && stats && (
          <div className="demo-header mb-4">
            <div className="demo-header-inner">
              <div className="flex items-center gap-3 mb-3">
                <div className="demo-icon">
                  <Activity size={20} />
                </div>
                <div>
                  <div className="text-[10px] uppercase tracking-wider" style={{ color: 'var(--dim)' }}>Demo Simulation</div>
                  <div className="demo-balance">${stats.bankroll?.toFixed(2) || '0.00'}</div>
                </div>
              </div>
              <div className="wallet-stats">
                <div className="wallet-stat">
                  <div className="wallet-stat-label">Deployed</div>
                  <div className="wallet-stat-value" style={{ color: 'var(--yellow)' }}>
                    ${stats.deployed?.toFixed(2) || '0.00'}
                  </div>
                </div>
                <div className="wallet-stat">
                  <div className="wallet-stat-label">P&L</div>
                  <div className="wallet-stat-value" style={{ color: (stats.pnl || 0) >= 0 ? 'var(--green)' : 'var(--red)' }}>
                    {(stats.pnl || 0) >= 0 ? '+' : ''}${stats.pnl?.toFixed(2) || '0.00'}
                  </div>
                </div>
                <div className="wallet-stat">
                  <div className="wallet-stat-label">Win Rate</div>
                  <div className="wallet-stat-value" style={{ color: (stats.wr || 0) >= 0.55 ? 'var(--green)' : 'var(--yellow)' }}>
                    {((stats.wr || 0) * 100).toFixed(1)}%
                  </div>
                </div>
              </div>
            </div>
          </div>
        )}

        {/* ═══ QUICK STATS BAR ═══ */}
        {stats && (
          <div className="quick-stats mb-4">
            <div className="quick-stat">
              <div className="quick-stat-icon" style={{ color: 'var(--green)' }}>
                <TrendingUp size={14} />
              </div>
              <div>
                <div className="quick-stat-label">Wins</div>
                <div className="quick-stat-value">{stats.wins || 0}</div>
              </div>
            </div>
            <div className="quick-stat">
              <div className="quick-stat-icon" style={{ color: 'var(--red)' }}>
                <TrendingDown size={14} />
              </div>
              <div>
                <div className="quick-stat-label">Losses</div>
                <div className="quick-stat-value">{stats.losses || 0}</div>
              </div>
            </div>
            <div className="quick-stat">
              <div className="quick-stat-icon" style={{ color: 'var(--accent-light)' }}>
                <Activity size={14} />
              </div>
              <div>
                <div className="quick-stat-label">Open</div>
                <div className="quick-stat-value">{stats.open || 0}</div>
              </div>
            </div>
            <div className="quick-stat">
              <div className="quick-stat-icon" style={{ color: 'var(--muted)' }}>
                <BarChart3 size={14} />
              </div>
              <div>
                <div className="quick-stat-label">Total</div>
                <div className="quick-stat-value">{stats.total || 0}</div>
              </div>
            </div>
          </div>
        )}

        {/* ═══ TAB CONTENT ═══ */}
        {error && !data ? (
          <div className="text-center py-12">
            <div className="text-2xl mb-2">⚠️</div>
            <div className="text-sm font-semibold mb-1" style={{ color: 'var(--red)' }}>Connection Error</div>
            <div className="text-xs mb-4" style={{ color: 'var(--dim)' }}>{error}</div>
            <button onClick={refresh} className="btn btn-primary btn-sm">Retry</button>
          </div>
        ) : !data ? (
          <SkeletonPage />
        ) : (
          <>
            <div style={{ display: tab === 'Overview'  ? 'block' : 'none' }}><Overview  data={data} account={account} /></div>
            <div style={{ display: tab === 'Proof'     ? 'block' : 'none' }}><Proof     data={data} /></div>
            <div style={{ display: tab === 'Positions' ? 'block' : 'none' }}><Positions data={data} /></div>
            <div style={{ display: tab === 'History'   ? 'block' : 'none' }}><History   data={data} /></div>
            <div style={{ display: tab === 'Learning'  ? 'block' : 'none' }}><Learning  data={data} /></div>
            <div style={{ display: tab === 'Config'    ? 'block' : 'none' }}><Config /></div>
          </>
        )}
      </main>

      {/* Footer */}
      <footer className="text-center py-4 text-[10px]" style={{ color: 'var(--dim)', borderTop: '1px solid var(--border2)' }}>
        <div className="flex items-center justify-center gap-3 mb-1">
          <Link href="/profile" style={{ color: 'var(--dim)' }}>Profile</Link>
          <Link href="/docs" style={{ color: 'var(--dim)' }}>Docs</Link>
          <Link href="/roadmap" style={{ color: 'var(--dim)' }}>Roadmap</Link>
          <Link href="/subscribe" style={{ color: 'var(--dim)' }}>Plans</Link>
        </div>
        Tritan v3.2 · Statistical Edge Trading
      </footer>

      <AssistantChat onApplySuggestion={handleApplySuggestion} />
      <OnboardingGuide onNavigate={(t) => setTab(t as Tab)} />
    </div>
  )
}
