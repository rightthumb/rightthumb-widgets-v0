#!/bin/bash

# Variables
OUTPUT_DIR="/home/rightthumb/phone/YoutTube_mp4"
URLS_FILE="/home/rightthumb/public_html/domains/eyeformeta.com/public_html/apps/md/notes/scott/_docs_/_YouTube/mp4/queue.md"
ERROR_FILE="/home/rightthumb/public_html/domains/eyeformeta.com/public_html/apps/md/notes/scott/_docs_/_YouTube/mp4/.App/err.md"
SUCCESS_FILE="/home/rightthumb/public_html/domains/eyeformeta.com/public_html/apps/md/notes/scott/_docs_/_YouTube/mp4/.App/success.md"
INITIATION_FILE="/home/rightthumb/public_html/domains/eyeformeta.com/public_html/apps/md/notes/scott/_docs_/_YouTube/mp4/.App/initiation.md"
LOG_FILE="/home/rightthumb/public_html/domains/eyeformeta.com/public_html/apps/md/notes/scott/_docs_/_YouTube/mp4/.App/run.md"
CONFIGS_FOLDER=$(dirname "$URLS_FILE")
TEMP_COPY=$(mktemp)   # Temporary file to keep a backup of URLs for safety
chmod 777 -R "$CONFIGS_FOLDER"

if [ ! -e "$URLS_FILE" ]; then
	echo "$(date): No queue file" >> "$ERROR_FILE"
	exit 0
fi

FILE_SIZE=$(stat -c %s "$URLS_FILE")

if [ "$FILE_SIZE" -lt 10 ]; then
	exit 0
fi

# Ensure youtube-dlc is installed
if ! command -v /usr/local/bin/youtube-dlc &> /dev/null; then
	echo "youtube-dlc is not installed. Please install it first."
	exit 0
fi

# Create output directory if it doesn't exist
mkdir -p "$OUTPUT_DIR"

# Backup content of URLs file to the safety temporary file and then clear the URLs file
cp "$URLS_FILE" "$TEMP_COPY"
cat "$URLS_FILE" >> "$INITIATION_FILE"
echo "" >>"$INITIATION_FILE"
echo "$(date)" >>"$INITIATION_FILE"
cat "$URLS_FILE" >> "$INITIATION_FILE"
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
	
	# Use youtube-dlc to download the video in mp4 format
	if /usr/local/bin/youtube-dlc -f mp4 -o "$OUTPUT_DIR/%(title)s.%(ext)s" "$url"; then
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
chmod 777 -R "$CONFIGS_FOLDER"
> "$LOG_FILE"
echo "Processing complete."