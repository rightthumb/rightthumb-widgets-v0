@echo off
CALL p popFile -f %1 > %tmpf%

rem echo 1 "%1"
SET /p folder=<%tmpf%
rem echo f "%folder%"
%folder:~0,1%:
cd "%folder%"
