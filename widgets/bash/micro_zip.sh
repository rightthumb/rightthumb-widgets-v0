#!/bin/bash

show_help() {
	echo "This is a smart app."
	echo "Usage: micro <folder/archive_name> [folder]"
	echo " if usage: micro folder.tar.xz   --> it will auto find the folder"
	echo " if usage: micro folder          --> it will assume you want folder.zip (-9)"
	echo "otherwise: micro folder.tar.gz folder"
	echo "Supported archive formats:"
	echo "  .zip .tar .tar.gz .tar.bz2 .gz .bz2 .rar .xz .tar.xz .7z .zst .lzma .lz4 .lzh .cab .ace .tar.Z .tar.lz .tar.lzma .tar.lzo .tar.lrz .tar.lzop"
}

install_if_not_exists() {
	dpkg -l "$1" &> /dev/null || sudo apt-get install -y "$1"
}

if [ "$#" -lt 1 ]; then
	show_help
	exit 1
fi

if [ "$#" -eq 1 ]; then
	# If the single argument is a directory, zip it.
	if [ -d "$1" ]; then
		FOLDER="$1"
		ARCHIVE_NAME="$FOLDER.zip"
	else
		# Strip decimals one-by-one and check for directory.
		tmp_arg="$1"
		while [[ "$tmp_arg" == *.* && ! -d "$tmp_arg" ]]; do
			tmp_arg="${tmp_arg%.*}"
		done

		# If a folder is found after stripping, set variables.
		if [ -d "$tmp_arg" ]; then
			FOLDER="$tmp_arg"
			ARCHIVE_NAME="$1"
		else
			echo "Error: Unable to determine folder."
			exit 1
		fi
	fi
else
	ARCHIVE_NAME="$1"
	FOLDER="$2"
fi



# show_help() {
# 	echo "Usage: $0 <folder> [archive_name]"
# 	echo "If archive_name isn't provided, a .zip file will be created by default."
# 	echo "Supported archive formats:"
# 	echo "  .zip .tar .tar.gz .tar.bz2 .gz .bz2 .rar .xz .tar.xz .7z .zst .lzma .lz4 .lzh .cab .ace .tar.Z .tar.lz .tar.lzma .tar.lzo .tar.lrz .tar.lzop"
# }

# install_if_not_exists() {
# 	dpkg -l "$1" &> /dev/null || sudo apt-get install -y "$1"
# }

# if [ "$#" -lt 1 ]; then
# 	show_help
# 	exit 1
# fi

# FOLDER="$1"
# ARCHIVE_NAME="${2:-$FOLDER.zip}"
case "$ARCHIVE_NAME" in
	*.zip)
		install_if_not_exists "zip"
		zip -9 -r -v "$ARCHIVE_NAME" "$FOLDER"
		;;
	*.tar)
		tar -cvf "$ARCHIVE_NAME" "$FOLDER"
		;;
	*.tar.gz)
		tar -czvf "$ARCHIVE_NAME" "$FOLDER"
		;;
	*.tar.bz2)
		tar -cjvf "$ARCHIVE_NAME" "$FOLDER"
		;;
	*.gz)
		install_if_not_exists "gzip"
		gzip -v "$FOLDER"
		;;
	*.bz2)
		install_if_not_exists "bzip2"
		bzip2 -v "$FOLDER"
		;;
	*.rar)
		install_if_not_exists "rar"
		rar a -v "$ARCHIVE_NAME" "$FOLDER"
		;;
	*.xz)
		install_if_not_exists "xz-utils"
		tar cJvf "$ARCHIVE_NAME" "$FOLDER"
		;;
	*.tar.xz)
		install_if_not_exists "xz-utils"
		tar cJvf "$ARCHIVE_NAME" "$FOLDER"
		;;
	*.7z)
		install_if_not_exists "p7zip-full"
		7z a -bd "$ARCHIVE_NAME" "$FOLDER"
		;;
	*.zst)
		install_if_not_exists "zstd"
		tar --zstd -cvf "$ARCHIVE_NAME" "$FOLDER"
		;;
	# ... more formats to be added ...
	*)
		echo "Unsupported or unspecified file extension."
		show_help
		exit 1
		;;
esac


echo "Compressed $FOLDER into $ARCHIVE_NAME!"