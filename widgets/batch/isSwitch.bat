@echo off

:: usage:
::     call runSet isSwitch %*
::     IF [%runSet%] == [true]

set "isSwitchTemp=%stmp%\isSwitchTemp.txt"

if [%1] == [] (
    echo null
    goto:eof
)
setlocal enabledelayedexpansion

set arg=%1
if "!arg:~0,1!"=="-" (
    set hasSwitch=true
) else (
    set hasSwitch=false
)
echo !hasSwitch!
endlocal
