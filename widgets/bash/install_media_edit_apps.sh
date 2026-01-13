#!/usr/bin/env bash
#
# install-media-tools.sh
# Install a set of common media tools (ffmpeg, ImageMagick, Tesseract, SoX, MediaInfo, ExifTool, Gifsicle)
# on major Linux distros, only if they are not already installed.

set -e

# --- Colors (fallback-safe) ---------------------------------------------------
if [ -t 1 ]; then
	RED="$(tput setaf 1 2>/dev/null || echo '')"
	GREEN="$(tput setaf 2 2>/dev/null || echo '')"
	YELLOW="$(tput setaf 3 2>/dev/null || echo '')"
	BLUE="$(tput setaf 4 2>/dev/null || echo '')"
	RESET="$(tput sgr0 2>/dev/null || echo '')"
else
	RED=""; GREEN=""; YELLOW=""; BLUE=""; RESET=""
fi

log_info()  { echo "${BLUE}[INFO]${RESET}  $*"; }
log_ok()    { echo "${GREEN}[OK]${RESET}    $*"; }
log_warn()  { echo "${YELLOW}[WARN]${RESET}  $*"; }
log_error() { echo "${RED}[ERROR]${RESET} $*" >&2; }

show_help() {
	cat <<EOF
${BLUE}Media Tools Installer${RESET}

This script installs a common set of video/audio/image utilities if they are not
already present on your system.

Tools:
  - ffmpeg        : Video/audio conversion & processing
  - ImageMagick   : 'convert', 'identify', etc. for image manipulation
  - Tesseract     : OCR engine (tesseract)
  - SoX           : Audio processing (sox)
  - MediaInfo     : Media file info (mediainfo)
  - ExifTool      : Metadata reader/writer (exiftool)
  - Gifsicle      : GIF optimizer/editor (gifsicle)

Supported package managers:
  - apt-get (Debian/Ubuntu)
  - dnf / yum (Fedora/RHEL/Alma/Rocky/CentOS)
  - pacman (Arch/Manjaro)
  - zypper (openSUSE)
  - apk (Alpine)

Usage:
  bash $(basename "$0")          Install all missing tools
  bash $(basename "$0") -h       Show this help

Notes:
  - You may be prompted for your sudo password.
  - Some distros may require extra repos (e.g., ffmpeg on RHEL/Fedora).

EOF
}

# --- Arg handling -------------------------------------------------------------
if [ "$1" = "-h" ] || [ "$1" = "--help" ]; then
	show_help
	exit 0
fi

# --- Detect package manager ---------------------------------------------------
detect_pkg_manager() {
	if command -v apt-get >/dev/null 2>&1; then
		PKG=apt-get
	elif command -v dnf >/dev/null 2>&1; then
		PKG=dnf
	elif command -v yum >/dev/null 2>&1; then
		PKG=yum
	elif command -v pacman >/dev/null 2>&1; then
		PKG=pacman
	elif command -v zypper >/dev/null 2>&1; then
		PKG=zypper
	elif command -v apk >/dev/null 2>&1; then
		PKG=apk
	else
		log_error "No supported package manager (apt-get/dnf/yum/pacman/zypper/apk) found."
		exit 1
	fi
	log_info "Detected package manager: ${PKG}"
}

# --- Install a single command with pm-specific package names ------------------
install_cmd() {
	# Parameters:
	# 1: command name to check (e.g., ffmpeg)
	# 2: apt package
	# 3: dnf/yum package
	# 4: pacman package
	# 5: zypper package
	# 6: apk package
	local cmd="$1"
	local pkg_apt="$2"
	local pkg_dnf="$3"
	local pkg_pac="$4"
	local pkg_zyp="$5"
	local pkg_apk="$6"

	if command -v "$cmd" >/dev/null 2>&1; then
		log_ok "$cmd is already installed."
		return 0
	fi

	log_info "$cmd not found; attempting to install..."

	case "$PKG" in
		apt-get)
			if [ -n "$pkg_apt" ]; then
				sudo apt-get update
				sudo apt-get install -y "$pkg_apt"
			else
				log_warn "No apt package mapping for $cmd; skipping."
			fi
			;;
		dnf)
			if [ -n "$pkg_dnf" ]; then
				sudo dnf install -y "$pkg_dnf"
			else
				log_warn "No dnf package mapping for $cmd; skipping."
			fi
			;;
		yum)
			if [ -n "$pkg_dnf" ]; then
				sudo yum install -y "$pkg_dnf"
			else
				log_warn "No yum package mapping for $cmd; skipping."
			fi
			;;
		pacman)
			if [ -n "$pkg_pac" ]; then
				sudo pacman -Sy --noconfirm "$pkg_pac"
			else
				log_warn "No pacman package mapping for $cmd; skipping."
			fi
			;;
		zypper)
			if [ -n "$pkg_zyp" ]; then
				sudo zypper install -y "$pkg_zyp"
			else
				log_warn "No zypper package mapping for $cmd; skipping."
			fi
			;;
		apk)
			if [ -n "$pkg_apk" ]; then
				sudo apk add "$pkg_apk"
			else
				log_warn "No apk package mapping for $cmd; skipping."
			fi
			;;
		*)
			log_error "Unknown package manager '$PKG'."
			return 1
			;;
	esac

	if command -v "$cmd" >/dev/null 2>&1; then
		log_ok "$cmd installed successfully."
	else
		log_warn "Tried to install $cmd, but it still was not found. You may need to enable extra repos."
	fi
}

# --- Main ---------------------------------------------------------------------
detect_pkg_manager

# ffmpeg
install_cmd "ffmpeg" \
	"ffmpeg" \
	"ffmpeg" \
	"ffmpeg" \
	"ffmpeg" \
	"ffmpeg"

# ImageMagick (convert/identify/etc.)
install_cmd "convert" \
	"imagemagick" \
	"ImageMagick" \
	"imagemagick" \
	"ImageMagick" \
	"imagemagick"

# Tesseract OCR
install_cmd "tesseract" \
	"tesseract-ocr" \
	"tesseract" \
	"tesseract" \
	"tesseract" \
	"tesseract-ocr"

# SoX (audio processing)
install_cmd "sox" \
	"sox" \
	"sox" \
	"sox" \
	"sox" \
	"sox"

# MediaInfo (media file info)
install_cmd "mediainfo" \
	"mediainfo" \
	"mediainfo" \
	"mediainfo" \
	"mediainfo" \
	"mediainfo"

# ExifTool (metadata)
install_cmd "exiftool" \
	"libimage-exiftool-perl" \
	"perl-Image-ExifTool" \
	"exiftool" \
	"exiftool" \
	"exiftool"

# Gifsicle (GIF optimizer)
install_cmd "gifsicle" \
	"gifsicle" \
	"gifsicle" \
	"gifsicle" \
	"gifsicle" \
	"gifsicle"

log_ok "All checks complete."
echo "You now have a solid media toolbox (where supported by your distro)."

touch $HOME/.rt/profile/vars/touches/.install_media_edit_apps.sh