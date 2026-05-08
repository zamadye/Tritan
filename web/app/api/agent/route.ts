import { NextResponse } from 'next/server'
import { exec } from 'child_process'
import { promisify } from 'util'
import fs from 'fs'
import path from 'path'

const execAsync = promisify(exec)
const ROOT = path.join(process.cwd(), '..')

// Whitelists — prevent injection
const ALLOWED_ACTIONS = new Set(['start', 'stop', 'restart', 'scan', 'switch_mode'])
const ALLOWED_MODES   = new Set(['demo', 'live'])

export async function GET() {
  try {
    const { stdout } = await execAsync('systemctl is-active tritan-agent')
    const active = stdout.trim() === 'active'
    const svc = fs.readFileSync('/etc/systemd/system/tritan-agent.service', 'utf-8')
    const mode = svc.includes('--mode live') ? 'live' : 'demo'
    return NextResponse.json({ active, mode })
  } catch {
    return NextResponse.json({ active: false, mode: 'demo' })
  }
}

export async function POST(req: Request) {
  const body = await req.json()
  const action: string = body.action ?? ''
  const mode:   string = body.mode   ?? ''

  // Whitelist validation
  if (!ALLOWED_ACTIONS.has(action)) {
    return NextResponse.json({ ok: false, error: 'Invalid action' }, { status: 400 })
  }
  if (action === 'switch_mode' && !ALLOWED_MODES.has(mode)) {
    return NextResponse.json({ ok: false, error: 'Invalid mode' }, { status: 400 })
  }

  try {
    if (action === 'start')   await execAsync('systemctl start tritan-agent')
    if (action === 'stop')    await execAsync('systemctl stop tritan-agent')
    if (action === 'restart') await execAsync('systemctl restart tritan-agent')
    if (action === 'scan') {
      // Use array form to prevent shell injection
      const { spawn } = await import('child_process')
      spawn('python3', ['main.py', '--mode', 'demo', 'scan'], { cwd: ROOT, detached: true }).unref()
    }
    if (action === 'switch_mode') {
      // mode is already validated against whitelist above
      let svc = fs.readFileSync('/etc/systemd/system/tritan-agent.service', 'utf-8')
      svc = svc.replace(/--mode (demo|live)/, `--mode ${mode}`)
      fs.writeFileSync('/etc/systemd/system/tritan-agent.service', svc)
      await execAsync('systemctl daemon-reload && systemctl restart tritan-agent')
    }
    return NextResponse.json({ ok: true })
  } catch (e: any) {
    return NextResponse.json({ ok: false, error: 'Command failed' }, { status: 500 })
  }
}
