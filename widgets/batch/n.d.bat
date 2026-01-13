@echo off

set /p PATH_FILE=<"%tt%\file-open.last"

set "shouldDelete="

echo.
echo %PATH_FILE%
echo.
set /p shouldDelete=Delete? 

if "%shouldDelete%" == "n" goto :eof
if "%shouldDelete%" == "no" goto :eof

del "%PATH_FILE%"
echo Deleted: %PATH_FILE%
echo.

@REM echo.
@REM echo %tt%\file-open.last.log
@REM echo.

set "shouldDelete="
set "PATH_FILE="
