#!/bin/bash

# Variables
DEST_DIR="/var/www/webdav/sullust_home/0/"
BACKUP_DIR="/var/_webdav"
LOG_DIR="/var/www/webdav/sullust_home/logs"
LOG_FILE="${LOG_DIR}/backup_$(date +%Y-%m-%d).log"
SLOTS=(1 2 3 4)
CURRENT_MONTH=$(date +%m)
CURRENT_SLOT=$((CURRENT_MONTH % 4))

# Ensure log directory exists
mkdir -p "$LOG_DIR"

# Determine target backup directory
TARGET_BACKUP="${BACKUP_DIR}/${SLOTS[$CURRENT_SLOT]}/"

# Remove old backup
rm -rf "$TARGET_BACKUP"

# Ensure target backup directory exists
mkdir -p "$TARGET_BACKUP"

# Perform rsync
rsync -avz --delete "$DEST_DIR/" "$TARGET_BACKUP" > "$LOG_FILE" 2>&1

# Crontab entry (commented out)
# 0 3 1 * *  /var/www/webdav/sullust_home/1234.sh