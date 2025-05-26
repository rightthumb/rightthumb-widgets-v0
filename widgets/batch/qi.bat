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
call p. fileBackup -open -i %qi%
if exist %qi% DEL /q %qi% 
echo.
for /F "tokens=*" %%A in (%myTables%\qi.txt) do CALL :PROCESS %%A
goto:eof

:PROCESS
    if exist %1 (
            echo Processing: %1
            dir /s/b "%1" >> %qi%
        ) else (
            echo Error: %1
        )
    goto:eof
goto:eof


 
