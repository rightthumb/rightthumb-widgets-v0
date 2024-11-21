#!/bin/bash

# Function to list all VMs
list_vms() {
	echo "Listing all VMs..."
	virsh list --all
}

# Function to start a VM
start_vm() {
	read -p "Enter the name of the VM to start: " vm_name
	virsh start "$vm_name" && echo "VM '$vm_name' started successfully." || echo "Failed to start VM '$vm_name'."
}

# Function to shutdown a VM
shutdown_vm() {
	read -p "Enter the name of the VM to shutdown: " vm_name
	virsh shutdown "$vm_name" && echo "VM '$vm_name' is shutting down." || echo "Failed to shutdown VM '$vm_name'."
}

# Function to restart a VM
restart_vm() {
	read -p "Enter the name of the VM to restart: " vm_name
	virsh reboot "$vm_name" && echo "VM '$vm_name' is restarting." || echo "Failed to restart VM '$vm_name'."
}

# Function to create a new VM
create_vm() {
	read -p "Enter a name for the new VM: " vm_name
	read -p "Enter the amount of RAM in MB (e.g., 2048): " vm_ram
	read -p "Enter the number of CPUs (e.g., 2): " vm_vcpus
	read -p "Enter the disk size in GB (e.g., 20): " vm_disk_size
	read -p "Enter the path to the ISO file: " iso_path
	disk_path="/var/lib/libvirt/images/${vm_name}.qcow2"

	echo "Creating a new disk image..."
	qemu-img create -f qcow2 "$disk_path" "${vm_disk_size}G"

	echo "Defining the virtual machine..."
	virt-install \
		--name "$vm_name" \
		--vcpus "$vm_vcpus" \
		--memory "$vm_ram" \
		--disk path="$disk_path",format=qcow2 \
		--cdrom "$iso_path" \
		--network bridge=br0 \
		--os-type linux \
		--os-variant ubuntu22.04 \
		--graphics none \
		--console pty,target_type=serial \
		--noautoconsole
}

# Function to delete a VM
delete_vm() {
	read -p "Enter the name of the VM to delete: " vm_name
	read -p "Are you sure you want to delete VM '$vm_name' and its disk? (yes/no): " confirmation
	if [[ "$confirmation" == "yes" ]]; then
		virsh destroy "$vm_name" 2>/dev/null
		virsh undefine "$vm_name" && echo "VM '$vm_name' has been deleted." || echo "Failed to delete VM '$vm_name'."
		read -p "Delete the VM disk as well? (yes/no): " delete_disk
		if [[ "$delete_disk" == "yes" ]]; then
			disk_path=$(virsh domblklist "$vm_name" | grep ".qcow2" | awk '{print $2}')
			if [[ -n "$disk_path" ]]; then
				rm -f "$disk_path" && echo "Disk '$disk_path' deleted." || echo "Failed to delete disk '$disk_path'."
			fi
		fi
	else
		echo "VM deletion canceled."
	fi
}

# Function to connect to a VM console
connect_vm_console() {
	read -p "Enter the name of the VM to connect to: " vm_name
	virsh console "$vm_name"
}

# Main menu
while true; do
	echo ""
	echo "Virtual Machine Management Menu"
	echo "1. List all VMs"
	echo "2. Start a VM"
	echo "3. Shutdown a VM"
	echo "4. Restart a VM"
	echo "5. Create a new VM"
	echo "6. Delete a VM"
	echo "7. Connect to a VM console"
	echo "8. Exit"
	echo ""
	read -p "Enter your choice (1-8): " choice

	case $choice in
		1) list_vms ;;
		2) start_vm ;;
		3) shutdown_vm ;;
		4) restart_vm ;;
		5) create_vm ;;
		6) delete_vm ;;
		7) connect_vm_console ;;
		8) echo "Exiting..."; break ;;
		*) echo "Invalid choice. Please try again." ;;
	esac
done