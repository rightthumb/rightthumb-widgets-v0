:set debug=rem
%debug%@echo off
title Find
set /p search=Enter Criteria-::
title Find %search%
set switch= /b /s
set log=%USERPROFILE%\desktop\search.txt
date /t > "%log%"
c:
echo c:
cd\
dir %search% %switch% >> "%log%"
f:
echo F:
cd\
dir %search% %switch% >> "%log%"
g:
echo G:
cd\
dir %search% %switch% >> "%log%"
h:
echo H:
cd\
dir %search% %switch% >> "%log%"
start notepad "%log%"
rem ----------------------------
cls
%debug%call %0

exit
pause
rem ----------------------------
i:
echo I:
cd\
dir %search% %switch% >> "%log%"
