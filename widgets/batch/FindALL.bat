:set debug=rem

rem ## {R2D2919B742E} ##
rem ###########################################################################
rem What if magic existed?
rem What if a place existed where your every thought and dream come to life.
rem There is only one catch: it has to be written down.
rem Such a place exists, it is called programming.
rem    - Scott Taylor Reph, RightThumb.com
rem ###########################################################################
rem ## {C3P0D40fAe8B} ##

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


 
