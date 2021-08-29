#!/bin/bash
# SCRIPT_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" &> /dev/null && pwd )"
# SCRIPT_DIR="${SCRIPT_DIR/bash\/nav/bash}"
# source  "$SCRIPT_DIR/load-vars.sh"

if [[ -n "$1" && "$1" != '-' ]]; then
  $PY $widgets/widgets/python/file_folder.py + $@
elif [ -n "$1" ]; then
	$PY $widgets/widgets/python/file_folder.py $@
else
  $PY $widgets/widgets/python/file_folder.py
fi
