#!/bin/bash
set -e

# ---------- Defaults ----------
AUTO=false
SAVE_FILE="$(pwd)/postgres_sync.yml"

# ---------- Help ----------
if [[ "$1" == "--help" || "$1" == "-h" || "$#" -eq 0 ]]; then
    echo "Usage:"
    echo "  $0 --name=pg1 --remote=backup_user@host [--mode=dump|rsync] [--auto] [--save=/path/to/yml] [--wg] [--cron]"
    echo
    echo "Options:"
    echo "  --name      PostgreSQL instance name (e.g., pg1)"
    echo "  --remote    SSH destination (user@host) for backup server"
    echo "  --mode      Sync method:"
    echo "                dump   = dump/restore over SSH (safe for live DBs)"
    echo "                rsync  = stop remote PG, rsync base dir (hot-spare style)"
    echo "  --auto      Skip prompts, full automation mode"
    echo "  --save      Save YAML metadata to this file (default: ./postgres_sync.yml)"
    echo "  --wg        (Planned) Enable WireGuard tunnel integration"
    echo "  --cron      Output a recommended crontab line for recurring sync"
    echo
    echo "Examples:"
    echo "  $0 --name=pg1 --remote=backup@192.168.1.100 --mode=dump --auto"
    echo "  $0 --name=pg1 --remote=backup@192.168.1.100 --mode=rsync --save=/opt/sync.yml"
    echo
    echo "Cron example:"
    echo "  */5 * * * * /path/to/$0 --name=pg1 --remote=backup@host --mode=dump --auto >> /var/log/pg_sync.log 2>&1"
    exit 0
fi


# ---------- Parse Args ----------
for ARG in "$@"; do
    case $ARG in
        --name=*) NAME="${ARG#*=}" ;;
        --remote=*) REMOTE="${ARG#*=}" ;;
        --mode=*) MODE="${ARG#*=}" ;;
        --auto) AUTO=true ;;
        --save=*) SAVE_FILE="${ARG#*=}" ;;
        *) echo "Unknown argument: $ARG" && exit 1 ;;
    esac
done

# ---------- Validation ----------
if [[ -z "$NAME" || -z "$REMOTE" ]]; then
    echo "Missing --name or --remote"
    exit 1
fi

MODE=${MODE:-dump}
TIMESTAMP=$(date +"%Y-%m-%d_%H-%M-%S")
PORT=$(grep port "/var/lib/postgresql/$NAME/postgresql.conf" | awk '{print $3}' | tr -d "'")
DATA_DIR="/var/lib/postgresql/$NAME"
TMP_DUMP="/tmp/${NAME}_${TIMESTAMP}.sql"
REMOTE_BASE="/var/backups/postgresql_sync/${NAME}_${TIMESTAMP}"

mkdir -p /tmp/postgres_sync_logs

# ---------- DUMP MODE ----------
if [[ "$MODE" == "dump" ]]; then
    echo "[+] Sync mode: DUMP -> $REMOTE"
    echo "[+] Creating SQL dump..."

    sudo -u postgres pg_dump -p "$PORT" > "$TMP_DUMP"

    echo "[+] Copying to remote..."
    ssh "$REMOTE" "mkdir -p $REMOTE_BASE"
    scp "$TMP_DUMP" "$REMOTE:$REMOTE_BASE/"

    echo "[+] Restoring on remote..."
    ssh "$REMOTE" "sudo -u postgres dropdb --if-exists $NAME && sudo -u postgres createdb $NAME"
    ssh "$REMOTE" "sudo -u postgres psql $NAME < $REMOTE_BASE/$(basename "$TMP_DUMP")"

    rm -f "$TMP_DUMP"

    # ---------- Append to YAML ----------
    echo >> "$SAVE_FILE"
    echo "# Sync (DUMP) - $TIMESTAMP" >> "$SAVE_FILE"
    echo "$NAME:" >> "$SAVE_FILE"
    echo "  method: dump" >> "$SAVE_FILE"
    echo "  remote: $REMOTE" >> "$SAVE_FILE"
    echo "  timestamp: $TIMESTAMP" >> "$SAVE_FILE"
    echo "  backup_dir: $REMOTE_BASE" >> "$SAVE_FILE"

# ---------- RSYNC MODE ----------
elif [[ "$MODE" == "rsync" ]]; then
    echo "[+] Sync mode: RSYNC -> $REMOTE"
    echo "[!] Stopping remote PostgreSQL instance first..."

    ssh "$REMOTE" "sudo systemctl stop postgresql || true"

    echo "[+] Syncing data directory..."
    rsync -az --delete -e ssh "$DATA_DIR/" "$REMOTE:$DATA_DIR/"

    echo "[+] Restarting remote PostgreSQL..."
    ssh "$REMOTE" "sudo systemctl start postgresql"

    # ---------- Append to YAML ----------
    echo >> "$SAVE_FILE"
    echo "# Sync (RSYNC) - $TIMESTAMP" >> "$SAVE_FILE"
    echo "$NAME:" >> "$SAVE_FILE"
    echo "  method: rsync" >> "$SAVE_FILE"
    echo "  remote: $REMOTE" >> "$SAVE_FILE"
    echo "  timestamp: $TIMESTAMP" >> "$SAVE_FILE"
    echo "  data_dir: $DATA_DIR" >> "$SAVE_FILE"

else
    echo "Invalid --mode. Use dump or rsync"
    exit 1
fi

# ---------- Done ----------
echo
echo "[✓] PostgreSQL '$NAME' synced to: $REMOTE"
echo "[📝] Log saved to: $SAVE_FILE"
echo
