#!/bin/bash

# Check if script argument is provided
if [ -z "$1" ]; then
    echo "Usage: $0 <MainClassName>"
    exit 1
fi

# Compile Java file
echo "Compiling Java files..."
javac "$1.java"
if [ $? -ne 0 ]; then
    echo "Compilation failed."
    exit $?
fi

# Create JAR file
echo "Creating JAR file..."
jar cvfm "$1.jar" Manifest.txt "$1.class"
if [ $? -ne 0 ]; then
    echo "Failed to create JAR file."
    exit $?
fi

echo "Build Complete. $1.jar is ready."

# Application Packaging
echo "Creating macOS DMG file..."
jpackage -t dmg -n "$1" --main-class "$1" -i . --main-jar "$1.jar"

if [ $? -ne 0 ]; then
    echo "Failed to create macOS DMG file."
    exit $?
fi

echo "macOS DMG file created successfully."
