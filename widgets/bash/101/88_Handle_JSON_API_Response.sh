#!/bin/bash
# Script to handle a JSON API response using jq

API_URL="https://api.example.com/data"

response=$(curl -s "$API_URL")
name=$(echo "$response" | jq -r '.name')

echo "Name from API response: $name"
