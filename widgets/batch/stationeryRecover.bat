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

echo.
set confirm=
set /p confirm= Recover Stationery? 
::echo =====================    
echo.
IF [%confirm%] == [y] CALL :Yes
IF NOT [%confirm%] == [y] CALL :No
GOTO:EOF

:Yes
echo Recovering Stationery... 
copy /y "D:\Program Files (x86)\Common Files\Microsoft Shared\Stationery\mainBK.html" "D:\Program Files (x86)\Common Files\Microsoft Shared\Stationery\main.html"
GOTO:EOF

:No
echo Skipped
GOTO:EOF