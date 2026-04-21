#!/bin/bash

# Define the folder path
FOLDER_PATH="/path/to/folder"

# Check if the folder exists
if [ -d "$FOLDER_PATH" ]; then
	echo "The folder '$FOLDER_PATH' exists."
else
	echo "The folder '$FOLDER_PATH' does not exist."
fi