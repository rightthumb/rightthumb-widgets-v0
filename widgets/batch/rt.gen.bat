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

set rt_base=D:\.rightthumb-widgets\widgets

if exist %rt_base%\bash\ (
  rmdir /s/q %rt_base%\bash\
)
if exist %rt_base%\batch\ (
  rmdir /s/q %rt_base%\batch\
)
if exist %rt_base%\databank\ (
  rmdir /s/q %rt_base%\databank\
)
if exist %rt_base%\powershell\ (
  rmdir /s/q %rt_base%\powershell\
)
if exist %rt_base%\python\ (
  rmdir /s/q %rt_base%\python\
)

mkdir %rt_base%\bash\
mkdir %rt_base%\batch\
mkdir %rt_base%\databank\
mkdir %rt_base%\powershell\
mkdir %rt_base%\python\

xcopy /s/d/y/c %widgets%\widgets\bash\ %rt_base%\bash\
xcopy /s/d/y/c %widgets%\widgets\batch\ %rt_base%\batch\
xcopy /s/d/y/c %widgets%\widgets\databank\ %rt_base%\databank\
xcopy /s/d/y/c %widgets%\widgets\powershell\ %rt_base%\powershell\
xcopy /s/d/y/c %widgets%\widgets\python\*.py %rt_base%\python\

 
