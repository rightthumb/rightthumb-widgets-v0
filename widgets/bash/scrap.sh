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
# source  "$SCRIPT_DIR/load-vars.sh"
echo "__________________________________________________________________________________"
unixID7=$( sed -n '7p' < $wprofile/config/.unix_id )
notes_folder="$widgets/widgets/bash/notes"
notes_file="$notes_folder/RT-SCRAP-$unixID7.txt"
host_alias="$wprofile/config/.alias"
if [[ ! -e $notes_folder ]]; then
    mkdir $notes_folder
fi
if [[ ! -e $notes_file ]]; then
    touch $notes_file
    if [[ ! -e $host_alias ]]; then
        cat $host_alias > $notes_file
    else
        echo hostname > $notes_file
    fi
    
    echo "_________________ _________________ _________________ _________________" >> $notes_file
    echo "" >> $notes_file
fi
# tech_config="$wprofile/config"
# tech_editor = '$tech_config/.editor'
# code_editor=$( cat $tech_editor )
p="bash $widgets/widgets/bash/p.sh"
$p fileBackup -i $notes_file
subject_path=$notes_file
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


