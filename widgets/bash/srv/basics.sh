#!/usr/bin/env bash
#
# install-server-tools.sh
#
# Multi-distro bootstrap script for a new server.
# - Categorized toolsets (basics, dev, langs, web, db, network, media)
# - Each category has tiers: minimal / basic / full
# - Uses "if command -v" checks so nothing is blanket-installed.
#
# Example usage:
#   bash install-server-tools.sh                 # show help (no args)
#   bash install-server-tools.sh --list          # list categories/tiers
#   bash install-server-tools.sh basics          # basics (default tier: basic)
#   bash install-server-tools.sh basics:full     # basics, full tier
#   bash install-server-tools.sh dev:full langs  # dev full + langs (basic)
#   bash install-server-tools.sh --all minimal   # ALL categories, minimal tier
#   bash install-server-tools.sh --tier full basics dev
#

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

# --- Help / usage -------------------------------------------------------------
show_help() {
	cat <<EOF
${BLUE}Server Tools Bootstrap${RESET}

This script installs common tools for a 25-year full-stack / infra dev:
- Basics     : nano, wget, curl, tree, htop, zip/unzip, rsync, jq, tmux, etc.
- Dev        : gcc/clang toolchains, make, cmake, git, git-lfs, docker, etc.
- Langs      : Python, pip, venv, Node.js, npm, Go, Rust (cargo), etc.
- Web        : nginx, PHP + CLI, Composer, PHP modules, curl.
- DB         : PostgreSQL, MariaDB/MySQL client & server, sqlite3.
- Network    : dnsutils/bind-tools (dig, nslookup, host), traceroute, whois, nmap, mtr.
- Media      : ffmpeg, ImageMagick, Tesseract, SoX, MediaInfo, ExifTool, Gifsicle.

Each category has three tiers:
  minimal  - smallest useful subset for that area
  basic    - what you'd typically want on a new dev/utility box
  full     - heavier, extra tools for that area

${YELLOW}NOTE on dig/dnsutils:${RESET}
  - On Debian/Ubuntu, 'dnsutils' installs: dig, nslookup, host, etc.
  - On RHEL/Fedora, 'bind-utils' provides similar client tools.
  - On Arch, 'bind-tools' provides dig/host/nslookup without running a DNS server.
  - On openSUSE, 'bind-utils' fills this role.
  - On Alpine, 'bind-tools' is the equivalent.

${BLUE}Usage:${RESET}
  ${GREEN}bash \$(basename "\$0") --list${RESET}
	Show categories and what they contain.

  ${GREEN}bash \$(basename "\$0") CATEGORY[:TIER] [CATEGORY[:TIER] ...]${RESET}
	Install specific categories. TIER = minimal|basic|full (default: basic).

	Examples:
		\$(basename "\$0") basics
		\$(basename "\$0") basics:full dev:full langs
		\$(basename "\$0") --tier full basics dev

  ${GREEN}bash \$(basename "\$0") --all [TIER]${RESET}
	Install ALL categories using TIER (default: basic).
	Examples:
		\$(basename "\$0") --all
		\$(basename "\$0") --all minimal
		\$(basename "\$0") --all full

  ${GREEN}bash \$(basename "\$0") --tier TIER CATEGORY [...]${RESET}
	Set a default tier for all category args that don't specify one.

  ${GREEN}bash \$(basename "\$0") -h | --help${RESET}
	Show this help.

EOF
}

list_categories() {
	cat <<EOF
${BLUE}Available categories and tiers:${RESET}

  ${GREEN}basics${RESET}
	minimal : nano, wget, curl, ca-certificates
	basic   : + htop, tree, zip, unzip, tar, rsync, gnupg
	full    : + ncdu, jq, screen, tmux, parted, lsof

  ${GREEN}dev${RESET}
	minimal : gcc toolchain, make, pkg-config
	basic   : + git, cmake, gdb
	full    : + clang, lldb, valgrind, strace, git-lfs, docker, docker-compose

  ${GREEN}langs${RESET}
	minimal : python3 + pip/venv
	basic   : + Node.js + npm, Go
	full    : + Rust (rustc + cargo), lld (LLVM linker, useful for wasm)

  ${GREEN}web${RESET}
	minimal : nginx web server, curl
	basic   : + PHP + PHP-CLI, Composer
	full    : + PHP extensions (curl, xml, mbstring)

  ${GREEN}db${RESET}
	minimal : PostgreSQL client, MariaDB/MySQL client, sqlite3
	basic   : + PostgreSQL server
	full    : + MariaDB/MySQL server

  ${GREEN}network${RESET}
	minimal : dnsutils/bind-tools (dig, host, nslookup)
	basic   : + traceroute, whois, net-tools
	full    : + nmap, mtr

  ${GREEN}media${RESET}
	minimal : ffmpeg, ImageMagick (convert)
	basic   : + SoX, MediaInfo
	full    : + Tesseract OCR, ExifTool, Gifsicle

EOF
}

