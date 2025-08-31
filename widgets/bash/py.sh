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

source $HOME/.bashrc


#!/bin/bash

stuff() {
    if [ -e "$1" ]
    then
        python3 "$@"
    else
        # $p py-finder  + $@ -percentage
        # cat 0-index.list | p line --c + "$@" | p pipe-cleaner -ext
        $p file -prefix -noext --c -folder "$widgets"/widgets/python + "$@"
    fi
}

if [ -z "$1" ]
then
    python3
else
    stuff "$@"
fi




# if [ $# -eq 0 ]
#     then
#         python3
#     else
#          $p py-finder  + $@ -percentage
# fi

