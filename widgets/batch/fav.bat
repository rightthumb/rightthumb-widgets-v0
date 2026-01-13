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

title Favorites Name Search
set log=%userprofile%\Desktop\Fav,name.txt


if [%1] == [] GOTO ASK
:AUTOSET
set find=%1
GOTO FINDFAV
:ASK
set /p find=Find:
GOTO FINDFAV

:FINDFAV
cd "%userprofile%\Favorites\"
cls
dir /s/b | find /i "%find%" > "%log%"
echo ----------------------
echo Request find %find% 
echo %pc% found:
type "%log%"
echo ----------------------
start notepad "%log%"
GOTO END



if [] == [] Do%
:END