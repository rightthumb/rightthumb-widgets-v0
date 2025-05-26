@echo off
set "shifty=%2"
:loop
shift
if "%2"=="" goto end
set "shifty=%shifty% %2"
goto loop
:end
