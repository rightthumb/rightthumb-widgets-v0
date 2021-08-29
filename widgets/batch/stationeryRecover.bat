@echo off
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