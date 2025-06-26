#!/bin/bash

# Optional arguments: port and description
PORT=${1:-8080}
DESCRIPTION=${2:-"Notify.sh server"}

# Install dependencies
sudo apt-get update && sudo apt-get install -y python3 python3-pip

# Install notify.sh
pip3 install notify-server

# Create a systemd service file for notify.sh
sudo cat << EOF > /etc/systemd/system/notify.service
[Unit]
Description=$DESCRIPTION
After=network.target

[Service]
Type=simple
ExecStart=/usr/local/bin/notify-server --port $PORT
Restart=on-failure

[Install]
WantedBy=multi-user.target
EOF

# Enable and start the notify.sh service
sudo systemctl enable notify.service
sudo systemctl start notify.service
