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

set burnME="%stmp%\unclaimed_tickets_history\history-%Session_ID%.txt"

if exist %burnME% (
	CALL:ASK
) else (
	echo.
	echo no history
	echo.
	CALL:ASK
)
GOTO:EOF

:ASK
set /p ask= burn?  
if [%ask%] == [n] (
	echo no burn
) else (
	if [%ask%] == [N] GOTO:NOPE
	if exist %burnME% del %burnME%
	exit
)
GOTO:EOF

:NOPE
echo no burn
GOTO:EOF


rem CALL p. unix
rem rmdir /s /q %widgets%\widgets\python\burn\windows
rem rmdir /s /q %widgets%\widgets\python\burn\unix
rem mkdir %widgets%\widgets\python\burn\windows
rem mkdir %widgets%\widgets\python\burn\unix

rem xcopy /s/d/y/c %widgets%\widgets\python\src\unix\*.py %widgets%\widgets\python\burn\unix\
rem xcopy /s/d/y/c %widgets%\widgets\python\*.py %widgets%\widgets\python\burn\windows\