#!/bin/bash
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
