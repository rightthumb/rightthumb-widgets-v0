#!/usr/bin/env bash
set -e

# ==============================
# CONFIG
# ==============================
IMAGE="kylemanna/openvpn"
CONTAINER="openvpn-server"
CONFIG_DIR="/opt/openvpn-data"
OVPN_PORT="1194"
PROTO="udp"

# If you want to force hostname/IP:
#   OVPN_HOST=myvpn.example.com ./openvpn-docker-manager.sh install
OVPN_HOST="${OVPN_HOST:-}"

# ==============================
# HELP
# ==============================
usage() {
	cat <<EOF
Usage:
  $0 install
	Install Docker (if needed), set up OpenVPN server in Docker, and start it.

  OVPN_HOST=myvpn.example.com $0 install
	Same as above, but explicitly set the VPN hostname.

  $0 add-client <name>
	Create a NEW client profile with a PASSWORD-PROTECTED key.
	You will be prompted for a password during key creation.
	Output: <name>.ovpn in current directory.

Examples:
  $0 install
  $0 install
  $0 install
  OVPN_HOST=vpn.mydomain.com $0 install
  $0 add-client NAME
  $0 add-client laptop
  $0 add-client phone
EOF
	exit 1
}

ACTION="$1"
[ -z "$ACTION" ] && usage

# ==============================
# DETECT PACKAGE MANAGER
# ==============================
detect_pkg_mgr() {
	if command -v apt-get >/dev/null 2>&1; then
		PKG="apt-get"
	elif command -v dnf >/dev/null 2>&1; then
		PKG="dnf"
	elif command -v yum >/dev/null 2>&1; then
		PKG="yum"
	elif command -v pacman >/dev/null 2>&1; then
		PKG="pacman"
	else
		echo "[ERROR] Unsupported Linux distro."
		exit 1
	fi
}

# ==============================
# INSTALL DOCKER IF NEEDED
# ==============================
ensure_docker() {
	if command -v docker >/dev/null 2>&1; then
		echo "[OK] Docker already installed."
		return
	fi

	echo "[INFO] Docker not found. Installing..."
	detect_pkg_mgr

	case "$PKG" in
		apt-get)
			sudo apt-get update
			sudo apt-get install -y ca-certificates curl gnupg lsb-release

			if [ ! -f /etc/apt/keyrings/docker.gpg ]; then
				sudo install -m 0755 -d /etc/apt/keyrings
				curl -fsSL https://download.docker.com/linux/ubuntu/gpg \
				| sudo gpg --dearmor -o /etc/apt/keyrings/docker.gpg
			fi

			if [ ! -f /etc/apt/sources.list.d/docker.list ]; then
				echo \
				"deb [arch=$(dpkg --print-architecture) signed-by=/etc/apt/keyrings/docker.gpg] \
				https://download.docker.com/linux/ubuntu $(lsb_release -cs) stable" \
				| sudo tee /etc/apt/sources.list.d/docker.list >/dev/null
			fi

			sudo apt-get update
			sudo apt-get install -y docker-ce docker-ce-cli containerd.io
			;;
		dnf)
			sudo dnf -y install dnf-plugins-core
			sudo dnf config-manager --add-repo https://download.docker.com/linux/centos/docker-ce.repo || true
			sudo dnf -y install docker-ce docker-ce-cli containerd.io
			;;
		yum)
			sudo yum install -y yum-utils
			sudo yum-config-manager --add-repo https://download.docker.com/linux/centos/docker-ce.repo || true
			sudo yum install -y docker-ce docker-ce-cli containerd.io
			;;
		pacman)
			sudo pacman -Sy --needed --noconfirm docker
			;;
	esac

	echo "[INFO] Enabling Docker..."
	sudo systemctl enable --now docker
}

# ==============================
# DETECT / SET OVPN_HOST
# ==============================
ensure_ovpn_host() {
	if [ -n "$OVPN_HOST" ]; then
		echo "[INFO] Using OVPN_HOST=$OVPN_HOST"
		return
	fi

	if command -v curl >/dev/null 2>&1; then
		echo "[INFO] Detecting public IP for OVPN_HOST..."
		OVPN_HOST="$(curl -s https://ipv4.icanhazip.com || true)"
		OVPN_HOST="${OVPN_HOST%%[[:space:]]*}"
	fi

	if [ -z "$OVPN_HOST" ]; then
		echo "[ERROR] Could not detect public IP."
		echo "        Re-run with:  OVPN_HOST=myvpn.example.com $0 install"
		exit 1
	fi

	echo "[INFO] Using OVPN_HOST=$OVPN_HOST"
}

