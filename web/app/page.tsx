'use client'
import { useState } from 'react'
import { Navbar } from '@/components/Navbar'
import { Overview } from '@/components/tabs/Overview'
import { Proof } from '@/components/tabs/Proof'
import { Positions } from '@/components/tabs/Positions'
import { Trades } from '@/components/tabs/Trades'
import { Learning } from '@/components/tabs/Learning'
import { Config } from '@/components/tabs/Config'
import { AssistantChat } from '@/components/AssistantChat'
import { OnboardingGuide } from '@/components/OnboardingGuide'
import { useData } from '@/hooks/useData'

type Tab = 'Overview' | 'Proof' | 'Positions' | 'Trades' | 'Learning' | 'Config'

export default function Home() {
  const { data, agent, account, loading, refresh, agentAction } = useData()
  const [tab, setTab] = useState<Tab>('Overview')
  const [pendingConfig, setPendingConfig] = useState<Record<string, string>>({})

  const handleApplySuggestion = async (key: string, value: string) => {
    // Apply suggestion: save to .env via settings API and switch to Config tab
    await fetch('/api/settings', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ [key]: value }),
    })
    setPendingConfig(prev => ({ ...prev, [key]: value }))
    setTab('Config')
  }

  if (!data) return (
    <div className="min-h-screen bg-[#0a0a18] flex items-center justify-center">
      <div className="text-center">
        <div className="text-2xl mb-2">🤖</div>
        <div className="text-[#6b7280] text-sm">Loading Tritan...</div>
      </div>
    </div>
  )

  return (
    <div className="min-h-screen bg-[#0a0a18] text-white" style={{ fontFamily: 'Inter, system-ui, sans-serif' }}>
      <Navbar tab={tab} setTab={setTab as any} agent={agent} loading={loading} onAction={agentAction} onRefresh={refresh} />
      <main className="main-content">
        {tab === 'Overview'  && <Overview  data={data} account={account} />}
        {tab === 'Proof'     && <Proof     data={data} />}
        {tab === 'Positions' && <Positions data={data} />}
        {tab === 'Trades'    && <Trades    data={data} />}
        {tab === 'Learning'  && <Learning  data={data} />}
        {tab === 'Config'    && <Config />}
      </main>
      <footer className="text-center text-[#374151] text-[10px] py-4 border-t border-[#1e1e3a]">
        Tritan v3.2 · Statistical Edge Trading · {new Date().toUTCString().slice(0, 25)}
      </footer>
      <AssistantChat onApplySuggestion={handleApplySuggestion} />
      <OnboardingGuide onNavigate={(t) => setTab(t as Tab)} />
    </div>
  )
}
