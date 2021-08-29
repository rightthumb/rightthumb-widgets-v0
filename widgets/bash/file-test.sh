#!/bin/bash
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