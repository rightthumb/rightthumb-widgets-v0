@echo off
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


