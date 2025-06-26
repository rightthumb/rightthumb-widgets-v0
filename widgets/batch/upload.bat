@echo off

REM This batch file uploads a given file to a specific endpoint
REM Usage: upload.bat <FILE_PATH>

set FILE_PATH=%1
set ENDPOINT_URL=https://softwaredevelopment.solutions/apps/terminal/upload/

curl -s -F "file=@%FILE_PATH%" %ENDPOINT_URL%

REM End of script
