@echo off

rem ## {R2D2919B742E} ##
rem ###########################################################################
rem What if magic existed?
rem What if a place existed where your every thought and dream come to life.
rem There is only one catch: it has to be written down.
rem Such a place exists, it is called programming.
rem    - Scott Taylor Reph, RightThumb.com
rem ###########################################################################
rem ## {C3P0D40fAe8B} ##



IF 1%2 NEQ +1%2 ( set gotoLine=0 ) ELSE ( set gotoLine=%2 )

if exist %1 (

    call p. fileBackup -f %*
    
    rem taskkill /im sublime_text.exe /f
    CALL:OPEN_FILE %1
    rem echo %*

) else (
    call :shouldcreate %1
)
goto:eof

:OPEN_FILE
    call p. file-open -f "%*"
    rem start "EDIT" %code_editor% "%*"
goto:eof

:shouldcreate
set "create="
             echo File doesn't exist
    set /p "create=-                  Create? "
    if [%create%] == [] (

    call :altlocations %*
    goto:eof

    ) else if [%create%] == [n] (
    goto:eof
    ) else if [%create%] == [y] (

    echo Create chosen
    call p. fileBackup -f %*
    rem taskkill /im sublime_text.exe /f
    CALL:OPEN_FILE %*
    rem echo %*
    goto:eof

    ) else if [%create%] == [x] (

    echo exit
    goto:eof

    ) else if [%create%] == [n] (

    call :altlocations %*

    ) else (

    echo end create
    goto:eof


    )





goto:eof
:altlocations
rem echo Checking other locations...
rem echo.
rem goto:eof

if exist %* (

    call p. fileBackup -f %*
    rem taskkill /im sublime_text.exe /f
    CALL:OPEN_FILE %*
    rem echo %*






) else if exist %myTables%\%*.json (

    call p. fileBackup -f %myTables%\%*.json
    rem taskkill /im sublime_text.exe /f
    CALL:OPEN_FILE %myTables%\%*.json
    rem echo %myTables%\%*.json


) else if exist %myTables%\%*.txt (

    call p. fileBackup -f %myTables%\%*.txt
    rem taskkill /im sublime_text.exe /f
    CALL:OPEN_FILE %myTables%\%*.txt
    rem echo %myTables%\%*.json




) else if exist %dbTables%\%*.json (

    call p. fileBackup -f %dbTables%\%*.json
    CALL:OPEN_FILE %dbTables%\%*.json

) else if exist %dbTables%\%* (

    call p. fileBackup -f %dbTables%\%*
    CALL:OPEN_FILE %dbTables%\%*

) else if exist %python%\%*.py (

    call p. fileBackup -f %python%\%*.py
    rem taskkill /im sublime_text.exe /f
    CALL:OPEN_FILE %python%\%*.py
    rem echo %python%\%*.py

) else if exist %phpFiles%\%*.php (

    call p. fileBackup -f %phpFiles%\%*.php
    rem taskkill /im sublime_text.exe /f
    CALL:OPEN_FILE %phpFiles%\%*.php
    rem echo %phpFiles%\%*.php

) else if exist %scriptroot%\%*.bat (

    call p. fileBackup -f %scriptroot%\%*.bat
    rem taskkill /im sublime_text.exe /f
    CALL:OPEN_FILE %scriptroot%\%*.bat
    rem echo %scriptroot%\%*.bat

) else if exist %powershell%\%*.ps1 (

    call p. fileBackup -f %powershell%\%*.ps1
    rem taskkill /im sublime_text.exe /f
    CALL:OPEN_FILE %powershell%\%*.ps1
    rem echo %powershell%\%*.ps1

) else if exist D:\_Scott\S_Documents\Projects\self\Powershell\%*.ps1 (

    call p. fileBackup -f D:\_Scott\S_Documents\Projects\self\Powershell\%*.ps1
    rem taskkill /im sublime_text.exe /f
    CALL:OPEN_FILE D:\_Scott\S_Documents\Projects\self\Powershell\%*.ps1
    rem echo D:\_Scott\S_Documents\Projects\self\Powershell\%*.ps1

) else if exist %myPhp%\%*.php (

    call p. fileBackup -f %myPhp%\%*.php
    rem taskkill /im sublime_text.exe /f
    CALL:OPEN_FILE %myPhp%\%*.php
    rem echo %myPhp%\%*.php

) else if exist %myPowershell%\%*.ps1 (

    call p. fileBackup -f %myPowershell%\%*.ps1
    rem taskkill /im sublime_text.exe /f
    CALL:OPEN_FILE %myPowershell%\%*.ps1
    rem echo %myPowershell%\%*.ps1

) else if exist %myPython%\%*.py (

    call p. fileBackup -f %myPython%\%*.py
    rem taskkill /im sublime_text.exe /f
    CALL:OPEN_FILE %myPython%\%*.py
    rem echo %myPython%\%*.py

) else if exist %myTables%\%* (

    call p. fileBackup -f %myTables%\%*
    rem taskkill /im sublime_text.exe /f
    CALL:OPEN_FILE %myTables%\%*
    rem echo %myTables%\%*





) else if exist %myDatabases%\%* (

    call p. fileBackup -f %myDatabases%\%*
    rem taskkill /im sublime_text.exe /f
    CALL:OPEN_FILE %myDatabases%\%*
    rem echo %myDatabases%\%*

) else if exist %myWebApp%\%* (

    call p. fileBackup -f %myWebApp%\%*
    rem taskkill /im sublime_text.exe /f
    CALL:OPEN_FILE %myWebApp%\%*
    rem echo %myWebApp%\%*

) else if exist %USERPROFILE%\Desktop\%* (

    call p. fileBackup -f %USERPROFILE%\Desktop\%*
    rem taskkill /im sublime_text.exe /f
    CALL:OPEN_FILE %USERPROFILE%\Desktop\%*
    rem echo %USERPROFILE%\Desktop\%*

) else (
    
    call p. fileBackup -f %*
    rem taskkill /im sublime_text.exe /f
    CALL:OPEN_FILE %*
    rem echo %*

)





     
