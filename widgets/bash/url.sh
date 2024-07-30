#!/bin/bash

theScript="$HOME/Downloads/URL-SCRIPT"

# Check if URL or code is provided
if [ -z "$1" ]; then
	echo "ERROR: no URL, ex: u <url> [args...]"
	exit 1
fi

# Check if the first argument starts with "http". If not, form the URL
if [[ "$1" != http* ]]; then
	# Extract the extension and base name from the filename
	filename="$1"
	ext="${filename##*.}"
	base="${filename%.*}"
	# If filename contains a slash, separate it into folder and script
	if [[ "$filename" == *"/"* ]]; then
		folder="${base%/*}"
		script="${base##*/}"
		URL="https://rightthumb.com/apps/code/$ext/$folder/$script.$ext"
	else
		URL="https://rightthumb.com/apps/code/$ext/$filename"
	fi
else
	URL="$1"
fi

# Shift the arguments
shift

# Create the Downloads directory if it doesn't exist
mkdir -p "$(dirname "$theScript")"

# Download the script
curl -fsSL "$URL" -o "$theScript"

# Read the first line (shebang) of the script
shebang=$(head -n 1 "$theScript")

# Check for a valid shebang line
if [[ $shebang == "#!"* ]]; then
	# If it has a valid shebang line, make it executable and run it
	chmod +x "$theScript"
	if [[ -f "$ww/widgets/python/shClean.py" ]]; then
		python3 $ww/widgets/python/shClean.py -f "$theScript" > /dev/null 2>&1
	fi
	# Use 'exec' to replace the current process with the script
	exec "$theScript" "$@"
else
	echo "Unsupported script type. Please make sure the script has a correct shebang."
fi