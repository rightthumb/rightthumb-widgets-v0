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
# echo $widgets
# echo $widgets


if [ -z ${widgets} ]; then source ~/.bashrc; fi
# source ~/.bashrc
subject=$1
shift
subject_path=$widgets/widgets/python/$subject.py
py_file=$widgets/widgets/python/file.py
py_folder=$widgets/widgets/python/
if [ -f "$subject_path" ]; then
    $PY $subject_path $@
else
    echo "did you mean"
    echo $subject_path
    $PY $py_file -folder $py_folder + $subject -noext -label ";tApps" -prefix ";t" +close "75"
fi


