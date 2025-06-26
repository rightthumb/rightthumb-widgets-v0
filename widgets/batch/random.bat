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


rem %py% %widgets%\widgets\remote\python\%1.py %*

CALL p. genuuid 
CALL p. genuuid -e
CALL p. genuuid -short
CALL p. genuuid -short -e
rem %py% -c "import random; print(random.randrange(100000000000000,1000000000000000));"
%py% -c "import time; e=time.time(); print(int(e));" 
