#!/bin/bash
# Script to parse JSON using jq

# Sample JSON
json='{"name": "John", "age": 30}'

# Parse and extract the name
name=$(echo "$json" | jq -r '.name')
echo "Name: $name"