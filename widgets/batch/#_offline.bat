@echo off
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
