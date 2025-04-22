#!/bin/bash
set -e

# ---------- Defaults ----------
BASE_DIR="/var/lib"
DEFAULT_PORT=27017
AUTO=false
SAVE_FILE="$(pwd)/mongoDB_settings.yml"

# ---------- Help Menu ----------
if [[ "$1" == "--help" || "$1" == "-h" || "$#" -eq 0 ]]; then
	echo "Usage:"
	echo "  $0 --name=mongo2 [--port=27018] [--auto] [--save=/path/to/settings.yml]"
	echo
	echo "  --name     MongoDB instance name (required)"
	echo "  --port     Optional port (auto-increments from 27017 if omitted)"
	echo "  --auto     Fully automated, no prompts"
	echo "  --save     Optional YAML log file (default: ./mongoDB_settings.yml)"
	echo
	echo "Example:"
	echo "  $0 --name=mongo2 --auto"
	exit 0
fi

# ---------- Argument Parsing ----------
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

DATA_DIR="/var/lib/$NAME"
CONF_FILE="/etc/${NAME}.conf"
LOGFILE="/var/log/${NAME}.log"

# ---------- Install MongoDB if needed ----------
if ! command -v mongod &>/dev/null; then
	echo "[+] Installing MongoDB..."

	if command -v apt &>/dev/null; then
		apt update
		apt install -y gnupg curl
		curl -fsSL https://pgp.mongodb.com/server-6.0.asc | gpg --dearmor -o /usr/share/keyrings/mongodb-server.gpg
		echo "deb [ signed-by=/usr/share/keyrings/mongodb-server.gpg ] https://repo.mongodb.org/apt/ubuntu $(lsb_release -sc)/mongodb-org/6.0 multiverse" > /etc/apt/sources.list.d/mongodb-org-6.0.list
		apt update && apt install -y mongodb-org
	elif command -v dnf &>/dev/null || command -v yum &>/dev/null; then
		cat <<EOF > /etc/yum.repos.d/mongodb-org.repo
[mongodb-org-6.0]
name=MongoDB Repository
baseurl=https://repo.mongodb.org/yum/redhat/\$releasever/mongodb-org/6.0/x86_64/
gpgcheck=1
enabled=1
gpgkey=https://pgp.mongodb.com/server-6.0.asc
EOF
		dnf install -y mongodb-org || yum install -y mongodb-org
	else
		echo "Unsupported package manager"
		exit 1
	fi
fi

# ---------- Auto Port Fallback ----------
if [[ -z "$PORT" ]]; then
	PORT=$DEFAULT_PORT
	while ss -tuln | grep -q ":$PORT"; do
		((PORT++))
	done
fi

# ---------- Prepare Data ----------
if [ -d "$DATA_DIR" ]; then
	echo "[!] Instance already exists: $NAME"
else
	echo "[+] Creating data directory: $DATA_DIR"
	mkdir -p "$DATA_DIR"
	chown -R mongodb:mongodb "$DATA_DIR"
fi

# ---------- Generate Config ----------
echo "[+] Writing config: $CONF_FILE"

cat <<EOF > "$CONF_FILE"
systemLog:
  destination: file
  path: $LOGFILE
  logAppend: true

storage:
  dbPath: $DATA_DIR

net:
  bindIp: 127.0.0.1
  port: $PORT
EOF

# ---------- Start MongoDB ----------
echo "[+] Starting MongoDB instance: $NAME"
mongod --config "$CONF_FILE" --fork

# ---------- Append to YAML Config ----------
echo >> "$SAVE_FILE"
echo "# Created on $(date)" >> "$SAVE_FILE"
echo "$NAME:" >> "$SAVE_FILE"
echo "  port: $PORT" >> "$SAVE_FILE"
echo "  data_dir: $DATA_DIR" >> "$SAVE_FILE"
echo "  config: $CONF_FILE" >> "$SAVE_FILE"
echo "  log_file: $LOGFILE" >> "$SAVE_FILE"

# ---------- Done ----------
echo
echo "[✓] MongoDB instance '$NAME' started"
echo "    Port     : $PORT"
echo "    Data Dir : $DATA_DIR"
echo "    Log File : $LOGFILE"
echo "    Config   : $CONF_FILE"
echo
echo "[📝] Settings saved to: $SAVE_FILE"
echo