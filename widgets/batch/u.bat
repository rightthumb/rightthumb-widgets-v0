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





set "URL_VAR=%1"

if "%URL_VAR:~0,6%"=="https:" (
	call url. %*
	goto:eof
)

if [%1] == [] (
	call p. site -u -f last
) else (
	call p. site -u -f %* 
)

