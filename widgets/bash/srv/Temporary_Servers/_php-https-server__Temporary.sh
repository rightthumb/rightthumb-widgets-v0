#!/bin/bash

DOMAIN="$1"
HTTPS_PORT="${2:-443}"  # Optional second argument, defaults to 443
CERT_PATH="/etc/letsencrypt/live/$DOMAIN"
HTTP_PORT=$((8000 + RANDOM % 1000))

show_help() {
    echo "🛠️  Temporary HTTPS PHP Server"
    echo ""
    echo "Usage: $0 <domain> [https-port]"
    echo ""
    echo "This script:"
    echo "  - Installs PHP and Certbot if missing"
    echo "  - Requests a Let's Encrypt certificate if needed"
    echo "  - Starts a local PHP server"
    echo "  - Wraps it in OpenSSL to serve over HTTPS"
    echo ""
    echo "🔐 The domain must point to this server and ports 80 and [https-port] must be open."
    echo "ℹ️  Example: sudo ./php-https-server.sh example.com 8443"
    exit 1
}

install_if_missing() {
    PKG="$1"
    if ! command -v "$PKG" >/dev/null 2>&1; then
        echo "📦 Installing $PKG..."
        sudo apt update && sudo apt install -y "$PKG"
    fi
}

# Validate arguments
if [[ -z "$DOMAIN" ]]; then
    show_help
fi

# 1. Install required tools
install_if_missing php
install_if_missing openssl

# Install certbot (snap preferred)
if ! command -v certbot >/dev/null 2>&1; then
    echo "📦 Installing certbot..."
    if command -v snap >/dev/null 2>&1; then
        sudo snap install core; sudo snap refresh core
        sudo snap install --classic certbot
        sudo ln -s /snap/bin/certbot /usr/bin/certbot
    else
        sudo apt update && sudo apt install -y certbot
    fi
fi

# 2. Generate cert if missing
if [[ ! -f "$CERT_PATH/fullchain.pem" || ! -f "$CERT_PATH/privkey.pem" ]]; then
    echo "🔐 No certificate found for $DOMAIN. Attempting to generate one..."
    sudo certbot certonly --standalone -d "$DOMAIN" --non-interactive --agree-tos -m "admin@$DOMAIN" || {
        echo "❌ Failed to generate certificate. Ensure your domain points to this VPS and ports 80 and $HTTPS_PORT are open."
        exit 1
    }
fi

echo "✅ Certificate ready at $CERT_PATH"

# 3. Start PHP dev server
echo "🚀 Starting PHP server on 127.0.0.1:$HTTP_PORT..."
php -S 127.0.0.1:$HTTP_PORT > /tmp/php_https_server.log 2>&1 &
PHP_PID=$!

# Clean up PHP server on exit
trap "kill $PHP_PID 2>/dev/null; echo -e '\n🛑 Servers stopped.'; exit" INT TERM

# 4. Serve over HTTPS using OpenSSL
echo "🌐 Serving https://$DOMAIN:$HTTPS_PORT/ from $(pwd)"
openssl s_server \
    -quiet \
    -accept "$HTTPS_PORT" \
    -key "$CERT_PATH/privkey.pem" \
    -cert "$CERT_PATH/fullchain.pem" \
    -proxy 127.0.0.1:$HTTP_PORT

# Cleanup
kill $PHP_PID 2>/dev/null
