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
# # source  "$SCRIPT_DIR/load-vars.sh"
# echo $PY $widgets/widgets/python/m.py -alias $1
$PY $widgets/widgets/python/m.py -alias $*

alias ref="source $HOME/.bashrc"

echo '> ref   to refresh .bashrc'
echo 'ref'

# if [ -f "$HOME/.m" ]; then
# 		echo source "$HOME/.bashrc"
# else
# 		echo "Instant Availability"
# 		echo "  touch ~/.m"
# fi