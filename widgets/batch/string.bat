@echo off
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

