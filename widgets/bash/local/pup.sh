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


srv=$1
file=$2
if [ $srv="1" ]; then
   srv="hoth"
fi
if [ $srv="h" ]; then
   srv="hoth"
fi
if [ $srv="2" ]; then
   srv="bespin"
fi
if [ $srv="b" ]; then
   srv="bespin"
fi
if [ $srv="3" ]; then
   srv="mandalore"
fi
if [ $srv="m" ]; then
   srv="mandalore"
fi
toSRV=$srv.eyeformeta.com

echo scp "/mnt/d/.rightthumb-widgets/widgets/python/$file.py" root@$toSRV:/opt/rightthumb-widgets-v0/widgets/python/