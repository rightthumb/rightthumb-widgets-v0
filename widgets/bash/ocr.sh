#!/usr/bin/env bash
# ocr.sh — Convert a file to text using ImageMagick + Tesseract.
# Works on Debian/Ubuntu, RHEL/CentOS/Alma/Rocky, Arch, openSUSE.
# Usage:
#   ./ocr.sh --install-only
#   ./ocr.sh -f input.pdf -o output.txt --lang eng --dpi 300
# Defaults: lang=eng, dpi=300, output=stdout

set -euo pipefail

LANG_CODE="eng"
DPI=300
OUTPUT="-"
INSTALL_ONLY=0
INPUT_FILE=""

err() { echo "[-] $*" >&2; exit 1; }
has() { command -v "$1" >/dev/null 2>&1; }

usage() {
	cat <<EOF
Usage:
  $0 --install-only
  $0 -f <file> [-o out.txt] [--lang eng] [--dpi 300]

Options:
  -f, --file         Input file (image or PDF)
  -o, --output       Output text file (default: stdout)
	--lang         Tesseract language code(s) (default: eng; e.g. 'eng+spa')
	--dpi          Rasterization DPI for PDFs/images (default: 300)
	--install-only Install required packages and exit
  -h, --help         Show this help

Examples:
  $0 --install-only
  $0 -f scan.pdf -o scan.txt
  $0 -f receipt.jpg --lang eng --dpi 400
EOF
}

if [ $# -eq 0 ]; then
	usage
	exit 1
fi

# --- Parse args ---
while (( "$#" )); do
	case "$1" in
		-f|--file) INPUT_FILE="${2:-}"; shift 2 ;;
		-o|--output) OUTPUT="${2:-}"; shift 2 ;;
		--lang) LANG_CODE="${2:-}"; shift 2 ;;
		--dpi) DPI="${2:-}"; shift 2 ;;
		--install-only) INSTALL_ONLY=1; shift ;;
		-h|--help) usage; exit 0 ;;
		*) err "Unknown option: $1 (use -h for help)";;
	esac
done

# --- Distro detection ---
detect_distro() {
	if [ -r /etc/os-release ]; then
		. /etc/os-release
		echo "${ID_LIKE:-$ID}"
	else
		uname -a
	fi
}
DISTRO="$(detect_distro | tr '[:upper:]' '[:lower:]')"

# --- Installers for required tools ---
install_deps() {
	echo "[*] Ensuring ImageMagick and Tesseract are installed..."
	if [[ "$DISTRO" == *"debian"* || "$DISTRO" == *"ubuntu"* ]]; then
		sudo apt-get update -y
		sudo apt-get install -y imagemagick tesseract-ocr
		# Optional: language packs example
		# sudo apt-get install -y tesseract-ocr-${LANG_CODE%%+*} || true
	elif [[ "$DISTRO" == *"rhel"* || "$DISTRO" == *"centos"* || "$DISTRO" == *"fedora"* || "$DISTRO" == *"rocky"* || "$DISTRO" == *"almalinux"* ]]; then
		# EPEL often needed for tesseract on RHEL-like
		if ! rpm -qa | grep -qi epel-release && has dnf; then
			sudo dnf install -y epel-release || true
		elif ! rpm -qa | grep -qi epel-release && has yum; then
			sudo yum install -y epel-release || true
		fi
		if has dnf; then
			sudo dnf install -y ImageMagick tesseract
		else
			sudo yum install -y ImageMagick tesseract
		fi
	elif [[ "$DISTRO" == *"arch"* ]]; then
		sudo pacman -Syu --noconfirm
		sudo pacman -S --noconfirm imagemagick tesseract
	elif [[ "$DISTRO" == *"suse"* || "$DISTRO" == *"opensuse"* ]]; then
		sudo zypper refresh
		sudo zypper install -y ImageMagick tesseract
	else
		err "Unsupported distro: $DISTRO. Install 'imagemagick' and 'tesseract' manually."
	fi
}

need_install=0
has convert || need_install=1
has tesseract || need_install=1
if (( need_install )); then install_deps; fi
if (( INSTALL_ONLY )); then
	echo "[+] Installation step complete."; exit 0
fi

# --- Validate input ---
[[ -n "$INPUT_FILE" ]] || { usage; err "Missing -f|--file"; }
[[ -r "$INPUT_FILE" ]] || err "Cannot read input file: $INPUT_FILE"

# --- Work dir ---
TMPDIR="$(mktemp -d -t ocr-XXXXXX)"
cleanup() { rm -rf "$TMPDIR"; }
trap cleanup EXIT

# --- Convert to an OCR-friendly image (TIFF) ---
# Notes:
# - For multi-page PDFs, ImageMagick writes page-0000.tif, etc.
# - Using -density (input DPI), -units PixelsPerInch, and -depth 8 for OCR quality.
# - We set colorspace to gray to reduce noise/size; adjust if needed.
echo "[*] Rasterizing '$INPUT_FILE' at ${DPI} DPI..."
# shellcheck disable=SC2086
convert -density "$DPI" -units PixelsPerInch "$INPUT_FILE" \
	-depth 8 -colorspace Gray -strip +repage "$TMPDIR/page-%04d.tif"

shopt -s nullglob
pages=("$TMPDIR"/page-*.tif)
(( ${#pages[@]} > 0 )) || err "Conversion produced no pages; check ImageMagick PDF policy or input."

# --- OCR all pages and concatenate ---
echo "[*] Running Tesseract OCR (lang=${LANG_CODE})..."
OUTFILE="${OUTPUT}"
if [[ "$OUTFILE" != "-" ]]; then
	: > "$OUTFILE"  # truncate/create
fi

for tif in "${pages[@]}"; do
	if [[ "$OUTFILE" == "-" ]]; then
		tesseract "$tif" stdout -l "$LANG_CODE"
	else
		tesseract "$tif" stdout -l "$LANG_CODE" >> "$OUTFILE"
		echo -e "\n" >> "$OUTFILE"
	fi
done

if [[ "$OUTFILE" != "-" ]]; then
	echo "[+] OCR complete → $OUTFILE"
fi