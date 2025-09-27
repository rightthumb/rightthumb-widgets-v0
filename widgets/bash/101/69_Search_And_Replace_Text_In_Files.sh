#!/bin/bash
# Script to search and replace text in files

FILE="example.txt"
SEARCH="oldtext"
REPLACE="newtext"

sed -i "s/$SEARCH/$REPLACE/g" "$FILE"
echo "Replaced '$SEARCH' with '$REPLACE' in $FILE."
