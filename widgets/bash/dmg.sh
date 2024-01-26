#!/bin/bash

# Check if two arguments are provided
if [ "$#" -ne 2 ]; then
    echo "Usage: $0 <Volume Name> <Source Folder>"
    exit 1
fi

VOL_NAME="$1"
SRC_FOLDER="$2"
TMP_DMG=$(mktemp /tmp/tmp.XXXXXX.dmg)
FINAL_DMG="${VOL_NAME}.dmg"

# Create a temporary DMG file with a unique name
if ! hdiutil create "$TMP_DMG" -ov -volname "$VOL_NAME" -fs HFS+ -srcfolder "$SRC_FOLDER"; then
    echo "Failed to create temporary DMG file."
    exit 1
fi

# Convert the temporary DMG to a compressed DMG
if ! hdiutil convert "$TMP_DMG" -format UDZO -o "$FINAL_DMG"; then
    echo "Failed to convert DMG file."
    rm "$TMP_DMG"
    exit 1
fi

# Remove the temporary DMG file
rm "$TMP_DMG"
