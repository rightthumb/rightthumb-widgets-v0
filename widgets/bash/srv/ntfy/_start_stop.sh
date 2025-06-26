#!/bin/bash

# ─────────────────────────────────────────────
# Usage: ./_start_stop.sh {start|stop} <port>
# Starts/stops ntfy on a specific port with JSON history enabled
# ─────────────────────────────────────────────

set -e

ACTION=$1
PORT=$2

# ───── Validate input ─────
if [[ -z "$PORT" || -z "$ACTION" ]]; then
    echo "Usage: $0 {start|stop} <port>"
    exit 1
fi

if ! [[ "$PORT" =~ ^[0-9]+$ ]]; then
    echo "❌ Port must be a number"
    exit 1
fi

if ! command -v ntfy &> /dev/null; then
    echo "❌ 'ntfy' is not installed or not in PATH"
    exit 1
fi

# ───── Paths per port ─────
CONFIG_DIR="/tmp/ntfy_config_$PORT"
PID_FILE="/tmp/ntfy_$PORT.pid"
CACHE_FILE="/var/cache/ntfy/ntfy_cache_$PORT.db"
ATTACH_DIR="/var/cache/ntfy/attachments_$PORT"

case $ACTION in
    start)
        echo "🔄 Starting ntfy on port $PORT..."

        if lsof -i :"$PORT" &>/dev/null; then
            echo "❌ Port $PORT is already in use. Stop the other service first."
            exit 1
        fi

        mkdir -p "$CONFIG_DIR"
        mkdir -p "$(dirname "$CACHE_FILE")"
        touch "$CACHE_FILE"
        mkdir -p "$ATTACH_DIR"

        cat > "$CONFIG_DIR/server.yml" <<EOF
listen-http: :$PORT
base-url: http://localhost:$PORT
cache-file: $CACHE_FILE
attachment-cache-dir: $ATTACH_DIR
EOF

        nohup ntfy serve --config "$CONFIG_DIR/server.yml" > /dev/null 2>&1 &
        PID=$!
        sleep 0.5

        if ! ps -p $PID > /dev/null; then
            echo "❌ ntfy failed to start. Check port conflicts or config issues."
            exit 1
        fi

        echo $PID > "$PID_FILE"
        echo "✅ ntfy started on port $PORT with PID $PID"
        echo "👉 Test: curl -d 'test' http://localhost:$PORT/demo"
        echo "👉 JSON: http://localhost:$PORT/demo.json"
        ;;
    stop)
        if [ -f "$PID_FILE" ]; then
            PID=$(cat "$PID_FILE")
            echo "🛑 Stopping ntfy on port $PORT with PID $PID..."
            kill "$PID" && rm -f "$PID_FILE"
            echo "✅ ntfy stopped on port $PORT."
        else
            echo "⚠️ No running ntfy instance found on port $PORT."
        fi
        ;;
    *)
        echo "❌ Invalid action: $ACTION"
        echo "Usage: $0 {start|stop} <port>"
        exit 1
        ;;
esac
