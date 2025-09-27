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

::set thisTimeStamp=%date:~-4,4%.%date:~-10,2%.%date:~-7,2%@%time:~0,2%:%time:~3,2%
set thisTimeStamp=%date:~-4,4%.%date:~-10,2%.%date:~-7,2%.%time:~0,2%.%time:~3,2%
echo %thisTimeStamp% > %widgets%\tech\scripts\verDate.txt
::echo :)