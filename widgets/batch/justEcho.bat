@echo off
set "justEcho=Test Variable Success"
set "justEcho1=Var One"
set "justEcho2=Var Two"

if "%~1"=="" (
    echo Default
) else if /I "%~1" == "echo" (
    shift
    call :subAction %*
) else if /I "%~1" == "echo2" (
    shift
    call :subAction %*
) else (
    echo %*
)
goto :eof

:subAction
if "%~1"=="" (
    echo No variables provided to echo.
    goto :eof
)

:loop
if "%~1"=="" goto :eof
if /I "%~1" == "echo" (
    shift
    goto loop
)
if /I "%~1" == "echo2" (
    shift
    goto loop
)

rem Store variable name safely
set "justEchoVarName=%~1"

rem Get the value of the variable
call set "justEchoVarValue=%%%justEchoVarName%%%"

rem Check if the variable is not empty
if not "%justEchoVarValue%"=="" (
    echo %justEchoVarValue%
)

shift
goto loop
