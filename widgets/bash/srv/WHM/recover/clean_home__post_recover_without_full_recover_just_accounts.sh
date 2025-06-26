#!/bin/bash

set -euo pipefail

# Get the current home directory
HOME_DIR=$(pwd)

# Sanity check: make sure we're inside /home
if [[ "$HOME_DIR" != /home/* ]]; then
    echo "❌ This script must be run from within a /home/username folder."
    exit 1
fi

OLD_DIR="$HOME_DIR/_old_cpanel_"
mkdir -p "$OLD_DIR"

# List of items to KEEP (don't move)
KEEP_LIST=(
    "public_html"
    "public_ftp"
    "mail"
    "ssl"
    ".bashrc"
    ".bash_profile"
    ".bash_logout"
    ".htaccess"
    ".htpasswds"
)

echo "🔍 Scanning $HOME_DIR for cleanup..."
shopt -s dotglob
for item in "$HOME_DIR"/*; do
    base_item=$(basename "$item")

    # Skip if it's in KEEP_LIST or it's the old folder itself
    if [[ " ${KEEP_LIST[*]} " =~ " $base_item " ]] || [[ "$base_item" == "old" ]]; then
        echo "✅ Keeping: $base_item"
        continue
    fi

    # Move everything else to 'old'
    echo "🚚 Moving: $base_item → $OLD_DIR/"
    mv "$item" "$OLD_DIR/"
done
shopt -u dotglob

echo "✅ Cleanup complete. Contents moved to: $OLD_DIR"
