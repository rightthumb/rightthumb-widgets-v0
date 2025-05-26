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
test_nautilus=$(which nautilus)
test_dolphin=$(which dolphin)
test_gnome=$(which gnome-open)
test_konquerer=$(which konquerer)
test_thunar=$(which thunar)
test_nohup=$(which nohup)
test_gio=$(which gio)
test_krusader=$(which krusader)
test_pcmanfm=$(which pcmanfm)
test_xfe=$(which xfe)
test_nemo=$(which nemo)
test_spacefm=$(which spacefm)
test_caja=$(which caja)
test_deepin=$(which deepin)
test_polo=$(which polo)
if [ ${#test_nautilus} -gt 0 ]
then
	echo nautilus
	nautilus .
elif [ ${#test_dolphin} -gt 0 ]
then
	echo dolphin
	dolphin .
elif [ ${#test_gnome} -gt 0 ]
then
	echo gnome-open
	gnome-open .
elif [ ${#test_konquerer} -gt 0 ]
then
	echo konquerer
	konquerer .
elif [ ${#test_thunar} -gt 0 ]
then
	echo thunar
	thunar .
elif [ ${#test_nohup} -gt 0 ]
then
	echo nohup
	nohup .
elif [ ${#test_gio} -gt 0 ]
then
	echo gio
	gio .
elif [ ${#test_krusader} -gt 0 ]
then
	echo krusader
	krusader .
elif [ ${#test_pcmanfm} -gt 0 ]
then
	echo pcmanfm
	pcmanfm .
elif [ ${#test_dolphin} -gt 0 ]
then
	echo dolphin
	dolphin .
elif [ ${#test_xfe} -gt 0 ]
then
	echo xfe
	xfe .
elif [ ${#test_nemo} -gt 0 ]
then
	echo nemo
	nemo .
elif [ ${#test_spacefm} -gt 0 ]
then
	echo spacefm
	spacefm .
elif [ ${#test_caja} -gt 0 ]
then
	echo caja
	caja .
elif [ ${#test_deepin} -gt 0 ]
then
	echo deepin
	deepin .
elif [ ${#test_polo} -gt 0 ]
then
	echo polo
	polo .
else
	open .
fi