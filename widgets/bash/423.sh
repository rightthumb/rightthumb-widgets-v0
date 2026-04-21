#!/bin/bash

# Create mp3 directory if it doesn't exist
mkdir -p mp3

# Convert all .mp4 files to .mp3
for file in *.mp4; do
	[ -e "$file" ] || continue
	ffmpeg -y -i "$file" -vn -acodec libmp3lame -ab 192k "mp3/${file%.mp4}.mp3"
done