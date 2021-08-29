#!/bin/bash
# Ask the user for login details
read -p 'Are you sure you want to continue connecting (yes/no/[fingerprint])?: ' cont
read -p 'Password: ' passvar
# read -sp 'Password: ' passvar
echo
echo cont $cont
echo pass $passvar