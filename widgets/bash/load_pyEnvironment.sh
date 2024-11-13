#!/bin/bash

# Directory containing the virtual environments
VENV_DIR="$HOME/.pyEnvironment"

# echo "Checking for virtual environments in $VENV_DIR..."

# Check if the directory exists
if [ -d "$VENV_DIR" ]; then
	# echo "Virtual environments found in $VENV_DIR:"
	for venv in $VENV_DIR/venv_*; do
		if [ -d "$venv" ]; then
			venv_name=$(basename "$venv")
			# echo "--------------------------------"
			# echo "Virtual Environment: $venv_name"
			# echo "To activate this environment, run:"
			# echo "source $venv/bin/activate"
			# echo "Remember, to deactivate any virtual environment, simply run: deactivate"
		fi
	done
	# echo "--------------------------------"
	# echo "Note: Only one virtual environment can be activated at a time."
# else
	# echo "No virtual environment directory found at $VENV_DIR."
fi




# # Directory containing the virtual environments
# VENV_DIR="$HOME/.pyEnvironment"

# # Check if the directory exists
# if [ -d "$VENV_DIR" ]; then
# 	for venv in $VENV_DIR/venv_*; do
# 		if [ -d "$venv" ]; then
# 			venv_name=$(basename "$venv")
# 			# Placeholder for operations on each virtual environment
# 			# Example: logging or performing some checks
# 			# This script currently does nothing visible with each virtual environment
# 		fi
# 	done
# else
# 	# Placeholder for handling the case where the directory does not exist
# 	# Example: logging or error handling
# fi