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


if [ ! -d $HOME/.rt ]; then
    mkdir $HOME/.rt
fi



if [ ! -f $HOME/.rt/tool ]; then
    if [ ! -f $HOME/.rt/tool.sh ]; then
        wget "https://reph.us/tools/file.php?file=tool.sh" -O $HOME/.rt/tool.sh
        chmod 777 $HOME/.rt/tool.sh
    fi
    bash $HOME/.rt/tool.sh -dl
fi
if [ ! -f $HOME/.rt/tool ]; then
    echo "root tool?"
fi


# FILE=$HOME/.rt/.path
# FILE2=$HOME/.rt/.config.hash
# if [ ! -d $HOME/.rt ]; then
#     mkdir $HOME/.rt
# fi
# if [ -f $FILE ]; then
#     config_1=$( sed -n '1p' < "$FILE" )
#     config_2=$( sed -n '2p' < "$FILE" )
# else
#     config_1=""
#     config_2=""
# fi
# if [ ${#config_1} -gt 1 ]; then
#     export widgets=$config_1
# fi

if [ -f $HOME/.rt/tool ]; then
    $( $HOME/.rt/tool -bash.vars )
fi
# alias t7="echo works"
# echo "t7"
# if [ ${#PY} -lt 1 ]; then
#     export PY="/usr/bin/python3"
# fi

# if [ ${#widgets} -lt 1 ]; then
#     export widgets="/opt/RightThumb"
# fi


# if [ ${#code_editor} -lt 1 ]; then
#     export code_editor="nano"
# fi

# if [ ${#code_editor_pre} -lt 1 ]; then
#     export code_editor_pre=""
# fi

# if [ ${#code_editor_suff} -lt 1 ]; then
#     export code_editor_suff=""
# fi


if [ "${#XDG_CURRENT_DESKTOP}" -lt 2 -a "${#GDMSESSION}" -lt 2 ]; then
    export code_editor="nano"
fi

if [ "${#XDG_CURRENT_DESKTOP}" -lt 2 -a "${#GDMSESSION}" -lt 2 ]; then
    export code_editor_pre=""
fi

if [ "${#XDG_CURRENT_DESKTOP}" -lt 2 -a "${#GDMSESSION}" -lt 2 ]; then
    export code_editor_suff=""
fi




