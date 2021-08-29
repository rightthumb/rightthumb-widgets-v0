#!/bin/bash
# SCRIPT_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" &> /dev/null && pwd )"
# SCRIPT_DIR="${SCRIPT_DIR/bash\/nav/bash}"
# source  "$SCRIPT_DIR/load-vars.sh"
# code_editor=$( cat "/opt/RightThumb/.editor" )
subject=$1
subject_path=$widgets/widgets/python/_rightThumb/_$subject/__init__.py
p="bash $widgets/widgets/bash/nav/p.sh"
if [[ ! -e $widgets/widgets/python/_rightThumb/_$subject ]]; then
    mkdir $widgets/widgets/python/_rightThumb/_$subject
    echo "directory created"
elif [[ ! -d $dir ]]; then
    echo "directory exists"
fi
$p fileBackup -i $subject_path
if [ "$code_editor_pre" = "" -a "$code_editor_suff" = "" ]; then
    echo 1
    $code_editor $subject_path
else
    if [ "$code_editor_pre" != "" -a "$code_editor_suff" != "" ]; then
        echo 2
        $code_editor_pre $code_editor $subject_path $code_editor_suff >/dev/null 2>&1
    else
        if [ "$code_editor_pre" != "" ]; then
            echo 3
            $code_editor_pre $code_editor $subject_path
        else
            echo 4
            $code_editor $subject_path $code_editor_suff >/dev/null 2>&1
        fi
    fi
fi
# $code_editor_pre $code_editor $subject_path $code_editor_suff>/dev/null 2>&1
