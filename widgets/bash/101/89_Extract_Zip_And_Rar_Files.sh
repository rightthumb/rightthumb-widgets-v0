#!/bin/bash
# Script to extract ZIP and RAR files

FILE="archive.zip"

if [[ "$FILE" == *.zip ]]; then
    unzip "$FILE"
elif [[ "$FILE" == *.rar ]]; then
    unrar x "$FILE"
else
    echo "Unsupported file format."
fi
