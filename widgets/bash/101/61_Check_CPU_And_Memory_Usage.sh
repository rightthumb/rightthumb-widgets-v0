#!/bin/bash
# Script to check CPU and memory usage

echo "CPU and Memory Usage:"
top -b -n 1 | head -n 10
