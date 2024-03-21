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

set importFolder=%pyroot%\_rightThumb\_%1
set __init__="%importFolder%\__init__.py"
set initExample="%importFolder%\_%1_init_example.py"
set child="%importFolder%\_%1.py"
set childExample="%importFolder%\_%1_example.py"
if [%1] == [] (
        goto:eof
    ) else (
        if not exist "%importFolder%\" md "%importFolder%\"

    )




if [%2] == [] (
        call p. fileBackup -open -i %__init__%
        start "EDIT" %code_editor% %__init__%
    ) else if [%2] == [-e] (
        start "EDIT" %code_editor% %initExample%
    ) else if [%2] == [-build] (
        echo.
        set /p file=File Name: 
        if [%file%] == [] goto:eof
        call p. fileBackup -open -i "%pyroot%\%file%.py"
        type %initExample% > "%pyroot%\%file%.py"
        call p. fileBackup -open -i %initExample%
        start "EDIT" %code_editor% "%pyroot%\%file%.py"
    ) else if [%3] == [] (
        call p. fileBackup -open -i %child%
        start "EDIT" %code_editor% %child%
    ) else if [%3] == [-e] (
        call p. fileBackup -open -i %childExample%
        start "EDIT" %code_editor% %childExample%
    ) else if [%3 == [-build] (
        echo.
        set /p file=File Name: 
        if [%file%] == [] goto:eof
        call p. fileBackup -open -i "%pyroot%\%file%.py"
        call p. fileBackup -open -i %childExample%
        type %childExample% > "%pyroot%\%file%.py"
        start "EDIT" %code_editor% "%pyroot%\%file%.py"
        
    )



rem epyi
rem eeee


 
