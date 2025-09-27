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
# SCRIPT_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" &> /dev/null && pwd )"
# SCRIPT_DIR="${SCRIPT_DIR/bash\/nav/bash}"
# source  "$SCRIPT_DIR/load-vars.sh"
# code_editor=$( cat "/opt/RightThumb/.editor" )
subject=$1
subject_path=$subject
# subject_path=./subject
p="bash $widgets/widgets/bash/nav/p.sh"
$p file-open -f $subject_path -backup
# if [ "$code_editor_pre" = "" -a "$code_editor_suff" = "" ]; then
#     echo 1
#     $code_editor $subject_path
# else
#     if [ "$code_editor_pre" != "" -a "$code_editor_suff" != "" ]; then
#         echo 2
#         $code_editor_pre $code_editor $subject_path $code_editor_suff >/dev/null 2>&1
#     else
#         if [ "$code_editor_pre" != "" ]; then
#             echo 3
#             $code_editor_pre $code_editor $subject_path
#         else
#             echo 4
#             $code_editor $subject_path $code_editor_suff >/dev/null 2>&1
#         fi
#     fi
# fi
# $code_editor_pre $code_editor $subject_path $code_editor_suff>/dev/null 2>&1