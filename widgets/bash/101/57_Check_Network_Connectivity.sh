#!/bin/bash
# Script to check network connectivity

# Ping a host
ping -c 4 google.com

# Check if a port is open
nc -zv localhost 22