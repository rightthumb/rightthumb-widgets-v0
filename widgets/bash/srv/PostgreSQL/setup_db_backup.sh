#!/bin/bash
set -e

# ---------- Defaults ----------
AUTO=false
SAVE_FILE="$(pwd)/backup_settings.yml"

# ---------- Help ----------
if [[ "$1" == "--help" || "$1" == "-h" || "$#" -eq 0 ]]; then
    echo "Usage:"
    echo "  $0 --type=postgres|mongo --name=instance_name [--auto] [--save=/path/to/yml]"
    echo
    echo "Example:"
    echo "  $0 --type=postgres --name=pg1 --auto"
    echo "  $0 --type=mongo --name=mongo1 --save=/opt/backups.yml"
    exit 0
fi

# ---------- Parse Args ----------
for ARG in "$@"; do
    case $ARG in
        --type=*) TYPE="${ARG#*=}" ;;
        --name=*) NAME="${ARG#*=}" ;;
        --auto) AUTO=true ;;
        --save=*) SAVE_FILE="${ARG#*=}" ;;
        *) echo "Unknown argument: $ARG" && exit 1 ;;
    esac
done

# ---------- Validation ----------
if [[ -z "$TYPE" || -z "$NAME" ]]; then
    echo "Missing --type or --name"
    exit 1
fi

TIMESTAMP=$(date +"%Y-%m-%d_%H-%M-%S")
BACKUP_BASE="/var/backups/${TYPE}_${NAME}"
mkdir -p "$BACKUP_BASE"

# ---------- PostgreSQL Backups ----------
if [[ "$TYPE" == "postgres" ]]; then
    echo "[+] Setting up PostgreSQL backups for '$NAME'"

    FULL_DUMP="$BACKUP_BASE/${NAME}_full_${TIMESTAMP}.sql"
    CUSTOM_DUMP="$BACKUP_BASE/${NAME}_custom_${TIMESTAMP}.dump"
    ALL_DBS="$BACKUP_BASE/all_dbs_${TIMESTAMP}.sql"

    sudo -u postgres pg_dump -p "$(grep port /var/lib/postgresql/$NAME/postgresql.conf | awk '{print $3}')" > "$FULL_DUMP"
    sudo -u postgres pg_dump -p "$(grep port /var/lib/postgresql/$NAME/postgresql.conf | awk '{print $3}')" -Fc -f "$CUSTOM_DUMP"
    sudo -u postgres pg_dumpall > "$ALL_DBS"

    # Append to YAML
    echo >> "$SAVE_FILE"
    echo "# PostgreSQL backup: $TIMESTAMP" >> "$SAVE_FILE"
    echo "$NAME:" >> "$SAVE_FILE"
    echo "  type: postgres" >> "$SAVE_FILE"
    echo "  full_dump: $FULL_DUMP" >> "$SAVE_FILE"
    echo "  custom_dump: $CUSTOM_DUMP" >> "$SAVE_FILE"
    echo "  all_dbs: $ALL_DBS" >> "$SAVE_FILE"

# ---------- MongoDB Backups ----------
elif [[ "$TYPE" == "mongo" ]]; then
    echo "[+] Setting up MongoDB backups for '$NAME'"

    FULL_DUMP="$BACKUP_BASE/${NAME}_full_${TIMESTAMP}"
    ARCHIVE_DUMP="$BACKUP_BASE/${NAME}_archive_${TIMESTAMP}.gz"

    mongodump --port "$(grep port /etc/${NAME}.conf | tail -1 | awk '{print $2}')" --out "$FULL_DUMP"
    mongodump --port "$(grep port /etc/${NAME}.conf | tail -1 | awk '{print $2}')" --archive="$ARCHIVE_DUMP" --gzip

    # Append to YAML
    echo >> "$SAVE_FILE"
    echo "# MongoDB backup: $TIMESTAMP" >> "$SAVE_FILE"
    echo "$NAME:" >> "$SAVE_FILE"
    echo "  type: mongo" >> "$SAVE_FILE"
    echo "  full_dump_dir: $FULL_DUMP" >> "$SAVE_FILE"
    echo "  archive_dump: $ARCHIVE_DUMP" >> "$SAVE_FILE"

else
    echo "Unsupported type: $TYPE"
    exit 1
fi

# ---------- Done ----------
echo
echo "[✓] Backup complete for '$NAME'"
echo "[📝] Settings saved to: $SAVE_FILE"
echo
