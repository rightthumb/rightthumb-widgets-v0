#!/bin/bash

# Function to check if a package is installed
function check_and_install() {
	if [ $# -eq 1 ]; then
		local package=$1
		local command=$1
	elif [ $# -eq 2 ]; then
		local command=$1
		local package=$2
	fi
	if ! which "$command" > /dev/null; then
		sudo apt install -y "$package"
	fi
}




# Check for the correct number of arguments
if [ "$#" -ne 1 ]; then
	echo "Usage: $0 <input_image>"
	exit 1
fi

check_and_install convert imagemagick
check_and_install tesseract tesseract-ocr


input_image="$1"
temp_image="temp_$(basename "$input_image")"

# Preprocess the image with ImageMagick's convert for better OCR
# Adjust these settings as needed for your specific images
convert "$input_image" -colorspace Gray -type Grayscale -contrast-stretch 0 -resize 300% "$temp_image"

# Use Tesseract to extract text from the preprocessed image and print it to the console
tesseract "$temp_image" stdout

# Clean up the temporary preprocessed image
rm "$temp_image"