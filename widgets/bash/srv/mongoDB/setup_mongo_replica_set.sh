#!/bin/bash
set -e

# ---------- Defaults ----------
AUTO=false
SAVE_FILE="$(pwd)/mongo_replica.yml"

# ---------- Help ----------
if [[ "$1" == "--help" || "$1" == "-h" || "$#" -eq 0 ]]; then
    echo "Usage:"
    echo "  $0 --name=mongo1 --remote=user@host --port=27017 [--auto] [--save=/path/to/yml]"
    echo
    echo "  --name     MongoDB instance name"
    echo "  --remote   SSH destination (user@host)"
    echo "  --port     MongoDB port on replica (default: 27017)"
    echo "  --auto     Full automation"
    echo "  --save     Append YAML log to this file"
    echo ""
    echo "One-time sync (archive):"
    echo "sudo ./sync_mongo_to_backup.sh --name=mongo1 --remote=backup@10.0.0.2 --mode=dump --auto"
    echo ""
    echo "Real-time replica set:"
    echo "sudo ./setup_mongo_replica_set.sh --name=mongo1 --remote=backup@10.0.0.2 --port=27017 --auto"
    echo ""
    exit 0
fi

# ---------- Parse Args ----------
PORT=27017
for ARG in "$@"; do
    case $ARG in
        --name=*) NAME="${ARG#*=}" ;;
        --remote=*) REMOTE="${ARG#*=}" ;;
        --port=*) PORT="${ARG#*=}" ;;
        --auto) AUTO=true ;;
        --save=*) SAVE_FILE="${ARG#*=}" ;;
        *) echo "Unknown argument: $ARG" && exit 1 ;;
    esac
done

if [[ -z "$NAME" || -z "$REMOTE" ]]; then
    echo "Missing --name or --remote"
    exit 1
fi

TIMESTAMP=$(date +"%Y-%m-%d_%H-%M-%S")

echo "[+] Initiating replica set"

# 1. Ensure replica MongoDB has replicaSet enabled in config
ssh "$REMOTE" "grep -q '^replication:' /etc/${NAME}.conf || echo -e '\nreplication:\n  replSetName: rs0' | sudo tee -a /etc/${NAME}.conf && sudo systemctl restart mongod || sudo systemctl restart $NAME"

# 2. Initialize replica set on primary (localhost)
mongo --port "$PORT" --eval '
rs.initiate({
  _id: "rs0",
  members: [
    { _id: 0, host: "localhost:'"$PORT"'" }
  ]
})'

# 3. Add remote member
mongo --port "$PORT" --eval 'rs.add("'"$REMOTE"':'"$PORT"'")'

# 4. Log
echo >> "$SAVE_FILE"
echo "# Replica Set Config: $TIMESTAMP" >> "$SAVE_FILE"
echo "$NAME:" >> "$SAVE_FILE"
echo "  type: replica_set" >> "$SAVE_FILE"
echo "  primary: localhost:$PORT" >> "$SAVE_FILE"
echo "  secondary: $REMOTE:$PORT" >> "$SAVE_FILE"
echo "  replSetName: rs0" >> "$SAVE_FILE"

echo
echo "[✓] Real-time replica set configured"
echo "[📝] Settings saved to: $SAVE_FILE"
echo
