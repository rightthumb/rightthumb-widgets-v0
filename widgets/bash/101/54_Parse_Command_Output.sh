#!/bin/bash
# Script to parse command output using cut, awk, and sed

# Using cut
echo "user@example.com" | cut -d "@" -f 1

# Using awk
echo "user@example.com" | awk -F "@" '{print $1}'

# Using sed
echo "Hello World" | sed 's/World/Universe/'