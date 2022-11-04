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

echo Press Q when done
"D:\Program Files (x86)\Windows Kits\10\Debuggers\x64\kd.exe" -z %1 -y srv*c:\pubsymbols*http://msdl.microsoft.com/download/symbols | find /i "Probably"


 
