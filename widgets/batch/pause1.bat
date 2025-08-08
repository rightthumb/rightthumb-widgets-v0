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

IF NOT [%1] == [] (SET b_delay=%1)
IF [%1] == [] (SET b_delay=2)
ping 127.0.0.1 -n %b_delay% -l 10 > "%stmp%\~"
IF EXIST "%stmp%\~" (del "%stmp%\~")