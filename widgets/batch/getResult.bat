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

set doThis=%1
IF [%1] == [] GOTO:EOF
CALL :DeQuote doThis
%doThis%>{6E5894A5FBA8}
set /p result=<{6E5894A5FBA8}

IF EXIST {6E5894A5FBA8} (
        del {6E5894A5FBA8}
    )
set doThis=

GOTO:EOF

:DeQuote
for /f "delims=" %%A in ('echo %%%1%%') do set %1=%%~A
GOTO:EOF



 
