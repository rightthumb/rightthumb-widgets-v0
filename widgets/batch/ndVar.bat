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

set input=%1
set input
set input=%input:"=%
call :getFile %1
GOTO NEXT
:getFile
set fileName=%~nx1
GOTO NEXT

:NEXT
if ["%input%"] == [""] GOTO END
set cnt=0
set log=%temp%\~nd_tmp.txt

dir "%input%" | find "/" > _tmp
set /p modraw=< _tmp
set mod=%modraw:~0,10%
set moddate=%mod:~-4,4%.%mod:~-10,2%.%mod:~-7,2%
del _tmp


if exist "%moddate%-%input%" goto DUPLICATE
goto UNIQUE

:DUPLICATE
echo Duplicate Actions

:LOOP
set /a  cnt=%cnt%+1
set check=%moddate%-%cnt%-%input%

 IF EXIST "%check%" (
	GOTO LOOP
 ) ELSE (
	set ndVar=%moddate%-%cnt%-%fileName%
	echo %check%
 )

goto END

:UNIQUE
set name=%moddate%-%input%
set ndVar=%moddate%-%fileName%
echo %name%
goto END


:END
 

:echo %name% > "%log%"
set "cnt="
set "modraw="
set "mod="
set "moddate="
set "check="
set "name="