#!/bin/bash

set -e

### ─────────────────────────────────────────────
### 🧠 HELP + ARG PARSING
### ─────────────────────────────────────────────

print_help() {
    echo "Usage:"
    echo "  $0 --domain your.domain.com"
    echo "  $0 --ip 123.123.123.123"
    echo "  $0 --domain auto         # uses hostname"
    echo "  $0 --ip auto             # uses first public IP"
    echo
    exit 1
}

BASE_URL=""
while [[ $# -gt 0 ]]; do
    case $1 in
        --domain)
            DOMAIN=$2
            [ "$DOMAIN" == "auto" ] && BASE_URL="http://$(hostname)"
            [ "$DOMAIN" != "auto" ] && BASE_URL="http://$DOMAIN"
            shift 2
            ;;
        --ip)
            IP=$2
            [ "$IP" == "auto" ] && BASE_URL="http://$(hostname -I | awk '{print $1}')"
            [ "$IP" != "auto" ] && BASE_URL="http://$IP"
            shift 2
            ;;
        *)
            print_help
            ;;
    esac
done

if [[ -z "$BASE_URL" ]]; then
    print_help
fi

echo "📡 Configuring ntfy to use base URL: $BASE_URL"

### ─────────────────────────────────────────────
### ✅ SKIP IF ALREADY INSTALLED
### ─────────────────────────────────────────────

if command -v ntfy &>/dev/null; then
    echo "✅ ntfy is already installed at: $(command -v ntfy)"
    echo "👉 Skipping build. To rebuild, uninstall first."
else

### ─────────────────────────────────────────────
### 📦 INSTALL PREREQUISITES + BUILD NTFY
### ─────────────────────────────────────────────

    echo "🔧 Installing prerequisites..."
    sudo apt update -y
    sudo apt install -y git make wget curl

    echo "🧱 Installing modern Node.js (v18) and npm if missing..."
    if ! command -v npm &>/dev/null || ! command -v node &>/dev/null; then
        curl -fsSL https://deb.nodesource.com/setup_18.x | sudo -E bash -
        sudo apt install -y nodejs
    fi

    echo "🛠️ Ensuring Go 1.21.6 is installed..."
    GO_VERSION=1.21.6
    GO_BIN=/usr/local/go/bin/go
    if ! $GO_BIN version 2>/dev/null | grep -q "go$GO_VERSION"; then
        cd /tmp
        wget -q https://go.dev/dl/go${GO_VERSION}.linux-amd64.tar.gz
        sudo rm -rf /usr/local/go
        sudo tar -C /usr/local -xzf go${GO_VERSION}.linux-amd64.tar.gz
        rm go${GO_VERSION}.linux-amd64.tar.gz
    fi
    export PATH=/usr/local/go/bin:$PATH

    echo "📥 Cloning ntfy source..."
    cd /tmp
    rm -rf ntfy
    git clone https://github.com/binwiederhier/ntfy.git
    cd ntfy

    echo "🔨 Building ntfy backend only..."
    make cli-linux-server

    echo "📦 Installing ntfy binary to /usr/local/bin/..."
    sudo mv dist/ntfy_linux_server/ntfy /usr/local/bin/

    echo "✅ Installed: $(ntfy version)"
fi

### ─────────────────────────────────────────────
### 🛠️ CONFIGURE + ENABLE SYSTEMD
### ─────────────────────────────────────────────

echo "👤 Creating 'ntfy' system user (if needed)..."
sudo useradd -r -s /bin/false ntfy || true

echo "📁 Creating data + config directories..."
sudo mkdir -p /var/cache/ntfy
sudo mkdir -p /etc/ntfy
sudo chown -R ntfy:ntfy /var/cache/ntfy /etc/ntfy

echo "📝 Writing ntfy config..."
sudo tee /etc/ntfy/server.yml > /dev/null <<EOF
listen-http: :80
base-url: ${BASE_URL}
cache-file: /var/cache/ntfy/cache.db
EOF

echo "🛠️ Writing ntfy systemd service..."
sudo tee /etc/systemd/system/ntfy.service > /dev/null <<EOF
[Unit]
Description=ntfy push notification service
After=network.target

[Service]
ExecStart=/usr/local/bin/ntfy serve --config /etc/ntfy/server.yml
Restart=on-failure
User=ntfy
Group=ntfy

[Install]
WantedBy=multi-user.target
EOF

echo "🚀 Enabling and starting ntfy..."
sudo systemctl daemon-reload
sudo systemctl enable ntfy
sudo systemctl restart ntfy

### ─────────────────────────────────────────────
### ✅ DONE
### ─────────────────────────────────────────────

echo
echo "✅ ntfy is installed and running!"
echo "👉 Test: curl -d 'test' ${BASE_URL}/demo"
echo "👉 JSON view: ${BASE_URL}/demo.json"
