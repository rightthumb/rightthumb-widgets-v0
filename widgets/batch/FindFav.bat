@echo off
title Favorites Name Search
set log=%userprofile%\Desktop\Fav,name.txt
prompt -

set /p find=Find:




cd "%userprofile%\Favorites\"
cls
dir /s/b | find /i "%find%" > "%log%"
start notepad "%log%"
cls
call %0