#!/usr/bin/env bash
set -euo pipefail

# Universal Docker installer for many distros
# Includes: Debian/Ubuntu (and Mint/Pop!/Kali/Raspberry Pi OS),
# RHEL/CentOS/Alma/Rocky/Oracle, Fedora, Arch/Manjaro,
# openSUSE Leap/Tumbleweed, Amazon Linux 2 & 2023, Alpine.

echo "[INFO] Detecting distribution..."
if [[ -r /etc/os-release ]]; then
	. /etc/os-release
else
	echo "[ERROR] /etc/os-release not found; cannot detect distro."
	exit 1
fi

need_cmd() { command -v "$1" >/dev/null 2>&1 || { echo "[ERROR] Missing command: $1"; exit 1; }; }

install_docker_debian() {
	echo "[INFO] Installing Docker CE on Debian/Ubuntu family..."
	sudo apt-get update
	sudo apt-get install -y ca-certificates curl gnupg lsb-release

	sudo install -m 0755 -d /etc/apt/keyrings
	curl -fsSL "https://download.docker.com/linux/${ID}/gpg" | sudo gpg --dearmor -o /etc/apt/keyrings/docker.gpg
	sudo chmod a+r /etc/apt/keyrings/docker.gpg

	codename="$(lsb_release -cs)"
	arch="$(dpkg --print-architecture)"
	echo "deb [arch=${arch} signed-by=/etc/apt/keyrings/docker.gpg] https://download.docker.com/linux/${ID} ${codename} stable" \
	| sudo tee /etc/apt/sources.list.d/docker.list >/dev/null

	sudo apt-get update
	sudo apt-get install -y docker-ce docker-ce-cli containerd.io docker-buildx-plugin docker-compose-plugin

	sudo systemctl enable --now docker
}

install_docker_rhel_like() {
	# RHEL / CentOS / Alma / Rocky / Oracle (ol)
	local base="${1}" # "centos" repo works for rhel-like
	echo "[INFO] Installing Docker CE on RHEL-like (${ID})..."
	sudo yum remove -y docker docker-client docker-client-latest docker-common docker-latest docker-latest-logrotate docker-logrotate docker-engine || true

	sudo yum install -y yum-utils
	sudo yum-config-manager --add-repo "https://download.docker.com/linux/${base}/docker-ce.repo"

	sudo yum install -y docker-ce docker-ce-cli containerd.io docker-buildx-plugin docker-compose-plugin
	sudo systemctl enable --now docker
}

install_docker_fedora() {
	echo "[INFO] Installing Docker CE on Fedora..."
	sudo dnf remove -y docker docker-client docker-client-latest docker-common docker-latest docker-latest-logrotate docker-logrotate docker-engine || true

	sudo dnf -y install dnf-plugins-core
	sudo dnf config-manager --add-repo https://download.docker.com/linux/fedora/docker-ce.repo

	sudo dnf install -y docker-ce docker-ce-cli containerd.io docker-buildx-plugin docker-compose-plugin
	sudo systemctl enable --now docker
}

install_docker_arch() {
	echo "[INFO] Installing Docker on Arch/Manjaro..."
	sudo pacman -Sy --noconfirm docker docker-compose
	sudo systemctl enable --now docker
}

install_docker_opensuse() {
	# openSUSE Leap/Tumbleweed—use distro packages (moby engine); compose v2 plugin may be named docker-compose or docker-compose-plugin depending on repo
	echo "[INFO] Installing Docker on openSUSE (Leap/Tumbleweed)..."
	sudo zypper refresh
	# Prefer docker + docker-compose if available; fall back to plugin naming
	if sudo zypper -n install --no-recommends docker docker-compose; then
		:
	else
		sudo zypper -n install --no-recommends docker docker-compose-plugin || sudo zypper -n install --no-recommends docker
	fi
	sudo systemctl enable --now docker
}

