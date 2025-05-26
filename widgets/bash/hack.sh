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
subject_path=$widgets/techApps/hack_profile
if [[ ! -e $subject_path ]]; then
    mkdir $subject_path
    echo "CREATED $subject_path "
elif [[ ! -d $subject_path ]]; then
    echo "EXISTS $subject_path "
fi
chromium-browser --no-sandbox --profile-directory=Default --disable-web-security --disable-site-isolation-trials --allow-running-insecure-content --user-data-dir=$subject_path "http://www.google.com/" 
# sudo chromium-browser --no-sandbox --profile-directory=Default --disable-web-security --disable-site-isolation-trials --allow-running-insecure-content --user-data-dir=$subject_path "http://www.google.com/" 
# javascript:{ var script = document.createElement('script');script.type = 'text/javascript'; if (location.protocol === 'https:') { script.src = 'https://reph.us/tools/tool.js'; } else { script.src = 'http://reph.us/tools/tool.js'; } document.head.appendChild(script);}


