module.exports = {
  apps: [{
    name: 'tritan-dashboard',
    script: 'server.js',
    cwd: '/root/Tritan/web/.next/standalone',
    env: {
      NODE_ENV: 'production',
      PORT: '3000',
      HOSTNAME: '0.0.0.0',
    },
    instances: 1,
    exec_mode: 'fork',
    autorestart: true,
    max_memory_restart: '256M',
    node_args: '--dns-result-order=ipv4first',
  }],
}
