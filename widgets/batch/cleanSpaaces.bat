@echo off
set file=%1
set thisFile=cleanSpaces.php
%php% %phpFiles%\%thisFile%
echo.
echo.
::fmscripts
GOTO END
drivers > ~out.txt & cleanSpaces ~out.txt > ~out.txt & parse ~out.txt "," 2  & del ~out.txt

:END