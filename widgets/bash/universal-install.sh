#!/usr/bin/env bash

set -e

show_help() {
cat << "EOF"
┌──────────────────────────────────────────────────────────────┐
│ ⚙️  Universal Dev Installer — Full Stack Autopilot Mode 🛠️    │
├──────────────────────────────────────────────────────────────┤
│ Usage: ./install.sh <name|github-url|pkg/path> [option]      │
│                                                              │
│ Positional:                                                  │
│   name         → Package name (e.g. cowsay, express)         │
│   github-url   → GitHub repo (e.g. github.com/user/repo)     │
│   /            → Composer-style or Git                        │
│                                                              │
│ Optional flags (prioritized):                                │
│   -git         → Clone using Git                             │
│   -c, --composer → Use Composer                              │
│   -bower       → Use Bower                                   │
│   -node        → Use npm/yarn                                │
│   -pip         → Use pip3 (with system bypass flags)         │
│   -gem         → Use Ruby gem                                │
│   -go          → Use Go module install                       │
│   -cargo       → Use Rust's cargo                            │
│   -all         → Try everything in order                     │
│   -h, --help   → Show this menu                              │
└──────────────────────────────────────────────────────────────┘
EOF
exit 0
}

# Show help if no args
if [ -z "$1" ]; then
    show_help
fi

PKG="$1"
OPTION="$2"
install_attempted=()

# Lowercase option just in case
OPTION="${OPTION,,}"

try_install() {
    local cmd="$1"
    echo "⚡ $cmd"
    if $cmd >/dev/null 2>&1; then
        echo "✅ Success: $cmd"
        exit 0
    else
        echo "❌ Failed: $cmd"
        install_attempted+=("$cmd")
    fi
}

# ──────────────────────────────────────────────
# 🎯 Priority Install Modes (Skip OS if specified)
# ──────────────────────────────────────────────

if [[ "$OPTION" == "-pip" ]]; then
    command -v pip3 && try_install "pip3 install $PKG --upgrade --no-cache-dir --break-system-packages"
    command -v pip && try_install "pip install $PKG --upgrade --no-cache-dir"
    exit 1
elif [[ "$OPTION" == "-node" ]]; then
    command -v npm && try_install "npm install -g $PKG --force"
    command -v yarn && try_install "yarn global add $PKG"
    exit 1
elif [[ "$OPTION" == "-bower" ]]; then
    command -v bower && try_install "bower install $PKG --force-latest"
    exit 1
elif [[ "$OPTION" == "-gem" ]]; then
    command -v gem && try_install "gem install $PKG --no-document"
    exit 1
elif [[ "$OPTION" == "-go" ]]; then
    command -v go && try_install "go install $PKG@latest"
    exit 1
elif [[ "$OPTION" == "-cargo" ]]; then
    command -v cargo && try_install "cargo install $PKG --force"
    exit 1
elif [[ "$OPTION" == "-git" ]]; then
    command -v git && try_install "git clone https://${PKG#https://}"
    exit 1
elif [[ "$OPTION" == "-c" || "$OPTION" == "--composer" ]]; then
    command -v composer && try_install "composer require $PKG"
    exit 1
elif [[ "$OPTION" == "-all" ]]; then
    echo "🌐 Trying all install methods..."
else
    # No switch? Don't try GitHub/Composer-style paths
    if [[ "$PKG" == *github.com* || "$PKG" == */* ]]; then
        echo "❗ Skipping GitHub/Composer-style install: use -git or -c"
        exit 1
    fi
fi

# ──────────────────────────────
# 🧠 OS Package Managers (no flag)
# ──────────────────────────────

if command -v apt >/dev/null 2>&1; then
    sudo apt update -y
    try_install "sudo apt install -y --fix-missing --allow-downgrades --allow-remove-essential --allow-change-held-packages $PKG"
elif command -v dnf >/dev/null 2>&1; then
    try_install "sudo dnf install -y --skip-broken $PKG"
elif command -v yum >/dev/null 2>&1; then
    try_install "sudo yum install -y --skip-broken $PKG"
elif command -v pacman >/dev/null 2>&1; then
    try_install "sudo pacman -Sy --noconfirm --needed $PKG"
elif command -v zypper >/dev/null 2>&1; then
    try_install "sudo zypper --non-interactive install $PKG"
elif command -v apk >/dev/null 2>&1; then
    try_install "sudo apk add --no-cache $PKG"
elif command -v brew >/dev/null 2>&1; then
    try_install "brew install $PKG"
elif command -v pkg >/dev/null 2>&1; then
    try_install "sudo pkg install -y $PKG"
elif command -v port >/dev/null 2>&1; then
    try_install "sudo port install $PKG"
elif command -v choco >/dev/null 2>&1; then
    try_install "choco install $PKG -y --ignore-checksums"
elif command -v scoop >/dev/null 2>&1; then
    try_install "scoop install $PKG"
elif uname | grep -qi msys; then
    command -v pacman && try_install "pacman -Sy --noconfirm --needed $PKG"
fi

# ──────────────────────────────
# 🔚 All failed
# ──────────────────────────────
echo "⚠️ All install attempts failed for: $PKG"
echo "Install attempts:"
for cmd in "${install_attempted[@]}"; do
    echo " - $cmd"
done

# 🔧 EXTENSION ZONE — Add Flatpak, Snap, or Custom Logic Below
