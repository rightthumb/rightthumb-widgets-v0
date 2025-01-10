#!/bin/bash
# Script to read a configuration file

CONFIG_FILE="config.cfg"

while IFS='=' read -r key value; do
    echo "$key = $value"
done < "$CONFIG_FILE"
