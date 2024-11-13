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

set log=i.i
date /t > %log%
time /t >> %log%
dir /s/b  >> %log%


:TEST
echo index file %log% has been created
echo ============== >> \index\logs\i.log.txt
date /t >> \index\logs\i.log.txt
time /t >> \index\logs\i.log.txt
dir /b %log% >> \index\logs\i.log.txt

 
