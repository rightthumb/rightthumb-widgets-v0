#!/bin/bash
# =====================================================
# Chroot Compressor / Decompressor
# Usage:
#   ./save-chroot.sh <archive-file> <folder> <action>
#
# Examples:
#   ./save-chroot.sh /root/ramchroot-backup.tar.zst /mnt/ramchroot compress
#   ./save-chroot.sh /root/ramchroot-backup.tar.zst /mnt/ramchroot decompress
# =====================================================

# -----------------------------
# Function: Show help
# -----------------------------
show_help() {
	cat << EOF

Usage:
  $(basename "$0") <archive-file> <folder> <action>

Arguments:
  <archive-file>   Path to the .tar.zst file (e.g. /root/backup.tar.zst)
  <folder>         Folder to compress or extract (e.g. /mnt/ramchroot)
  <action>         Must be either 'compress' or 'decompress'

Examples:
  $(basename "$0") /root/chroot.tar.zst /mnt/chroot compress
  $(basename "$0") /root/chroot.tar.zst /mnt/chroot decompress

EOF
}

# -----------------------------
# Argument Validation
# -----------------------------
if [ $# -ne 3 ]; then
	echo "❌ Error: Missing arguments."
	show_help
	exit 1
fi

ARCHIVE="$1"
FOLDER="$2"
ACTION="$3"

# Ensure folder exists
if [ ! -d "$FOLDER" ]; then
	echo "❌ Error: Folder '$FOLDER' does not exist."
	exit 2
fi

# Ensure zstd is installed
if ! command -v zstd >/dev/null 2>&1; then
	echo "⚙️ Installing zstd..."
	sudo dnf install -y zstd || { echo "❌ Failed to install zstd."; exit 3; }
fi

# -----------------------------
# Perform Action
# -----------------------------
case "$ACTION" in
	compress)
		echo "📦 Compressing '$FOLDER' -> '$ARCHIVE'"
		tar -czpf "$ARCHIVE" -C "$FOLDER" . \
			&& echo "✅ Compression complete: $ARCHIVE" \
			|| echo "❌ Compression failed."
		;;
	decompress)
		echo "📂 Decompressing '$ARCHIVE' -> '$FOLDER'"
		tar -I pigz -xpf "$ARCHIVE" -C "$FOLDER" \
			&& echo "✅ Decompression complete: $FOLDER" \
			|| echo "❌ Decompression failed."
		;;
	*)
		echo "❌ Invalid action: '$ACTION'"
		show_help
		exit 4
		;;
esac