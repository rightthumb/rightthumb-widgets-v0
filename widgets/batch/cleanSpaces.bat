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

set file=%1
set thisFile=cleanSpaces.php
%php% %phpFiles%\%thisFile%
echo.
echo.
::fmscripts
GOTO END
drivers > ~out.txt & cleanSpaces ~out.txt > ~out2.txt & parse ~out2.txt "," 2  & del ~out*

:END