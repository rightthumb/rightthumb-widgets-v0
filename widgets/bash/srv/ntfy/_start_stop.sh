#!/bin/bash

# Check if port is provided
if [ -z "$2" ]; then
  echo "Usage: $0 {start|stop} <port>"
  exit 1
fi

ACTION=$1
PORT=$2

case $ACTION in
  start)
	echo "Starting ntfy on port $PORT..."
	nohup ntfy serve --host 0.0.0.0 --port "$PORT" > /dev/null 2>&1 &
	echo $! > /tmp/ntfy_$PORT.pid
	echo "ntfy started on port $PORT with PID $(cat /tmp/ntfy_$PORT.pid)"
	;;
  stop)
	if [ -f /tmp/ntfy_$PORT.pid ]; then
	PID=$(cat /tmp/ntfy_$PORT.pid)
	echo "Stopping ntfy on port $PORT with PID $PID..."
	kill "$PID"
	rm /tmp/ntfy_$PORT.pid
	echo "ntfy stopped on port $PORT."
	else
	echo "No running ntfy instance found on port $PORT."
	fi
	;;
  *)
	echo "Invalid action. Use 'start' or 'stop'."
	;;
esac