# ==============================
# INSTALL / INIT SERVER
# ==============================
do_install() {
	ensure_docker
	ensure_ovpn_host

	sudo mkdir -p "$CONFIG_DIR"
	sudo chmod 700 "$CONFIG_DIR"

	echo "[INFO] Pulling OpenVPN image: $IMAGE"
	sudo docker pull "$IMAGE"

	# Initialize PKI & server config if not already done
	if [ ! -d "$CONFIG_DIR/pki" ]; then
		echo "[INFO] Initializing OpenVPN config in $CONFIG_DIR"

		# Generate server config
		sudo docker run --rm \
		-v "$CONFIG_DIR":/etc/openvpn \
		"$IMAGE" \
		ovpn_genconfig -u "${PROTO}://${OVPN_HOST}:${OVPN_PORT}"

		# Initialize PKI (INTERACTIVE for CA details, no passphrase on server key)
		sudo docker run --rm -it \
		-e EASYRSA_BATCH=1 \
		-v "$CONFIG_DIR":/etc/openvpn \
		"$IMAGE" \
		ovpn_initpki nopass
	else
		echo "[OK] Existing OpenVPN config found at $CONFIG_DIR (skipping init)."
	fi

	# Stop existing container if any
	if sudo docker ps -a --format '{{.Names}}' | grep -q "^$CONTAINER$"; then
		echo "[INFO] Stopping old OpenVPN container..."
		sudo docker stop "$CONTAINER" || true
		sudo docker rm "$CONTAINER" || true
	fi

	# Start server container
	echo "[INFO] Starting OpenVPN server container: $CONTAINER"
	sudo docker run -d \
	--name "$CONTAINER" \
	--cap-add=NET_ADMIN \
	--device /dev/net/tun \
	-v "$CONFIG_DIR":/etc/openvpn \
	-p "${OVPN_PORT}:${OVPN_PORT}/${PROTO}" \
	--restart unless-stopped \
	"$IMAGE"

	cat <<EOF
======================================================
[DONE] OpenVPN server container is running: $CONTAINER
Config directory: $CONFIG_DIR
Host: $OVPN_HOST
Port: ${OVPN_PORT}/${PROTO}

Next step: create clients using:
  $0 add-client <name>

OPTIONAL: Enable IP forwarding and NAT on the host:
  sudo sysctl -w net.ipv4.ip_forward=1
  # Then add iptables/ufw rules to NAT traffic via tun0 as needed.
======================================================
EOF
}

# ==============================
# ADD CLIENT (PASSWORD-PROTECTED)
# ==============================
do_add_client() {
	CLIENT_NAME="$1"
	if [ -z "$CLIENT_NAME" ]; then
		echo "[ERROR] Missing client name."
		echo "Usage: $0 add-client <name>"
		exit 1
	fi

	if [ ! -d "$CONFIG_DIR/pki" ]; then
		echo "[ERROR] PKI not initialized. Run '$0 install' first."
		exit 1
	fi

	echo "[INFO] Creating client '$CLIENT_NAME' with PASSWORD-PROTECTED key."
	echo "[INFO] You will be prompted for the key password."

	# IMPORTANT: no 'nopass' here -> client key will require password
	sudo docker run --rm -it \
	-e EASYRSA_BATCH=0 \
	-v "$CONFIG_DIR":/etc/openvpn \
	"$IMAGE" \
	easyrsa build-client-full "$CLIENT_NAME"

	OUT_FILE="${CLIENT_NAME}.ovpn"
	echo "[INFO] Exporting client profile to: $OUT_FILE"

	sudo docker run --rm \
	-v "$CONFIG_DIR":/etc/openvpn \
	"$IMAGE" \
	ovpn_getclient "$CLIENT_NAME" > "$OUT_FILE"

	sudo chown "$(id -u):$(id -g)" "$OUT_FILE"

	cat <<EOF
======================================================
[DONE] Client created: $CLIENT_NAME
Profile file: $(pwd)/$OUT_FILE

This client certificate uses an ENCRYPTED private key.
The user MUST enter the password each time they connect.

Import ${OUT_FILE} into your OpenVPN client on laptop/phone.
======================================================
EOF
}

# ==============================
# MAIN DISPATCH
# ==============================
case "$ACTION" in
	install)
		shift
		do_install "$@"
		;;
	add-client)
		shift
		do_add_client "$@"
		;;
	*)
		usage
		;;
esac