#!/bin/bash

if [ "$#" -ne 1 ]; then
	echo "Usage: $0 <shared_directory>"
	exit 1
fi

# Default shared directory
shared_directory="$1"

# Install Samba
sudo apt update
sudo apt install -y samba
sudo apt install -y samba-common-bin

# Configure Samba
sudo cp /etc/samba/smb.conf /etc/samba/smb.conf.backup   # Backup the original smb.conf
sudo cat <<EOF | sudo tee /etc/samba/smb.conf
[global]
   workgroup = WORKGROUP
   server string = Samba Server %v
   netbios name = ubuntu
   security = user
   map to guest = bad user
   dns proxy = no
   #============================ Share Definitions ============================== 
   [shared]
	path = $shared_directory
	browsable =yes
	writable = yes
	guest ok = yes
	read only = no
EOF

# Set permissions on the shared directory
sudo mkdir -p "$shared_directory"
sudo chmod -R 777 "$shared_directory"

# Restart Samba
sudo systemctl restart smbd

# Enable Samba in the firewall
sudo ufw allow samba

echo "SMB sharing is set up. The shared directory is: $shared_directory"