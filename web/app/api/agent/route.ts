import { NextResponse } from 'next/server'
import { exec } from 'child_process'
import { promisify } from 'util'
import fs from 'fs'
import path from 'path'

const execAsync = promisify(exec)
const ROOT = path.join(process.cwd(), '..')

export async function GET() {
  try {
    const { stdout } = await execAsync('systemctl is-active polymarket-agent')
    const active = stdout.trim() === 'active'
    const svc = fs.readFileSync('/etc/systemd/system/polymarket-agent.service', 'utf-8')
    const mode = svc.includes('--mode live') ? 'live' : 'demo'
    return NextResponse.json({ active, mode })
  } catch {
    return NextResponse.json({ active: false, mode: 'demo' })
  }
}

export async function POST(req: Request) {
  const { action, mode } = await req.json()
  try {
    if (action === 'start')   await execAsync('systemctl start polymarket-agent')
    if (action === 'stop')    await execAsync('systemctl stop polymarket-agent')
    if (action === 'restart') await execAsync('systemctl restart polymarket-agent')
    if (action === 'scan') {
      execAsync(`cd ${ROOT} && python3 main.py --mode demo scan`).catch(() => {})
    }
    if (action === 'switch_mode' && mode) {
      let svc = fs.readFileSync('/etc/systemd/system/polymarket-agent.service', 'utf-8')
      svc = svc.replace(/--mode (demo|live)/, `--mode ${mode}`)
      fs.writeFileSync('/etc/systemd/system/polymarket-agent.service', svc)
      await execAsync('systemctl daemon-reload && systemctl restart polymarket-agent')
    }
    return NextResponse.json({ ok: true })
  } catch (e: any) {
    return NextResponse.json({ ok: false, error: e.message }, { status: 500 })
  }
}
