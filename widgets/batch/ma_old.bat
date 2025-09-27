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


set alias=d:\tech\MyScripts\log\script-bookmarks\alias\a.%1.bat
GOTO START

:(setting temp path)
set where=%sroot%\script-bookmarks\alias\where.tmp
cd > "%where%"
set /p apath=<"%where%"
set alias=%scriptroot%\script-bookmarks\alias\a.%1.bat

--------------------
<ea batch
@echo off
:VAR
set alias=%scriptroot%\script-bookmarks\alias\a.%1.bat
GOTO BAT
notes:
ma  _alias_name
_file
:BAT
start notepad "%alias%"
GOTO END
:END
ea batch>
--------------------


:START
echo. >> %alias%
start notepad %alias%

GOTO END





:SKIP
set sroot=d:\tech\MyScripts\log
if not [%1] == [] GOTO AUTO
set /p alias=Name? 
set p=%sroot%\script-bookmarks\alias\a.%alias%.bat
GOTO SKIP


:debug
set /p do=Alias Command: 
echo. %do%
set /p run=Check by running? 
if [%run%] == [y] set /p call=Add 'CALL' as prefix for .bat? 
if [%call%] == [y] call %p%
if [%run%] == [y] %p%

:SKIP




GOTO END

:AUTO

set p=%sroot%\script-bookmarks\alias\a.%1.bat
shift
echo a.%*
set do=%*
echo %apath%\%do% >"%p%"


:END