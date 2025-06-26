#!/bin/bash
# Script to demonstrate output redirection

echo "This is a log message" > output.log
echo "This is an appended log message" >> output.log

# Redirect errors to a file
ls nonexistentfile 2> error.log

# Redirect both output and errors
ls /etc > output.log 2>&1