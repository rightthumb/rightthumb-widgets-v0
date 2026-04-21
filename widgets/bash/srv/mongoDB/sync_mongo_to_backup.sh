#!/bin/bash
set -e

# ---------- Defaults ----------
AUTO=false
SAVE_FILE="$(pwd)/mongo_sync.yml"

# ---------- Help ----------
if [[ "$1" == "--help" || "$1" == "-h" || "$#" -eq 0 ]]; then
    echo "Usage:"
    echo "  $0 --name=mongo1 --remote=user@host [--mode=dump|rsync] [--auto] [--save=/path/to/yml]"
    echo
    echo "  --name     MongoDB instance name (e.g., mongo1)"
    echo "  --remote   SSH destination (user@host)"
    echo "  --mode     dump (archive transfer) or rsync (data dir copy)"
    echo "  --auto     No prompts"
    echo "  --save     Append metadata to YAML file"
    echo
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
DATA_DIR="/var/lib/$NAME"
REMOTE_BASE="/var/backups/mongo_sync/${NAME}_${TIMESTAMP}"

mkdir -p /tmp/mongo_sync_logs

# ---------- Get MongoDB port from config ----------
PORT=$(grep port /etc/${NAME}.conf | awk '{print $2}')

# ---------- DUMP ----------
if [[ "$MODE" == "dump" ]]; then
    ARCHIVE="/tmp/${NAME}_${TIMESTAMP}.archive.gz"
    echo "[+] Creating dump..."
    mongodump --port "$PORT" --archive="$ARCHIVE" --gzip

    echo "[+] Copying to $REMOTE"
    ssh "$REMOTE" "mkdir -p $REMOTE_BASE"
    scp "$ARCHIVE" "$REMOTE:$REMOTE_BASE/"

    echo "[+] Restoring on remote"
    ssh "$REMOTE" "mongorestore --archive=$REMOTE_BASE/$(basename "$ARCHIVE") --gzip --drop"

    rm -f "$ARCHIVE"

    echo >> "$SAVE_FILE"
    echo "# MongoDB dump sync: $TIMESTAMP" >> "$SAVE_FILE"
    echo "$NAME:" >> "$SAVE_FILE"
    echo "  method: dump" >> "$SAVE_FILE"
    echo "  remote: $REMOTE" >> "$SAVE_FILE"
    echo "  archive: $REMOTE_BASE/$(basename "$ARCHIVE")" >> "$SAVE_FILE"

# ---------- RSYNC ----------
elif [[ "$MODE" == "rsync" ]]; then
    echo "[!] Shutting down remote MongoDB before rsync"
    ssh "$REMOTE" "sudo systemctl stop mongod || sudo systemctl stop $NAME || true"

    echo "[+] Syncing data directory..."
    rsync -az --delete -e ssh "$DATA_DIR/" "$REMOTE:$DATA_DIR/"

    echo "[+] Restarting remote MongoDB"
    ssh "$REMOTE" "sudo systemctl start mongod || sudo systemctl start $NAME"

    echo >> "$SAVE_FILE"
    echo "# MongoDB rsync sync: $TIMESTAMP" >> "$SAVE_FILE"
    echo "$NAME:" >> "$SAVE_FILE"
    echo "  method: rsync" >> "$SAVE_FILE"
    echo "  remote: $REMOTE" >> "$SAVE_FILE"
    echo "  data_dir: $DATA_DIR" >> "$SAVE_FILE"

else
    echo "Invalid --mode (use dump or rsync)"
    exit 1
fi

echo
echo "[✓] MongoDB '$NAME' synced to: $REMOTE"
echo "[📝] Settings saved to: $SAVE_FILE"
echo
