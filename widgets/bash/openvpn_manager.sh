#!/bin/bash

# Function to install OpenVPN terminal version
install_terminal() {
	sudo apt update
	sudo apt install -y openvpn
}

# Function to install OpenVPN GUI version
install_gui() {
	sudo apt update
	sudo apt install -y network-manager-openvpn network-manager-openvpn-gnome
	sudo systemctl restart NetworkManager
}

# Function to add an OpenVPN configuration file
add_ovpn_file() {
	local ovpn_file="$2"
	sudo cp "$ovpn_file" /etc/openvpn/
	sudo chmod 600 /etc/openvpn/$(basename "$ovpn_file")
	echo "Configuration file added."
}

# Function to list OpenVPN configuration files
list_vpn_files() {
	echo "Available VPN configurations:"
	ls /etc/openvpn/*.ovpn | xargs -n 1 basename | sed 's/.ovpn//'
}

# Function to connect to an OpenVPN configuration
connect_vpn() {
	local vpn_name="$2"
	sudo openvpn --config /etc/openvpn/"$vpn_name".ovpn
}

# Function to disconnect OpenVPN
disconnect_vpn() {
	sudo killall openvpn
}

# Function to open OpenVPN GUI
open_gui() {
	nm-connection-editor
}

# Function to show help message
show_help() {
	echo "OpenVPN Management Script"
	echo "Usage: $0 [option] [additional info]"
	echo "Options:"
	echo "  -it, --install-terminal             Install OpenVPN terminal version"
	echo "  -ig, --install-gui                  Install OpenVPN GUI version"
	echo "  -a,  --add <path_to_ovpn_file>      Add an OpenVPN configuration file"
	echo "  -c,  --connect <vpn_config_name>    Connect to an OpenVPN configuration"
	echo "  -d,  --disconnect                   Disconnect OpenVPN"
	echo "  -og, --open-gui                     Open OpenVPN GUI"
	echo "  -l,  --list                         List available VPN configurations"
	echo "  -h,  --help                         Show this help message"
}

# Main script
case "$1" in
	-it|--install-terminal)
		install_terminal
		;;
	-ig|--install-gui)
		install_gui
		;;
	-a|--add)
		add_ovpn_file "$@"
		;;
	-c|--connect)
		connect_vpn "$@"
		;;
	-d|--disconnect)
		disconnect_vpn
		;;
	-og|--open-gui)
		open_gui
		;;
	-l|--list)
		list_vpn_files
		;;
	-h|--help|*)
		show_help
		;;
esac