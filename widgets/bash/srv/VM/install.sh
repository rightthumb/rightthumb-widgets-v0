#!/bin/bash

# Check if the script is run as root
if [ "$(id -u)" -ne 0 ]; then
  echo "This script must be run as root."
  exit 1
fi

echo "Updating system and installing KVM and virtualization tools..."
# Update system and install required software
apt update && apt upgrade -y
apt install -y qemu-kvm libvirt-daemon-system libvirt-clients bridge-utils virt-manager wget

echo "Downloading Ubuntu ISO..."
# Download the latest Ubuntu ISO
ISO_PATH="/var/lib/libvirt/images/ubuntu.iso"
wget -O "$ISO_PATH" https://releases.ubuntu.com/22.04/ubuntu-22.04.5-live-server-amd64.iso
if [ $? -ne 0 ]; then
  echo "Failed to download Ubuntu ISO. Exiting."
  exit 1
fi

echo "Setting up network bridge (br0)..."
# Configure Netplan for bridge networking
NETPLAN_CONFIG="/etc/netplan/01-netcfg.yaml"
cat > "$NETPLAN_CONFIG" <<EOF
network:
  version: 2
  renderer: networkd
  ethernets:
    eno1:
      dhcp4: no
  bridges:
    br0:
      interfaces: [eno1]
      dhcp4: yes
EOF

# Fix file permissions for Netplan configuration
chmod 600 "$NETPLAN_CONFIG"
chown root:root "$NETPLAN_CONFIG"

echo "Applying Netplan configuration..."
netplan generate
if netplan apply; then
  echo "Netplan applied successfully."
else
  echo "Netplan application failed. Please check your configuration."
  exit 1
fi

echo "Checking network bridge setup..."
if ip a | grep -qw br0; then
  echo "Bridge 'br0' is configured and active."
else
  echo "Bridge 'br0' setup failed. Please verify the configuration."
  exit 1
fi

echo "Creating a disk for the VM..."
# Create a virtual disk for the VM
VM_NAME="myvm"
DISK_PATH="/var/lib/libvirt/images/${VM_NAME}.qcow2"
VM_MEMORY=2048 # Memory in MB
VM_VCPUS=2     # Number of CPUs
qemu-img create -f qcow2 "$DISK_PATH" 20G

echo "Defining the virtual machine..."
# Define and start the VM
virt-install \
  --name "$VM_NAME" \
  --vcpus "$VM_VCPUS" \
  --memory "$VM_MEMORY" \
  --disk path="$DISK_PATH",format=qcow2 \
  --cdrom "$ISO_PATH" \
  --network bridge=br0 \
  --os-variant ubuntu22.04 \
  --graphics none \
  --console pty,target_type=serial \
  --noautoconsole

if [ $? -eq 0 ]; then
  echo "VM setup complete. Use the following command to access the VM console:"
  echo "virsh console ${VM_NAME}"
else
  echo "VM installation failed. Please check the logs."
fi
