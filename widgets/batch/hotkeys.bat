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


:if not exist "%systemroot%\system32\-monitor.bat" xcopy  /y %0 %systemroot%\system32\
mode 30,2
color 2f
call %userprofile%\rr
echo hotkeys listener
call p. hotkeys
