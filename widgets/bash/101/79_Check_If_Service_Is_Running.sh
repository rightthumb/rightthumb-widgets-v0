#!/bin/bash
# Script to check if a service is running

SERVICE="ssh"

if systemctl is-active --quiet "$SERVICE"; then
    echo "$SERVICE is running."
else
    echo "$SERVICE is not running."
fi
