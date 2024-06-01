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
	read -p "Enter the path to the .ovpn file: " ovpn_file
	sudo cp "$ovpn_file" /etc/openvpn/
	sudo chmod 600 /etc/openvpn/$(basename "$ovpn_file")
	echo "Configuration file added."
}

# Function to connect to an OpenVPN configuration
connect_vpn() {
	read -p "Enter the name of the VPN configuration file (without .ovpn extension): " vpn_name
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
	echo "Usage: $0 [option]"
	echo "Options:"
	echo "  -it, --install-terminal     Install OpenVPN terminal version"
	echo "  -ig, --install-gui          Install OpenVPN GUI version"
	echo "  -a, --add                   Add an OpenVPN configuration file"
	echo "  -c, --connect               Connect to an OpenVPN configuration"
	echo "  -d, --disconnect            Disconnect OpenVPN"
	echo "  -og, --open-gui             Open OpenVPN GUI"
	echo "  -h, --help                  Show this help message"
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
		add_ovpn_file
		;;
	-c|--connect)
		connect_vpn
		;;
	-d|--disconnect)
		disconnect_vpn
		;;
	-og|--open-gui)
		open_gui
		;;
	-h|--help|*)
		show_help
		;;
esac



# #!/bin/bash

# # OpenVPN Management Script

# OPENVPN_DIR="/etc/openvpn"
# CONFIG_DIR="$OPENVPN_DIR/config"
# LOG_FILE="$OPENVPN_DIR/openvpn.log"
# OPENVPN_SERVICE="openvpn"

# function install_openvpn_terminal() {
#     sudo apt-get update
#     sudo apt-get install -y openvpn
# }

# function install_openvpn_gui() {
#     sudo apt-get update
#     sudo apt-get install -y network-manager-openvpn-gnome
# }

# function add_ovpn_file() {
#     read -p "Enter the path to your .ovpn file: " ovpn_file
#     sudo cp "$ovpn_file" "$CONFIG_DIR/"
#     echo "Copied $ovpn_file to $CONFIG_DIR"
# }

# function connect_vpn() {
#     read -p "Enter the name of the .ovpn file (without extension): " ovpn_file
#     sudo openvpn --config "$CONFIG_DIR/$ovpn_file.ovpn" --daemon --log "$LOG_FILE"
#     echo "Connected to VPN using $ovpn_file.ovpn"
# }

# function disconnect_vpn() {
#     sudo killall openvpn
#     echo "Disconnected from VPN"
# }

# function start_openvpn_service() {
#     sudo systemctl start "$OPENVPN_SERVICE"
#     echo "OpenVPN service started"
# }

# function stop_openvpn_service() {
#     sudo systemctl stop "$OPENVPN_SERVICE"
#     echo "OpenVPN service stopped"
# }

# function status_openvpn_service() {
#     sudo systemctl status "$OPENVPN_SERVICE"
# }

# function open_vpn_gui() {
#     nm-connection-editor
# }

# function usage() {
#     echo "OpenVPN Management Script"
#     echo
#     echo "Usage: $0 [option]"
#     echo "Options:"
#     echo "  --install-terminal   Install OpenVPN terminal version"
#     echo "  --install-gui        Install OpenVPN GUI version"
#     echo "  --add-ovpn           Add an .ovpn file"
#     echo "  --connect            Connect to a VPN"
#     echo "  --disconnect         Disconnect from the VPN"
#     echo "  --start-service      Start OpenVPN service"
#     echo "  --stop-service       Stop OpenVPN service"
#     echo "  --status-service     Show OpenVPN service status"
#     echo "  --open-gui           Open OpenVPN GUI"
#     echo "  --help               Show this help message"
#     echo
# }

# if [ "$#" -eq 0 ]; then
#     usage
#     exit 1
# fi

# case "$1" in
#     --install-terminal)
#         install_openvpn_terminal
#         ;;
#     --install-gui)
#         install_openvpn_gui
#         ;;
#     --add-ovpn)
#         add_ovpn_file
#         ;;
#     --connect)
#         connect_vpn
#         ;;
#     --disconnect)
#         disconnect_vpn
#         ;;
#     --start-service)
#         start_openvpn_service
#         ;;
#     --stop-service)
#         stop_openvpn_service
#         ;;
#     --status-service)
#         status_openvpn_service
#         ;;
#     --open-gui)
#         open_vpn_gui
#         ;;
#     --help)
#         usage
#         ;;
#     *)
#         echo "Unknown option: $1"
#         usage
#         exit 1
#         ;;
# esac