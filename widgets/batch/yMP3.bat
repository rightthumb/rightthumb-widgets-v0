@echo off

SET VIDEO=%1
CALL :dequote VIDEO
if [%2] == [] (
	CALL yAudio "%VIDEO%" & CALL autoMP3
) else (
	CALL yAudio "%VIDEO%" & CALL autoMP3 %2
)

Goto :eof
:DeQuote
for /f "delims=" %%A in ('echo %%%1%%') do set %1=%%~A
Goto :eof

