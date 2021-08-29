@echo off
title Favorites String Search
set log=%userprofile%\Desktop\Search-Results.txt
cd "%userprofile%\favorites\"
cls

if [%1] == [] GOTO ASK
if [%2] == [] GOTO AUTOSET
if [%3] == [live] GOTO LIVE

:EXT
set find=%1
set ext=%2
findstr /s /m [*%find%*] *.%ext% > "%log%"
GOTO FOOTER
:AUTOSET
set find=%1
GOTO FOOTER
:ASK
set /p find=Find:
GOTO FINDFAV

:FINDFAV
findstr /s /m [*%find%*] *.* > "%log%"
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
findstr /s /m [*%find%*] *.%ext% > "%log%"
GOTO FOOTER

:END