# --- Arg handling -------------------------------------------------------------
if [ $# -eq 0 ]; then
	show_help
	exit 0
fi

# default tier if not specified on a token
TIER_DEFAULT="basic"

ALL_CATEGORIES=(basics dev langs web db network media)

CATEGORY_DESC_basics="Shell essentials: editors, downloaders, file utils."
CATEGORY_DESC_dev="Compiler toolchains, build tools, debugging."
CATEGORY_DESC_langs="Language runtimes and package managers."
CATEGORY_DESC_web="Web servers and PHP stack."
CATEGORY_DESC_db="Database clients/servers."
CATEGORY_DESC_network="DNS and networking tools (dig, traceroute, etc.)."
CATEGORY_DESC_media="Media tools (ffmpeg, ImageMagick, OCR, etc.)."

REQUESTED=()

while [ $# -gt 0 ]; do
	case "$1" in
		-h|--help)
			show_help
			exit 0
			;;
		--list)
			list_categories
			exit 0
			;;
		--tier)
			shift
			if [ -z "$1" ]; then
				log_error "--tier requires an argument (minimal|basic|full)."
				exit 1
			fi
			TIER_DEFAULT="$1"
			;;
		--all)
			shift
			tier="${1:-$TIER_DEFAULT}"
			case "$tier" in
				minimal|basic|full) ;;
				*)
					log_error "Invalid tier '$tier' for --all (use minimal|basic|full)."
					exit 1
					;;
			esac
			for c in "${ALL_CATEGORIES[@]}"; do
				REQUESTED+=("$c:$tier")
			done
			;;
		*)
			# CATEGORY or CATEGORY:TIER
			spec="$1"
			cat_name="${spec%%:*}"
			tier="${spec#*:}"
			if [ "$tier" = "$cat_name" ]; then
				tier="$TIER_DEFAULT"
			fi
			case "$tier" in
				minimal|basic|full) ;;
				*)
					log_error "Invalid tier '$tier' in spec '$spec' (use minimal|basic|full)."
					exit 1
					;;
			esac
			REQUESTED+=("$cat_name:$tier")
			;;
	esac
	shift
done

