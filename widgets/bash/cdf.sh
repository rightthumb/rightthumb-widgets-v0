#!/bin/bash
# SCRIPT_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" &> /dev/null && pwd )"
# source  "$SCRIPT_DIR/load-vars.sh"
bookmarked_folder=$($PY $widgets/widgets/python/popFile.py -file $1)
echo $bookmarked_folder
cd $bookmarked_folder
exec bash
# pushd $bookmarked_folder
# pushd $bookmarked_folder > /dev/null
# export PWD=$bookmarked_folder
