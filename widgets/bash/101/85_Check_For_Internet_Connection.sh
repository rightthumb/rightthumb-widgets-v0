#!/bin/bash
# Script to check for an active internet connection

PING_RESULT=$(ping -c 1 google.com &> /dev/null && echo "Connected" || echo "Disconnected")

echo "Internet connection status: $PING_RESULT"
