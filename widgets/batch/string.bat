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

title String Search
set log=%userprofile%\Desktop\String-Search.txt
:cd "%userprofile%\favorites\"
cls

if [%1] == [] GOTO ASK
if [%2] == [] GOTO AUTOSET
if [%3] == [live] GOTO LIVE

:EXT
set find=%1
set ext=%2
findstr /i/s /m "%find%" *.%ext% > "%log%"
GOTO FOOTER
:AUTOSET
set find=%1
findstr /i/r "%find%" * > "%log%"
GOTO FOOTER
:ASK
set /p find=Find:
GOTO FINDFAV

:FINDFAV
findstr /i/r "%find%" * > "%log%"
GOTO FOOTER

if [] == [] Do%
:FOOTER
echo ----------------------
echo Request find %find% 
echo %pc% found:
type "%log%"
echo ----------------------
start notepad "%log%"
GOTO END

:LIVE
set find=%1
set ext=%2
findstr /i/s /m "%find%" *.%ext% > "%log%"
GOTO FOOTER

:END