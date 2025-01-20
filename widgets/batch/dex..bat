@echo off


if [%1] == [n] (
	call:name index.db
	goto:eof
)
if [%1] == [new] (
	call:name index.db
	goto:eof
)

call p. indexDBs -db index.db -r -update -type c %*

goto:eof



:contains
:: %1 - The variable value
:: %2 - The search string

echo %~1 | findstr /I /C:"%~2" >nul
if %errorlevel% equ 0 (
    echo The variable "%~1" contains "%~2".
) else (
    call :doesNotContain "%~1" "%~2"
)


if [%1] == [] (
	call:name index.db
	call p. indexDBs -db index.db -r -update -type c %*
	@REM call p. indexDB-files
) else (
	call:name %1
	@REM call p. indexDB-files -db %1
	call p. indexDBs  -r -update -type c -db %*
)
goto:eof
:name
if exist %1 (
	call nd %1
)
goto:eof