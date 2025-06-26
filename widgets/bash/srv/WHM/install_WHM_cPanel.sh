#!/bin/bash

set -euo pipefail

# Colors
GREEN='\033[0;32m'
CYAN='\033[1;36m'
YELLOW='\033[1;33m'
NC='\033[0m' # No Color

echo -e "${CYAN}🚀 Starting base system setup and SSL prep...${NC}"

echo -e "${YELLOW}📦 Installing updates and popular repos...${NC}"
# sudo ./Add_Repos__apt_dnf_yum_pacman.sh

echo -e "${YELLOW}🔍 Detecting package manager and installing dependencies (perl, curl, certbot)...${NC}"

if command -v yum &>/dev/null; then
	sudo yum install -y perl curl certbot || sudo yum install -y --skip-broken perl curl
elif command -v dnf &>/dev/null; then
	sudo dnf install -y perl curl certbot || sudo dnf install -y --allowerasing perl curl
elif command -v apt &>/dev/null; then
	sudo apt update
	sudo apt install -y --fix-broken perl curl certbot || sudo apt install -y perl curl certbot --allow-unauthenticated
elif command -v pacman &>/dev/null; then
	sudo pacman -Sy --noconfirm perl curl certbot || sudo pacman -Sy --needed perl curl
elif command -v zypper &>/dev/null; then
	sudo zypper --non-interactive install perl curl certbot || sudo zypper install -f perl curl
elif command -v apk &>/dev/null; then
	sudo apk add --no-cache perl curl certbot || sudo apk fix
elif command -v xbps-install &>/dev/null; then
	sudo xbps-install -Sy perl curl certbot || sudo xbps-install -Sf perl curl
elif command -v eopkg &>/dev/null; then
	sudo eopkg install -y perl curl certbot || sudo eopkg install --reinstall perl curl
elif command -v nix-env &>/dev/null; then
	nix-env -iA nixpkgs.perl nixpkgs.curl || true
else
	echo -e "${RED}❌ Unsupported or unknown package manager. Please install curl and perl manually.${NC}"
	exit 1
fi

HOSTNAME=$(cat /etc/hostname)
LOGFILE="/var/log/preinstall_certbot_$(date +%F_%H-%M-%S).log"

echo -e "${CYAN}🔐 Issuing Let's Encrypt SSL certificate for: ${GREEN}$HOSTNAME${NC}"
echo -e "📄 Logging output to: ${YELLOW}$LOGFILE${NC}"
echo "--------------------------------------------"

certbot certonly --standalone \
	--non-interactive \
	--agree-tos \
	--register-unsafely-without-email \
	--preferred-challenges http \
	-d "$HOSTNAME" \
	2>&1 | tee "$LOGFILE"

echo "--------------------------------------------"
echo -e "${GREEN}✅ Certbot completed successfully.${NC}"
echo -e "📁 Certificate directory: ${YELLOW}/etc/letsencrypt/live/$HOSTNAME/${NC}"
echo -e "🧾 Certbot log: ${YELLOW}$LOGFILE${NC}"

echo -e "${CYAN}⬇️ Downloading and running cPanel installer...${NC}"
cd /home
curl -o latest -L https://securedownloads.cpanel.net/latest
chmod +x latest
sudo ./latest --skip-license --force

echo ""
echo -e "${CYAN}ℹ️  Certbot Results Summary${NC}"
echo "────────────────────────────────────────────"
if [[ -f "$LOGFILE" ]]; then
	cat "$LOGFILE"
else
	echo -e "${YELLOW}⚠️  No certbot log file found in /var/log/preinstall_certbot_*.log${NC}"
fi
echo "────────────────────────────────────────────"

echo -e "${GREEN}✅ Initial server setup complete! WHM/cPanel installation started.${NC}"