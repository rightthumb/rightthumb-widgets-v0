#!/bin/bash

# Check if the domain argument is provided
if [ -z "$1" ]; then
	echo "Usage: ./script_name [domain] [username]"
	exit 1
fi

domain=$1

# Check if the username argument is provided, otherwise default to "scott"
if [ -z "$2" ]; then
	ssh_user="scott"
else
	ssh_user=$2
fi

# Convert shortcuts to usernames if provided
case "$ssh_user" in
	s)
		ssh_user="scott"
		;;
	r)
		ssh_user="root"
		;;
	a)
		ssh_user="admin"
		;;
esac

# For debugging purposes, we're echoing the command to see it
echo ssh-copy-id -i ~/.ssh/id_rsa.pub $ssh_user@$domain.m-eta.app
ssh-copy-id -i ~/.ssh/id_rsa.pub $ssh_user@$domain.m-eta.app
