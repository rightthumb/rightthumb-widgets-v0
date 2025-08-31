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


SET VIDEO=%1
CALL :dequote VIDEO
if [%2] == [] (
	echo yAudio "%VIDEO%" & CALL autoMP3
	CALL yAudio "%VIDEO%" & CALL autoMP3
) else (
	echo yAudio "%VIDEO%" & CALL autoMP3 %2
	CALL yAudio "%VIDEO%" & CALL autoMP3 %2
)

Goto :eof
:DeQuote
for /f "delims=" %%A in ('echo %%%1%%') do set %1=%%~A
Goto :eof