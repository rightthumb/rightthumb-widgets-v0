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

# https://stedolan.github.io/jq/
# SCRIPT_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" &> /dev/null && pwd )"
# source  "$SCRIPT_DIR/load-vars.sh"
if ! which python3 > /dev/null; then
	echo -e "python3 not found! Install? (y/n) \c"
	read
	if "$REPLY" = "y"; then
		apt-get install python3
	fi
fi
# apt-get install python3
[ ! -d $widgets ] && mkdir $widgets
[ ! -d $widgets/tech ] && mkdir $widgets/tech
[ ! -d $widgets/widgets ] && mkdir $widgets/widgets
[ ! -d $widgets/widgets/python ] && mkdir $widgets/widgets/python
[ ! -d $widgets/widgets/python/src ] && mkdir $widgets/widgets/python/src
[ ! -d $widgets/widgets/python ] && mkdir $widgets/widgets/python
chmod -R 777 $widgets
cp -r  ../python/_rightThumb/ ./
chmod -R 777 ../../
$PY ./shCleanSimple.py
# widgets="/opt/RightThumb"
subject_path=$widgets/widgets
cp -rf ../bash $subject_path/
cp -rf ../python/ $subject_path/python/src/
cp -rf ../batch $subject_path/
cp -rf ../documentation $subject_path/
cp -rf ../javascript $subject_path/
cp -rf ../library $subject_path/
cp -rf ../php $subject_path/
cp -rf ../remote $subject_path/
cp -rf ../vbs $subject_path/
cp -rf ../powershell $subject_path/
			
			
			
			
			
			
			
# ./aliasGen.sh >> $HOME/.bashrc
echo "./auto_setup.sh --DEFAULT"
echo "./auto_setup.sh --FORCE"
echo "./auto_setup.sh --SUDO"