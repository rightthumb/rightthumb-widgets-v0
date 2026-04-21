#!/bin/bash

# Function to convert video to MP3
convert_to_mp3() {
    input_file="$1"
    output_file="${input_file// /_}"  # Replace spaces with underscores
    output_file="${output_file//__/}"  # Remove double underscores
    output_file="${output_file%.*}.mp3"  # Remove movie extension and add .mp3
    output_file="${output_file//\(*\)}"  # Remove all parentheses and their contents
    output_file="${output_file#"${output_file%%[![:space:]]*}"}"  # Trim leading spaces
    output_file="${output_file%"${output_file##*[![:space:]]}"}"   # Trim trailing spaces

    ffmpeg -i "$input_file" -vn -acodec libmp3lame -q:a 4 "$output_file"
}

# Check if ffmpeg is installed
if ! command -v ffmpeg &>/dev/null; then
    echo "Error: ffmpeg is not installed. Please install ffmpeg to continue."
    exit 1
fi

# Check if an argument is provided
if [ $# -eq 0 ]; then
    echo "Usage: $0 <input_filename>"
    exit 1
fi

# Invoke the conversion function with the input filename
convert_to_mp3 "$1"
