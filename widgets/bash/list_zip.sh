#!/bin/bash

# list_archive_contents.sh
# A script to list the contents of various archive file types.

show_help() {
	echo "Usage: $0 <archive_name>"
	echo "Supported archive formats:"
	echo "  .zip .tar .tar.gz .tar.bz2 .gz .bz2 .rar .xz .tar.xz .7z .zst .lzma .lz4 .lzh .cab .ace .tar.Z .tar.lz .tar.lzma .tar.lzo .tar.lrz .tar.lzop"
}

install_if_not_exists() {
	if ! command -v "$1" &> /dev/null; then
		echo "Installing $1..."
		sudo apt-get update
		sudo apt-get install -y "$1"
		if [ $? -ne 0 ]; then
			echo "Failed to install $1. Please install it manually."
			exit 1
		fi
	fi
}

if [ "$#" -ne 1 ]; then
	show_help
	exit 1
fi

ARCHIVE_NAME="$1"

if [ ! -f "$ARCHIVE_NAME" ]; then
	echo "Error: File '$ARCHIVE_NAME' does not exist."
	exit 1
fi

case "$ARCHIVE_NAME" in
	*.zip)
		install_if_not_exists "unzip"
		unzip -l "$ARCHIVE_NAME"
		;;
	*.tar)
		tar -tf "$ARCHIVE_NAME"
		;;
	*.tar.gz | *.tgz)
		tar -tzf "$ARCHIVE_NAME"
		;;
	*.tar.bz2 | *.tbz2)
		tar -tjf "$ARCHIVE_NAME"
		;;
	*.gz)
		install_if_not_exists "gzip"
		gzip -l "$ARCHIVE_NAME"
		;;
	*.bz2)
		install_if_not_exists "bzip2"
		bzip2 -l "$ARCHIVE_NAME"
		;;
	*.rar)
		install_if_not_exists "unrar"
		unrar l "$ARCHIVE_NAME"
		;;
	*.xz | *.tar.xz)
		install_if_not_exists "xz-utils"
		tar -tJf "$ARCHIVE_NAME"
		;;
	*.7z)
		install_if_not_exists "p7zip-full"
		7z l "$ARCHIVE_NAME"
		;;
	*.zst)
		install_if_not_exists "zstd"
		zstd -lv "$ARCHIVE_NAME"
		;;
	*.lzma)
		install_if_not_exists "lzma"
		lzma -lv "$ARCHIVE_NAME"
		;;
	*.lz4)
		install_if_not_exists "lz4"
		lz4 -l "$ARCHIVE_NAME"
		;;
	*.lzh)
		install_if_not_exists "lha"
		lha l "$ARCHIVE_NAME"
		;;
	*.cab)
		install_if_not_exists "cabextract"
		cabextract -l "$ARCHIVE_NAME"
		;;
	*.ace)
		install_if_not_exists "unace"
		unace l "$ARCHIVE_NAME"
		;;
	*.tar.Z)
		tar -tZf "$ARCHIVE_NAME"
		;;
	*.tar.lz)
		install_if_not_exists "lzip"
		tar --lzip -tf "$ARCHIVE_NAME"
		;;
	*.tar.lzma)
		install_if_not_exists "lzma"
		tar --lzma -tf "$ARCHIVE_NAME"
		;;
	*.tar.lzo)
		install_if_not_exists "lzop"
		tar --lzop -tf "$ARCHIVE_NAME"
		;;
	*.tar.lrz)
		install_if_not_exists "lrzip"
		lrzuntar --list "$ARCHIVE_NAME"
		;;
	*.tar.lzop)
		install_if_not_exists "lzop"
		tar --lzop -tf "$ARCHIVE_NAME"
		;;
	*)
		echo "Unsupported file extension."
		show_help
		exit 1
		;;
esac

exit 0