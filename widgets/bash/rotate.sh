#!/bin/bash

if [ "$#" -ne 1 ]; then
    echo "Usage: ./rotate.sh <image_file>"
    exit 1
fi

input_file="$1"
output_file="${input_file%.*}.${input_file##*.}"

ffmpeg -y -i "$input_file" -vf transpose=1 "$output_file"
# ffmpeg -y -i "$input_file" -vf transpose=1 "$output_file"
# ffmpeg -y -i "$input_file" -vf transpose=1 "$output_file"
