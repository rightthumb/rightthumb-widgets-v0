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










# Function to create a new VM with static IP
# create_vm() {
#     # Get the host's IP address, subnet mask, and gateway
#     host_ip=$(ip -o -f inet addr show | awk '/scope global/ {print $4}' | cut -d'/' -f1)
#     host_subnet_mask=$(ip -o -f inet addr show | awk '/scope global/ {print $4}' | head -1 | cut -d'/' -f2)
#     default_gateway=$(ip route | grep default | awk '{print $3}')

#     # Calculate the next IP address
#     IFS='.' read -r i1 i2 i3 i4 <<< "$host_ip"
#     next_ip="${i1}.${i2}.${i3}.$((i4 + 1))"

#     read -p "Enter a name for the new VM: " vm_name
#     read -p "Enter the amount of RAM in MB (e.g., 2048): " vm_ram

#     # Get the total number of CPUs available on the host
#     total_cpus=$(nproc)
#     recommended_cpus=$((total_cpus / 2)) # Recommend half the total CPUs for the VM
#     [[ $recommended_cpus -lt 1 ]] && recommended_cpus=1 # Ensure at least 1 CPU

#     read -p "Enter the number of CPUs (e.g., ${total_cpus}) [Recommended: ${recommended_cpus}]: " vm_vcpus
#     vm_vcpus=${vm_vcpus:-$recommended_cpus} # Use the recommended value if input is empty

#     read -p "Enter the disk size in GB (e.g., 20): " vm_disk_size
#     read -p "Enter the static IP address to assign (default: ${next_ip}): " vm_ip
#     vm_ip=${vm_ip:-$next_ip} # Use the calculated next IP if input is empty
#     read -p "Enter the subnet mask (default: ${host_subnet_mask}): " vm_netmask
#     vm_netmask=${vm_netmask:-$host_subnet_mask} # Use the host's subnet mask if input is empty
#     read -p "Enter the gateway (default: ${default_gateway}): " vm_gateway
#     vm_gateway=${vm_gateway:-$default_gateway} # Use the host's gateway if input is empty
#     read -p "Enter a username for the VM (default: ubuntu): " vm_user
#     read -p "Enter a password for the user: " -s vm_password
#     echo ""

#     # Ask for the ISO file path
#     read -p "Enter the path to the ISO file (e.g., /var/lib/libvirt/images/ubuntu.iso): " iso_path
#     if [[ ! -f "$iso_path" ]]; then
#         echo "Error: ISO file '$iso_path' does not exist. Exiting."
#         exit 1
#     fi

#     disk_path="/var/lib/libvirt/images/${vm_name}.qcow2"
#     config_dir="/var/lib/libvirt/images/${vm_name}-cloud-init"

#     echo "Creating a new disk image..."
#     qemu-img create -f qcow2 "$disk_path" "${vm_disk_size}G"

#     echo "Creating cloud-init config for automated installation..."
#     mkdir -p "$config_dir"
#     cat > "$config_dir/meta-data" <<EOF
# instance-id: ${vm_name}
# local-hostname: ${vm_name}
# EOF

#     encrypted_password=$(python3 -c "import crypt; print(crypt.crypt('${vm_password}', crypt.mksalt(crypt.METHOD_SHA512)))")

#     cat > "$config_dir/user-data" <<EOF
# #cloud-config
# network:
#   version: 2
#   ethernets:
#     eth0:
#       dhcp4: false
#       addresses:
#         - ${vm_ip}/${vm_netmask}
#       gateway4: ${vm_gateway}
#       nameservers:
#         addresses:
#           - 8.8.8.8
#           - 8.8.4.4
# users:
#   - name: ${vm_user:-ubuntu}
#     passwd: ${encrypted_password}
#     lock_passwd: false
#     ssh_authorized_keys: []
#     sudo: ['ALL=(ALL) NOPASSWD:ALL']
#     shell: /bin/bash
# ssh_pwauth: true
# chpasswd:
#   expire: false

# # Run the notification script after first boot
# runcmd:
#   - curl -s "https://notify.sds.sh/?sub=terminal&title=${vm_name}&message=os_install_complete"
# EOF

#     cloud_iso="${config_dir}/cloud-init.iso"
#     genisoimage -output "$cloud_iso" -volid cidata -joliet -rock \
#         "$config_dir/user-data" "$config_dir/meta-data"

#     echo "Defining the virtual machine and starting the installation..."
#     virt-install \
#         --name "$vm_name" \
#         --vcpus "$vm_vcpus" \
#         --memory "$vm_ram" \
#         --disk path="$disk_path",format=qcow2 \
#         --disk path="$cloud_iso",device=cdrom \
#         --cdrom "$iso_path" \
#         --os-variant ubuntu22.04 \
#         --network bridge=br0 \
#         --graphics vnc,listen=0.0.0.0 \
#         --console pty,target_type=serial \
#         --noautoconsole \
#         --boot hd,cdrom

#     echo "VM '$vm_name' created. You can connect via VNC."
#     echo "To find the VNC port, run: virsh vncdisplay $vm_name"
# }






