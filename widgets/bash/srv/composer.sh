#!/usr/bin/env bash
#
# install-composer-multi.sh
#
# Multi-distro Composer installer.
# - Detects package manager
# - Installs PHP CLI if needed
# - Chooses a CLI PHP binary
# - Installs composer.phar
# - Creates /usr/local/bin/composer wrapper using the CLI SAPI
#
# Usage:
#   bash install-composer-multi.sh
#   COMPOSER_VERSION=2.9.2 bash install-composer-multi.sh
#

set -euo pipefail

COMPOSER_VERSION="${COMPOSER_VERSION:-latest}"
INSTALL_DIR="${INSTALL_DIR:-/usr/local/bin}"
COMPOSER_BIN_NAME="${COMPOSER_BIN_NAME:-composer}"

# ----------------------------------------------------------
# Helper: log
# ----------------------------------------------------------
log() {
    printf '[INFO] %s\n' "$*" >&2
}

warn() {
    printf '[WARN] %s\n' "$*" >&2
}

err() {
    printf '[ERROR] %s\n' "$*" >&2
    exit 1
}

# ----------------------------------------------------------
# Detect package manager
# ----------------------------------------------------------
detect_pm() {
    if command -v apt-get >/dev/null 2>&1; then
        echo "apt"
    elif command -v dnf >/dev/null 2>&1; then
        echo "dnf"
    elif command -v yum >/dev/null 2>&1; then
        echo "yum"
    elif command -v pacman >/dev/null 2>&1; then
        echo "pacman"
    elif command -v zypper >/dev/null 2>&1; then
        echo "zypper"
    elif command -v apk >/dev/null 2>&1; then
        echo "apk"
    else
        echo ""
    fi
}

PM="$(detect_pm)"
if [ -z "$PM" ]; then
    err "Could not detect supported package manager (apt/dnf/yum/pacman/zypper/apk)."
fi

log "Detected package manager: $PM"

# ----------------------------------------------------------
# Ensure PHP CLI is installed
# ----------------------------------------------------------
ensure_php_cli() {
    log "Ensuring PHP CLI is installed..."

    case "$PM" in
        apt)
            sudo apt-get update -y
            sudo apt-get install -y php-cli php-common php-json php-mbstring
            ;;
        dnf)
            # EL8/EL9 style (Alma/Rocky/CentOS Stream)
            sudo dnf install -y php-cli php-common php-json php-mbstring
            ;;
        yum)
            sudo yum install -y php-cli php-common php-json php-mbstring
            ;;
        pacman)
            sudo pacman -Sy --noconfirm php
            ;;
        zypper)
            sudo zypper install -y php-cli php-common php-mbstring
            ;;
        apk)
            # Alpine – adjust version here if needed
            sudo apk add --no-cache php81-cli php81-phar php81-mbstring
            ;;
        *)
            err "Unsupported package manager for PHP install: $PM"
            ;;
    esac
}

# ----------------------------------------------------------
# Choose a CLI PHP binary
# ----------------------------------------------------------
choose_php_bin() {
    # Order matters – try "php" first, then versioned binaries.
    local candidates=(
        php
        php8.3 php8.2 php8.1 php8.0 php7.4
        php81 php82 php83
    )

    for bin in "${candidates[@]}"; do
        if command -v "$bin" >/dev/null 2>&1; then
            # Check SAPI
            local sapi
            sapi="$("$bin" -r 'echo php_sapi_name();' 2>/dev/null || true)"
            if [ "$sapi" = "cli" ]; then
                echo "$bin"
                return 0
            else
                warn "Found PHP binary '$bin' but SAPI is '$sapi', not 'cli'. Skipping."
            fi
        fi
    done

    return 1
}

# ----------------------------------------------------------
# Main
# ----------------------------------------------------------

# 1) Ensure PHP CLI is available
PHP_BIN=""

if ! PHP_BIN="$(choose_php_bin)"; then
    log "No suitable PHP CLI binary found; attempting to install PHP CLI..."
    ensure_php_cli

    # Try again
    if ! PHP_BIN="$(choose_php_bin)"; then
        err "Unable to find a PHP CLI binary even after installation. Aborting."
    fi
fi

log "Using PHP binary: $PHP_BIN"

# 2) Check for existing composer installation
if [ -e "$INSTALL_DIR/$COMPOSER_BIN_NAME" ] || [ -e "$INSTALL_DIR/composer.phar" ]; then
    err "Composer already appears to be installed in $INSTALL_DIR. Aborting to avoid overwriting."
fi

# 3) Download composer installer
TMP_DIR="$(mktemp -d)"
trap 'rm -rf "$TMP_DIR"' EXIT

log "Downloading Composer installer..."
curl -sS https://getcomposer.org/installer -o "$TMP_DIR/composer-setup.php"

# Optionally pin a version
if [ "$COMPOSER_VERSION" != "latest" ]; then
    log "Installing Composer version: $COMPOSER_VERSION"
    "$PHP_BIN" "$TMP_DIR/composer-setup.php" --version="$COMPOSER_VERSION" --install-dir="$TMP_DIR" --filename=composer.phar
else
    log "Installing latest Composer version..."
    "$PHP_BIN" "$TMP_DIR/composer-setup.php" --install-dir="$TMP_DIR" --filename=composer.phar
fi

# 4) Move composer.phar into place
log "Moving composer.phar to $INSTALL_DIR..."
sudo mkdir -p "$INSTALL_DIR"
sudo cp "$TMP_DIR/composer.phar" "$INSTALL_DIR/composer.phar"
sudo chmod 755 "$INSTALL_DIR/composer.phar"

# 5) Create wrapper script that always uses the CLI PHP binary
WRAPPER="$INSTALL_DIR/$COMPOSER_BIN_NAME"

log "Creating wrapper script at $WRAPPER..."

sudo bash -c "cat > '$WRAPPER'" <<EOF
#!/usr/bin/env bash
# Wrapper for Composer to always use the CLI PHP binary.
exec "$PHP_BIN" "$INSTALL_DIR/composer.phar" "\$@"
EOF

sudo chmod 755 "$WRAPPER"

log "Composer installed successfully as '$WRAPPER'."

log "Version check:"
"$WRAPPER" --version
