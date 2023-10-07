#!/bin/bash

# Install dependencies
sudo apt-get update && sudo apt-get install -y python3 python3-pip

# Install notify.sh
pip3 install notify-server

# Create a systemd service file for notify.sh
sudo cat << EOF > /etc/systemd/system/notify.service
[Unit]
Description=Notify.sh server
After=network.target

[Service]
Type=simple
ExecStart=/usr/local/bin/notify-server
Restart=on-failure

[Install]
WantedBy=multi-user.target
EOF

# Enable and start the notify.sh service
sudo systemctl enable notify.service
sudo systemctl start notify.service
