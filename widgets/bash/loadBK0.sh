#!/bin/bash

# loadBK https://rightthumb.com/OFFSITE/cowsay.tar.xz /usr/share/cowsay/cows
# loadBK https://rightthumb.com/OFFSITE/figlet.tar.xz /usr/share/figlet


# Check if the correct number of arguments are provided
if [ "$#" -ne 2 ]; then
	echo "Usage: $0 <url> <destination>"
	exit 1
fi

# Get the URL and destination directory from the arguments
url="$1"
destination="$2"

# Get the filename from the URL
filename=$(basename "$url")

# Create a temporary directory for downloading and extracting the file
tempdir=$(mktemp -d)

# tempdir="$HOME/decompress_temp"
# [ -d "$tempdir" ] && rm -rf "$tempdir"



# Download the file to the temporary directory
wget -P "$tempdir" "$url"

# Determine the file extension and use the appropriate decompression method
case "$filename" in
	*.zip)
		apt-get install -y unzip
		unzip "$tempdir/$filename" -d "$tempdir"
		;;
	*.tar)
		tar -xf "$tempdir/$filename" -C "$tempdir"
		;;
	*.tar.gz)
		tar -xzf "$tempdir/$filename" -C "$tempdir"
		;;
	*.tar.bz2)
		tar -xjf "$tempdir/$filename" -C "$tempdir"
		;;
	*.gz)
		apt-get install -y gzip
		gzip -d "$tempdir/$filename"
		;;
	*.bz2)
		apt-get install -y bzip2
		bzip2 -d "$tempdir/$filename"
		;;
	*.rar)
		apt-get install -y unrar
		unrar x "$tempdir/$filename" "$tempdir"
		;;
	*.xz|*.tar.xz)
		apt-get install -y xz-utils
		tar -xJf "$tempdir/$filename" -C "$tempdir"
		;;
	*.7z)
		apt-get install -y p7zip-full
		7z x "$tempdir/$filename" -o"$tempdir"
		;;
	*.zst)
		apt-get install -y zstd
		tar -I zstd -xf "$tempdir/$filename" -C "$tempdir"
		;;
	*.lzma)
		apt-get install -y xz-utils
		tar --lzma -xf "$tempdir/$filename" -C "$tempdir"
		;;
	*.lz4)
		apt-get install -y liblz4-tool
		lz4 -d "$tempdir/$filename" "$tempdir/$(basename "$filename" .lz4)"
		;;
	*.lzh)
		apt-get install -y lhasa
		lhasa x "$tempdir/$filename" -C "$tempdir"
		;;
	*.cab)
		apt-get install -y cabextract
		cabextract -d "$tempdir" "$tempdir/$filename"
		;;
	*.ace)
		apt-get install -y unace
		unace x -y "$tempdir/$filename" -o "$tempdir"
		;;
	*)
		echo "Unsupported file extension."
		exit 1
		;;
esac

payload_dir=$( python3 $ww/widgets/python/locateDecompressedFiles.py  "$tempdir")


# source $HOME/.bashrc
# $p files
# echo "python3 $ww/widgets/python/locateDecompressedFiles.py  $tempdir"
# echo "mv $payload_dir/* $destination"


[ -d "$payload_dir" ] && mv "$payload_dir"/* "$destination"


# # Move the payload to the destination directory
# # Find the first regular file within the extracted contents
# first_file=$(find "$tempdir" -type f | head -n 1)

# if [ -n "$first_file" ]; then
#     # Extract the parent directory of the first file found
#     payload_dir=$(dirname "$first_file")
	
#     # Move the contents of the payload directory to the destination directory
#     mv "$payload_dir"/* "$destination"
# else
#     echo "No files found in the extracted contents."
#     exit 1
# fi

# # Clean up the temporary directory
# rm -rf "$tempdir"

# echo "Files have been successfully extracted and moved to the destination directory."

# exit 0