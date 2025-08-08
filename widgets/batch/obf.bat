@echo off



if "%2"=="" echo Usage: obf ^<input_file^> ^<output_file^>
if "%2"=="" exit /b 1

setlocal

set "file=%~1"
set "ext=%~x1"


if /i "%ext%"==".py" (
	call :py_dst_nd "%2"
	copy "%1" "%2"
	pyarmor obfuscate "%2"
) else if /i "%ext%"==".php" (
	php %ww%\obfuscators\yakpro-po\yakpro-po.php  "%1" -o "%2"
) else if /i "%ext%"==".js" (
	javascript-obfuscator "%1" --output "%2"
) else (
	echo works with .py, .php, and .js files only.
)
goto :eof
:rename_src
set "filename=file.js"

:: Extract base name without extension
for %%F in ("%filename%") do (
	set "basename=%%~nF"
)

:: Rename the file
ren "%filename%" "%basename%.src.js"
goto :eof

:py_dst_nd
if exist "%1" call nd "%1"
goto :eof


endlocal