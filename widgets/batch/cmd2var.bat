@echo off

:: Use this to reduce file writes

for /f "delims=" %%i in ('%*') do set cmd2var=%%i
echo %cmd2var%