if [ ${#REQUESTED[@]} -eq 0 ]; then
	show_help
	exit 0
fi

# --- Detect package manager ---------------------------------------------------
PKG=""

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

# --- Ubuntu universe/multiverse helper ---------------------------------------
enable_ubuntu_universe_multiverse() {
	# Only relevant for apt-based Ubuntu
	if [ "$PKG" != "apt-get" ]; then
		return
	fi
	if [ ! -r /etc/os-release ] || ! grep -qi "ubuntu" /etc/os-release; then
		return
	fi

	log_info "Ensuring Ubuntu universe/multiverse repositories are enabled..."
	if ! command -v add-apt-repository >/dev/null 2>&1; then
		log_info "Installing software-properties-common to get add-apt-repository..."
		set +e
		sudo apt-get install -y software-properties-common
		local rc=$?
		set -e
		if [ $rc -ne 0 ]; then
			log_warn "Could not install software-properties-common; skipping universe/multiverse enable."
			return
		fi
	fi

	set +e
	sudo add-apt-repository -y universe
	sudo add-apt-repository -y multiverse
	local rc=$?
	set -e

	if [ $rc -eq 0 ]; then
		log_ok "Universe/multiverse enabled (or already enabled)."
	else
		log_warn "Failed to auto-enable universe/multiverse; you may need to fix sources manually."
	fi
}

# --- apt-get update once + error handling ------------------------------------
APT_UPDATED=0
APT_UPDATE_FAILED=0

apt_update_once() {
	if [ "$APT_UPDATE_FAILED" -eq 1 ]; then
		return
	fi
	if [ "$APT_UPDATED" -eq 1 ]; then
		return
	fi

	log_info "Running apt-get update once (for all apt installs)..."
	set +e
	sudo apt-get update
	local rc=$?
	set -e

	if [ $rc -ne 0 ]; then
		APT_UPDATE_FAILED=1
		log_error "apt-get update failed (rc=$rc)."
		log_error "Fix /etc/apt/sources.list and /etc/apt/sources.list.d/* then rerun this script."
	else
		APT_UPDATED=1
		log_ok "apt-get update completed successfully."
	fi
}

# --- Install a single command with pm-specific package names ------------------
# entry string format:
#   cmd|apt|dnf|pacman|zypper|apk|description
install_entry() {
	local entry="$1"
	local category="$2"

	IFS='|' read -r cmd pkg_apt pkg_dnf pkg_pac pkg_zyp pkg_apk desc <<< "$entry"

	if [ -z "$cmd" ]; then
		return 0
	fi

	if command -v "$cmd" >/dev/null 2>&1; then
		log_ok "[$category] $cmd is already installed (${desc})."
		return 0
	fi

	log_info "[$category] $cmd not found; attempting to install (${desc})..."

	case "$PKG" in
		apt-get)
			if [ -n "$pkg_apt" ]; then
				apt_update_once
				if [ "$APT_UPDATE_FAILED" -eq 1 ]; then
					log_warn "[$category] Skipping $cmd because apt-get update failed."
					return
				fi
				sudo apt-get install -y $pkg_apt
			else
				log_warn "[$category] No apt package mapping for $cmd; skipping."
			fi
			;;
		dnf)
			if [ -n "$pkg_dnf" ]; then
				sudo dnf install -y $pkg_dnf
			else
				log_warn "[$category] No dnf package mapping for $cmd; skipping."
			fi
			;;
		yum)
			if [ -n "$pkg_dnf" ]; then
				sudo yum install -y $pkg_dnf
			else
				log_warn "[$category] No yum package mapping for $cmd; skipping."
			fi
			;;
		pacman)
			if [ -n "$pkg_pac" ]; then
				sudo pacman -Sy --noconfirm $pkg_pac
			else
				log_warn "[$category] No pacman package mapping for $cmd; skipping."
			fi
			;;
		zypper)
			if [ -n "$pkg_zyp" ]; then
				sudo zypper install -y $pkg_zyp
			else
				log_warn "[$category] No zypper package mapping for $cmd; skipping."
			fi
			;;
		apk)
			if [ -n "$pkg_apk" ]; then
				sudo apk add $pkg_apk
			else
				log_warn "[$category] No apk package mapping for $cmd; skipping."
			fi
			;;
		*)
			log_error "Unknown package manager '$PKG'."
			return 1
			;;
	esac

	if command -v "$cmd" >/dev/null 2>&1; then
		log_ok "[$category] $cmd installed successfully."
	else
		log_warn "[$category] Tried to install $cmd, but it still was not found."
	fi
}

# --- Category definitions -----------------------------------------------------
# Each entry is:
#   cmd|apt|dnf|pacman|zypper|apk|description

# BASICS -----------------------------------------------------------------------
CATEGORY_basics_minimal=(
	"nano|nano|nano|nano|nano|nano|Basic terminal text editor"
	"wget|wget|wget|wget|wget|wget|HTTP/HTTPS downloader"
	"curl|curl|curl|curl|curl|curl|Data transfer (HTTP/FTP/etc.)"
	"update-ca-certificates|ca-certificates|ca-certificates|ca-certificates|ca-certificates|ca-certificates|CA certificate bundle updater"
)

CATEGORY_basics_basic=(
	"${CATEGORY_basics_minimal[@]}"
	"htop|htop|htop|htop|htop|htop|Interactive process viewer"
	"tree|tree|tree|tree|tree|tree|Recursive directory listing"
	"zip|zip|zip|zip|zip|zip|Zip archiver"
	"unzip|unzip|unzip|unzip|unzip|unzip|Unzip utility"
	"tar|tar|tar|tar|tar|tar|Tar archive utility"
	"rsync|rsync|rsync|rsync|rsync|rsync|File sync/copy tool"
	"gpg|gnupg|gnupg2|gnupg|gpg2|gnupg|GnuPG (OpenPGP crypto & signing)"
)

