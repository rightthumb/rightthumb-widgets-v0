#!/bin/bash
set -e

# ---------- Defaults ----------
AUTO=false
SAVE_FILE="$(pwd)/postgres_sync.yml"

# ---------- Help Menu ----------
if [[ "$1" == "--help" || "$1" == "-h" || "$#" -eq 0 ]]; then
    echo "Usage:"
    echo "  $0 --name=pg1 --remote=user@replica_host --replica-db=pg1 [--auto] [--save=/path/to/yml]"
    echo
    echo "  --name         Name of primary instance (e.g., pg1)"
    echo "  --remote       SSH target for the replica server (user@host)"
    echo "  --replica-db   Name of the DB on the replica (will be created if missing)"
    echo "  --save         Save YAML sync metadata (default: ./postgres_sync.yml)"
    echo "  --auto         No prompts (assumes SSH and Postgres access is ready)"
    echo
    exit 0
fi

# ---------- Parse Args ----------
for ARG in "$@"; do
    case $ARG in
        --name=*) NAME="${ARG#*=}" ;;
        --remote=*) REMOTE="${ARG#*=}" ;;
        --replica-db=*) REPLICA_DB="${ARG#*=}" ;;
        --auto) AUTO=true ;;
        --save=*) SAVE_FILE="${ARG#*=}" ;;
        *) echo "Unknown argument: $ARG" && exit 1 ;;
    esac
done

# ---------- Validation ----------
if [[ -z "$NAME" || -z "$REMOTE" || -z "$REPLICA_DB" ]]; then
    echo "Missing required argument"
    exit 1
fi

PORT=$(grep port "/var/lib/postgresql/$NAME/postgresql.conf" | awk '{print $3}' | tr -d "'")
TIMESTAMP=$(date +"%Y-%m-%d_%H-%M-%S")

echo "[+] Starting logical replication setup for: $NAME → $REMOTE/$REPLICA_DB"

# ---------- 1. Primary: Enable logical replication ----------
echo "[+] Configuring primary instance for replication..."

PG_CONF="/var/lib/postgresql/$NAME/postgresql.conf"
sed -i "s/^#*wal_level =.*/wal_level = logical/" "$PG_CONF"
sed -i "s/^#*max_replication_slots =.*/max_replication_slots = 10/" "$PG_CONF"
sed -i "s/^#*max_wal_senders =.*/max_wal_senders = 10/" "$PG_CONF"

echo "host replication all 127.0.0.1/32 md5" >> "/var/lib/postgresql/$NAME/pg_hba.conf"
echo "host all all 127.0.0.1/32 md5" >> "/var/lib/postgresql/$NAME/pg_hba.conf"

sudo -u postgres pg_ctl -D "/var/lib/postgresql/$NAME" reload

# ---------- 2. Primary: Create publication ----------
echo "[+] Creating publication..."

sudo -u postgres psql -p "$PORT" -c "DROP PUBLICATION IF EXISTS ${NAME}_pub;"
sudo -u postgres psql -p "$PORT" -c "CREATE PUBLICATION ${NAME}_pub FOR ALL TABLES;"

# ---------- 3. Remote: Create database & subscription ----------
echo "[+] Setting up replica on $REMOTE"

ssh "$REMOTE" bash <<EOF
    set -e
    echo "[REMOTE] Creating database $REPLICA_DB if needed..."
    sudo -u postgres psql -tc "SELECT 1 FROM pg_database WHERE datname = '$REPLICA_DB'" | grep -q 1 || sudo -u postgres createdb $REPLICA_DB

    echo "[REMOTE] Creating subscription to primary..."
    sudo -u postgres psql -d "$REPLICA_DB" -c "DROP SUBSCRIPTION IF EXISTS ${NAME}_sub;"
    sudo -u postgres psql -d "$REPLICA_DB" -c \\
      "CREATE SUBSCRIPTION ${NAME}_sub CONNECTION 'host=localhost port=$PORT user=postgres dbname=$NAME' PUBLICATION ${NAME}_pub WITH (create_slot = true, copy_data = true);"
EOF

# ---------- 4. Save to YAML ----------
echo >> "$SAVE_FILE"
echo "# Logical Replication Sync: $TIMESTAMP" >> "$SAVE_FILE"
echo "$NAME:" >> "$SAVE_FILE"
echo "  type: logical_replication" >> "$SAVE_FILE"
echo "  publication: ${NAME}_pub" >> "$SAVE_FILE"
echo "  replica:" >> "$SAVE_FILE"
echo "    ssh: $REMOTE" >> "$SAVE_FILE"
echo "    database: $REPLICA_DB" >> "$SAVE_FILE"
echo "    subscription: ${NAME}_sub" >> "$SAVE_FILE"
echo "  status: configured" >> "$SAVE_FILE"

echo
echo "[✓] Real-time sync configured: $NAME → $REMOTE/$REPLICA_DB"
echo "[📝] Settings saved to: $SAVE_FILE"
echo
