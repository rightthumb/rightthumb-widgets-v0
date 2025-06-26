#!/bin/bash

sudo apt-get update -y

echo "https://rustdesk.com/docs/en/self-host/rustdesk-server-oss/ubuntu-server/docker/#2-setup-server"

cd ~ && mkdir -p docker/rustdesk-server/data

cd $HOME/docker/rustdesk-server/

cat <<EOL > compose.yml
services:
  hbbs:
    container_name: hbbs
    image: rustdesk/rustdesk-server:latest
    command: hbbs
    volumes:
      - ./data:/root
    network_mode: host
    depends_on:
      - hbbr
    restart: always

  hbbr:
    container_name: hbbr
    image: rustdesk/rustdesk-server:latest
    command: hbbr
    volumes:
      - ./data:/root
    network_mode: host
    restart: always

# Because using docker host mode
# Just in case you forgot the ports:
# 21114 TCP for web console, only available in Pro version
# 21115 TCP for NAT type test
# 21116 TCP TCP hole punching
# 21116 UDP heartbeat/ID server
# 21117 TCP relay
# 21118/21119 TCP for web socket if you want to run web client
EOL

sudo apt install docker docker.io docker-compose-plugin containerd runc  -y
sudo systemctl start docker

sudo docker-compose up -d
