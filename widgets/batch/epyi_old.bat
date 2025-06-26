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


set rtApp=%1
if [%1] == [base] set rtApp=base3

set importFolder=%python%\_rightThumb\_%rtApp%
set __init__="%importFolder%\__init__.py"
set initExample="%importFolder%\_%rtApp%_init_example.py"
set child="%importFolder%\_%rtApp%.py"
set childExample="%importFolder%\_%rtApp%_example.py"
set childSample="%importFolder%\_%rtApp%_sample.py"
set childCommands="%importFolder%\_commands.py"

rem echo 1 %1
rem echo 2 %2
rem goto:eof
set fileName=
if [%1] == [?] (

    echo epyi base                   edit init import
    echo.
    echo epyi base -build newApp     create new app
    echo epyi base -e                edit new app template
    echo.
    echo epyi base -cmd              print list of commands
    echo epyi base -cmde             edit list of commands
    echo.
    echo epyi base -s                edit sample
    echo.
    goto:eof
)

if [%1] == [] (
        goto:eof
    ) else (
        if not exist "%importFolder%\" md "%importFolder%\"

    )


if [%2] == [-build] (
        if [%3] == [] (
                echo.&set /p fileName=fileName Name: 
            ) else (
                set fileName=%3
            )
    ) else (set placeholder99=0)


if [%2] == [] (

        if not exist "%__init__%" (
            set /p initOpen=Create new init? 
        ) else (
            set initOpen=y
        )
        if [%initOpen%] == [y] (
            call p. fileBackup -i %__init__%
            start "EDIT" %code_editor% %__init__%
            echo %__init__%
        ) else (
            goto:eof
        )
    ) else if [%2] == [-e] (
        start "EDIT" %code_editor% %initExample%
        echo %initExample%
    ) else if [%2] == [-build] (
        rem echo.
        rem set /p fileName=fileName Name: 
        echo %fileName%
        if [%fileName%] == [] goto:eof

        if exist "%python%\%fileName%.py" (

                echo App already exists
                set /p action=Replace App?: 
                if [%action%] == [y] (
                        call p. fileBackup -i "%python%\%fileName%.py"
                        type %initExample% > "%python%\%fileName%.py"
                        rem call p. fileBackup -i "%python%\%fileName%.py"
                    ) else (
                        call p. fileBackup -i "%python%\%fileName%.py"
                    )

                start "EDIT" %code_editor% "%python%\%fileName%.py"
                echo %python%\%fileName%.py

            ) else (
                call p. fileBackup -i "%python%\%fileName%.py"
                type %initExample% > "%python%\%fileName%.py"
                call p. fileBackup -i "%python%\%fileName%.py"
                start "EDIT" %code_editor% "%python%\%fileName%.py"
                echo %python%\%fileName%.py
            )
    ) else if [%2] == [-s] (
        call p. fileBackup -i %childSample%
        start "EDIT" %code_editor% %childSample%
        echo %childSample%
    ) else if ["%2"] == ["-cmd"] (
        if exist %childCommands% (
                cls
                echo.
                type %childCommands%
            ) else (
                call p. fileBackup -i %childCommands%
                start "EDIT" %code_editor% %childCommands%
                echo %childCommands%
            )
        echo.
        echo.
        echo.
        echo %childCommands%
    ) else if ["%2"] == ["-cmde"] (
        call p. fileBackup -i %childCommands%
        start "EDIT" %code_editor% %childCommands%
        echo %childCommands%
    

        echo.
        echo.
        echo.
        echo %childCommands%
    ) else if [%3] == [] (
        call p. fileBackup -i %child%
        start "EDIT" %code_editor% %child%
        echo %child%
    ) else if [%3] == [-e] (
        call p. fileBackup -i %childExample%
        start "EDIT" %code_editor% %childExample%
        echo %childExample%
    ) else if [%3] == [-build] (
        rem echo.
        rem set /p fileName=fileName Name: 
        rem if [%fileName%] == [] goto:eof

        if exist "%python%\%fileName%.py" (
                echo App already exists
                call p. fileBackup -i "%python%\%fileName%.py"
                start "EDIT" %code_editor% "%python%\%fileName%.py"
                echo %python%\%fileName%.py
            ) else (
                call p. fileBackup -i "%python%\%fileName%.py"
                type %childExample% > "%python%\%fileName%.py"
                call p. fileBackup -i "%python%\%fileName%.py"
                start "EDIT" %code_editor% "%python%\%fileName%.py"
                echo %python%\%fileName%.py
            )
    )

goto:eof
:HELP
goto:eof

:CMDS
goto:eof
rem epyi
rem eeee


 
