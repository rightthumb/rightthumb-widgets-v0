#!/bin/bash

# Detect Operating System based on directory existence
if [ -d "/Users" ]; then
	OS_TYPE="Mac"
elif [ -d "/home" ]; then
	OS_TYPE="Linux"
else
	OS_TYPE="Unknown"
fi

# Function to download a file from a URL
download_file() {
	URL="$1"
	DESTINATION="$2"

	if command -v curl > /dev/null 2>&1; then
		curl -L "$URL" -o "$DESTINATION"
	elif command -v wget > /dev/null 2>&1; then
		wget "$URL" -O "$DESTINATION"
	else
		echo "Error: Neither curl nor wget is installed."
		exit 1
	fi
	echo "Download completed: $DESTINATION"
}

# Function to upload a file to a server
upload_file2() {
	FILE_PATH="$1"
	SERVER_URL="https://sds.sh/a/up/"

	curl -F "uploaded_file=@${FILE_PATH}" "${SERVER_URL}"
	echo "Uploading..."
}
upload_file() {
	FILE_PATH="$1"
	ENDPOINT_URL="https://sds.sh/a/up/"
	echo "Uploading..."
	curl -s -F "file=@$FILE_PATH" $ENDPOINT_URL
}
# Function to mount a .dmg file on macOS
open_dmg() {
	DMG_PATH="$1"

	if [ "$OS_TYPE" = "Mac" ]; then
		echo "Mounting $DMG_PATH on macOS..."
		hdiutil attach "$DMG_PATH"
	else
		echo "Opening .dmg files is not supported on Linux."
	fi
}

# Function to create a .dmg file from a folder on macOS
create_dmg() {
	SOURCE_FOLDER="$1"
	OUTPUT_DMG="$2"

	if [ "$OS_TYPE" = "Mac" ]; then
		echo "Creating .dmg file from $SOURCE_FOLDER on macOS..."
		hdiutil create -volname "Custom Volume" -srcfolder "$SOURCE_FOLDER" -ov -format UDZO "$OUTPUT_DMG"
	else
		echo "Creating .dmg files is not directly supported on Linux."
	fi
}

# Function to unzip a file
unzip_file() {
	ARCHIVE_PATH="$1"
	DESTINATION="$2"

	if ! command -v unzip > /dev/null 2>&1; then
		echo "Unzip utility not found, installing..."
		sudo apt-get install -y unzip
	fi

	unzip "$ARCHIVE_PATH" -d "$DESTINATION"
	echo "Unzipping completed to: $DESTINATION"
}

# Function to create a ZIP archive
create_zip() {
	SOURCE_FOLDER="$1"
	OUTPUT_ZIP="$2"

	if ! command -v zip > /dev/null 2>&1; then
		echo "Zip utility not found, installing..."
		sudo apt-get install -y zip
	fi

	zip -r "$OUTPUT_ZIP" "$SOURCE_FOLDER"
	echo "ZIP archive created: $OUTPUT_ZIP"
}

# Help menu
print_help() {
	echo "Usage: $0 [option]..."
	echo "Options:"
	echo "  -d, --download <URL> <destination>   Download file from URL."
	echo "  -u, --upload <file> <URL>            Upload a file to a server."
	echo "  -o, --open-dmg <dmg-path>            Mount a .dmg file (macOS only)."
	echo "  -cd, --create-dmg <source> <dmg>     Create a .dmg file from a folder (macOS only)."
	echo "  -z, --unzip <archive> <destination>  Unzip a file."
	echo "  -cz, --create-zip <source> <zip>     Create a ZIP archive from a folder."
	echo "  -h, --help                           Display this help and exit."
	exit 0
}

# Parse command line options
while [[ "$#" -gt 0 ]]; do
	case $1 in
		-d|--download) download_file "$2" "$3"; shift 3 ;;
		-u|--upload) upload_file "$2"; shift 2 ;;
		-o|--open-dmg) open_dmg "$2"; shift 2 ;;
		-cd|--create-dmg) create_dmg "$2" "$3"; shift 3 ;;
		-z|--unzip) unzip_file "$2" "$3"; shift 3 ;;
		-cz|--create-zip) create_zip "$2" "$3"; shift 3 ;;
		-h|--help) print_help ;;
		*) echo "Unknown option: $1" >&2; print_help ;;
	esac
done

# If no options were passed, show help
if [ "$#" -eq 0 ]; then
	print_help
fi




# #!/bin/bash

# # Check if two arguments are provided
# if [ "$#" -ne 2 ]; then
#     echo "Usage: $0 <Volume Name> <Source Folder>"
#     exit 1
# fi

# VOL_NAME="$1"
# SRC_FOLDER="$2"
# TMP_DMG=$(mktemp /tmp/tmp.XXXXXX.dmg)
# FINAL_DMG="${VOL_NAME}.dmg"

# # Create a temporary DMG file with a unique name
# if ! hdiutil create "$TMP_DMG" -ov -volname "$VOL_NAME" -fs HFS+ -srcfolder "$SRC_FOLDER"; then
#     echo "Failed to create temporary DMG file."
#     exit 1
# fi

# # Convert the temporary DMG to a compressed DMG
# if ! hdiutil convert "$TMP_DMG" -format UDZO -o "$FINAL_DMG"; then
#     echo "Failed to convert DMG file."
#     rm "$TMP_DMG"
#     exit 1
# fi

# # Remove the temporary DMG file
# rm "$TMP_DMG"