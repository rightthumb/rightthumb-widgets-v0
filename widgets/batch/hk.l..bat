@echo off

set /p "hkpin=PIN: "

if [%hkpin%]==[] (
    call:nopassword
) else (
    call:password %hkpin%
)

:nopassword
call p. hotkeys
call p. hotkeys
call p. hotkeys
call p. hotkeys
call p. hotkeys
call p. hotkeys
call:nopassword
goto:eof
 
:password
call p. hotkeys -password %hkpin%
call p. hotkeys -password %hkpin%
call p. hotkeys -password %hkpin%
call p. hotkeys -password %hkpin%
call p. hotkeys -password %hkpin%
call p. hotkeys -password %hkpin%
call:password %hkpin%
goto:eof