CATEGORY_basics_full=(
	"${CATEGORY_basics_basic[@]}"
	"ncdu|ncdu|ncdu|ncdu|ncdu|ncdu|NCurses disk usage viewer"
	"jq|jq|jq|jq|jq|jq|JSON processor"
	"screen|screen|screen|screen|screen|screen|Terminal multiplexer"
	"tmux|tmux|tmux|tmux|tmux|tmux|Terminal multiplexer (tmux)"
	"lsof|lsof|lsof|lsof|lsof|lsof|List open files"
	"parted|parted|parted|parted|parted|parted|Partition manager"
)

# DEV --------------------------------------------------------------------------
CATEGORY_dev_minimal=(
	"gcc|build-essential|gcc gcc-c++ make|base-devel|gcc gcc-c++ make|build-base|C/C++ compiler & build essentials"
	"pkg-config|pkg-config|pkgconf-pkg-config|pkgconf|pkgconf-pkg-config|pkgconf|pkg-config (build helper)"
	"make|make|make|make|make|make|Make build tool"
)

CATEGORY_dev_basic=(
	"${CATEGORY_dev_minimal[@]}"
	"git|git|git|git|git|git|Git version control"
	"cmake|cmake|cmake|cmake|cmake|cmake|CMake build system"
	"gdb|gdb|gdb|gdb|gdb|gdb|GNU debugger"
)

CATEGORY_dev_full=(
	"${CATEGORY_dev_basic[@]}"
	"clang|clang|clang|clang|clang|clang|Clang C/C++ compiler"
	"lldb|lldb|lldb|lldb|lldb|lldb|Clang/LLVM debugger"
	"valgrind|valgrind|valgrind|valgrind|valgrind|valgrind|Memory debugging/profiling"
	"strace|strace|strace|strace|strace|strace|System call tracer"
	"git-lfs|git-lfs|git-lfs|git-lfs|git-lfs|git-lfs|Git Large File Storage"
	"docker|docker.io|docker|docker|docker|docker|Docker engine CLI"
	"docker-compose|docker-compose|docker-compose|docker-compose|docker-compose|docker-compose|Docker Compose tool"
)

# LANGS ------------------------------------------------------------------------
CATEGORY_langs_minimal=(
	"python3|python3|python3|python|python3|python3|Python 3 interpreter"
	"pip3|python3-pip|python3-pip|python-pip|python3-pip|py3-pip|Python 3 package manager"
	"virtualenv|python3-venv|python3-virtualenv|python-virtualenv|python3-virtualenv|py3-virtualenv|Python virtual environments"
)

CATEGORY_langs_basic=(
	"${CATEGORY_langs_minimal[@]}"
	"node|nodejs|nodejs|nodejs|nodejs|nodejs|Node.js runtime (node command)"
	"npm|npm|npm|npm|npm|npm|Node.js package manager"
	"go|golang|golang|go|go|go|Go language toolchain"
)

CATEGORY_langs_full=(
	"${CATEGORY_langs_basic[@]}"
	"rustc|rustc|rust|rust|rust|rust|Rust compiler"
	"cargo|cargo|cargo|cargo|cargo|cargo|Rust package manager"
	"lld|lld|lld|lld|lld|lld|LLVM linker (useful for wasm toolchains)"
)

# WEB --------------------------------------------------------------------------
CATEGORY_web_minimal=(
	"nginx|nginx|nginx|nginx|nginx|nginx|Nginx web server"
	"curl|curl|curl|curl|curl|curl|HTTP client (for health checks, APIs)"
)

CATEGORY_web_basic=(
	"${CATEGORY_web_minimal[@]}"
	"php|php php-cli|php php-cli|php php-cli|php php-cli|php81 php81-cli|PHP runtime"
	"php-cli|php-cli|php-cli|php|php-cli|php81-cli|PHP CLI binary"
	"composer|composer|composer|composer|composer|composer|PHP dependency manager"
)

CATEGORY_web_full=(
	"${CATEGORY_web_basic[@]}"
	"php-curl|php-curl|php-curl|php-curl|php-curl|php81-curl|PHP cURL extension"
	"php-xml|php-xml|php-xml|php-xml|php-xml|php81-xml|PHP XML extension"
	"php-mbstring|php-mbstring|php-mbstring|php-mbstring|php-mbstring|php81-mbstring|PHP mbstring extension"
)

