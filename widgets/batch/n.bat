@echo off

IF 1%2 NEQ +1%2 ( set gotoLine=0 ) ELSE ( set gotoLine=%2 )
if exist %1 (
	CALL:OPEN_FILE %1
) else (
	call :shouldcreate %*
)
goto:eof

:OPEN_FILE
set "shouldcreate="
if [%create%] == [y] if not exist "%~1" (
	set "shouldcreate=+c"
	@REM echo. > "%~1"
	@REM echo File created: %1
)

	call p. file-open %shouldcreate% -backup -f %*
goto:eof

:shouldcreate
if [%2] == [-y] (
	set create=y
) else if [%2] == [y] (
	set create=y
) else (
	set "create="
	echo File doesn't exist
	set /p "create=-                  Create? "
)
if [%create%] == [] (
	call :altlocations %1
	goto:eof
) else if [%create%] == [n] (
	goto:eof
) else if [%create%] == [y] (
	echo Create chosen
	CALL:OPEN_FILE %1
	goto:eof
) else if [%create%] == [x] (
	echo exit
	goto:eof
) else if [%create%] == [n] (
	call :altlocations %1
) else (
	echo end create
	goto:eof
)
goto:eof
:altlocations

if not [%2] == [] (
	call p. file-open -backup -alias %*
) else if exist %* (
	CALL:OPEN_FILE %*
) else if exist %myTables%\%* (
	CALL:OPEN_FILE %myTables%\%*
) else if exist %myTables%\%*.json (
	CALL:OPEN_FILE %myTables%\%*.json
) else if exist %myTables%\%*.txt (
	CALL:OPEN_FILE %myTables%\%*.txt
) else if exist %python%\%*.py (
	CALL:OPEN_FILE %python%\%*.py
) else if exist %phpFiles%\%*.php (
	CALL:OPEN_FILE %phpFiles%\%*.php
) else if exist %scriptroot%\%*.bat (
	CALL:OPEN_FILE %scriptroot%\%*.bat
) else if exist %powershell%\%*.ps1 (
	CALL:OPEN_FILE %powershell%\%*.ps1
) else if exist D:\_Scott\S_Documents\Projects\self\Powershell\%*.ps1 (
	CALL:OPEN_FILE D:\_Scott\S_Documents\Projects\self\Powershell\%*.ps1
) else if exist %myPhp%\%*.php (
	CALL:OPEN_FILE %myPhp%\%*.php
) else if exist %myPowershell%\%*.ps1 (
	CALL:OPEN_FILE %myPowershell%\%*.ps1
) else if exist %myPython%\%*.py (
	CALL:OPEN_FILE %myPython%\%*.py
) else if exist %myDatabases%\%* (
	CALL:OPEN_FILE %myDatabases%\%*
) else if exist %myWebApp%\%* (
	CALL:OPEN_FILE %myWebApp%\%*
) else if exist %USERPROFILE%\Desktop\%* (
	CALL:OPEN_FILE %USERPROFILE%\Desktop\%*
) else if exist %dbTables%\%*.json (
	CALL:OPEN_FILE %dbTables%\%*.json
) else if exist %dbTables%\%* (
	CALL:OPEN_FILE %dbTables%\%*
) else (
	CALL:OPEN_FILE %*
)