@echo off
setlocal enabledelayedexpansion

:: Prompt for the command to run
set "cmd="
set /p cmd=Enter command to run: 

:: Prompt for loop count (0 = infinite)
set "loops="
set /p loops=How many loops? (0 = infinite): 

:: Ask if screen should clear each loop
set "clr="
set /p clr=Clear screen between loops? (y/n): 

echo.
echo Running...
echo -------------------------

:: Infinite loop mode
if "%loops%"=="0" (
    :infinite
        if /i "%clr%"=="y" cls
        echo Running command: %cmd%
        %cmd%
    goto infinite
)

:: Finite loop mode
set /a count=0
:finite
    if /i "%clr%"=="y" cls
    echo Loop !count! of %loops%
    %cmd%
    set /a count+=1
    if !count! LSS %loops% goto finite

echo Done.
exit /b
