#!/bin/bash

# Check if a source directory is provided as an argument
if [ -z "$1" ]; then
  echo "Usage: $0 <source_directory>"
  exit 1
fi

# Define the source directory and ensure it has a trailing slash
SOURCE_DIR="$1"
[[ "${SOURCE_DIR: -1}" != "/" ]] && SOURCE_DIR="${SOURCE_DIR}/"

# Check if the source directory exists
if [ ! -d "$SOURCE_DIR" ]; then
  echo "Error: Source directory '$SOURCE_DIR' does not exist."
  exit 1
fi

# Auto-login to Ossus (ensure the script path is correct and executable)
/opt/rightthumb-widgets-v0/widgets/bash/srv/webdav/vps-auto_login_ossus.sh --clean

if [ $? -ne 0 ]; then
  echo "Error: Failed to auto-login to Ossus."
  exit 1
fi

# Set the destination directory based on SOURCE_DIR
if [[ "$SOURCE_DIR" == /home/* ]]; then
  DEST_DIR="/mnt/ossus/backups/sullust$SOURCE_DIR"
else
  HOSTNAME=$(cat /etc/hostname)
  DEST_DIR="/mnt/ossus/backups/folders/${HOSTNAME}${SOURCE_DIR}/$(date +%s)"

fi

# Create the destination directory if it doesn't exist and check for errors
mkdir -p "$DEST_DIR"
if [ $? -ne 0 ]; then
  echo "Error: Failed to create destination directory '$DEST_DIR'."
  exit 1
fi

if [[ "$1" == "--quick" ]]; then
  add="--exclude=/vendor/ --exclude=/.git/ --exclude=/composer/ --exclude=/investing.sds.sh/  --exclude='/wp-*'"
else
  echo "not quick, thorough"
  add=""
fi

# Run rsync with appropriate options and check for success
rsync -avzu --ignore-errors --force --no-links --inplace $add "$SOURCE_DIR" "$DEST_DIR"
if [ $? -ne 0 ]; then
  echo "Error: rsync failed to sync files."
  exit 1
fi

echo "Sync completed successfully."