#!/usr/bin/env bash

# =========================================================
# UniversalDocLib Installer
# =========================================================
# Modes:
#   ./install_universal_doc.sh              (auto detect)
#   ./install_universal_doc.sh --break      (force break-system-packages)
#   ./install_universal_doc.sh --user       (pip --user)
#   ./install_universal_doc.sh --venv       (create venv)
#
# =========================================================

set -e

PYTHON_BIN=${PYTHON_BIN:-python3}

MODE="auto"

for arg in "$@"; do
	case "$arg" in
		--break) MODE="break" ;;
		--user)  MODE="user" ;;
		--venv)  MODE="venv" ;;
	esac
done

echo "[info] python: $PYTHON_BIN"
echo "[info] mode: $MODE"

# =========================================================
# Package list (your doc system stack)
# =========================================================

PKGS=(
	"python-docx"
	"beautifulsoup4"
	"openpyxl"
	"python-pptx"
	"EbookLib"
	"pylatexenc"
	"striprtf"
	"pdfminer.six"
	"pdfplumber"
	"rich"
)

# Optional extras (safe to fail)
OPTIONAL_PKGS=(
	"pymupdf4llm"
)

# =========================================================
# Detect pip break-system-packages requirement
# =========================================================

detect_break_needed() {
	OUTPUT=$($PYTHON_BIN -m pip install test-package-does-not-exist 2>&1 || true)
	echo "$OUTPUT" | grep -q "externally-managed-environment"
}

# =========================================================
# Install methods
# =========================================================

install_break() {
	echo "[mode] break-system-packages"
	$PYTHON_BIN -m pip install --break-system-packages "${PKGS[@]}"
}

install_user() {
	echo "[mode] user install"
	$PYTHON_BIN -m pip install --user "${PKGS[@]}"
}

install_venv() {
	echo "[mode] venv install"
	VENV_DIR="./venv_universal_doc"

	$PYTHON_BIN -m venv "$VENV_DIR"
	source "$VENV_DIR/bin/activate"

	pip install --upgrade pip
	pip install "${PKGS[@]}"

	echo
	echo "[info] activate with:"
	echo "source $VENV_DIR/bin/activate"
}

install_auto() {
	echo "[mode] auto detect"

	if detect_break_needed; then
		echo "[info] detected externally managed python"
		install_break
	else
		echo "[info] normal pip environment"
		$PYTHON_BIN -m pip install "${PKGS[@]}"
	fi
}

# =========================================================
# Run selected mode
# =========================================================

case "$MODE" in
	break) install_break ;;
	user)  install_user ;;
	venv)  install_venv ;;
	auto)  install_auto ;;
esac

# =========================================================
# Optional installs (non-fatal)
# =========================================================

echo
echo "[info] installing optional packages..."

for pkg in "${OPTIONAL_PKGS[@]}"; do
	if $PYTHON_BIN -m pip install "$pkg" 2>/dev/null; then
		echo "[ok] $pkg installed"
	else
		echo "[skip] $pkg failed (non-critical)"
	fi
done

# =========================================================
# Verify key modules
# =========================================================

echo
echo "[info] verifying modules..."

$PYTHON_BIN - <<'PY'
modules = [
	"docx",
	"bs4",
	"openpyxl",
	"pptx",
	"ebooklib",
	"pylatexenc",
	"striprtf",
	"pdfminer",
	"pdfplumber",
	"rich",
]

for m in modules:
	try:
		__import__(m)
		print(f"[ok] {m}")
	except Exception as e:
		print(f"[fail] {m} :: {e}")
PY

echo
echo "[done] UniversalDocLib environment ready"