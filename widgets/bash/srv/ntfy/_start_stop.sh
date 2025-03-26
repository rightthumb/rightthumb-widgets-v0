#!/bin/bash

# ─────────────────────────────────────────────
# Usage: ./ntfy_port_control.sh {start|stop} <port>
# Starts/stops ntfy on a specific port with JSON enabled
# ─────────────────────────────────────────────

set -e

ACTION=$1
PORT=$2

# ───── Check usage ─────
if [[ -z "$PORT" || -z "$ACTION" ]]; then
	echo "Usage: $0 {start|stop} <port>"
	exit 1
fi

# ───── Validate port ─────
if ! [[ "$PORT" =~ ^[0-9]+$ ]]; then
	echo "❌ Port must be a number"
	exit 1
fi

# ───── Check ntfy exists ─────
if ! command -v ntfy &> /dev/null; then
	echo "❌ 'ntfy' is not installed or not in PATH"
	exit 1
fi

CONFIG_DIR="/tmp/ntfy_config_$PORT"
PID_FILE="/tmp/ntfy_$PORT.pid"
CACHE_FILE="/tmp/ntfy_cache_$PORT.db"

case $ACTION in
	start)
		echo "🔄 Starting ntfy on port $PORT..."

		mkdir -p "$CONFIG_DIR"
		cat > "$CONFIG_DIR/server.yml" <<EOF
listen-http: :$PORT
base-url: http://localhost:$PORT
cache-file: $CACHE_FILE
EOF

		nohup ntfy serve --config "$CONFIG_DIR/server.yml" > /dev/null 2>&1 &
		echo $! > "$PID_FILE"

		echo "✅ ntfy started on port $PORT with PID $(cat $PID_FILE)"
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