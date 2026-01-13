#!/bin/bash

sudo openssl req -new -x509 -days 365 -nodes \
  -out /etc/ssl/private/server.crt \
  -keyout /etc/ssl/private/server.key \
  -subj "/C=US/ST=State/L=City/O=Org/OU=Dev/CN=$(hostname)"

sudo chown postgres:postgres /etc/ssl/private/server.*
sudo chmod 600 /etc/ssl/private/server.key
sudo systemctl restart postgresql
