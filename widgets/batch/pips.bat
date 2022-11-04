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

set pathBackup=%path%


set path=%pathBackup:%USERPROFILE%\AppData\Local\Programs\Python\=D:\techApps\Python\%

"D:\techApps\Python\Python36-32\Scripts\pip.exe" %*

set path=%pathBackup:%USERPROFILE%\AppData\Local\Programs\Python\=%USERPROFILE%\AppData\Local\Programs\Python\%

"%USERPROFILE%\AppData\Local\Programs\Python\Python36-32\Scripts\pip.exe" %*

set path=%pathBackup:%USERPROFILE%\AppData\Local\Programs\Python\=D:\Apps\Python\%

"D:\Apps\Python\Python36-32\Scripts\pip.exe" %*

set path=%pathBackup%
rem "D:\techApps\Python\Python36-32\Scripts\pip.exe"
rem "%USERPROFILE%\AppData\Local\Programs\Python\Python36-32\Scripts\pip.exe"
rem "D:\Apps\Python\Python36-32\Scripts\pip.exe"

 
