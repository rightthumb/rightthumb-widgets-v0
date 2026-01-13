#!/usr/bin/env bash
# ---------------------------------------------------------
# meta_search.sh
# A portable metadata + filename indexer for Linux.
# Safe for "/", because it automatically avoids system dirs.
# 693651dc-8498-8329-a75d-1df405a2267c
# ---------------------------------------------------------

# Directories to skip ALWAYS
SKIP_DIRS=(
	"/proc"
	"/sys"
	"/dev"
	"/run"
	"/tmp"
	"/var/run"
	"/var/cache"
)

INDEX_FILE="meta_index.tsv"

usage() {
	echo "Usage:"
	echo "  $0 index [path]"
	echo "  $0 search \"keyword\""
	exit 1
}

# -----------------------------------------
# Check if path should be skipped
# -----------------------------------------
should_skip() {
	local path="$1"
	for skip in "${SKIP_DIRS[@]}"; do
		case "$path" in
			"$skip"*) return 0 ;;
		esac
	done
	return 1
}

# -----------------------------------------
# INDEX MODE
# -----------------------------------------
index_folder() {
	local folder="$1"

	if [[ ! -d "$folder" ]]; then
		echo "ERROR: '$folder' is not a directory."
		exit 1
	fi

	echo "Building index from: $folder"
	echo "Output: $INDEX_FILE"
	echo -e "FILE\tSIZE\tTYPE\tMETA" > "$INDEX_FILE"

	while IFS= read -r -d '' file; do
		# Skip directories we shouldn't enter
		if should_skip "$file"; then
			continue
		fi

		# If it's a file, extract metadata
		if [[ -f "$file" ]]; then
			size=$(stat -c%s "$file" 2>/dev/null)
			type=$(file -b "$file" 2>/dev/null)
			
			# Extract EXIF + general metadata
			meta=$(exiftool -s -s -s "$file" 2>/dev/null | tr '\n' ';')

			echo -e "${file}\t${size}\t${type}\t${meta}" >> "$INDEX_FILE"
		fi
	done < <(find "$folder" -mindepth 1 -print0 2>/dev/null)

	echo "Index complete."
}

# -----------------------------------------
# SEARCH MODE
# -----------------------------------------
search_index() {
	local query="$1"

	if [[ ! -f "$INDEX_FILE" ]]; then
		echo "No index found. Run:"
		echo "  $0 index [path]"
		exit 1
	fi

	echo "Searching for: $query"
	grep -i --color=always "$query" "$INDEX_FILE"
}

# -----------------------------------------
# MAIN
# -----------------------------------------
cmd="$1"
arg="$2"

case "$cmd" in
	index)
		index_folder "${arg:-.}"
		;;
	search)
		search_index "$arg"
		;;
	*)
		usage
		;;
esac