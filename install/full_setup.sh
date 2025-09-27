#!/bin/bash

REQUIRE_URL="https://rightthumb.com/python_require.txt"
REQUIRE_FILE="/opt/rightthumb-widgets-v0/install/full_require.txt"

# Create directory if it doesn't exist
mkdir -p "$(dirname "$REQUIRE_FILE")"

# Check if file exists
if [ -f "$REQUIRE_FILE" ]; then
    read -p "$REQUIRE_FILE already exists. Download again? [y/N]: " confirm
    case "$confirm" in
        [yY][eE][sS]|[yY])
            curl -fsSL "$REQUIRE_URL" -o "$REQUIRE_FILE" || { echo "Download failed"; exit 1; }
            ;;
        *)
            echo "Using existing file."
            ;;
    esac
else
    curl -fsSL "$REQUIRE_URL" -o "$REQUIRE_FILE" || { echo "Download failed"; exit 1; }
fi

# Read and install packages
while read -r package; do
    if [[ -n "$package" && ! "$package" =~ ^# ]]; then
        pip3 install --upgrade --no-cache-dir --break-system-packages "$package" || true
        echo ''
    fi
done < "$REQUIRE_FILE"
