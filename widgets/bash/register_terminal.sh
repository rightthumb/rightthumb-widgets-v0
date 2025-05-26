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
# source  "$SCRIPT_DIR/load-vars.sh"
terminal_name_path="$wprofile/config/.terminal"
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


# x='test'
# if [ -z ${TERM+x} ]; then TERM=dumb; fi


