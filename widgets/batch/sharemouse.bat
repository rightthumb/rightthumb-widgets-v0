@echo off

call lab ShareMouse
set "ShareMouseLoop="
echo Fixing ShareMouse
call kill ShareMouse
start "" "C:\Program Files (x86)\ShareMouse\ShareMouse.exe"

set /p ShareMouseLoop=Loop: 

if not [%ShareMouseLoop%] == [] goto:eof

echo _______________________________________________________
echo.
call %0