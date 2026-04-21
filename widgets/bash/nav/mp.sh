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
# echo $SCRIPT_DIR
# source  "$SCRIPT_DIR/load-vars.sh"
# echo $ww
# echo $ww

# if [ -z ${widgets} ]; then source ~/.bashrc; fi
# source ~/.bashrc
subject=$1
shift
subject_path=$h/widgets/python/$subject.py
py_file=$h/widgets/python/file.py
py_folder=$h/widgets/python/
# echo $subject_path
if [ -f "$subject_path" ]; then
	$PY $subject_path $@
else
	echo ""
	echo "did you mean"
#    echo $subject_path
#    $PY $py_file -folder $py_folder + $subject -noext -label ";tApps" -prefix ";t" +close "75"
#    $p py-finder -percentage  + $@
#/bin/bash $ww/bash/py.sh $@
	$p py-finder -percentage  + $subject
fi

if [ -f "$h/vars/terminal/$Session_ID.sh" ]; then
	source "$h/vars/terminal/$Session_ID.sh"
fi