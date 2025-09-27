#!/bin/bash
# Script to check if a port is open

HOST="localhost"
PORT=22

nc -zv "$HOST" "$PORT" && echo "Port $PORT is open." || echo "Port $PORT is closed."
