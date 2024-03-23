#!/bin/bash

# Check if an input file was provided
if [ "$#" -ne 1 ]; then
	echo "Usage: $0 <input_movie_file>"
	exit 1
fi

input_file="$1"
output_file="${input_file%.*}_for_tablet.mp4"

# Use ffmpeg to get the video resolution
resolution=$(ffmpeg -i "$input_file" 2>&1 | grep -oP 'Stream.*Video.*\K\d{3,}x\d{3,}')

# Extract width and height
width=$(echo $resolution | cut -d'x' -f1)
height=$(echo $resolution | cut -d'x' -f2)

# Set the target resolution
target_width=1920
target_height=1080

# Check if conversion is needed
if [ "$width" -le "$target_width" ] && [ "$height" -le "$target_height" ]; then
	echo "Input video is already optimized for a large tablet. Copying video stream..."
	ffmpeg -i "$input_file" -c:v copy -c:a aac "$output_file"
else
	echo "Converting video for optimal large tablet viewing..."
	ffmpeg -i "$input_file" -vf "scale=$target_width:$target_height:force_original_aspect_ratio=decrease,pad=$target_width:$target_height:(ow-iw)/2:(oh-ih)/2" -c:v libx264 -preset fast -c:a aac "$output_file"
fi

echo "Conversion completed: $output_file"