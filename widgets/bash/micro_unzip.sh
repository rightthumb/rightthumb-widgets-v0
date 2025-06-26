#!/bin/bash

show_help() {
	echo "Usage: $0 <archive_name> [output_folder]"
	echo "If output_folder isn't provided, the current directory will be used."
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

ARCHIVE_NAME="$1"
OUTPUT_FOLDER="${2:-.}"

case "$ARCHIVE_NAME" in
	*.zip)
		install_if_not_exists "unzip"
		unzip "$ARCHIVE_NAME" -d "$OUTPUT_FOLDER"
		;;
	*.tar)
		tar -xf "$ARCHIVE_NAME" -C "$OUTPUT_FOLDER"
		;;
	*.tar.gz)
		tar -xzf "$ARCHIVE_NAME" -C "$OUTPUT_FOLDER"
		;;
	*.tar.bz2)
		tar -xjf "$ARCHIVE_NAME" -C "$OUTPUT_FOLDER"
		;;
	*.gz)
		install_if_not_exists "gzip"
		gzip -d "$ARCHIVE_NAME"
		;;
	*.bz2)
		install_if_not_exists "bzip2"
		bzip2 -d "$ARCHIVE_NAME"
		;;
	*.rar)
		install_if_not_exists "unrar"
		unrar x "$ARCHIVE_NAME"
		# unrar x "$ARCHIVE_NAME" "$OUTPUT_FOLDER"
		;;
	*.xz|*.tar.xz)
		install_if_not_exists "xz-utils"
		tar -xJf "$ARCHIVE_NAME" -C "$OUTPUT_FOLDER"
		;;
	*.7z)
		install_if_not_exists "p7zip-full"
		7z x "$ARCHIVE_NAME" -o"$OUTPUT_FOLDER"
		;;
	*.zst)
		install_if_not_exists "zstd"
		tar --zstd -xf "$ARCHIVE_NAME" -C "$OUTPUT_FOLDER"
		;;
	*.lzma)
		install_if_not_exists "lzma"
		tar --lzma -xf "$ARCHIVE_NAME" -C "$OUTPUT_FOLDER"
		;;
	*.lz4)
		install_if_not_exists "liblz4-tool"
		tar --lz4 -xf "$ARCHIVE_NAME" -C "$OUTPUT_FOLDER"
		;;
	*.lzh)
		install_if_not_exists "lhasa"
		lhasa x "$ARCHIVE_NAME" -o "$OUTPUT_FOLDER"
		;;
	*.cab)
		install_if_not_exists "cabextract"
		cabextract -d "$OUTPUT_FOLDER" "$ARCHIVE_NAME"
		;;
	*.ace)
		install_if_not_exists "unace"
		unace x "$ARCHIVE_NAME" -d "$OUTPUT_FOLDER"
		;;
	*.tar.Z)
		tar -xZf "$ARCHIVE_NAME" -C "$OUTPUT_FOLDER"
		;;
	*.tar.lz)
		install_if_not_exists "lzip"
		tar --lzip -xf "$ARCHIVE_NAME" -C "$OUTPUT_FOLDER"
		;;
	*.tar.lzma)
		tar --lzma -xf "$ARCHIVE_NAME" -C "$OUTPUT_FOLDER"
		;;
	*.tar.lzo)
		install_if_not_exists "lzop"
		tar --lzop -xf "$ARCHIVE_NAME" -C "$OUTPUT_FOLDER"
		;;
	*.tar.lrz)
		install_if_not_exists "lrzip"
		lrzuntar "$ARCHIVE_NAME"
		;;
	*.tar.lzop)
		install_if_not_exists "lzop"
		tar --lzop -xf "$ARCHIVE_NAME" -C "$OUTPUT_FOLDER"
		;;
	# ... more formats to be added ...
	*)
		echo "Unsupported file extension."
		exit 1
		;;
esac

echo "Decompressed $ARCHIVE_NAME to $OUTPUT_FOLDER!"