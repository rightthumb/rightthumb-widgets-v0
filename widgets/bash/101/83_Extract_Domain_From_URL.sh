#!/bin/bash
# Script to extract the domain from a URL

URL="https://www.example.com/path/page.html"

DOMAIN=$(echo "$URL" | awk -F[/:] '{print $4}')
echo "Extracted domain: $DOMAIN"
