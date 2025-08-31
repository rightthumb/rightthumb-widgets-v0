#!/bin/bash
# Script to generate a random password

LENGTH=12
PASSWORD=$(tr -dc 'A-Za-z0-9!@#$%^&*()_+' < /dev/urandom | head -c $LENGTH)

echo "Generated password: $PASSWORD"
