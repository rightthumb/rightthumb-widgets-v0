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




CALL p popFile -f %1 > %tmpf%

rem echo 1 "%1"
SET /p folder=<%tmpf%
rem echo f "%folder%"
%folder:~0,1%:
cd "%folder%"
echo %folder%
echo.

 
