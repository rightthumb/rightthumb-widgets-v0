@echo off &setlocal

rem ## {R2D2919B742E} ##
rem ###########################################################################
rem What if magic existed?
rem What if a place existed where your every thought and dream come to life.
rem There is only one catch: it has to be written down.
rem Such a place exists, it is called programming.
rem    - Scott Taylor Reph, RightThumb.com
rem ###########################################################################
rem ## {C3P0D40fAe8B} ##

if not exist ~ echo  " >~ & star string "
if not exist ~ goto END
set "search=%1"
set "em= -*#*- "
set "replace=%em%%search%%em%"
set "textfile=~"
set "newfile=_new.txt"

(for /f "delims=" %%i in ('findstr "^" "%textfile%"') do (
	set "line=%%i"
	setlocal enabledelayedexpansion
	set "line=!line:%search%=%replace%!"
	echo(!line!
	endlocal
))>"%newfile%"
type "%newfile%"
GOTO END

:end