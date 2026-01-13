#!/bin/bash
# Script to check if the user is root

if [ "$EUID" -ne 0 ]; then
    echo "You must be root to run this script."
    exit 1
fi

echo "You are root."
