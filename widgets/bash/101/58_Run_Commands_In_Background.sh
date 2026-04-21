#!/bin/bash
# Script to run commands in the background

# Run a command in the background
my_script.sh &

# Run a long-running command and keep it running even after logout
nohup my_long_running_script.sh > output.log &