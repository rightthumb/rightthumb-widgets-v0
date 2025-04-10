#!/bin/bash
set -e

# ------------------ YUM ------------------
if which yum &>/dev/null; then
	echo "📦 Detected: yum"
	sudo yum clean all -y
	sudo yum makecache
	sudo yum update -y
	sudo yum upgrade -y

	sudo yum install -y epel-release || true

	sudo yum localinstall -y \
		https://download1.rpmfusion.org/free/el/rpmfusion-free-release-7.noarch.rpm \
		https://download1.rpmfusion.org/nonfree/el/rpmfusion-nonfree-release-7.noarch.rpm

	sudo rpm --import http://li.nux.ro/download/nux/RPM-GPG-KEY-nux.ro
	sudo yum install -y https://li.nux.ro/download/nux/dextop/el7/x86_64/nux-dextop-release-0-5.el7.nux.noarch.rpm || true

	curl -fsSL https://rpm.nodesource.com/setup_18.x | sudo bash -
	sudo yum install -y nodejs

	sudo yum makecache
	sudo yum upgrade -y
fi

# ------------------ DNF ------------------
if which dnf &>/dev/null; then
	echo "📦 Detected: dnf"
	RHEL_VERSION=$(rpm -E %rhel)

	sudo dnf clean all -y
	sudo dnf makecache
	sudo dnf update -y
	sudo dnf upgrade -y

	sudo dnf install -y epel-release || true

	sudo dnf install -y \
		https://download1.rpmfusion.org/free/el/rpmfusion-free-release-${RHEL_VERSION}.noarch.rpm \
		https://download1.rpmfusion.org/nonfree/el/rpmfusion-nonfree-release-${RHEL_VERSION}.noarch.rpm

	curl -fsSL https://rpm.nodesource.com/setup_18.x | sudo bash -
	sudo dnf install -y nodejs

	sudo dnf makecache
	sudo dnf upgrade -y
fi

# ------------------ APT ------------------
if which apt &>/dev/null; then
	echo "📦 Detected: apt"
	sudo apt update
	sudo apt upgrade -y

	sudo apt install -y software-properties-common curl gnupg lsb-release ca-certificates

	curl -fsSL https://deb.nodesource.com/setup_18.x | sudo -E bash -
	sudo apt update
	sudo apt upgrade -y
	sudo apt install -y nodejs
fi

# ------------------ PACMAN ------------------
if which pacman &>/dev/null; then
	echo "📦 Detected: pacman"
	sudo pacman -Syu --noconfirm
	sudo pacman -S --noconfirm base-devel git curl nodejs npm neofetch
fi

echo "✅ All available repos added and system fully updated."