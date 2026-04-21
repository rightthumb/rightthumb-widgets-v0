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

# while read p; do
#   echo "$p"
# done <file-in.txt
# if ! which python3 > /dev/null; then
#     echo "A"
# fi
# if python3 -c "import math" > /dev/null; then
#     echo "B"
# fi
# test=$(python3 -c "try:import math99;except Exception as e:print(x);") > /dev/null
# if $test > /dev/null; then
#     echo "C"
# fi
test=$( ./py-imports  math )
echo $test

