#!/bin/bash
# /root/Tritan/service.sh — manage tritan services
# Usage: ./service.sh start|stop|restart|status

BACKEND_LOG=/tmp/tritan-agent.log
FRONTEND_LOG=/tmp/tritan-web.log

start_backend() {
    if pgrep -f "main.py run" > /dev/null; then
        echo "Backend already running (PID: $(pgrep -f 'main.py run'))"
        return
    fi
    rm -f $BACKEND_LOG
    setsid /root/Tritan/.venv/bin/python /root/Tritan/main.py run >> $BACKEND_LOG 2>&1 < /dev/null &
    disown $!
    sleep 2
    PID=$(pgrep -f "main.py run")
    [ -n "$PID" ] && echo "Backend started (PID: $PID)" || echo "Backend failed to start"
}

start_frontend() {
    if pgrep -f "next-server" > /dev/null; then
        echo "Frontend already running (PID: $(pgrep -f 'next start'))"
        return
    fi
    rm -f $FRONTEND_LOG
    cd /root/Tritan/web
    setsid node node_modules/.bin/next start -p 3001 -H 0.0.0.0 >> $FRONTEND_LOG 2>&1 < /dev/null &
    disown $!
    sleep 4
    PID=$(pgrep -f "next-server")
    [ -n "$PID" ] && echo "Frontend started (PID: $PID)" || echo "Frontend failed to start"
}

stop_backend() {
    pkill -f "main.py run" 2>/dev/null && echo "Backend stopped" || echo "Backend was not running"
}

stop_frontend() {
    pkill -f "next start" 2>/dev/null && echo "Frontend stopped" || echo "Frontend was not running"
}

status() {
    BPID=$(pgrep -f "main.py run")
    FPID=$(pgrep -f "next-server")
    [ -n "$BPID" ] && echo "Backend:  ✅ running (PID: $BPID)" || echo "Backend:  ❌ stopped"
    [ -n "$FPID" ] && echo "Frontend: ✅ running (PID: $FPID) → http://localhost:3001" || echo "Frontend: ❌ stopped"
}

case "$1" in
    start)   start_backend; start_frontend ;;
    stop)    stop_backend;  stop_frontend  ;;
    restart) stop_backend; stop_frontend; sleep 1; start_backend; start_frontend ;;
    status)  status ;;
    *) echo "Usage: $0 start|stop|restart|status"; exit 1 ;;
esac
