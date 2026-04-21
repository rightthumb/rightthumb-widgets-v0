@echo off

call lab ShareMouse
set "ShareMouseLoop="
echo Fixing ShareMouse
call kill ShareMouse
start "" "C:\Program Files (x86)\ShareMouse\ShareMouse.exe"

set /p ShareMouseLoop=Loop: 

if not [%ShareMouseLoop%] == [] goto:kill

echo _______________________________________________________
echo.
call %0
goto:eof
:kill
call kill sharemouse