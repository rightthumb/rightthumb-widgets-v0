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
# https://imdbpy.github.io/downloads/
set -e
function run_command(  ) {
    EXIT_CODE=0
    eval "$1 || EXIT_CODE=\$?"
    # ret=$?
    if [ $EXIT_CODE -ne 0 ]; then
            echo ""
            echo "   FAIL    $1 "
            echo ""
    else
            echo ""
            echo "   SUCCESS $1 "
            echo ""
    fi
}
# run_command ""
if [[ "$*" == *--tools*reg* ]]
then
    run_command "sudo apt-get update"
    run_command "sudo apt-get upgrade"
    # http://manpages.ubuntu.com/manpages/xenial/man1/regshell.1.html
    run_command "sudo apt install registry-tools"
    
else
    echo "./auto_setup.sh --tools reg # missing"
fi
if [[ "$*" == *--DEFAULT* ]]
  then
    # python and pip3
    run_command "sudo emoji update"
    run_command "sudo apt-get upgrade"
    run_command "sudo apt install python3 -y"
    run_command "sudo apt install python3-pip3 -y"
    run_command "sudo apt-get update python3 -y"
    run_command "sudo apt update python3-pip3 -y"
    run_command "sudo -H pip3 install --upgrade pip3 -y"
    run_command "pip3 install --upgrade setuptools pip"
    # # applications:
    run_command "$PY -m pip install simplejson"
    run_command "$PY -m pip install binaryornot"
    run_command "$PY -m pip install cssselect"
    run_command "$PY -m pip install colorama"
    run_command "$PY -m pip install pymysql"
    run_command "$PY -m pip install Crypto"
    run_command "$PY -m pip install tzlocal"
    run_command "$PY -m pip install termcolor"
    run_command "$PY -m pip install datetime"
    run_command "$PY -m pip install pyAesCrypt"
    run_command "$PY -m pip install zipfile36"
    run_command "$PY -m pip install zipfile"
    run_command "$PY -m pip install tarfile"
    run_command "$PY -m pip install wget"
    
    run_command "$PY -m pip install pywin32"
    # ?
    run_command "$PY -m pip install stickytape"
    run_command "$PY -m pip install dnspython"
    run_command "$PY -m pip install pymongo"
    run_command "$PY -m pip install arrow"
    run_command "$PY -m pip install mycloudhome"
    
    run_command "$PY -m pip install pyperclip"
    run_command "$PY -m pip install pyAesCrypt"
    run_command "$PY -m pip install pycrypto"
    run_command "$PY -m pip install arrow"
    run_command "$PY -m pip install pymysql"
    run_command "$PY -m pip install sshtunnel"
    run_command "$PY -m pip install gtts"
    run_command "$PY -m pip install emoji"
    
    run_command "$PY -m pip install pyreadline"
    # run_command "$PY -m pip install icmplib"
    # run_command "$PY -m pip install pyping"
    run_command "$PY -m pip install ping"
    run_command "$PY -m pip install netaddr"
    run_command "$PY -m pip install getmac"
    run_command "$PY -m pip install native_web_app"
    # run_command "$PY -m pip install mac_vendor_lookup"
    # run_command "$PY -m pip install scapy"
    # ?
    
    run_command "$PY -m pip install psutil"
    run_command "sudo apt install fonts-noto-color-emoji"
    # run_command "sudo apt install mpg321 -y"
    
    # run_command "$PY -m pip install stardate-goddard"
    # run_command "sudo apt-get install python3-pyperclip -y"
    run_command "sudo apt-get install python3-dateutil -y"
    run_command "sudo apt-get install python3-pyodbc -y"
    run_command "sudo apt-get install python3-paramiko -y"
    run_command "sudo apt-get install python3-pandas -y"
    run_command "sudo apt-get install python3-openssl -y"
    run_command "sudo apt-get install python3-sqlite3 -y"
    run_command "sudo apt install xclip xsel"
    # run_command "sudo apt-get install unzip -y"
    # run_command "sudo apt-get install dnsutil -y"
    # run_command "sudo apt-get install nmap -y"
    # run_command "sudo apt-get install at -y"
    # run_command "sudo apt-get install chromium-browser -y"
    # # run_command "sudo apt install chromium-browser -y"
    # run_command "sudo apt install openssh-server nano -y"
    # run_command "sudo snap install powershell --classic"
    
    # # python:
    # run_command "pip3 install binaryornot --no-input -q"
    # run_command "pip3 install simplejson --no-input -q"
    # run_command "pip3 install lxml --no-input -q"
    # run_command "pip3 install cssselect --no-input -q"
    # run_command "pip3 install arrow --no-input -q"
    # run_command "pip3 install colorama --no-input -q"
    
    # run_command "pip3 install sshtunnel --no-input -q"
    # run_command "pip3 install stat --no-input -q"
    # run_command "pip3 install stickytape --no-input -q"
    # run_command "sudo apt-get install python3-sshtunnel -y"
    # run_command "pip3 install pymysql --no-input -q"
    # run_command "pip3 install Crypto --no-input -q"
    # run_command "pip3 install pycrypto --no-input -q"
    # run_command "sudo apt-get install python3-dateutil -y"
    # run_command "sudo apt-get install python3-pyodbc -y"
    # run_command "sudo apt-get install python3-paramiko -y"
    # run_command "sudo apt-get install python3-pandas -y"
    # run_command "sudo apt-get install p7zip-full -y"
    # run_command "pip3 install tzlocal --no-input -q"
    # run_command "pip3 install pytz --no-input -q"
    # run_command "pip3 install dnspython --no-input -q"
    # run_command "sudo apt-get install python3-dnspython -y"
    # run_command "pip3 install pymongo --no-input -q"
    # run_command "sudo apt-get install python3-openssl -y"
