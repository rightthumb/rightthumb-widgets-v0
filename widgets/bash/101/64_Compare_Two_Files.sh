#!/bin/bash
# Script to compare two files

FILE1="file1.txt"
FILE2="file2.txt"

if cmp -s "$FILE1" "$FILE2"; then
    echo "Files are identical."
else
    echo "Files are different."
fi
