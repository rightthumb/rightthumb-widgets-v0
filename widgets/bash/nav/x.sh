#!/bin/bash

# ## {R2D2919B742E} ##
# ###########################################################################
# What if magic existed?
# What if a place existed where your every thought and dream come to life.
# There is only one catch: it has to be written down.
# Such a place exists, it is called programming.
#    - Scott Taylor Reph, RightThumb.com
# ###########################################################################
# ## {C3P0D40fAe8B} ##

# SCRIPT_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" &> /dev/null && pwd )"
# SCRIPT_DIR="${SCRIPT_DIR/bash\/nav/bash}"
# source  "$SCRIPT_DIR/load-vars.sh"
who=$( whoami )
unixID7=$( sed -n '7p' < $wprofile/config/.unix_id )
history_folder="$widgets/widgets/bash/history"
history_file="$history_folder/RT-HISTORY-$unixID7-$who.txt"
bashrc_folder="$widgets/widgets/bash/bashrc"
bashrc_file="$bashrc_folder/RT-BASHRC-$unixID7-$who.txt"
widgets="$widgets"
thisHistory=$HOME/.bash_history
thisBashrc=$HOME/.bashrc
p="python $widgets/widgets/bash/nav/p.sh"
py_app=$widgets/widgets/python/autoBackup.py
p="bash $widgets/widgets/bash/nav/p.sh"
if [[ ! -e $history_folder ]]; then
	mkdir $history_folder
fi
if [[ ! -e $bashrc_folder ]]; then
	mkdir $bashrc_folder
fi
$p fileBackup -i $history_file
$p fileBackup -i $history_file
cat $thisHistory > $history_file
cat $thisBashrc > $bashrc_file
if [[ -n "$1"  ]]
then
	$p  autoBackup -ago $1
else
	$p  autoBackup -ago 1d
fi
exit
terminal_name=$TERM
if [[ ! -e $terminal_name ]]; then
	read -p 'close all terminals?: ' shouldClose
	if [[ "$shouldClose" == "y" ]]; then
		echo "YES, closing"
		terminal_name_path="$wprofile/config/.terminal"
		terminal_name=$( cat $terminal_name_path )
		echo "killall $terminal_name"
		killall $terminal_name
	else
		echo "NOT, closing"
	fi
	
else
	echo "EXAMPLE:"
	echo "         myterminal"
	echo "         or"
	echo "         ( pstree to find terminal name )"
	echo "         register_terminal xfce4-terminal"
fi