#!/bin/bash
# Script to check file type and size

FILE="example.txt"

# Check file type
file "$FILE"

# Check file size
du -h "$FILE"
