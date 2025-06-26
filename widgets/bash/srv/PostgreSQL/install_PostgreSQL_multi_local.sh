#!/bin/bash
set -e

BASE_DIR="/var/lib/postgresql"
DEFAULT_PORT=5432
AUTO=false
NAME=""
PORT=""
SAVE_DIR="/opt/db.yml"

# Help menu
if [[ "$1" == "--help" || "$1" == "-h" || "$#" -eq 0 ]]; then
	echo "Usage: $0 --name=pg1 [--port=5433] [--auto]"
	echo
	echo "Creates PostgreSQL instance and saves config to /opt/db.yml/pg1.yml"
	echo
	exit 0
fi

# Parse args
for ARG in "$@"; do
	case $ARG in
		--name=*) NAME="${ARG#*=}" ;;
		--port=*) PORT="${ARG#*=}" ;;
		--auto) AUTO=true ;;
		*) echo "Unknown argument: $ARG" && exit 1 ;;
	esac
done

# ---------- Port Detection ----------
if [[ -z "$PORT" ]]; then
	PORT=$DEFAULT_PORT
	while ss -tuln | grep -q ":$PORT"; do
		echo "[!] Port $PORT is in use... trying next"
		((PORT++))
	done
	echo "[✓] Using port $PORT"
fi

if [[ -z "$NAME" ]]; then
	echo "Missing --name"
	exit 1
fi

# Prepare paths
DATA_DIR="$BASE_DIR/$NAME"
LOGFILE="$BASE_DIR/${NAME}_logfile.log"
CONF_FILE="$DATA_DIR/postgresql.conf"
YAML_FILE="$SAVE_DIR/${NAME}.yml"
mkdir -p "$SAVE_DIR"

# Install PostgreSQL if missing
if ! command -v initdb &>/dev/null; then
	if command -v apt &>/dev/null; then
		apt update && apt install -y postgresql
	elif command -v yum &>/dev/null; then
		yum install -y postgresql-server
	fi
fi

# Port fallback
if [[ -z "$PORT" ]]; then
	PORT=$DEFAULT_PORT
	while ss -tuln | grep -q ":$PORT"; do ((PORT++)); done
fi

PASS=$(openssl rand -base64 24)

# Init new data dir
if [ ! -d "$DATA_DIR" ]; then
	mkdir -p "$DATA_DIR"
	chown -R postgres:postgres "$DATA_DIR"
	sudo -u postgres initdb -D "$DATA_DIR"
fi

touch "$LOGFILE"
chown postgres:postgres "$LOGFILE"
chmod 600 "$LOGFILE"

# Update config
sed -i "s/^#port =.*/port = $PORT/" "$CONF_FILE"
sed -i "s/^#listen_addresses =.*/listen_addresses = 'localhost'/" "$CONF_FILE"
echo "host all all 127.0.0.1/32 md5" >> "$DATA_DIR/pg_hba.conf"

# Start instance
sudo -u postgres pg_ctl -D "$DATA_DIR" -l "$LOGFILE" start
sleep 2
sudo -u postgres psql -p "$PORT" -c "ALTER USER postgres WITH PASSWORD '$PASS';"

# ---------- Write YAML Config ----------
{
	echo "# PostgreSQL instance created: $(date)"
	echo "$NAME:"
	echo "  type: postgresql"
	echo "  port: $PORT"
	echo "  data: $DATA_DIR"
	echo "  config: $CONF_FILE"
	echo "  log: $LOGFILE"
	echo "  start: pg_ctl -D $DATA_DIR -l $LOGFILE start"
	echo "  stop: pg_ctl -D $DATA_DIR stop"
	echo "  restart: pg_ctl -D $DATA_DIR -l $LOGFILE restart"
	echo "  users:"
	echo "    postgres:"
	echo "      password: \"#!/en|$ENCRYPTED_PASS\""    # <-------- password write
} >> "$YAML_FILE"




echo
echo "[✓] PostgreSQL instance '$NAME' is running on port $PORT"
echo "[📝] Settings saved to: $YAML_FILE"
echo