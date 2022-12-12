@echo off

call c
echo.
echo     Session ID: %Session_ID%
echo.

if [%1] == [] (
	call p terminal-timer -session
) else (
	call p terminal-timer -session -m %1
)