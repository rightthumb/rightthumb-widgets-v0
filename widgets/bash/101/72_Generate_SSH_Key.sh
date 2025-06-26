#!/bin/bash
# Script to generate an SSH key

ssh-keygen -t rsa -b 4096 -C "your_email@example.com"
echo "SSH key generated."
