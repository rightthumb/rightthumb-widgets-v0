@echo off

REM This batch file uploads a given file to a specific endpoint
REM Usage: upload.bat <FILE_PATH>

set /p apiKey=API Key: 

set FILE_PATH=%1
set "ENDPOINT_URL=https://softwaredevelopmentsolutionsllc.com/apps/terminal/upload/?api=%apiKey%"

curl -s -F "file=@%FILE_PATH%" "%ENDPOINT_URL%"

REM End of script