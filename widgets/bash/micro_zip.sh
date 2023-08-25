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
		zip -9 -r "$ARCHIVE_NAME" "$FOLDER"
		;;
	*.tar)
		tar -cf "$ARCHIVE_NAME" "$FOLDER"
		;;
	*.tar.gz)
		tar -czf "$ARCHIVE_NAME" "$FOLDER"
		;;
	*.tar.bz2)
		tar -cjf "$ARCHIVE_NAME" "$FOLDER"
		;;
	*.gz)
		install_if_not_exists "gzip"
		gzip "$FOLDER"
		;;
	*.bz2)
		install_if_not_exists "bzip2"
		bzip2 "$FOLDER"
		;;
	*.rar)
		install_if_not_exists "rar"
		# rar a -o- -inul -ep1 "$ARCHIVE_NAME" "$FOLDER"
		rar a "$ARCHIVE_NAME" "$FOLDER"
		;;
	*.xz)
		install_if_not_exists "xz-utils"
		tar cJf "$ARCHIVE_NAME" "$FOLDER"
		;;
	*.tar.xz)
		install_if_not_exists "xz-utils"
		tar cJf "$ARCHIVE_NAME" "$FOLDER"
		;;
	*.7z)
		install_if_not_exists "p7zip-full"
		7z a "$ARCHIVE_NAME" "$FOLDER"
		;;
	*.zst)
		install_if_not_exists "zstd"
		tar --zstd -cf "$ARCHIVE_NAME" "$FOLDER"
		;;
	*.lzma)
		install_if_not_exists "lzma"
		tar --lzma -cf "$ARCHIVE_NAME" "$FOLDER"
		;;
	*.lz4)
		install_if_not_exists "liblz4-tool"
		tar --lz4 -cf "$ARCHIVE_NAME" "$FOLDER"
		;;
	*.lzh)
		install_if_not_exists "lha"
		lha a "$ARCHIVE_NAME" "$FOLDER"
		;;
	*.cab)
		install_if_not_exists "cabextract"
		# cab format doesn't have a native Linux compressor tool. You might need external utilities or use Windows.
		echo "Compression to CAB format is not supported directly. Consider using a different tool or operating system."
		;;
	*.ace)
		# ACE format doesn't have a native Linux compressor tool due to patent restrictions and other reasons.
		echo "Compression to ACE format is not supported. Consider using a different format."
		;;
	*.tar.Z)
		install_if_not_exists "compress"
		tar -cZf "$ARCHIVE_NAME" "$FOLDER"
		;;
	*.tar.lz)
		install_if_not_exists "lzip"
		tar --lzip -cf "$ARCHIVE_NAME" "$FOLDER"
		;;
	*.tar.lzma)
		install_if_not_exists "lzma"
		tar --lzma -cf "$ARCHIVE_NAME" "$FOLDER"
		;;
	*.tar.lzo)
		install_if_not_exists "lzop"
		tar --lzo -cf "$ARCHIVE_NAME" "$FOLDER"
		;;
	*.tar.lrz)
		install_if_not_exists "lrzip"
		lrzip -z -o "$ARCHIVE_NAME" "$FOLDER"
		;;
	*.tar.lzop)
		install_if_not_exists "lzop"
		tar --lzop -cf "$ARCHIVE_NAME" "$FOLDER"
		;;
	# ... more formats to be added ...
	*)
		echo "Unsupported or unspecified file extension."
		show_help
		exit 1
		;;
esac

echo "Compressed $FOLDER into $ARCHIVE_NAME!"
