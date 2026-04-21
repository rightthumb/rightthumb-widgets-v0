#!/bin/bash
# Script to encrypt and decrypt files using OpenSSL

FILE="example.txt"
PASSWORD="mysecurepassword"

# Encrypt the file
openssl enc -aes-256-cbc -salt -in "$FILE" -out "$FILE.enc" -k "$PASSWORD"
echo "File encrypted as $FILE.enc."

# Decrypt the file
openssl enc -aes-256-cbc -d -in "$FILE.enc" -out "$FILE.dec" -k "$PASSWORD"
echo "File decrypted as $FILE.dec."
