@echo off

if [%1]==[] (
    call:nopassword
) else (
    call:password %1
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
call p. hotkeys -password %1
call p. hotkeys -password %1
call p. hotkeys -password %1
call p. hotkeys -password %1
call p. hotkeys -password %1
call p. hotkeys -password %1
call:password %1
goto:eof