#!/bin/bash
# SCRIPT_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" &> /dev/null && pwd )"
# SCRIPT_DIR="${SCRIPT_DIR/bash\/dt/bash}"
# source  "$SCRIPT_DIR/load-vars.sh"
$widgets/widgets/bash/dt/vnc_watch.sh> /dev/null 2>&1 & 
vncserver-start
