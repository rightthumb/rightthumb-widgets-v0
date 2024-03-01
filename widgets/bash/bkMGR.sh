#!/bin/bash

# Check for minimum required arguments
if [ $# -lt 2 ]; then
  echo "Usage:"
  echo "$0 <archive_path.tar.gz> -list"
  echo "$0 <archive_path.tar.gz> -meta <file_name>"
  echo "$0 <archive_path.tar.gz> -x <file_or_folder_name>"
  exit 1
fi

# Assign command-line arguments to variables
ARCHIVE_PATH="$1"
OPERATION="$2"
TARGET="$3" # This is either the file for -meta or the file/folder for -x

# Function to list contents of the archive
list_contents() {
  tar -tf "$ARCHIVE_PATH"
}

# Function to show metadata of a file (using -meta as list file details)
show_meta() {
  if tar -tf "$ARCHIVE_PATH" | grep -q "$TARGET"; then
	echo "File $TARGET exists in the archive. Details:"
	tar -tvf "$ARCHIVE_PATH" | grep "$TARGET"
  else
	echo "File $TARGET does not exist in the archive."
  fi
}

# Function to extract a specific file or folder
extract_target() {
  if tar -tf "$ARCHIVE_PATH" | grep -q "$TARGET"; then
	tar -xzf "$ARCHIVE_PATH" "$TARGET"
	echo "$TARGET extracted successfully."
  else
	echo "File or folder $TARGET does not exist in the archive."
  fi
}

# Perform operation based on the switch provided
case "$OPERATION" in
  -list)
	list_contents
	;;
  -meta)
	if [ -z "$TARGET" ]; then
	echo "Please specify a file name for metadata."
	exit 1
	fi
	show_meta
	;;
  -x)
	if [ -z "$TARGET" ]; then
	echo "Please specify a file or folder name to extract."
	exit 1
	fi
	extract_target
	;;
  *)
	echo "Invalid operation: $OPERATION"
	usage
	;;
esac