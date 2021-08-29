@echo off
call timestamp ats noEcho
set appPath=D:\techApps\Python
echo =============================================== >> %appPath%\log.txt
echo %now% >> %appPath%\log.txt
echo. >> %appPath%\log.txt
xcopy /s/d/y/c c:\Python27\*.* %appPath%\Python27\ >> %appPath%\log.txt
xcopy /s/d/y/c "D:\Users\Scott\AppData\Local\Programs\Python\Python36-32\*.*" "%appPath%\Python36-32\" >> %appPath%\log.txt
xcopy /s/d/y/c %appPath%\Python27\*.* c:\Python27\ >> %appPath%\log.txt
xcopy /s/d/y/c "%appPath%\Python36-32\*.*" "D:\Users\Scott\AppData\Local\Programs\Python\Python36-32\" >> %appPath%\log.txt

