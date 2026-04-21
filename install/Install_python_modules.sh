#!/usr/bin/env bash

# =========================================================
# Generic Python Module Installer
# =========================================================
# Usage examples:
#
#   ./install_python_modules.sh requests numpy pandas
#   ./install_python_modules.sh requirements.txt
#   ./install_python_modules.sh base.txt extras.txt
#   ./install_python_modules.sh requests flask extra.txt
#
# Modes:
#   ./install_python_modules.sh [packages/files...]              (auto detect)
#   ./install_python_modules.sh --break [packages/files...]
#   ./install_python_modules.sh --user  [packages/files...]
#   ./install_python_modules.sh --venv  [packages/files...]
#
# Optional:
#   PYTHON_BIN=python3.11 ./install_python_modules.sh requests
#   VENV_DIR=.venv ./install_python_modules.sh --venv requests
#
# Notes:
# - Any argument ending in .txt is treated as a requirements file
# - Lines starting with # or blank lines are ignored
# - In auto mode, --break-system-packages is only used if needed
# =========================================================

set -euo pipefail

PYTHON_BIN="${PYTHON_BIN:-python3}"
VENV_DIR="${VENV_DIR:-./venv_python_modules}"
MODE="auto"

declare -a CLI_PKGS=()
declare -a REQ_FILES=()
declare -a OPTIONAL_PKGS=()

usage() {
	cat <<'EOF'
Usage:
  install_python_modules.sh [--break|--user|--venv] <pkg|requirements.txt> [...]

Examples:
  install_python_modules.sh requests numpy pandas
  install_python_modules.sh requirements.txt
  install_python_modules.sh base.txt extras.txt
  install_python_modules.sh requests flask extras.txt

Options:
  --break     Force pip install --break-system-packages
  --user      Use pip install --user
  --venv      Create/use a virtual environment and install there
  --optional  Start marking following pkg/file args as optional packages
  --help      Show this help

Behavior:
  - Any argument ending in .txt is treated as a requirements file
  - In auto mode, the script only uses --break-system-packages if required
  - Optional packages do not fail the script if they cannot be installed

Examples with optional:
  install_python_modules.sh requests rich --optional pymupdf4llm
  install_python_modules.sh core.txt --optional extras.txt
EOF
}

# =========================================================
# Parse args
# =========================================================

OPTIONAL_MODE=0

while (($#)); do
	arg="$1"
	case "$arg" in
		--break) MODE="break" ;;
		--user) MODE="user" ;;
		--venv) MODE="venv" ;;
		--optional) OPTIONAL_MODE=1 ;;
		--help|-h)
			usage
			exit 0
			;;
		*)
			if [[ "$arg" == *.txt ]]; then
				if [[ ! -f "$arg" ]]; then
					echo "[error] requirements file not found: $arg" >&2
					exit 1
				fi
				if [[ $OPTIONAL_MODE -eq 1 ]]; then
					OPTIONAL_PKGS+=("__REQFILE__:$arg")
				else
					REQ_FILES+=("$arg")
				fi
			else
				if [[ $OPTIONAL_MODE -eq 1 ]]; then
					OPTIONAL_PKGS+=("$arg")
				else
					CLI_PKGS+=("$arg")
				fi
			fi
			;;
	esac
	shift
done

