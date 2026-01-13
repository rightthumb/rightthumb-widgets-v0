#!/bin/bash

# Exit immediately if a command exits with a non-zero status
set -e

# Check if an application name was provided
if [ -z "$1" ]; then
    echo "Usage: $0 <AppName>"
    exit 1
fi

# Define the application name and main class based on the first argument
APP_NAME="$1"
MAIN_CLASS="$1"

# Compile the Java file
echo "Compiling Java file..."
javac "${APP_NAME}.java"

# Create the JAR file
echo "Creating JAR file..."
jar cvfm "${APP_NAME}.jar" Manifest.txt "${APP_NAME}.class"

echo "JAR build complete. ${APP_NAME}.jar is ready."

# Create the application image and package as .deb
echo "Creating application image and packaging into .deb..."
jpackage --type deb --input . --name "${APP_NAME}" --main-jar "${APP_NAME}.jar" --main-class "${MAIN_CLASS}" --dest dist --verbose

echo ".deb package created successfully. Check the 'dist' directory."
