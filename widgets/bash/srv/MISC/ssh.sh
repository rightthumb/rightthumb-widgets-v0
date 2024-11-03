#!/usr/bin/expect -f

# Remove the existing SSH directory
spawn rm -rf ~/.ssh
expect eof

# Start the SSH key generation process
spawn ssh-keygen -t rsa

# Expect the prompts and provide the necessary inputs
expect "Enter file in which to save the key*"
send "\r"

expect "Enter passphrase*"
send "\r"

expect "Enter same passphrase again:"
send "\r"

# Wait for the process to complete
expect eof