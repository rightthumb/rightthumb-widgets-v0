#!/bin/bash
# -------------------------------------------------------------
# usbdrv.sh – Mount or unmount Windows USB drives in WSL
#
# Usage:
#   usbdrv.sh <drive-letter>          # mount
#   usbdrv.sh -u <drive-letter>       # unmount
#   usbdrv.sh -f <drive-letter>       # force unmount (lazy)
#
# -------------------------------------------------------------

# --- Colors ---------------------------------------------------------------
GREEN="\033[1;32m"
RED="\033[1;31m"
CYAN="\033[1;36m"
RESET="\033[0m"

help() {
    echo -e "${CYAN}Usage:${RESET}"
    echo -e "  $0 <drive-letter>        ${GREEN}# mount drive${RESET}"
    echo -e "  $0 -u <drive-letter>     ${GREEN}# unmount drive${RESET}"
    echo -e "  $0 -f <drive-letter>     ${GREEN}# force unmount (lazy)${RESET}"
    echo ""
    echo -e "${CYAN}Examples:${RESET}"
    echo -e "  $0 e"
    echo -e "  $0 -u e"
    echo -e "  $0 -f e"
    exit 1
}

# --- No args → help -------------------------------------------------------
[ $# -eq 0 ] && help

# --- Mode flags -----------------------------------------------------------
UNMOUNT=0
FORCE=0

case "$1" in
    -u|--unmount) UNMOUNT=1; shift ;;
    -f|--force)   FORCE=1; UNMOUNT=1; shift ;;
esac

# --- Require a drive letter ------------------------------------------------
[ -z "$1" ] && help

# Normalize letter
LETTER="${1:0:1}"
ULETTER=$(echo "$LETTER" | tr '[:lower:]' '[:upper:]')
LLETTER=$(echo "$LETTER" | tr '[:upper:]' '[:lower:]')

WIN_DRIVE="${ULETTER}:"
WSL_MOUNT="/mnt/${LLETTER}"

# --- Unmount ---------------------------------------------------------------
if [ "$UNMOUNT" -eq 1 ]; then
    if [ "$FORCE" -eq 1 ]; then
        echo -e "${RED}Force-unmounting ${WIN_DRIVE} from ${WSL_MOUNT} ...${RESET}"
        sudo umount -l "$WSL_MOUNT" 2>/dev/null
    else
        echo -e "${RED}Unmounting ${WIN_DRIVE} from ${WSL_MOUNT} ...${RESET}"
        sudo umount "$WSL_MOUNT" 2>/dev/null
    fi

    if [ $? -eq 0 ]; then
        echo -e "${GREEN}Unmounted successfully.${RESET}"
    else
        echo -e "${RED}Could not unmount. Drive may not be mounted.${RESET}"
    fi
    exit 0
fi

# --- Mount ---------------------------------------------------------------
echo -e "${CYAN}Mounting ${WIN_DRIVE} to ${WSL_MOUNT} ...${RESET}"

sudo mkdir -p "$WSL_MOUNT"
sudo mount -t drvfs "$WIN_DRIVE" "$WSL_MOUNT"

if [ $? -eq 0 ]; then
    echo -e "${GREEN}Mounted at ${WSL_MOUNT}${RESET}"
else
    echo -e "${RED}Mount failed. Ensure Windows sees ${WIN_DRIVE}.${RESET}"
fi
