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

set spa_notes=D:\Documents and Settings\Scott\My Documents\Sites\Spa_Moritz2010\spa_notes.txt

if ["%1"] == ["log"] start notepad "%spa_notes%"
if ["%1"] == ["log"] GOTO END

if ["%1"] == [""] set /p spa_note=Note? 
if not ["%1"] == [""] set n=%1 %2 %3 %4 %5 %6 %7 %8 %9

echo ========================== >> "%spa_notes%"
echo %date% @ %time% >> "%spa_notes%"

echo %spa_note% >> "%spa_notes%"

:END

 
