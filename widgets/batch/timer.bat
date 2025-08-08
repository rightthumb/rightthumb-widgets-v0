@echo off

set timer=True
call c
echo.
echo     Session ID: %Session_ID%
echo.
call grn
rem echo %timer%
if [%1] == [] (
	call p. terminal-timer -session
) else (
	call p. terminal-timer -session -m %1
)