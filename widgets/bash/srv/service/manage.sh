#!/bin/bash

LOGFILE="/var/log/service_manager.log"
SERVICEDIR="/etc/systemd/system"

function log {
	echo "$(date): $1" >> $LOGFILE
}

function add_service {
	read -p "Enter the name of the service: " service_name
	script_path="/usr/local/bin/$service_name.sh"

	# Create the shell script
	sudo nano "$script_path"
	sudo chmod +x "$script_path"

	# Create the systemd service file
	service_file="$SERVICEDIR/$service_name.service"
	sudo tee "$service_file" > /dev/null <<EOF
[Unit]
Description=$service_name Service
After=network.target

[Service]
ExecStart=$script_path

[Install]
WantedBy=default.target
EOF

	sudo systemctl enable "$service_name.service"
	log "Created and enabled service $service_name"
	echo "Service $service_name created and enabled."
}

function list_services {
	echo "Services created by this script:"
	grep 'Created and enabled service' $LOGFILE | awk -F 'service ' '{print $2}'
}

function manage_service {
	action=$1
	service_name=$2

	if [ -z "$service_name" ]; then
		echo "Please provide a service name."
		exit 1
	fi

	sudo systemctl $action "$service_name.service"

	if [ $? -eq 0 ]; then
		echo "Service $service_name $actioned successfully."
		log "Service $service_name $actioned successfully."
	else
		echo "Failed to $action service $service_name."
	fi
}

case $1 in
	-a|--add)
		add_service
		;;
	-l|--list)
		list_services
		;;
	-start)
		manage_service start $2
		;;
	-stop)
		manage_service stop $2
		;;
	-restart)
		manage_service restart $2
		;;
	*)
		echo "Usage: $0 {-a|--add|-l|--list|-start|-stop|-restart} [service_name]"
		;;
esac