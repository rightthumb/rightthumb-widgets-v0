@echo off
IF EXIST E:\tech\scripts\instanceID.sys (set /p test=<E:\tech\scripts\instanceID.sys echo E:\) & IF [%test%] == [%adminID%] (set adminDrive=E:\&GOTO END)
echo.
echo NOT END
:END
echo.
echo END