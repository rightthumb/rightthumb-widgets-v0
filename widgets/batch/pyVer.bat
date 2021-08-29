@echo off
::call pyVer %1
find /c "#A1695618" "%python%\%1.py"
if %errorlevel% equ 1 call :notfound %1
GOTO :EOF
:notfound
%py% "%python%\2to3.py" -w %1
%py% "%python%\labelFile.py" %1 #A1695618-Converted
call pyVer2 %1
GOTO :EOF