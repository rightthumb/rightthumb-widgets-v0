@echo off

REM If no arguments, default to index.db
if [%1] == [] (
	call :name index.db
	call p. indexDB-files
	goto :eof
)

REM If %1 contains ".db", use -db switch
echo %1 | findstr /i "\.db" >nul
if not errorlevel 1 (
	call :name %1
	echo %1
	call p. indexDB-files -db %*
) else (
	call p. indexDB-files + %*
)
goto :eof

:name
if exist %1 (
	call nd %1
)
goto :eof