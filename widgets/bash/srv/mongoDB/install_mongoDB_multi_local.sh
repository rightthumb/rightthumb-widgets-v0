#!/bin/bash
set -e

# ---------- Defaults ----------
BASE_DIR="/var/lib"
DEFAULT_PORT=27017
AUTO=false
NAME=""
PORT=""
SAVE_DIR="/opt/db.yml"

# ---------- Help ----------
if [[ "$1" == "--help" || "$1" == "-h" || "$#" -eq 0 ]]; then
	echo "Usage:"
	echo "  $0 --name=mongo1 [--port=27018] [--auto]"
	echo
	echo "Creates MongoDB instance and saves config to /opt/db.yml/mongo1.yml"
	echo "Includes admin user setup and startup instructions"
	exit 0
fi

# ---------- Parse Args ----------
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


# ---------- Validation ----------
if [[ -z "$NAME" ]]; then
	echo "❌ Missing --name"
	exit 1
fi

DATA_DIR="/var/lib/$NAME"
CONF_FILE="/etc/${NAME}.conf"
LOGFILE="/var/log/${NAME}.log"
YAML_FILE="$SAVE_DIR/${NAME}.yml"
ADMIN_USER="admin"
ADMIN_PASS=$(openssl rand -base64 16)

# ---------- Create save folder ----------
mkdir -p "$SAVE_DIR"

# ---------- Ensure mongodb user exists ----------
if ! id mongodb &>/dev/null; then
	useradd --system --home /var/lib/mongo --shell /sbin/nologin mongodb
fi

# ---------- Install MongoDB if needed ----------
if ! command -v mongod &>/dev/null; then
	echo "[+] Installing MongoDB..."
	if command -v apt &>/dev/null; then
		apt update
		apt install -y mongodb-org
	elif command -v dnf &>/dev/null || command -v yum &>/dev/null; then
		yum install -y mongodb-org
	else
		echo "Unsupported package manager"
		exit 1
	fi
fi

# ---------- Port Detection ----------
if [[ -z "$PORT" ]]; then
	PORT=$DEFAULT_PORT
	while ss -tuln | grep -q ":$PORT"; do ((PORT++)); done
fi

# ---------- Create folders ----------
mkdir -p "$DATA_DIR"
touch "$LOGFILE"
chown -R mongodb:mongodb "$DATA_DIR"
chown mongodb:mongodb "$LOGFILE"
chmod 600 "$LOGFILE"

# ---------- Generate Config ----------
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

security:
  authorization: enabled
EOF

# ---------- Start Instance ----------
mongod --config "$CONF_FILE" --fork
sleep 2

# ---------- Create Admin User ----------
mongosh --port "$PORT" --eval "
use admin
db.createUser({
  user: '$ADMIN_USER',
  pwd: '$ADMIN_PASS',
  roles: [ { role: 'root', db: 'admin' } ]
})
"

# ---------- Write YAML Config ----------
{
	echo "# MongoDB instance created: $(date)"
	echo "$NAME:"
	echo "  type: mongodb"
	echo "  port: $PORT"
	echo "  data: $DATA_DIR"
	echo "  config: $CONF_FILE"
	echo "  log: $LOGFILE"
	echo "  start: mongod --config $CONF_FILE --fork"
	echo "  stop: mongod --config $CONF_FILE --shutdown"
	echo "  restart: \"mongod --config $CONF_FILE --shutdown && sleep 1 && mongod --config $CONF_FILE --fork\""
	echo "  users:"
	echo "    $ADMIN_USER:"
	echo "      password: \"#!/en|$ENCRYPTED_PASS\""    # <-------- password write
} >> "$YAML_FILE"





# ---------- Final Output ----------
echo
echo "[✓] MongoDB instance '$NAME' is running on port $PORT"
echo "[📝] Settings saved to: $YAML_FILE"
echo
echo "────────────────────────────────────────────"
echo "🔐 Admin Login:"
echo "  user: $ADMIN_USER"
echo "  pass: $ADMIN_PASS"
echo
echo "🖥️  Start the instance manually:"
echo "  mongod --config $CONF_FILE --fork"
echo
echo "🛑 Stop the instance manually:"
echo "  mongod --config $CONF_FILE --shutdown"
echo
echo "🔗 Connect:"
echo "  mongosh --port $PORT -u $ADMIN_USER -p --authenticationDatabase admin"
echo "────────────────────────────────────────────"
echo