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
np_0=$widgets/widgets/bash/newpage/0.htm
np_1=$widgets/widgets/bash/newpage/1.htm
np_2=$widgets/widgets/bash/newpage/2.htm
if [[ "$*" == *--0* ]]
  then
      cat $np_0
  else
    
    if [[ "$*" == *--1* ]]
      then
          cat $np_1
      else
        if [[ "$*" == *--2* ]]
          then
              cat $np_2
          else
              echo "missing --0"
            echo "missing --1"
            echo "missing --2"
        fi
    fi
fi


