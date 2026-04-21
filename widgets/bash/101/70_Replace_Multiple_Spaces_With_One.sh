#!/bin/bash
# Script to replace multiple spaces with a single space in a file

FILE="example.txt"

sed -i 's/ \+/ /g' "$FILE"
echo "Replaced multiple spaces with a single space in $FILE."
