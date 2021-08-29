@echo off
cls
call p file +  *.7z 
SET take_action=n
echo.
SET /p take_action= Stop ? 
echo.
if EXIST *.7z call :ARCHIVE_FILES
goto:eof
:ARCHIVE_FILES
	IF NOT [%take_action%] == [y] move *.7z %archive7z%\>nul
goto:eof

