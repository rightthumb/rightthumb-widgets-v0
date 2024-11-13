@echo off
if [%1] == [-ask] (
    echo ask>"%stmp%/pin_ask"
)
if [%1] == [-noask] (
    call :noask
)
if [%vault_pin%] == [] (
    call p loginPIN
    set /p vault_pin=<"%stmp%/pin"
    call rm "%stmp%/pin" --c
    echo pin set
) else (
    echo pin is set
)
goto :eof
:noask
if exist "%stmp%/pin_ask" (
    del "%stmp%/pin_ask"
    echo ask setting removed
) else (
    echo no ask setting found
)