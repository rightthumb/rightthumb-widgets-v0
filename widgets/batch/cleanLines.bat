@echo off
set file=%1
set thisFile=cleanLines.php
%php% %phpFiles%\%thisFile%
echo.
echo.
::fmscripts
GOTO END
auditFMDB type > ~out.txt & cleanLines ~out.txt & del ~out.txt

:END