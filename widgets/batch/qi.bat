@echo off
cls
call p fileBackup -i %qi%
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
