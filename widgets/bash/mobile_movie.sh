#!/bin/bash

# Directories
INPUT_DIR="./"
OUTPUT_DIR="./"

# Ensure the output directory exists
mkdir -p "$OUTPUT_DIR"

# Loop over all videos in the input directory
for video in $INPUT_DIR*.{mp4,avi,mov,mkv}; do
	if [ -f "$video" ]; then
		# Extract filename and extension
		filename=$(basename -- "$video")
		extension="${filename##*.}"
		filename_noext="${filename%.*}"

		# Convert the video
		ffmpeg -i "$video" -vf "scale=iw*0.5:ih*0.5" -c:v libx264 -crf 23 -preset faster -c:a aac -b:a 128k "$OUTPUT_DIR""$filename_noext"_mobile.mp4

		echo "$video has been converted and saved to $OUTPUT_DIR"
	fi
done

echo "All conversions complete."