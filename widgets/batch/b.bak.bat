:v2

rem ## {R2D2919B742E} ##
rem ###########################################################################
rem What if magic existed?
rem What if a place existed where your every thought and dream come to life.
rem There is only one catch: it has to be written down.
rem Such a place exists, it is called programming.
rem    - Scott Taylor Reph, RightThumb.com
rem ###########################################################################
rem ## {C3P0D40fAe8B} ##

@echo off

if [%1] == [HELP] GOTO HELP
if [%1] == [help] GOTO HELP
if [%1] == [h] GOTO HELP


set sroot=D:\tech\MyScripts\log
set p=%sroot%\script-bookmarks\BM-%1.txt
set /p back=<"%p%"
set bname=%1


if not [%2] == [] GOTO CHECKVAR
if [%1] == [HELP] GOTO HELP

cd %back%
GOTO END


:CHECKVAR
if [%2] == [-e] dir "%back%\*.exe" /s/b 
if [%2] == [-run] (set run="%back%\%3" | echo run= %run%)



GOTO END
:HELP
echo.==================================
echo examples: 7z represents bookmark
echo.
echo. bm cd change:     b 7z 
echo. bm list exe:      b 7z -e
echo. bm file as var:   b 7z -run 7z.exe
echo. 

:END




 
