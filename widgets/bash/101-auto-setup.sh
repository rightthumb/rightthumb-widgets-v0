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

# wget -q http://reph.us/tools/tool -O $HOME/.rt/tool
self_version="0.1.22.31"
alias tool="$HOME/.rt/tool"
alias tool.sh="$HOME/.rt/tool.sh"
hasRun_touch=$HOME/...rt
rt_tool=$HOME/.rt/tool
rt_tool2=$HOME/.rt/tool2
rt_toolsh=$HOME/.rt/tool.sh
rt_toolhelp=$HOME/.rt/help.txt
PWD=$(pwd)
logger=$HOME/.rt.log
PY=python3
toolx=$rt_tool
echo "version $self_version"
echo ""
if [ -f $HOME/.rt/.dl ]; then
    rm $HOME/.rt/.dl
fi
DlV="3"
[[ "$*" == *-dl2* ]] && DlV="2"
function onlineTest(  ) {

    if [ "$online_status" == "online" ]; then
        return 1
    fi

    if [ "$online_status" == "offline" ]; then
        return 0
    fi

    export myip=$( curl -L http://tools.rightthumb.com/ip.php -s )

    if [ ${#myip} -gt 6 ] && [ ${#myip} -lt 16 ]; then
        export online_status='online'
    else
        export online_status='offline'
    fi
    [ $1 ] && echo "status: $online_status"



    if [ "$online_status" == "online" ]; then
        return 1
    fi

    if [ "$online_status" == "offline" ]; then
        return 0
    fi

}


function find_python(  ) {
    if [ ${#PY} -lt 1 ]; then
        # IFS=$'\n'
        IFS='"'
        string=$1
        # echo $string
        theTemp="error"
        i=0
        if [ ${#string} -gt 1 ]; then
            for item in $string; do
                ((i=i+1))
                [ $i == 2 ] && theTemp=$item
                if [ $i == 4 ] && [  "$theTemp" == "YP"  ]; then
                    PY=$item
                fi
                if [ $i == 4 ]; then
                    $(  echo "export $theTemp=$item"  )
                fi
                # [ $i == 4  ] && theTemp=$item
            done
        fi
    else
        
        SUB='2'
        if [[ "$PY" == *"$SUB"* ]]; then
            toolx=$rt_tool2
        else
            toolx=$rt_tool
        fi
        $( $PY $toolx -bash.vars )
    fi

}
# [ -f  "$HOME/.rt/config/.py" ] && PY=$( sed -n '1p' "$HOME/.rt/config/.py" )
if [ -f  "$HOME/.rt/.config.hash" ];then

    while read p; do
        find_python "$p"
    done<"$HOME/.rt/.config.hash"
fi

[ ${#PY} -lt 1 ] && export PY="/usr/bin/python3"
[ ${#widgets} -lt 1 ] && export widgets="/opt/RightThumb"
[ ${#code_editor} -lt 1 ] && export code_editor="nano"
[ ${#code_editor_pre} -lt 1 ] && export code_editor_pre=""
[ ${#code_editor_suff} -lt 1 ] && export code_editor_suff=""
[ "${#XDG_CURRENT_DESKTOP}" -lt 2 -a "${#GDMSESSION}" -lt 2 ] && export code_editor="nano"
[ "${#XDG_CURRENT_DESKTOP}" -lt 2 -a "${#GDMSESSION}" -lt 2 ] && export code_editor_pre=""
[ "${#XDG_CURRENT_DESKTOP}" -lt 2 -a "${#GDMSESSION}" -lt 2 ] && export code_editor_suff=""

if [[ "$*" == *--dump* ]]; then
    echo ""
    echo "         PY = $PY"
    echo " widgets = $widgets"
    echo "code_editor = $code_editor"
    echo ""
    onlineTest 
    echo "      status: $online_status"
    echo "          ip: $myip"
    echo ""
    exit 0
fi

if [ ! -d  "$HOME/.rt" ];then
    mkdir "$HOME/.rt"
fi








[[ "$*" == *--c* ]] && echo $(date -u)>$logger
[ ! -f $logger ]    && echo $(date -u)>$logger
# echo "PWD: $PWD";
# xx
# function isFile() {
#     if [ -f "$1" ]; then
#         return 1
#     else
#         return 2
#     fi
#     return 2
# }
# function isfolder() {
#     if [ -d "$1" ]; then
#         return 1
#     else
#         return 2
#     fi
#     return 2
# }
# xx
function run_command(  ) {
    echo "__________________________________________________________________________________________"
    echo running: $1
    # echo running: $1
    # echo running: $1
    # echo running: $1
    EXIT_CODE=0
    eval "$1 || EXIT_CODE=\$?"
    # ret=$?
    if [ $EXIT_CODE -ne 0 ]; then
            echo "bad.fail, "$1>> $logger
            echo ""
            echo "   FAIL    $1 "
            echo ""
    else
            echo "good.success, "$1>> $logger
            echo ""
            echo "   SUCCESS $1 "
            echo ""
    fi
    # echo finish: $1
    # echo finish: $1
    # echo finish: $1
    # echo finish: $1
    echo "__________________________________________________________________________________________"
}
[[ "$*" == *-dl* ]] && re_download="yes" || re_download="no"
# echo -e " delete and download $rt_tool,... ? (y/n) \c"
# read
# if [  "$REPLY" == "y"  ]; then
#     re_download="yes"
# else
#     re_download="no"
# fi
# [ -d  $(pwd)/install ] && chmod -R 777 $(pwd)/install  > /dev/null
# [ -d  $(pwd)/install ] && chown scott $(pwd)/install
# echo re_download $re_download "|"$REPLY"|"
[ ! -d  "$HOME/.rt" ] && mkdir "$HOME/.rt"



# [ ! -d  "$HOME/.rt/config" ] && mkdir "$HOME/.rt/config"
# onlineTest 1
# if [ "$online_status" == "online" ]; then

declare -A mydic


[ $DlV == "3" ] && mydic['tool']=$rt_tool
[ $DlV == "2" ] && mydic['tool2']=$rt_tool2
mydic['tool.sh']=$rt_toolsh
mydic['help.txt']=$rt_toolhelp



for key in "${!mydic[@]}"; do
    key_path=${mydic[$key]}

    if [ -f  "$key_path" ] ; then
        if [ $re_download == "yes" ] ; then
            onlineTest 1
            if [ "$online_status" == "online" ]; then
                rm $key_path
                wget -q "http://reph.us/tools/file.php?file=$key" -O $key_path
                [ -f $rt_tool ] && $PY $rt_tool -header.fix.file $key_path
                [ -f $rt_tool ] && $PY $rt_tool -sh.file $key_path
                
                
            fi
        fi
    else
        onlineTest 1
        if [ "$online_status" == "online" ]; then
            wget -q "http://reph.us/tools/file.php?file=$key" -O $key_path
            [ -f $rt_tool ] && $PY $rt_tool -header.fix.file $key_path
            [ -f $rt_tool ] && $PY $rt_tool -sh.file $key_path
        fi
    fi
    # echo "$key = ${mydic[$key]}"
done


# unset mydic
# declare -A mydic2
# # mydic2['bashrc.py']=$widgets/widgets/python/bashrc.py
# mydic2['load-vars.sh']=$widgets/widgets/bash/load-vars.sh

# for key in "${!mydic2[@]}"; do
#     key_path=${mydic2[$key]}
#     if [ -f  "$key_path" ] ; then
#         if [ $re_download == "yes" ] ; then
#             onlineTest 1
#             if [ "$online_status" == "online" ]; then
#                 rm $key_path
#                 wget -q "http://reph.us/tools/file.php?file=$key" -O $key_path
#                 $PY $rt_tool -header.fix.file $key_path
#                 $PY $rt_tool -sh.file $key_path
#             fi
#         fi
#     fi
# done


chmod -R 777 $HOME/.rt/* > /dev/null
# $rt_tool -sh.file $toolx.sh --c
# $rt_tool -sh.file $toolx --c q
# exit 0
function process_py_A() {
    where=$(pwd)"/install/py/A"
    echo "process_py_A()"
    while read p; do
        [ ${#p} -gt 1 ] && [ $($rt_tool -import $p) = "no" ] && run_command "${py_install_cmd/SUBJECT/$p}"
    done < $where
}
function process_py_APT() {
    where=$(pwd)"/install/py/apt"
    echo "process_py_APT()"
    while read p; do
        [ ${#p} -gt 1 ] && [ $($rt_tool -import $p) = "no" ] && run_command "${py_install_cmd/SUBJECT/$p}"
    done < $where
}
function script_help() {
    
    echo "script_help()"
    echo "-dl      = download tool, tool.sh, help.txt"
    echo "-dl2      = download tool2, tool.sh, help.txt"
    echo "-py.a    = $(pwd)/install/py/A"
    echo "-py.b    = $(pwd)/install/py/B"
    echo "-py.*    = $py_install_cmd_A"
    echo "-py.py   = $py_install_cmd_B"
    echo "-py.apt  = $py_install_cmd_C"
    echo ""
    echo "-apt.up  = apt-get update; apt-get upgrade;ets..."
    echo "-apt.*   = $apt_install_cmd_A"
    echo "-apt.a   = $(pwd)/install/apt/A"
    echo "-apt.b   = $(pwd)/install/apt/B"
    echo "-apt.c   = $(pwd)/install/apt/C"
    echo "-apt.d   = $(pwd)/install/apt/DEB"
    echo "-apt.deb = $(pwd)/install/apt/DEB"
    echo ""
    echo "-emoji   = apt-get install fonts-noto-color-emoji"
    echo ""
    echo "--dump   = echo some vars"
    echo ""
    echo ""
    echo "-pip3.a  = pip3 install basic"
    echo ""
    echo ""
}
function update_apt() {
    echo "update_apt()"
    run_command "apt-get update"
    run_command "apt-get upgrade"
    run_command "apt-get install python3 -y"
    run_command "apt-get install python3-pip3 -y"
    run_command "apt-get update python3 -y"
    run_command "apt-get update $PY-pip3 -y"
    run_command "python3 -H pip3 install --upgrade pip3 -y"
    run_command "pip3 install --upgrade setuptools pip"
}
function process_py_B() {
    where=$(pwd)"/install/py/B"
    echo "process_py_B()"
    while read p; do
        if [ ${#p} -gt 1 ] && [ $($rt_tool -import $p) = "no" ]; then
            echo -e "$p not found! Install? (y/n) \c"
            read
            if "$REPLY" = "y"; then
                run_command "${py_install_cmd/SUBJECT/$p}"
            fi
        fi
    done < $where
}
function process_apt_A() {
    where=$(pwd)"/install/apt/A"
    echo "process_apt_A()"
    while read p; do
        # echo $p
    if [ ${#p} -gt 1 ]; then
        # echo $p
        theTest=$( which $p > /dev/null )
        # echo theTest $theTest
        if [[ ! $theTest  ]]; then
            run_command "${apt_install_cmd_A/SUBJECT/$p}"
        fi
    fi
    
        
    done < $where
}
function process_apt_B() {
    where=$(pwd)"/install/apt/B"
    echo "process_apt_B()"
    while read p; do
        doThis=false
        [ ${#p} -gt 1 ] && [ ! which $p > /dev/null ] && doThis=true
        if $doThis; then
            echo -e "$p not found! Install? (y/n) \c"
            read
            if "$REPLY" = "y"; then
                run_command "${apt_install_cmd_A/SUBJECT/$p}"
            fi
        fi
    done < $where
}
function process_apt_C() {
    where=$(pwd)"/install/apt/C"
    echo "process_apt_C()"
    while read p; do
        doThis=false
        [ ${#p} -gt 1 ] && [ ! which $p > /dev/null ] && doThis=true
        if $doThis; then
            echo -e "$p not found! Install? (y/n) \c"
            read
            if "$REPLY" = "y"; then
                run_command "${apt_install_cmd_A/SUBJECT/$p}"
            fi
        fi
    done < $where
}
function process_apt_DEB() {
    where=$(pwd)"/install/apt/DEB"
    echo "process_apt_DEB()"
    while read p; do
        echo $p
    done < $where
}
function loadVars(){
    initializer
    # echo ""
    # echo ""
    # echo $(  -f  $rt_tool )
    # echo ""
    # echo ""
    # if [ !  -f  $rt_tool  ]; then
    #     wget -q http://reph.us/tools/tool -O $rt_tool
    #     # run_command "wget -q http://reph.us/tools/tool -O $rt_tool"
    # fi
    # echo -e "$p not found! Install? (y/n) \c"
    # read
    # if "$REPLY" = "y"; then
    #     run_command "${apt_install_cmd_A/SUBJECT/$p}"
    # fi
    # echo $HOME/.rt/.config.hash
    # $( $rt_tool -json $HOME/.rt/.config.hash )

    # echo $widgets
    if [ ! -d $widgets ]; then
        mkdir $widgets
    fi
    if [ ! -d $widgets/tech ]; then
        mkdir $widgets/tech
    fi
    if [ ! -d $widgets/widgets ]; then
        mkdir $widgets/widgets
    fi
    if [ ! -d $widgets/widgets/python ]; then
        mkdir $widgets/widgets/python
    fi
    if [ ! -d $widgets/widgets/python/src ]; then
        mkdir $widgets/widgets/python/src
    fi
    if [ ! -d $widgets/widgets/python ]; then
        mkdir $widgets/widgets/python
    fi

}
py_install_cmd_A='pip3 install    SUBJECT    --no-input -q'
py_install_cmd_B=$PY' -m pip install    SUBJECT    --no-input -q'
py_install_cmd_C='apt-get install    python3-SUBJECT    -y'
apt_install_cmd_A='apt-get install    SUBJECT    -y'
py_install_cmd=$py_install_cmd_A
function initializer() {
    # cd $HOME
    if ! which curl > /dev/null; then
        sudo apt-get install curl
    fi
    if ! which wget > /dev/null; then
        sudo apt-get install wget
    fi
    if ! which python3 > /dev/null; then
        sudo apt-get install python3
    fi
    if ! which pip3 > /dev/null; then
        sudo apt-get install python3-pip
    fi
    
    if ! which unzip > /dev/null; then
        sudo apt-get install unzip
    fi
    # p='simplejson'
    # testThis=$( $rt_tool -import $p)
    # echo testThis $testThis simplejson
    # [ ${#p} -gt 1 ] && [ $testThis = "no" ] && run_command "${py_install_cmd/SUBJECT/$p}"
    # [ ${#p} -gt 1 ] && [ $testThis = "no" ] && run_command "${py_install_cmd/SUBJECT/$p}"
}
function post_initializer() {
    touch $hasRun_touch
    dl_install_linux
    dl_install_databank
    # [ !  -d  $HOME/.rt/dl ] && run_command "mkdir $HOME/.rt/dl"
    # cd $HOME/.rt/dl
    
    # [ !  -f  $HOME/.rt/dl/linux.zip  ] && wget http://reph.us/tools/linux.zip
    # [ !  -f  $HOME/.rt/dl/databank.zip  ] && wget http://reph.us/tools/databank.zip
    # [ !  -d  $HOME/.rt/dl/linux ] && [  -f  $HOME/.rt/dl/linux.zip  ] && run_command "unzip linux.zip -d linux"
    # [ !  -d  $HOME/.rt/dl/databank ] && [  -f  $HOME/.rt/dl/databank.zip  ] && run_command "unzip databank.zip -d databank"
    # # chown scott $HOME/.rt/*
    # chmod -R 777 $HOME/.rt/*  > /dev/null
    # cd $HOME/.rt/dl/linux/tech/linux/bash
    # echo $( pwd )
    # echo $( pwd )
    # echo $( pwd )

    # if ! which python3 > /dev/null; then
    #     echo -e "python3 not found! Install? (y/n) \c"
    #     read
    #     if "$REPLY" = "y"; then
    #         apt-get install python3
    #     fi
    # fi
    # # apt-get install python3
    # [ ! -d $widgets ] && mkdir $widgets
    # [ ! -d $widgets/tech ] && mkdir $widgets/tech
    # [ ! -d $widgets/widgets ] && mkdir $widgets/widgets
    # [ ! -d $widgets/widgets/python ] && mkdir $widgets/widgets/python
    # [ ! -d $widgets/widgets/python/src ] && mkdir $widgets/widgets/python/src
    # [ ! -d $widgets/widgets/python ] && mkdir $widgets/widgets/python
    # chmod -R $HOME/.rt  > /dev/null
    # chmod -R 777 $HOME/.rt/*  > /dev/null
    # # chmod -R 777 $widgets  > /dev/null
    # cp -r  ../python/_rightThumb/ ./
    # $PY ./shCleanSimple.py
    # subject_path=$widgets/widgets
    # echo $subject_path
    # cp -rf ../bash $subject_path/
    # cp -rf ../python/ $subject_path/python/src/
    # cp -rf ../batch $subject_path/
    # cp -rf ../documentation $subject_path/
    # cp -rf ../javascript $subject_path/
    # cp -rf ../library $subject_path/
    # cp -rf ../php $subject_path/
    # cp -rf ../remote $subject_path/
    # cp -rf ../vbs $subject_path/
    # cp -rf ../powershell $subject_path/
    # echo $subject_path


    # cd $HOME/.rt/dl/databank/widgets/databank
    # echo $( pwd )
    # echo $( pwd )
    # echo $( pwd )
    # echo $subject_path
    # echo $subject_path
    # echo $subject_path
    # cp -r ../databank $subject_path
    # echo $subject_path
    # echo $subject_path
    # echo $subject_path

    # cd $widgets/widgets/python
    # echo $widgets/widgets/python
    # echo $PY $widgets/widgets/python/bashrc.py
    # $PY $toolx -bashrc.default
}

function dl_install_databank() {
    touch $hasRun_touch

    [ !  -d  $HOME/.rt/dl ] && run_command "mkdir $HOME/.rt/dl"
    cd $HOME/.rt/dl
    
    [ !  -f  $HOME/.rt/dl/databank.zip  ] && wget http://reph.us/tools/databank.zip
    [ !  -d  $HOME/.rt/dl/databank ] && [  -f  $HOME/.rt/dl/databank.zip  ] && run_command "unzip databank.zip -d databank"

    chmod -R 777 $HOME/.rt/*  > /dev/null



    cd $HOME/.rt/dl/databank/widgets/databank
    echo $( pwd )
    echo $subject_path
    cp -r ../databank $subject_path
    echo $subject_path
}

function dl_install_linux() {
    touch $hasRun_touch
    [ !  -d  $HOME/.rt/dl ] && run_command "mkdir $HOME/.rt/dl"
    cd $HOME/.rt/dl
    
    [ !  -f  $HOME/.rt/dl/linux.zip  ] && wget http://reph.us/tools/linux.zip
    [ !  -d  $HOME/.rt/dl/linux ] && [  -f  $HOME/.rt/dl/linux.zip  ] && run_command "unzip linux.zip -d linux"
    # chown scott $HOME/.rt/*
    chmod -R 777 $HOME/.rt/*  > /dev/null
    cd $HOME/.rt/dl/linux/tech/linux/bash
    echo $( pwd )
    echo $( pwd )
    echo $( pwd )

    if ! which python3 > /dev/null; then
        echo -e "python3 not found! Install? (y/n) \c"
        read
        if "$REPLY" = "y"; then
            sudo apt-get install python3
        fi
    fi
    # apt-get install python3
    [ ! -d $widgets ] && mkdir $widgets
    [ ! -d $widgets/tech ] && mkdir $widgets/tech
    [ ! -d $widgets/widgets ] && mkdir $widgets/widgets
    [ ! -d $widgets/widgets/python ] && mkdir $widgets/widgets/python
    [ ! -d $widgets/widgets/python/src ] && mkdir $widgets/widgets/python/src
    [ ! -d $widgets/widgets/python ] && mkdir $widgets/widgets/python
    chmod -R $HOME/.rt  > /dev/null
    chmod -R 777 $HOME/.rt/*  > /dev/null
    # chmod -R 777 $widgets  > /dev/null
    cp -r  ../python/_rightThumb/ ./
    $PY ./shCleanSimple.py
    subject_path=$widgets/widgets
    echo $subject_path
    cp -rf ../bash $subject_path/
    cp -rf ../python/ $subject_path/python/src/
    cp -rf ../batch $subject_path/
    cp -rf ../documentation $subject_path/
    cp -rf ../javascript $subject_path/
    cp -rf ../library $subject_path/
    cp -rf ../php $subject_path/
    cp -rf ../remote $subject_path/
    cp -rf ../vbs $subject_path/
    cp -rf ../powershell $subject_path/
    echo $subject_path


}

function pip3_install() {
    pip3 install simplejson
    pip3 install xtarfile
    pip3 install binaryornot
    pip3 install cssselect
    pip3 install colorama
    pip3 install setuptools-rust
    pip3 install pymysql
    pip3 install Crypto
    pip3 install tzlocal
    pip3 install termcolor
    pip3 install datetime
    pip3 install pyAesCrypt
    pip3 install zipfile36
    pip3 install zipfile
    pip3 install tarfile
    pip3 install wget
    pip3 install pywin32
    pip3 install stickytape
    pip3 install dnspython
    pip3 install pymongo
    pip3 install arrow
    pip3 install mycloudhome
    pip3 install pyperclip
    pip3 install pyAesCrypt
    pip3 install pycrypto
    pip3 install arrow
    pip3 install pymysql
    pip3 install sshtunnel
    pip3 install gtts
    pip3 install emoji
    pip3 install pyreadline
    pip3 install ping
    pip3 install netaddr
    pip3 install getmac
    pip3 install native_web_app
    pip3 install psutil
    pip3 install forward
}

loadVars

if [[ "$*" == *-linux* ]]; then
    if [ -f  "$HOME/.rt/dl/linux.zip" ]; then
        rm  "$HOME/.rt/dl/linux.zip"
    fi
    if [ -d  "$HOME/.rt/dl/linux" ]; then
        rm -rf "$HOME/.rt/dl/linux"
    fi

fi



[[ "$*" == *-py.py* ]]     && py_install_cmd=$py_install_cmd_B
[[ "$*" == *-py.apt* ]]    && py_install_cmd=$py_install_cmd_C
[[ "$*" == *-py.a* ]]      && process_py_A
[[ "$*" == *-py.b* ]]      && process_py_B
[[ "$*" == *-py.apt* ]]      && process_py_APT
[[ "$*" == *-apt.up* ]]    && update_apt
[[ "$*" == *-apt.a* ]]    && process_apt_A
[[ "$*" == *-apt.b* ]]    && process_apt_B
[[ "$*" == *-apt.c* ]]    && process_apt_C
[[ "$*" == *-apt.d* ]]    && process_apt_DEB
[[ "$*" == *-apt.deb* ]]    && process_apt_DEB
[[ "$*" == *-dl.dl* ]]    && post_initializer
[[ "$*" == *-dl.linux* ]]    && dl_install_linux
[[ "$*" == *-dl.databank* ]]    && dl_install_databank

[[ "$*" == *-linux* ]]    && dl_install_linux
[[ "$*" == *-databank* ]]    && dl_install_databank
[[ "$*" == *-pip3.a* ]]    && pip3_install
[[ "$*" == *-emoji* ]]    && run_command "apt-get install fonts-noto-color-emoji"
[[ "$*" == "" ]]           && script_help


