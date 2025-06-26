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

title Changing name and pc
cd %systemroot%\system32
set /p n=<name.txt
set /p pc=<pc.txt
set oldn=%code_editor%
set oldpc=%pc%



:AUTO
set n=%1
echo %code_editor% > name.txt
cls
echo New name is %code_editor%
:GOTO END


:AUTOPC
set pc=%2
echo %pc% > pc.txt
cls
echo New Name is %code_editor%
echo New PC name is %pc%
GOTO END

:END
echo -------------------------
title name: [old = %old% , new = %code_editor%] PC: [old = %oldpc% , new = %pc%] 




 
