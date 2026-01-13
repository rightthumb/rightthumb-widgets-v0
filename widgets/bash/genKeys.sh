#!/bin/bash

# Check if 'expect' is installed
if ! command -v expect &>/dev/null; then
	echo "Expect not found. Installing..."
	sudo apt-get update
	sudo apt-get install -y expect
fi

# Check and delete existing default SSH key files if they exist
rm -rf ~/.ssh
# if [ -e "$HOME/.ssh/id_rsa" ]; then
# 	rm -f "$HOME/.ssh/id_rsa"
# fi

if [ -e "$HOME/.ssh/id_rsa.pub" ]; then
	rm -f "$HOME/.ssh/id_rsa.pub"
fi

# Now run the expect script
/usr/bin/expect << EOF

set timeout 20

spawn ssh-keygen -t rsa

# Keep pressing Enter for all questions or exit if the process ends
expect {
	":" {
		send "\r"
		exp_continue
	}
	eof {
		exit
	}
}

EOF