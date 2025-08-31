#!/bin/bash

# Check if an application name was provided
if [ -z "$1" ]; then
    echo "Usage: $0 <AppName>"
    exit 1
fi

# Define application name and main class based on the first argument
APP_NAME="$1"
MAIN_CLASS="$1"

# Compile the Java file
echo "Compiling Java file..."
javac "${APP_NAME}.java"
if [ $? -ne 0 ]; then
    echo "Compilation failed."
    exit 1
fi

# Create the JAR file
echo "Creating JAR file..."
jar cvfm "${APP_NAME}.jar" Manifest.txt "${APP_NAME}.class"
if [ $? -ne 0 ]; then
    echo "Failed to create JAR file."
    exit 1
fi

echo "JAR build complete. ${APP_NAME}.jar is ready."

# Package as an .app bundle using jpackage
echo "Packaging into an .app bundle..."
jpackage --type app-image --input . --name "${APP_NAME}" --main-jar "${APP_NAME}.jar" --main-class "${MAIN_CLASS}" --dest dist
if [ $? -ne 0 ]; then
    echo "Failed to create .app bundle."
    exit 1
fi

echo ".app bundle created successfully. Check the 'dist' directory."
