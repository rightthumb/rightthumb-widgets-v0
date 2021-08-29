@echo off
cls
call p file +  *.zip
SET take_action=n
echo.
SET /p take_action= Stop ? 
echo.
if EXIST *.zip call :ARCHIVE_FILES
goto:eof
:ARCHIVE_FILES
	IF NOT [%take_action%] == [y] move *.zip %archive7z%\>nul
goto:eof

