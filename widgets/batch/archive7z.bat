@echo off

rem ## {R2D2919B742E} ##
rem ###########################################################################
rem What if magic existed?
rem What if a place existed where your every thought and dream come to life.
rem There is only one catch: it has to be written down.
rem Such a place exists, it is called programming.
rem    - Scott Taylor Reph, RightThumb.com
rem ###########################################################################
rem ## {C3P0D40fAe8B} ##

cls
call p. file +  *.7z 
SET take_action=n
echo.
SET /p take_action= Stop ? 
echo.
if EXIST *.7z call :ARCHIVE_FILES
goto:eof
:ARCHIVE_FILES
    IF NOT [%take_action%] == [y] move *.7z %archive7z%\>nul
goto:eof



 