if [[ ${#CLI_PKGS[@]} -eq 0 && ${#REQ_FILES[@]} -eq 0 ]]; then
	echo "[error] no packages or .txt files provided"
	echo
	usage
	exit 1
fi

echo "[info] python: $PYTHON_BIN"
echo "[info] mode: $MODE"

# =========================================================
# Build package list
# =========================================================

declare -a PKGS=()

add_pkg_if_missing() {
	local pkg="$1"
	local existing
	for existing in "${PKGS[@]}"; do
		[[ "$existing" == "$pkg" ]] && return 0
	done
	PKGS+=("$pkg")
}

read_requirements_file() {
	local file="$1"
	while IFS= read -r line || [[ -n "$line" ]]; do
		# trim leading/trailing whitespace
		line="${line#"${line%%[![:space:]]*}"}"
		line="${line%"${line##*[![:space:]]}"}"

		# skip blank lines and comments
		[[ -z "$line" ]] && continue
		[[ "$line" == \#* ]] && continue

		add_pkg_if_missing "$line"
	done < "$file"
}

for pkg in "${CLI_PKGS[@]}"; do
	add_pkg_if_missing "$pkg"
done

for file in "${REQ_FILES[@]}"; do
	echo "[info] loading requirements from: $file"
	read_requirements_file "$file"
done

if [[ ${#PKGS[@]} -eq 0 ]]; then
	echo "[error] no installable packages found"
	exit 1
fi

echo "[info] packages to install:"
for pkg in "${PKGS[@]}"; do
	echo "  - $pkg"
done

# =========================================================
# Helpers
# =========================================================

PIP_ARGS=()

detect_break_needed() {
	local output
	output="$($PYTHON_BIN -m pip install --dry-run test-package-does-not-exist 2>&1 || true)"

	if echo "$output" | grep -qi "externally-managed-environment"; then
		return 0
	fi

	if echo "$output" | grep -qi "externally managed"; then
		return 0
	fi

	return 1
}

setup_pip_args_for_mode() {
	case "$MODE" in
		break)
			PIP_ARGS=(--break-system-packages)
			echo "[mode] break-system-packages"
			;;
		user)
			PIP_ARGS=(--user)
			echo "[mode] user install"
			;;
		venv)
			PIP_ARGS=()
			echo "[mode] venv install"
			;;
		auto)
			echo "[mode] auto detect"
			if detect_break_needed; then
				echo "[info] detected externally managed python"
				PIP_ARGS=(--break-system-packages)
			else
				echo "[info] normal pip environment"
				PIP_ARGS=()
			fi
			;;
		*)
			echo "[error] unknown mode: $MODE" >&2
			exit 1
			;;
	esac
}

run_pip_install() {
	"$PYTHON_BIN" -m pip install "${PIP_ARGS[@]}" "$@"
}

# =========================================================
# venv setup if requested
# =========================================================

if [[ "$MODE" == "venv" ]]; then
	"$PYTHON_BIN" -m venv "$VENV_DIR"
	# shellcheck disable=SC1090
	source "$VENV_DIR/bin/activate"
	PYTHON_BIN="python"
	echo "[info] venv: $VENV_DIR"
	echo "[info] upgraded python in venv: $PYTHON_BIN"
	"$PYTHON_BIN" -m pip install --upgrade pip
fi

setup_pip_args_for_mode

# =========================================================
# Install main packages
# =========================================================

echo
echo "[info] installing main packages..."
run_pip_install "${PKGS[@]}"

# =========================================================
# Install optional packages/files (non-fatal)
# =========================================================

if [[ ${#OPTIONAL_PKGS[@]} -gt 0 ]]; then
	echo
	echo "[info] installing optional packages..."

	for item in "${OPTIONAL_PKGS[@]}"; do
		if [[ "$item" == __REQFILE__:* ]]; then
			reqfile="${item#__REQFILE__:}"
			echo "[info] loading optional requirements from: $reqfile"

			while IFS= read -r line || [[ -n "$line" ]]; do
				line="${line#"${line%%[![:space:]]*}"}"
				line="${line%"${line##*[![:space:]]}"}"
				[[ -z "$line" ]] && continue
				[[ "$line" == \#* ]] && continue

				if run_pip_install "$line" >/dev/null 2>&1; then
					echo "[ok] $line installed"
				else
					echo "[skip] $line failed (non-critical)"
				fi
			done < "$reqfile"
		else
			if run_pip_install "$item" >/dev/null 2>&1; then
				echo "[ok] $item installed"
			else
				echo "[skip] $item failed (non-critical)"
			fi
		fi
	done
fi

# =========================================================
# Verify installed modules where possible
# =========================================================

echo
echo "[info] verifying installed packages..."

PKG_LIST_FILE="$(mktemp)"
printf '%s\n' "${PKGS[@]}" > "$PKG_LIST_FILE"

"$PYTHON_BIN" - <<'PY' "$PKG_LIST_FILE"
import importlib.metadata
import pathlib
import re
import sys

pkg_file = pathlib.Path(sys.argv[1])
requested = [line.strip() for line in pkg_file.read_text().splitlines() if line.strip()]

def normalize(name: str) -> str:
	return re.sub(r"[-_.]+", "-", name).lower()

installed = {}
for dist in importlib.metadata.distributions():
	try:
		name = dist.metadata["Name"]
		if name:
			installed[normalize(name)] = name
	except Exception:
		pass

ok = 0
fail = 0

for req in requested:
	base = req
	for sep in ["==", ">=", "<=", "~=", "!=", ">", "<", "["]:
		if sep in base:
			base = base.split(sep, 1)[0]
	key = normalize(base.strip())

	if key in installed:
		print(f"[ok] {req} -> installed as {installed[key]}")
		ok += 1
	else:
		print(f"[fail] {req} -> not found in installed distributions")
		fail += 1

print()
print(f"[summary] ok={ok} fail={fail}")
PY

rm -f "$PKG_LIST_FILE"

echo
if [[ "$MODE" == "venv" ]]; then
	echo "[info] activate with:"
	echo "source $VENV_DIR/bin/activate"
	echo
fi

echo "[done] Python module installation complete"