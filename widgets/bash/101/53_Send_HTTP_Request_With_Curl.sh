#!/bin/bash
# Script to send an HTTP request using curl

URL="https://api.example.com/data"

# Send GET request
response=$(curl -s "$URL")

echo "Response: $response"