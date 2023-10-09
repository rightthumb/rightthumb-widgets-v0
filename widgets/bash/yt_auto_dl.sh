#!/bin/bash

# Variables
URLS_FILE="/home/rightthumb/public_html/domains/eyeformeta.com/public_html/apps/md/notes/scott/_docs_/music/yt_auto/dl.md"
ERROR_FILE="/home/rightthumb/public_html/domains/eyeformeta.com/public_html/apps/md/notes/scott/_docs_/music/yt_auto/err.md"
OUTPUT_DIR="/home/rightthumb/phone/YoutTube_mp3"
SUCCESS_FILE="/home/rightthumb/public_html/domains/eyeformeta.com/public_html/apps/md/notes/scott/_docs_/music/yt_auto/success.md"   # Specify your success log file path
TEMP_COPY=$(mktemp)   # Temporary file to keep a backup of URLs for safety
/usr/local/bin/youtube-dlc
# Ensure youtube-dlc is installed
if ! command -v /usr/local/bin/youtube-dlc &> /dev/null; then
	echo "youtube-dlc is not installed. Please install it first."
	exit 1
fi

# Create output directory if it doesn't exist
mkdir -p "$OUTPUT_DIR"

# Backup content of URLs file to the safety temporary file and then clear the URLs file
cp "$URLS_FILE" "$TEMP_COPY"
> "$URLS_FILE"

# Process each URL from the temporary backup file
while IFS= read -r line; do
	# Trim whitespace
	url=$(echo "$line" | xargs)
	
	# Skip blank lines
	if [ -z "$url" ]; then
		continue
	fi

	echo "Processing $url"
	
	# Use youtube-dlc to download the audio in mp3 format
	if /usr/local/bin/youtube-dlc -x --audio-format mp3 -o "$OUTPUT_DIR/%(title)s.%(ext)s" "$url"; then
		# If the above command was successful, log to the success file
		echo "$url - Successfully downloaded" >> "$SUCCESS_FILE"
	else
		# If there was an error, save the URL to the error file
		echo "$url" >> "$ERROR_FILE"
	fi

	# Processed URLs are not added back to the main URLS_FILE, so they are effectively removed
done < "$TEMP_COPY"

# Cleanup
rm "$TEMP_COPY"
chmod 777 -R "$OUTPUT_DIR"
echo "Processing complete."