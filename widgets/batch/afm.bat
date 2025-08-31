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

CALL m back
CALL b fmaudit
set out={022D63C9-6556-9BB0-8A71-73659D88BA05}
set bat={84012C6C-5C99-0F37-F788-749098F91A09}.bat
set search=%1
findstr /i /r /m "%search%" "*.*" > %out%
set thisFile=fmr.php
ping google.com -n 1 >nul
%php% %phpFiles%\%thisFile%
ping google.com -n 1 >nul
if exist %bat% call %bat%
ping google.com -n 1 >nul
if exist %bat% del /q %bat%
if exist %out% del /q %out%
GOTO END
auditFMDB type > ~out.txt & cleanLines ~out.txt & del ~out.txt

:END
CALL b back

:: also fma