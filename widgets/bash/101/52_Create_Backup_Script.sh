#!/bin/bash
# Script to create a backup

SOURCE_DIR="/path/to/source"
DEST_DIR="/path/to/backup"

# Create a tar.gz archive
tar -czf "$DEST_DIR/backup_$(date +%F).tar.gz" "$SOURCE_DIR"

echo "Backup created: $DEST_DIR/backup_$(date +%F).tar.gz"