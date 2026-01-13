#!/usr/bin/env bash

input="$1"

if [[ -z "$input" ]]; then
	echo "Usage: $0 <video-file>"
	exit 1
fi

if [[ ! -f "$input" ]]; then
	echo "File not found: $input"
	exit 1
fi

dir="$(dirname "$input")"
base="$(basename "$input")"
out="${dir}/${base%.*}.mp3"

if [[ -f "$out" ]]; then
	echo "MP3 already exists, skipping: $out"
	exit 0
fi

echo "Converting: $input → $out"
ffmpeg -hide_banner -loglevel error -i "$input" -vn -acodec libmp3lame -b:a 192k "$out"

echo "Done: $out"