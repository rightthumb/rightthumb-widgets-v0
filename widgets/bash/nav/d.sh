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

if [[ -n "$1" && "$1" != '-' ]]; then
  $PY $widgets/widgets/python/file_folder.py + $@
elif [ -n "$1" ]; then
	$PY $widgets/widgets/python/file_folder.py $@
else
  $PY $widgets/widgets/python/file_folder.py
fi


