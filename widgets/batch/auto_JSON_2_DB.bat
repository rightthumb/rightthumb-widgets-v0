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

CALL %USERPROFILE%\cc.bat

echo conversion issue
CALL p. json2DB -build -app -i %1
echo b issue
CALL b db
echo dba issue
CALL p. dba -app %1
PAUSE
PAUSE