else
    echo "./auto_setup.sh --DEFAULT # missing"
fi
# run_command ""
# if [[ "$*" == *--FORCE* ]]
# then
#     # auto pip
    
    # run_command "pip3 install nltk --no-input -q"
    # run_command "pip3 install csv --no-input -q"
    # run_command "pip3 install webbrowser --no-input -q"
    # run_command "pip3 install termcolor --no-input -q"
    # run_command "pip3 install threading --no-input -q"
    # run_command "pip3 install Crypto --no-input -q"
    # run_command "pip3 install pathlib --no-input -q"
    # run_command "pip3 install pickle --no-input -q"
    # run_command "pip3 install selenium --no-input -q"
    # run_command "pip3 install tkinter --no-input -q"
    # run_command "pip3 install webbrowser --no-input -q"
    # run_command "pip3 install databank --no-input -q"
    # run_command "pip3 install math --no-input -q"
    # run_command "pip3 install bs4 --no-input -q"
    # run_command "pip3 install hashlib --no-input -q"
    # run_command "pip3 install socket --no-input -q"
    # run_command "pip3 install urllib --no-input -q"
    # run_command "pip3 install uuid --no-input -q"
    # run_command "pip3 install base64 --no-input -q"
    # run_command "pip3 install operator --no-input -q"
    # run_command "pip3 install random --no-input -q"
    # run_command "pip3 install sqlite3 --no-input -q"
    # run_command "pip3 install re --no-input -q"
    # run_command "pip3 install glob --no-input -q"
    # run_command "pip3 install subprocess --no-input -q"
    # run_command "pip3 install platform --no-input -q"
    # run_command "pip3 install simplejson --no-input -q"
    # run_command "pip3 install shutil --no-input -q"
    # run_command "pip3 install lxml --no-input -q"
    # run_command "pip3 install cssselect --no-input -q"
    # run_command "pip3 install requests --no-input -q"
    # run_command "pip3 install datetime --no-input -q"
    # run_command "pip3 install time --no-input -q"
    # run_command "pip3 install wmi --no-input -q"
    # # auto apt
    # run_command "sudo apt-get install python3-nltk -y"
    # run_command "sudo apt-get install python3-csv -y"
    # run_command "sudo apt-get install python3-webbrowser -y"
    # run_command "sudo apt-get install python3-termcolor -y"
    # run_command "sudo apt-get install python3-threading -y"
    # run_command "sudo apt-get install python3-Crypto -y"
    # run_command "sudo apt-get install python3-pathlib -y"
    # run_command "sudo apt-get install python3-pickle -y"
    # run_command "sudo apt-get install python3-selenium -y"
    # run_command "sudo apt-get install python3-tkinter -y"
    # run_command "sudo apt-get install python3-webbrowser -y"
    # run_command "sudo apt-get install python3-databank -y"
    # run_command "sudo apt-get install python3-math -y"
    # run_command "sudo apt-get install python3-bs4 -y"
    # run_command "sudo apt-get install python3-hashlib -y"
    # run_command "sudo apt-get install python3-socket -y"
    # run_command "sudo apt-get install python3-urllib -y"
    # run_command "sudo apt-get install python3-uuid -y"
    # run_command "sudo apt-get install python3-base64 -y"
    # run_command "sudo apt-get install python3-operator -y"
    # run_command "sudo apt-get install python3-random -y"
    # run_command "sudo apt-get install python3-sqlite3 -y"
    # run_command "sudo apt-get install python3-re -y"
    # run_command "sudo apt-get install python3-glob -y"
    # run_command "sudo apt-get install python3-subprocess -y"
    # run_command "sudo apt-get install python3-platform -y"
    # run_command "sudo apt-get install python3-simplejson -y"
    # run_command "sudo apt-get install python3-shutil -y"
    # run_command "sudo apt-get install python3-lxml -y"
    # run_command "sudo apt-get install python3-cssselect -y"
    # run_command "sudo apt-get install python3-requests -y"
    # run_command "sudo apt-get install python3-datetime -y"
    # run_command "sudo apt-get install python3-time -y"
