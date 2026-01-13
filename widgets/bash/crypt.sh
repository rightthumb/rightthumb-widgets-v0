#!/bin/bash

fi=$1
entire="n"

if [ "$2" == "-d" ]; then
    $p fileBackup -open -f %fi%
    $p decrypt-docs -delete -f "$fi"
    $p secureFiles -delete -en -f "$fi"
    echo "done"
    exit 0
fi

if [ "$2" == "-delete" ]; then
    $p fileBackup -open -f %fi%
    $p secureFiles -delete -en -f "$fi"
    $p decrypt-docs -delete -f "$fi"
    echo "done"
    exit 0
fi
partial_function() {
    echo "PARTIAL selected"
    $p secureFiles -delete -en -f "$fi"
    $p decrypt-docs -f "$fi"
    echo "partial encryption configured"
}

entire_function() {
    echo "ENTIRE selected"
    $p decrypt-docs -delete -f "$fi"
    $p secureFiles -en -f "$fi"
    echo "entire-file encryption configured"
}

read -p "encrypt entire file? " entire
if [ "$entire" == "y" ]; then
    entire_function
else
    partial_function
fi
exit 0

