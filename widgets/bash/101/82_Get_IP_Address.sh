#!/bin/bash
# Script to get the IP address of the system

IP_ADDRESS=$(hostname -I | awk '{print $1}')
echo "Your IP address is: $IP_ADDRESS"