install_docker_amazon_linux_2() {
	echo "[INFO] Installing Docker on Amazon Linux 2..."
	# AL2 uses amazon-linux-extras to provide docker (moby engine). Compose v2 can be installed as a plugin package if available.
	sudo yum install -y amazon-linux-extras
	sudo amazon-linux-extras enable docker
	sudo yum clean metadata
	sudo yum install -y docker
	# Compose v2 plugin (if available via repositories)
	sudo yum install -y docker-compose-plugin || true
	sudo systemctl enable --now docker
}

install_docker_amazon_linux_2023() {
	echo "[INFO] Installing Docker (moby) on Amazon Linux 2023..."
	# AL2023 typically ships moby packages via dnf (Docker-compatible)
	sudo dnf -y install moby-engine moby-cli containerd
	# Compose v2 plugin may be available as docker-compose-plugin; otherwise install docker-compose (python) if present
	sudo dnf -y install docker-compose-plugin || sudo dnf -y install docker-compose || true
	sudo systemctl enable --now docker || sudo systemctl enable --now moby || true
}

install_docker_alpine() {
	echo "[INFO] Installing Docker on Alpine..."
	need_cmd apk
	sudo apk update
	# docker-cli-compose provides the Compose v2 plugin integration
	sudo apk add --no-cache docker docker-cli-compose containerd
	sudo rc-update add docker boot
	sudo service docker start
}

# Normalize derivatives into their families
case "${ID_LIKE:-$ID}" in
	*debian*|*ubuntu*)
		case "$ID" in
			ubuntu|debian|linuxmint|pop|kali|raspbian)
				install_docker_debian
				;;
			*)
				# Unknown Debian-like—try as Debian
				ID=debian
				install_docker_debian
				;;
		esac
		;;
	*rhel*|*centos*|*fedora*)
		case "$ID" in
			centos|rhel|almalinux|rocky|ol)  install_docker_rhel_like centos ;;
			fedora)                           install_docker_fedora ;;
			amzn)
				# Distinguish AL2 vs AL2023
				if [[ "${VERSION_ID%%.*}" -ge 2023 || "${VERSION_ID}" == "2023" ]]; then
					install_docker_amazon_linux_2023
				else
					install_docker_amazon_linux_2
				fi
				;;
			*)
				# Fallback: treat as RHEL-like via centos repo
				install_docker_rhel_like centos
				;;
		esac
		;;
	*suse*)
		case "$ID" in
			opensuse*|sles)
				install_docker_opensuse
				;;
			*)
				install_docker_opensuse
				;;
		esac
		;;
	*)
		case "$ID" in
			arch|manjaro) install_docker_arch ;;
			alpine)       install_docker_alpine ;;
			opensuse*|sles) install_docker_opensuse ;;
			amzn)
				if [[ "${VERSION_ID%%.*}" -ge 2023 || "${VERSION_ID}" == "2023" ]]; then
					install_docker_amazon_linux_2023
				else
					install_docker_amazon_linux_2
				fi
				;;
			*)
				echo "[ERROR] Unsupported or unrecognized distribution: ID='$ID' (ID_LIKE='${ID_LIKE:-}')"
				echo "        You can run this on a supported distro or install manually: https://docs.docker.com/engine/install/"
				exit 1
				;;
		esac
		;;
esac

echo "[INFO] Docker installation complete. Testing..."
if sudo docker run --rm hello-world; then
	echo "[INFO] ✅ Docker works!"
else
	echo "[WARN] Docker test failed. Check 'systemctl status docker' (or 'service docker status' on Alpine) and logs."
fi

# Optional: add current user to docker group so 'sudo' isn't required (effective after re-login)
if getent group docker >/dev/null 2>&1; then
	if [[ -n "${SUDO_USER:-}" ]]; then
		sudo usermod -aG docker "$SUDO_USER" || true
		echo "[INFO] Added $SUDO_USER to 'docker' group (log out/in to take effect)."
	fi
fi