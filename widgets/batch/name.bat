@echo off
set /p n=<name.txt
set /p pc=<pc.txt
set old=%code_editor%
title name change: old = %code_editor%
IF "%1" == "pc" GOTO PC
IF "%1" == "" GOTO NAME

:AUTO
set n=%1
echo %code_editor% > name.txt
cls
echo New name is %code_editor%
GOTO END

:NAME
echo Name is now: %code_editor% 
set /p n=New Name?:
echo %code_editor% > name.txt
cls
echo New name is %code_editor%
GOTO END

:PC
IF NOT "%2" == "pc" GOTO AUTOPC
echo PC name is now: %code_editor% 
set /p n=New PC Name?:
echo %code_editor% > pc.txt
cls
echo New name is %code_editor%
GOTO END

:AUTOPC
set n=%2
echo %code_editor% > pc.txt
cls
echo New PC name is %code_editor%
set
GOTO END

:END
echo -------------------------
title name change: old = %old% , new = %code_editor%
pause
