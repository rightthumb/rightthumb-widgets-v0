@echo off


if not [%1] == [] (
    call pathFromPythonPath %1
    echo Installing pip3...
    curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py
    call pathFromPythonPath
    %py% get-pip.py
    del get-pip.py

)

if not [%pip3%] == [] (
    %pip3% install -r ..\require.txt
) else (
    pip3 install -r ..\require.txt
)
goto:eof


