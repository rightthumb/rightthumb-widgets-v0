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
### 📦 INSTALL NTFY
### ─────────────────────────────────────────────

echo "🔧 Updating packages and installing prerequisites..."
sudo apt update -y
sudo apt install -y curl wget

echo "📥 Downloading ntfy package..."
ARCH=$(uname -m)
RELEASE_URL="https://github.com/binwiederhier/ntfy/releases/latest/download/ntfy_${ARCH}.deb"
wget -O ntfy.deb "$RELEASE_URL"

echo "📦 Installing ntfy..."
sudo dpkg -i ntfy.deb
rm ntfy.deb

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
ExecStart=/usr/bin/ntfy serve --config /etc/ntfy/server.yml
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
echo "👉 Test it: curl -d 'test' ${BASE_URL}/demo"
echo "👉 JSON view: ${BASE_URL}/demo.json"