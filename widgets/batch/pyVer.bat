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

::call pyVer %1
find /c "#A1695618" "%python%\%1.py"
if %errorlevel% equ 1 call :notfound %1
GOTO :EOF
:notfound
%py% "%python%\2to3.py" -w %1
%py% "%python%\labelFile.py" %1 #A1695618-Converted
call pyVer2 %1
GOTO :EOF

 
