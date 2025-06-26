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

mode 50,30
echo offline
echo offline
echo offline
echo offline
echo offline
echo offline
echo offline

set count=
  :blink

  set count=%count%-
color %blink_0_color%
@ping 127.0.0.1 -n %b_delay% -l 10> nul
color %blink_1_color%
@ping 127.0.0.1 -n %b_delay% -l 10> nul

  if not "%count%"=="-------" %then% GOTO blink
exit


 
