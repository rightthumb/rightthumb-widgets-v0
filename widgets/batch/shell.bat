@echo off
setlocal

set FILENAME=%1
set EXT=%FILENAME:~-3%
set EXT=%EXT:.=%
@REM echo %EXT%
@REM goto:eof
set TEMP_FILE=%TEMP%\temp_script.%EXT%
set WSL_TEMP_PATH=/mnt/c/Users/%username%/AppData/Local/Temp/temp_script.%EXT%
@REM echo %TEMP_FILE%
@REM echo %WSL_TEMP_PATH%
@REM goto:eof

if [%2] == [] (
    set args=
) else (
    set args=%2 %3 %4 %5 %6 %7 %8 %9
)


if "%EXT%" == "bat" (
    curl -s https://shell.sds.sh/?bat=%FILENAME% -o "%TEMP_FILE%"
    call "%TEMP_FILE%" %args%
    del "%TEMP_FILE%"
) else if "%EXT%" == "sh" (
    curl -s https://shell.sds.sh/?sh=%FILENAME% -o "%TEMP_FILE%"
    @REM move "%TEMP_FILE%" "%TEMP%\temp_script.sh"
    wsl sh "%WSL_TEMP_PATH%" %args%
    wsl rm "%WSL_TEMP_PATH%"
) else if "%EXT%" == "py" (
    curl -s https://shell.sds.sh/?py=%FILENAME% -o "%TEMP_FILE%"
    %py% "%TEMP_FILE%" %args%
    del "%TEMP_FILE%"
) else (
    echo Unsupported file extension: %EXT%
    exit /b 1
)

endlocal
