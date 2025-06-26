@echo off
setlocal

set schema=%stmp%\gpt.prompt



:: Default to index.db
set "db=index.db"

:: Check if the argument exists
if not "%~1"=="" (
    echo %~1 | findstr /i "\.db \.sqlite" >nul
    if not errorlevel 1 (
        set "db=%~1"
    )
)

call schema %db% > %schema%

call p. gpt    --s "act as an expert in sqlite sql one liners."        -p "schema of sqlite db" "%schema%" "query sqlite in one line  %*     db file path: %db%" | call p. script-helper + sqlite3 -sq > %stmp%\gpt.bat

@REM call %stmp%\gpt.bat
echo.
echo.
type %stmp%\gpt.bat
echo.
echo.
@REM echo %prompt%
set /p prompt=<%stmp%\gpt.bat

set /p "run=Run: "
if "%run%"=="y" call %stmp%\gpt.bat
endlocal
