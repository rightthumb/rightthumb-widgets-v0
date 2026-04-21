#!/bin/bash

# Function to show help message
show_help() {
	echo "Usage: listarch <path_to_file1> [path_to_file2] ..."
	echo "List the contents of archive files."
	echo "Supported archive formats:"
	echo "  .zip .tar .tar.gz .tar.bz2 .gz .bz2 .rar .xz .tar.xz .7z .zst .lzma .lz4 .lzh .cab .ace .tar.Z .tar.lz .tar.lzma .tar.lzo .tar.lrz .tar.lzop"
}

# Function to check and install necessary utilities
install_if_not_exists() {
	dpkg -l "$1" &> /dev/null || sudo apt-get install -y "$1"
}

# Function to list contents of an archive file
list_contents() {
	local archive_path="$1"
	case "$archive_path" in
		*.zip)
			unzip -l "$archive_path"
			;;
		*.tar)
			tar -tvf "$archive_path"
			;;
		*.tar.gz | *.tgz)
			tar -ztvf "$archive_path"
			;;
		*.tar.bz2 | *.tbz2)
			tar -jtvf "$archive_path"
			;;
		*.gz)
			echo "Gzip does not support listing contents without extracting."
			;;
		*.bz2)
			echo "Bzip2 does not support listing contents without extracting."
			;;
		*.rar)
			unrar l "$archive_path"
			;;
		*.xz | *.tar.xz)
			tar -Jtvf "$archive_path"
			;;
		*.7z)
			7z l "$archive_path"
			;;
		*.zst)
			tar --zstd -tvf "$archive_path"
			;;
		# Add more formats as needed
		*)
			echo "Unsupported or unspecified file extension for '$archive_path'."
			;;
	esac
}

# Check if at least one path is provided
if [ "$#" -lt 1 ]; then
	show_help
	exit 1
fi

# Iterate over all provided paths and list contents
for path in "$@"; do
	if [ -f "$path" ]; then
		echo "Listing contents of: $path"
		list_contents "$path"
		echo "--------------------------------"
	else
		echo "Error: '$path' is not a valid file."
	fi
done