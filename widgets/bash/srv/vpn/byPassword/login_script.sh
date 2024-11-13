#!/bin/bash
PSW_FILE="/etc/openvpn/psw-file"

# Read username and password from the file specified by $1
USER_NAME=$(head -n 1 "$1")
PASS_WORD=$(tail -n 1 "$1")

# Check credentials
CORRECT_CREDS=$(grep -E "^$USER_NAME $PASS_WORD$" $PSW_FILE)
echo "Username: $USER_NAME, Password: $PASS_WORD" > /opt/_ovpn_test  # For debugging

if [ -n "$CORRECT_CREDS" ]; then
	exit 0  # Authentication success
else
	exit 1  # Authentication failure
fi

# echo $?