create_vm() {
    # Get the host's IP address, subnet mask, and gateway
    host_ip=$(ip -o -f inet addr show | awk '/scope global/ {print $4}' | cut -d'/' -f1)
    host_subnet_mask=$(ip -o -f inet addr show | awk '/scope global/ {print $4}' | head -1 | cut -d'/' -f2)
    default_gateway=$(ip route | grep default | awk '{print $3}')

    # Calculate the next IP address
    IFS='.' read -r i1 i2 i3 i4 <<< "$host_ip"
    next_ip="${i1}.${i2}.${i3}.$((i4 + 1))"

    read -p "Enter a name for the new VM: " vm_name
    read -p "Enter the amount of RAM in MB (e.g., 2048): " vm_ram

    # Get the total number of CPUs available on the host
    total_cpus=$(nproc)
    recommended_cpus=$((total_cpus / 2)) # Recommend half the total CPUs for the VM
    [[ $recommended_cpus -lt 1 ]] && recommended_cpus=1 # Ensure at least 1 CPU

    read -p "Enter the number of CPUs (e.g., ${total_cpus}) [Recommended: ${recommended_cpus}]: " vm_vcpus
    vm_vcpus=${vm_vcpus:-$recommended_cpus} # Use the recommended value if input is empty

    # Assign disk path
    disk_path="/var/lib/libvirt/images/${vm_name}.qcow2"

    # Copy the base Ubuntu image as the new VM's disk
    echo "Copying base image to ${disk_path}..."
    if [[ ! -f /var/lib/libvirt/images/ubuntu-22.04.qcow2 ]]; then
        echo "Error: Base image '/var/lib/libvirt/images/ubuntu-22.04.qcow2' not found. Exiting."
        exit 1
    fi
    cp /var/lib/libvirt/images/ubuntu-22.04.qcow2 "$disk_path"

    # Prompt for the root password
    read -s -p "Enter the root password for the VM: " root_password
    echo ""

    # Set the root password using virt-customize
    echo "Setting root password..."
    sudo virt-customize -a "$disk_path" --root-password password:"$root_password"
    if [[ $? -ne 0 ]]; then
        echo "Error: Failed to set root password. Exiting."
        exit 1
    fi

    echo "Root password set successfully."

    # Define the VM with the copied disk
    echo "Defining the virtual machine and starting it..."
    virt-install \
        --name "$vm_name" \
        --vcpus "$vm_vcpus" \
        --memory "$vm_ram" \
        --disk path="$disk_path",format=qcow2 \
        --os-variant ubuntu22.04 \
        --network bridge=br0 \
        --graphics vnc,listen=0.0.0.0,passwd="$root_password" \
        --import \
        --noautoconsole

    echo "VM '$vm_name' created. You can connect via VNC using the root password."
    echo "To find the VNC port, run: virsh vncdisplay $vm_name"
}












# Function to delete a VM
delete_vm() {
    read -p "Enter the name of the VM to delete: " vm_name
    echo "This will permanently delete the VM '$vm_name' and its associated resources."
    read -p "Are you sure you want to proceed? (yes/no): " confirmation
    if [[ "$confirmation" == "yes" ]]; then
        echo "Shutting down the VM..."
        virsh shutdown "$vm_name" 2>/dev/null || echo "VM '$vm_name' is not running."
        echo "Undefining the VM..."
        virsh undefine "$vm_name" && echo "VM '$vm_name' undefined." || echo "Failed to undefine VM."
        echo "Removing VM disk..."
        vm_disk="/var/lib/libvirt/images/${vm_name}.qcow2"
        [[ -f "$vm_disk" ]] && rm -f "$vm_disk" && echo "Disk deleted." || echo "No disk found."
        echo "Removing cloud-init files..."
        cloud_init_dir="/var/lib/libvirt/images/${vm_name}-cloud-init/"
        [[ -d "$cloud_init_dir" ]] && rm -rf "$cloud_init_dir" && echo "Cloud-init files deleted." || echo "No cloud-init files found."
        echo "VM '$vm_name' has been deleted."
    else
        echo "VM deletion canceled."
    fi
}

# Function to connect to a VM console
connect_vm_console() {
    read -p "Enter the name of the VM to connect to: " vm_name
    virsh console "$vm_name"
}

autostart() {
    read -p "Enter the name of the VM to start automatically on host boot: " vm_name
    virsh autostart "$vm_name" && echo "VM '$vm_name' is set to start automatically on host boot."
}
autostartDisable() {
    read -p "Enter the name of the VM to not start automatically on host boot: " vm_name
    virsh autostart --disable "$vm_name" && echo "VM '$vm_name' will not start automatically on host boot."
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
    echo "8. Auto start a VM"
    echo "9. Auto start disable a VM"
    echo "10. Exit"
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
        8) autostart ;;
        9) autostartDisable ;;
        10) echo "Exiting..."; break ;;
        *) echo "Invalid choice. Please try again." ;;
    esac
done
