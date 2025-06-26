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

SET /p Drive=<%userprofile%\.tk421
SET widgets=%Drive:~0,1%
CALL %widgets%\widgets\batch\c.bat
CALL b lynx
SET do=%1
zip appServer.%do% appServer.%do%
SET /p pause=pause: 

 
