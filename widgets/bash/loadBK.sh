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
# wget -P "$tempdir" "$url"
curl -fsSL "$url" -o "$tempdir"
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
	*.tar.Z)
		tar -xZf "$tempdir/$filename" -C "$tempdir"
		;;
	*.tar.lz)
		apt-get install -y lzip
		lzip -d "$tempdir/$filename"
		tar -xf "$tempdir/$(basename "$filename" .lz)" -C "$tempdir"
		;;
	*.tar.lzma)
		apt-get install -y xz-utils
		unlzma -c "$tempdir/$filename" | tar -xf - -C "$tempdir"
		;;
	*.tar.lzo)
		apt-get install -y lzo
		lzop -d "$tempdir/$filename"
		tar -xf "$tempdir/$(basename "$filename" .lzo)" -C "$tempdir"
		;;
	*.tar.lrz)
		apt-get install -y lrzip
		lrzuntar "$tempdir/$filename" "$tempdir"
		;;
	*.tar.lzop)
		apt-get install -y lzop
		lzop -d "$tempdir/$filename"
		tar -xf "$tempdir/$(basename "$filename" .lzop)" -C "$tempdir"
		;;
	*)
		echo "Unsupported file extension."
		exit 1
		;;
esac

payload_dir=$(python3 $ww/python/locateDecompressedFiles.py "$tempdir")

[ -d "$payload_dir" ] && mv "$payload_dir"/* "$destination"

# Clean up the temporary directory
rm -rf "$tempdir"

echo "Files have been successfully extracted and moved to the destination directory."

exit 0