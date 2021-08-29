@echo off
title TechReph Search Engine
set log=%userprofile%\Desktop\Search-Results.txt


if [%1] == [] GOTO ASK
:AUTOSET
set find=%1 %2 %3 %4
GOTO FINDFAV
:ASK
set /p find=Find:
GOTO FINDFAV

:FINDFAV
title (TechReph Search Engine) Finding: %find%

cls
echo Searching file content 
findstr /s /m "%find%" > "%log%"
echo ----------------------
echo Request find %find% 
echo %pc% found:
type "%log%"
echo ----------------------
start notepad "%log%"
GOTO END



if [] == [] Do%
:END


