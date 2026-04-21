#!/bin/bash

# Default shared directory

if [ "$#" -ne 3 ]; then
   echo "Usage: $0 <shared_directory> <domain> <domain_admin>"
   exit 1
fi

# Domain settings
shared_directory="$1"
domain="$2"
domain_admin="$3"

# Install Samba
sudo apt update
sudo apt install -y samba

# Configure Samba
sudo cp /etc/samba/smb.conf /etc/samba/smb.conf.backup   # Backup the original smb.conf
sudo cat <<EOF | sudo tee /etc/samba/smb.conf
[global]
   workgroup = $domain
   realm = $domain
   server string = Samba Server %v
   security = ADS
   encrypt passwords = yes
   passdb backend = tdbsam
   obey pam restrictions = yes
   unix password sync = yes
   passwd program = /usr/bin/passwd %u
   passwd chat = *Enter\snew\s*\spassword:* %n\n *Retype\snew\s*\spassword:* %n\n *password\supdated\ssuccessfully* .
   pam password change = yes
   map to guest = bad user
   usershare allow guests = yes
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