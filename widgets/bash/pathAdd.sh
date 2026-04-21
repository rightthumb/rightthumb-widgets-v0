#!/bin/bash

if [ -z "$1" ]; then
    echo "Usage: append_path.sh /your/path"
    exit 1
fi

export PATH="$PATH:$1"
echo "PATH updated: $PATH"
