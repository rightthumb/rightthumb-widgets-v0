#!/bin/bash
# Script to create an interactive menu

echo "1. Option 1"
echo "2. Option 2"
echo "3. Exit"

# Read user choice
read -p "Choose an option: " choice

# Handle user input
case $choice in
	1) echo "You chose Option 1";;
	2) echo "You chose Option 2";;
	3) exit;;
	*) echo "Invalid choice";;
esac