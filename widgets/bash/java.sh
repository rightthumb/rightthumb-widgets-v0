#!/bin/bash

# Compilation
echo "Compiling Java files..."
javac "$1.java"
if [ $? -ne 0 ]; then
	echo "Compilation failed."
	exit $?
fi

# JAR Creation
echo "Creating JAR file..."
jar cvfm "$1.jar" Manifest.txt "$1.class"
if [ $? -ne 0 ]; then
	echo "Failed to create JAR file."
	exit $?
fi

echo "Build Complete. $1.jar is ready."

# Application Packaging
echo "Creating application image..."
mkdir -p "app"
mv "$1.jar" "app/"
jpackage --type app-image --input app --name "$1" --main-jar "$1.jar" --main-class "$1" --temp temp-dir

if [ $? -ne 0 ]; then
	echo "Failed to create application image."
	exit $?
fi

echo "Application image created successfully."

# https://chat.openai.com/c/3aa3c014-32a6-4270-b9e4-db6301ffe2cc