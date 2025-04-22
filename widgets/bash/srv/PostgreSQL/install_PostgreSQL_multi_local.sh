#!/bin/bash
set -e

# ---------- Defaults ----------
BASE_DIR="/var/lib/postgresql"
DEFAULT_PORT=5432
AUTO=false
SAVE_FILE="$(pwd)/postgres_settings.yml"

# ---------- Help Menu ----------
if [[ "$1" == "--help" || "$1" == "-h" || "$#" -eq 0 ]]; then
	echo "Usage:"
	echo "  $0 --name=pg1 [--port=5433] [--auto] [--save=/path/to/settings.yml]"
	echo
	echo "  --name     PostgreSQL instance name (required)"
	echo "  --port     Optional port (auto-increments if omitted)"
	echo "  --auto     Fully automated mode"
	echo "  --save     Alternate YAML config file (default: ./postgres_settings.yml)"
	echo
	echo "Example:"
	echo "  $0 --name=pg2 --auto"
	exit 0
fi

# ---------- Parse Args ----------
for ARG in "$@"; do
	case $ARG in
		--name=*) NAME="${ARG#*=}" ;;
		--port=*) PORT="${ARG#*=}" ;;
		--auto) AUTO=true ;;
		--save=*) SAVE_FILE="${ARG#*=}" ;;
		*) echo "Unknown argument: $ARG" && exit 1 ;;
	esac
done

# ---------- Validation ----------
if [[ -z "$NAME" ]]; then
	echo "Missing --name"
	exit 1
fi

DATA_DIR="$BASE_DIR/$NAME"
LOGFILE="$BASE_DIR/${NAME}_logfile.log"
CONF_FILE="$DATA_DIR/postgresql.conf"

# ---------- Install PostgreSQL if missing ----------
if ! command -v initdb &>/dev/null; then
	echo "[+] Installing PostgreSQL..."

	if command -v apt &>/dev/null; then
		apt update && apt install -y postgresql
	elif command -v dnf &>/dev/null; then
		dnf install -y postgresql-server
	elif command -v yum &>/dev/null; then
		yum install -y postgresql-server
	elif command -v pacman &>/dev/null; then
		pacman -Sy --noconfirm postgresql
	else
		echo "Unsupported package manager"
		exit 1
	fi
fi

# ---------- Auto Port Detection ----------
if [[ -z "$PORT" ]]; then
	PORT=$DEFAULT_PORT
	while ss -tuln | grep -q ":$PORT"; do
		((PORT++))
	done
fi

# ---------- Generate Password ----------
PASS=$(openssl rand -base64 24)

# ---------- Create Data Dir ----------
if [ -d "$DATA_DIR" ]; then
	echo "[!] Instance already exists: $NAME"
else
	echo "[+] Creating data dir: $DATA_DIR"
	mkdir -p "$DATA_DIR"
	chown -R postgres:postgres "$DATA_DIR"
	sudo -u postgres initdb -D "$DATA_DIR"
fi

# ---------- Configure Instance ----------
sed -i "s/^#port =.*/port = $PORT/" "$CONF_FILE"
sed -i "s/^#listen_addresses =.*/listen_addresses = 'localhost'/" "$CONF_FILE"

echo "host all all 127.0.0.1/32 md5" >> "$DATA_DIR/pg_hba.conf"
echo "host all all ::1/128 md5" >> "$DATA_DIR/pg_hba.conf"

# ---------- Start Server ----------
echo "[+] Starting PostgreSQL instance: $NAME"
sudo -u postgres pg_ctl -D "$DATA_DIR" -l "$LOGFILE" start

# ---------- Set Password ----------
sudo -u postgres psql -p "$PORT" -c "ALTER USER postgres WITH PASSWORD '$PASS';"

# ---------- Save to YAML ----------
echo >> "$SAVE_FILE"
echo "# Created on $(date)" >> "$SAVE_FILE"
echo "$NAME:" >> "$SAVE_FILE"
echo "  port: $PORT" >> "$SAVE_FILE"
echo "  password: \"$PASS\"" >> "$SAVE_FILE"
echo "  data_dir: $DATA_DIR" >> "$SAVE_FILE"
echo "  config: $CONF_FILE" >> "$SAVE_FILE"
echo "  log_file: $LOGFILE" >> "$SAVE_FILE"

# ---------- Output Summary ----------
echo
echo "[✓] PostgreSQL instance '$NAME' started"
echo "    Port     : $PORT"
echo "    Password : $PASS"
echo "    Data Dir : $DATA_DIR"
echo "    Log File : $LOGFILE"
echo "    Config   : $CONF_FILE"
echo
echo "[📝] Settings saved to: $SAVE_FILE"
echo