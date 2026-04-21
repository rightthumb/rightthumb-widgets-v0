#!/bin/bash

usage() {
	echo "Usage:"
	echo "  $0 <file> [trim_start_seconds] [trim_end_seconds]"
	echo
	echo "Arguments:"
	echo "  file                 Audio or video file (mp4, mp3, etc.)"
	echo "  trim_start_seconds   Seconds to remove from the beginning (default: 0)"
	echo "  trim_end_seconds     Seconds to remove from the end (default: 0)"
	echo
	echo "Recap:"
	echo "  - Keeps the original file format (mp4 stays mp4, mp3 stays mp3)"
	echo "  - Supports fractional seconds (e.g. 0.5)"
	echo "  - Missing args default to 0"
	echo "  - You can explicitly pass 0 to disable trimming on either end"
	echo "  - Original file is never modified"
	echo "  - Output file is written as: filename.trimmed.ext"
	echo "  - Uses stream copy (-c copy) for fast, no-reencode trimming"
	echo
	echo "Examples:"
	echo "  $0 video.mp4"
	echo "  $0 video.mp4 0.5"
	echo "  $0 video.mp4 0.5 0.5"
	echo "  $0 song.mp3 0 1"
}

# Require at least the file argument
if [ "$#" -lt 1 ]; then
	usage
	exit 1
fi

FILE="$1"
TRIM_START="${2:-0}"
TRIM_END="${3:-0}"

if [ ! -f "$FILE" ]; then
	echo "File not found: $FILE"
	exit 1
fi

BASE="${FILE%.*}"
EXT="${FILE##*.}"
OUT="${BASE}.trimmed.${EXT}"

# Get duration (audio or video)
DURATION=$(ffprobe -v error \
	-show_entries format=duration \
	-of default=noprint_wrappers=1:nokey=1 "$FILE")

NEW_DURATION=$(awk "BEGIN {print $DURATION - ($TRIM_START + $TRIM_END)}")

# Prevent invalid output
if (( $(echo "$NEW_DURATION <= 0" | bc -l) )); then
	echo "Error: trim exceeds or equals file duration"
	exit 1
fi

echo "Trimming:"
echo "  File:        $FILE"
echo "  Trim start:  ${TRIM_START}s"
echo "  Trim end:    ${TRIM_END}s"
echo "  New length:  ${NEW_DURATION}s"
echo "  Output:      $OUT"

ffmpeg -y \
	-ss "$TRIM_START" \
	-i "$FILE" \
	-t "$NEW_DURATION" \
	-c copy \
	"$OUT"

echo "Done."