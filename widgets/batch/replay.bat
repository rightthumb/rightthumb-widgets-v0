@echo off

if "%~1"=="" goto:noargs

call p. har_url_inject_replay -url %*
goto:after

:noargs
call p. har_url_inject_replay

:after
echo.
echo ------------------------------------------------------------
echo.
call p. script-helper -color green     replay https://example.com
echo.

call p. script-helper -color cyan This command is a wrapper for har_url_inject_replay
call p. script-helper -color cyan When arguments are supplied the wrapper automatically adds -url
echo.
call p. script-helper -color cyan Example:
echo.
call p. script-helper -color cyan Equivalent command:
call p. script-helper -color cyan     p. har_url_inject_replay -url https://example.com

echo.
echo ------------------------------------------------------------
echo.