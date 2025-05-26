@echo off

set /p command="Enter the command to execute (or type 'exit' to quit): "
:loop
if "%command%"=="exit" goto :eof
%command%
goto :loop
