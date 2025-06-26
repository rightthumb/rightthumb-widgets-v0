#!/bin/bash
# Script to parse HTML content using grep and sed

HTML_FILE="example.html"

# Extract all links from the HTML file
grep -oP '(?<=href=")[^"]*' "$HTML_FILE"
