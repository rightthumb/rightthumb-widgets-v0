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

# replace=$1
# one=$(  echo  | sed -e "s/12345678/${replace}/g"  )
# one="'echo -ne \"\033]0; $1 \007\"'"
# two='PROMPT_COMMAND='$one
t=$1;PROMPT_COMMAND='echo -en "\033]0; $(echo $t) \a"'

# echo $two | bash
# $two
# exec "$two"
# exec( $two )