# DB ---------------------------------------------------------------------------
CATEGORY_db_minimal=(
	"psql|postgresql-client|postgresql|postgresql|postgresql-client|postgresql-client|PostgreSQL client"
	"mysql|mysql-client|mariadb|mariadb-clients|mariadb-client|mariadb-client|MySQL/MariaDB client"
	"sqlite3|sqlite3|sqlite|sqlite|sqlite3|sqlite|SQLite CLI"
)

CATEGORY_db_basic=(
	"${CATEGORY_db_minimal[@]}"
	"postgres|postgresql|postgresql-server|postgresql|postgresql-server|postgresql|PostgreSQL server"
)

CATEGORY_db_full=(
	"${CATEGORY_db_basic[@]}"
	"mysqld|mariadb-server|mariadb-server|mariadb|mariadb|mariadb|MariaDB/MySQL server"
)

# NETWORK ----------------------------------------------------------------------
CATEGORY_network_minimal=(
	"dig|dnsutils|bind-utils|bind-tools|bind-utils|bind-tools|DNS client tools (dig/host/nslookup)"
)

CATEGORY_network_basic=(
	"${CATEGORY_network_minimal[@]}"
	"traceroute|traceroute|traceroute|traceroute|traceroute|traceroute|Trace network route"
	"whois|whois|whois|whois|whois|whois|WHOIS client"
	"ifconfig|net-tools|net-tools|net-tools|net-tools|net-tools|Legacy net-tools (ifconfig, netstat, etc.)"
)

CATEGORY_network_full=(
	"${CATEGORY_network_basic[@]}"
	"nmap|nmap|nmap|nmap|nmap|nmap|Network scanner"
	"mtr|mtr-tiny|mtr|mtr|mtr|mtr|My traceroute (combined traceroute+ping)"
)

# MEDIA ------------------------------------------------------------------------
CATEGORY_media_minimal=(
	"ffmpeg|ffmpeg|ffmpeg|ffmpeg|ffmpeg|ffmpeg|Video/audio conversion & processing"
	"convert|imagemagick|ImageMagick|imagemagick|ImageMagick|imagemagick|ImageMagick (convert/identify)"
)

CATEGORY_media_basic=(
	"${CATEGORY_media_minimal[@]}"
	"sox|sox|sox|sox|sox|sox|Audio processing (SoX)"
	"mediainfo|mediainfo|mediainfo|mediainfo|mediainfo|mediainfo|Media file metadata viewer"
)

CATEGORY_media_full=(
	"${CATEGORY_media_basic[@]}"
	"tesseract|tesseract-ocr|tesseract|tesseract|tesseract|tesseract-ocr|OCR engine (Tesseract)"
	"exiftool|libimage-exiftool-perl|perl-Image-ExifTool|exiftool|exiftool|exiftool|Metadata reader/writer (ExifTool)"
	"gifsicle|gifsicle|gifsicle|gifsicle|gifsicle|gifsicle|GIF optimizer/editor"
)

# --- Install a category/tier --------------------------------------------------
install_category() {
	local category="$1"
	local tier="$2"
	local var_name="CATEGORY_${category}_${tier}"

	# nameref to array
	local -n ref="$var_name"

	log_info "Installing category '${category}' with tier '${tier}'..."

	if [ ${#ref[@]} -eq 0 ]; then
		log_warn "Category '$category' tier '$tier' is empty."
		return
	fi

	for entry in "${ref[@]}"; do
		install_entry "$entry" "$category/$tier"
	done

	log_ok "Finished category '${category}' (tier '${tier}')."
}

# --- Main ---------------------------------------------------------------------
detect_pkg_manager

# For Ubuntu + apt, try to ensure universe/multiverse are enabled
enable_ubuntu_universe_multiverse

for spec in "${REQUESTED[@]}"; do
	cat_name="${spec%%:*}"
	tier="${spec#*:}"

	case "$cat_name" in
		basics|dev|langs|web|db|network|media) ;;
		*)
			log_warn "Unknown category '$cat_name'; skipping."
			continue
			;;
	esac

	install_category "$cat_name" "$tier"
done

log_ok "All requested category checks complete."
echo "You now have a solid base of tools installed (where supported by your distro)."

touch "$HOME/.rt/profile/vars/touches/.install_server_tools.sh" 2>/dev/null || true