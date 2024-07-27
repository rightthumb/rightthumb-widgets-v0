@echo off

if [%pip3%] == [] (
    %pip3% install -r ..\require-hotkeys.txt
) else (
    pip3 install -r ..\require-hotkeys.txt
)
goto:eof


echo Installing pip3...
curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py
python get-pip.py
del get-pip.py