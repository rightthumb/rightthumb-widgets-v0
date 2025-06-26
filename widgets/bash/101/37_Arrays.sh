#!/bin/bash

# Array pretending to be a Pythonic dictionary
ARRAY=( "cow:moo"
		"dinosaur:roar"
		"bird:chirp"
		"bash:rock" )

for animal in "${ARRAY[@]}" ; do
	KEY="${animal%%:*}"
	VALUE="${animal##*:}"
	printf "%s likes to %s.\n" "$KEY" "$VALUE"
done

printf "%s is an extinct animal which likes to %s\n" "${ARRAY[1]%%:*}" "${ARRAY[1]##*:}







# Another way to do the same thing

declare -A hashmap
hashmap["key"]="value"
hashmap["key2"]="value2"
echo "${hashmap["key"]}"
for key in ${!hashmap[@]}; do echo $key; done
for value in ${hashmap[@]}; do echo $value; done
echo hashmap has ${#hashmap[@]} elements


## this

declare -A hashmap
hashmap["key1"]="value1"
hashmap["key2"]="value2"
echo "${hashmap["key"]}"
for key in ${!hashmap[@]}; do
echo "${key} ${hashmap[$key]}"
done