#!/bin/bash
# Script to sort the content of a file

FILE="names.txt"

# Sort the file alphabetically
sort "$FILE" > sorted_names.txt

echo "Sorted content saved to sorted_names.txt."
