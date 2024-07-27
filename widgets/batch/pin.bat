@echo off

rem Define the handler for Ctrl+C (SIGINT)
set "CtrlCHandler=exit"

set asked=0
if "%1" == "-ask" (
    echo ask>"%stmp%/pin_ask"
) else if "%1" == "-noask" (
    call :noask
)

if "%vault_pin%" == "" (
    call :ask
) else (
    call :check
)
goto :eof

:noask
if exist "%stmp%/pin_ask" (
    del "%stmp%/pin_ask"
    echo ask setting removed
) else (
    echo no ask setting found
)
goto :eof

:ask
set /a asked+=1
if %asked% gtr 3 (
    echo too many attempts
    exit
)
call p. loginPIN
set /p vault_pin=<"%stmp%/pin"
if "%vault_pin%" == "" (
    echo no pin entered
    call x
)
call rm "%stmp%/pin" --c
if not exist "%rt%\profile\config\.vault.%vault_pin%" (
    call :ask
) else (
    echo pin set
)
goto :eof

:check
if not exist "%rt%\profile\config\.vault.%vault_pin%" (
    call :ask
) else (
    echo pin is set
)
goto :eof
