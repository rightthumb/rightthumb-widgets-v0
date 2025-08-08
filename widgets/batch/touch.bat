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

if [%1] == [] (
		call :ACTION1
	) else (
		call :ACTION2 %*
	)
GOTO:EOF
:ACTION1
cls
echo.
call p. touch ?
echo.
GOTO:EOF
:ACTION2
if [%2] == [] (
		call :ACTION3 %1
	) else (
		call :ACTION4 %*
	)
GOTO:EOF



:ACTION3
cls
echo.
call p. touch -f %1 -mod now
echo.
GOTO:EOF

:ACTION4
cls
echo.
call p. touch %*
echo.
GOTO:EOF