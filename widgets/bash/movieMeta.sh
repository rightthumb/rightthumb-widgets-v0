#!/bin/bash

# Update system repositories
# sudo apt-get update

# Install ffmpeg, mediainfo, and exiftool
sudo apt-get install -y ffmpeg mediainfo libimage-exiftool-perl

# Check if a file path is provided as an argument
if [ -z "$1" ]
then
  echo "Please provide a file path."
  exit 1
fi

# File path from the first argument
FILE_PATH="$1"

# Using ffmpeg to extract metadata
echo "Metadata from ffmpeg:"
ffmpeg -i "$FILE_PATH" -hide_banner

# Using mediainfo to extract metadata
echo "Metadata from mediainfo:"
mediainfo "$FILE_PATH"

# Using exiftool to extract metadata
echo "Metadata from exiftool:"
exiftool "$FILE_PATH"