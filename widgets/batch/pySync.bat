@echo off
set /p Drive=<%userprofile%\.tk421
set widgets=%Drive:~0,1%
echo %widgets%


IF NOT EXIST %widgets%:\ (CALL :ERROR) 
IF EXIST %widgets%:\ (CALL :START) 
GOTO:EOF

