@echo off

call c
echo.
echo     Session ID: %Session_ID%
echo.

if [%1] == [] (
	call p beeps -session
) else (
	call p beeps -session -m %1
)