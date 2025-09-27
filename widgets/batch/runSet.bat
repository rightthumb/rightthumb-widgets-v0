@echo off

if "%~2"=="" (
	set "runSet=null"
	goto :eof
)

if not defined stmp set "stmp=%TEMP%"
if not exist "%stmp%" mkdir "%stmp%"

:: Run command and output to temp file
call %* > "%stmp%\runSet.txt" 2>&1

type "%stmp%\runSet.txt" > "%stmp%\runSet2.txt"

:: Read first line using redirect and set /p (no for-loop)
set "runSet="
< "%stmp%\runSet2.txt" set /p runSet=