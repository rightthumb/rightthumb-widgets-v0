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
bookmarked_folder=$($PY $widgets/widgets/python/b.py -alias $1)
echo $bookmarked_folder
cd $bookmarked_folder
$SHELL
#exec bash
# pushd $bookmarked_folder
# pushd $bookmarked_folder > /dev/null
# export PWD=$bookmarked_folder