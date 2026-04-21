#!/bin/bash

# Define the file path
FILE="/mnt/c/Users/Scott/AppData/Local/Packages/Microsoft.WindowsTerminal_8wekyb3d8bbwe/LocalState/settings.json"

# Check if the file exists
if [[ ! -f "$FILE" ]]; then
  echo "File not found!"
  exit 1
fi

# Read the file content
CONTENT=$(cat "$FILE")

# Check and toggle between "ctrl+w" and "ctrl+shift+w"
if echo "$CONTENT" | grep -q "\"ctrl+w\""; then
  sed -i 's/"ctrl+w"/"ctrl+shift+w"/g' "$FILE"
  echo "Changed to ctrl+shift+w"
elif echo "$CONTENT" | grep -q "\"ctrl+shift+w\""; then
  sed -i 's/"ctrl+shift+w"/"ctrl+w"/g' "$FILE"
  echo "Changed to ctrl+w"
else
  echo "Neither ctrl+w nor ctrl+shift+w found in the file."
fi
