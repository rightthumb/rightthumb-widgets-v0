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



if [ -f $HOME/.rt/profile/vars/config.sh ]; then
    source $HOME/.rt/profile/vars/config.sh
fi

if [ -f $HOME/.rt/profile/vars/personal.sh ]; then
    source $HOME/.rt/profile/vars/personal.sh
fi





if [ "${#XDG_CURRENT_DESKTOP}" -lt 2 -a "${#GDMSESSION}" -lt 2 ]; then
    export code_editor="nano"
fi

if [ "${#XDG_CURRENT_DESKTOP}" -lt 2 -a "${#GDMSESSION}" -lt 2 ]; then
    export code_editor_pre=""
fi

if [ "${#XDG_CURRENT_DESKTOP}" -lt 2 -a "${#GDMSESSION}" -lt 2 ]; then
    export code_editor_suff=""
fi




