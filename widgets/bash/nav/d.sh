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




# Check if the first argument ($1) is non-empty (-n "$1"),
# and does NOT equal '-' or start with a dash (i.e., it's a valid filename or folder name, not a flag)
if [[ -n "$1" && "$1" != '-' && $1 != -* ]]; then
	# If so, run file_folder.py and prepend '+' to the arguments
	$PY $widgets/widgets/python/file_folder.py + $@
	
# If $1 is non-empty but *is* '-' or starts with a dash (i.e., it's a flag like -r or --help)
elif [ -n "$1" ]; then
	# Run file_folder.py with arguments as-is (likely passing flags)
	$PY $widgets/widgets/python/file_folder.py $@

# If no arguments were passed at all
else
	# Run file_folder.py with no arguments
	$PY $widgets/widgets/python/file_folder.py
fi