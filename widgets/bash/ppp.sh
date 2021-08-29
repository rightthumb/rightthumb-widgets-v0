#!/bin/bash
# SCRIPT_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" &> /dev/null && pwd )"
# source  "$SCRIPT_DIR/load-vars.sh"
widgets="/mnt/d"
subject=$1
shift
subject_path=$widgets/widgets/python/$subject.py
py_file=$widgets/widgets/python/file.py
py_folder=$widgets/widgets/python/
if [ -f "$subject_path" ]; then
    $PY $subject_path $@
else
	echo "did you mean"
	$PY $py_file -folder $py_folder + $subject -noext -label ";tApps" -prefix ";t" +close 70
fi
 