# else
#     echo "./auto_setup.sh --FORCE # missing"
# fi
if [[ "$*" == *--SUDO* ]]
then
    run_command "sudo $PY -m pip install simplejson"
    run_command "sudo $PY -m pip install binaryornot"
    run_command "sudo $PY -m pip install cssselect"
    run_command "sudo $PY -m pip install arrow"
    run_command "sudo $PY -m pip install colorama"
    run_command "sudo $PY -m pip install stickytape"
    run_command "sudo $PY -m pip install pymysql"
    run_command "sudo $PY -m pip install Crypto"
    run_command "sudo $PY -m pip install tzlocal"
    run_command "sudo $PY -m pip install dnspython"
    run_command "sudo $PY -m pip install pymongo"
    run_command "sudo $PY -m pip install termcolor"
    run_command "sudo $PY -m pip install datetime"
    # run_command "sudo apt-get install youtube-dl -y"
    # run_command "sudo pip3 install binaryornot --no-input -q"
    # run_command "sudo pip3 install simplejson --no-input -q"
    # run_command "sudo pip3 install lxml --no-input -q"
    # run_command "sudo pip3 install cssselect --no-input -q"
    # run_command "sudo pip3 install arrow --no-input -q"
    # run_command "sudo pip3 install colorama --no-input -q"
    # run_command "sudo pip3 install sshtunnel --no-input -q"
    # run_command "sudo pip3 install stat --no-input -q"
    # run_command "sudo pip3 install stickytape --no-input -q"
    # run_command "sudo pip3 install pymysql --no-input -q"
    # run_command "sudo pip3 install Crypto --no-input -q"
    # run_command "sudo pip3 install pycrypto --no-input -q"
    # run_command "sudo pip3 install tzlocal --no-input -q"
    # run_command "sudo pip3 install pytz --no-input -q"
    # run_command "sudo pip3 install nltk --no-input -q"
    # run_command "sudo pip3 install csv --no-input -q"
    # run_command "sudo pip3 install webbrowser --no-input -q"
    # run_command "sudo pip3 install termcolor --no-input -q"
    # run_command "sudo pip3 install threading --no-input -q"
    # run_command "sudo pip3 install Crypto --no-input -q"
    # run_command "sudo pip3 install pathlib --no-input -q"
    # run_command "sudo pip3 install pickle --no-input -q"
    # run_command "sudo pip3 install selenium --no-input -q"
    # run_command "sudo pip3 install tkinter --no-input -q"
    # run_command "sudo pip3 install webbrowser --no-input -q"
    # run_command "sudo pip3 install databank --no-input -q"
    # run_command "sudo pip3 install math --no-input -q"
    # run_command "sudo pip3 install bs4 --no-input -q"
    # run_command "sudo pip3 install hashlib --no-input -q"
    # run_command "sudo pip3 install socket --no-input -q"
    # run_command "sudo pip3 install urllib --no-input -q"
    # run_command "sudo pip3 install uuid --no-input -q"
    # run_command "sudo pip3 install base64 --no-input -q"
    # run_command "sudo pip3 install operator --no-input -q"
    # run_command "sudo pip3 install random --no-input -q"
    # run_command "sudo pip3 install sqlite3 --no-input -q"
    # run_command "sudo pip3 install re --no-input -q"
    # run_command "sudo pip3 install glob --no-input -q"
    # run_command "sudo pip3 install subprocess --no-input -q"
    # run_command "sudo pip3 install platform --no-input -q"
    # run_command "sudo pip3 install simplejson --no-input -q"
    # run_command "sudo pip3 install shutil --no-input -q"
    # run_command "sudo pip3 install lxml --no-input -q"
    # run_command "sudo pip3 install cssselect --no-input -q"
    # run_command "sudo pip3 install requests --no-input -q"
    # run_command "sudo pip3 install datetime --no-input -q"
    # run_command "sudo pip3 install time --no-input -q"
    # run_command "sudo pip3 install wmi --no-input -q"
else
    echo "./auto_setup.sh --SUDO # missing"
fi
if [[ "$*" == *--FIX_CLOUD* ]]
then
    run_command "pip3 uninstall dnspython"
    run_command "pip3 install dnspython"
    run_command "pip3 uninstall sshtunnel"
    run_command "pip3 install sshtunnel"
    
    run_command "pip3 uninstall pymysql"
    run_command "pip3 install pymysql"
    # run_command "XXXX"
else
    echo "./auto_setup.sh --FIX_CLOUD # missing"
fi

