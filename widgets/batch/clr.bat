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

:http://ss64.com/nt/color.html
echo does not work
if ["%1"] == [""] GOTO END
if not exist ~ echo  " >~ & clr string "
if not exist ~ GOTO END
findstr /a:1 "%1" ~
:END