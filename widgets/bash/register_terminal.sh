#!/bin/bash
# SCRIPT_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" &> /dev/null && pwd )"
# source  "$SCRIPT_DIR/load-vars.sh"
terminal_name_path="$widgets/tech/hosts/$(hostname)/config/.terminal"
if [[ ! -e $terminal_name_path ]]; then
	touch $terminal_name_path
fi
# terminal_name=$( cat $terminal_name_path )
if [[ -n "$1" ]]
then
	echo "$1" > $terminal_name_path
else
	echo "EXAMPLE:"
	echo "         register_terminal xfce4-terminal"
fi
