@echo off
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