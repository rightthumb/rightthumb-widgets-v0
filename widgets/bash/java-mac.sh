#!/bin/bash

# Checking if the script argument is provided
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

# Create application image using jpackage
echo "Creating macOS application image..."
jpackage --type app-image --input . --name "$1" --main-jar "$1.jar" --main-class $1

if [ $? -ne 0 ]; then
    echo "Failed to create macOS application image."
    exit $?
fi

echo "macOS application image created successfully."
