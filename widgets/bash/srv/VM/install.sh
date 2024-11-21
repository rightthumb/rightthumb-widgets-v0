#!/bin/bash

# Check if the script is run as root
if [ "$(id -u)" -ne 0 ]; then
  echo "This script must be run as root."
  exit 1
fi

echo "Updating system and installing KVM and virtualization tools..."
# Update system and install required software
apt update -y && apt upgrade -y
apt install -y qemu-kvm libvirt-daemon-system libvirt-clients bridge-utils virt-manager genisoimage

echo "Enabling and starting libvirt service..."
# Enable and start the libvirt service
systemctl enable libvirtd
systemctl start libvirtd

echo "Checking if KVM is installed and operational..."
# Check if KVM is installed properly
if ! kvm-ok; then
  echo "KVM is not properly configured or not supported by your CPU."
  exit 1
fi

echo "Creating a network bridge (br0)..."
# Configure a network bridge
cat > /etc/netplan/01-netcfg.yaml <<EOF
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

echo "Applying network configuration..."
netplan apply

echo "Creating a disk for the VM..."
# Create a 20GB virtual disk for the VM
VM_NAME="myvm"
DISK_PATH="/var/lib/libvirt/images/${VM_NAME}.qcow2"
ISO_PATH="/var/lib/libvirt/images/ubuntu.iso"
VM_MEMORY=2048 # Memory in MB
VM_VCPUS=2     # Number of CPUs

mkdir -p /var/lib/libvirt/images
qemu-img create -f qcow2 "$DISK_PATH" 20G

echo "Downloading Ubuntu ISO..."
# Download an Ubuntu ISO (you can replace the URL with the version you need)
wget -O "$ISO_PATH" https://releases.ubuntu.com/22.04/ubuntu-22.04.3-live-server-amd64.iso

echo "Defining the virtual machine..."
# Create and define a new virtual machine
virt-install \
  --name "$VM_NAME" \
  --vcpus "$VM_VCPUS" \
  --memory "$VM_MEMORY" \
  --disk path="$DISK_PATH",format=qcow2 \
  --cdrom "$ISO_PATH" \
  --network bridge=br0 \
  --os-type linux \
  --os-variant ubuntu22.04 \
  --graphics none \
  --console pty,target_type=serial \
  --noautoconsole

echo "VM setup complete. Use the following command to access the VM console:"
echo "virsh console ${VM_NAME}"