#!/bin/bash

if [ -z "$2" ]; then
    $p link -f "$1"
else
    $p link -src "$1" -dst "$2"
fi
