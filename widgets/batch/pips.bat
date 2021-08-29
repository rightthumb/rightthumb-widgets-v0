@echo off
set pathBackup=%path%


set path=%pathBackup:D:\Users\Scott\AppData\Local\Programs\Python\=D:\techApps\Python\%

"D:\techApps\Python\Python36-32\Scripts\pip.exe" %*

set path=%pathBackup:D:\Users\Scott\AppData\Local\Programs\Python\=D:\Users\Scott\AppData\Local\Programs\Python\%

"D:\Users\Scott\AppData\Local\Programs\Python\Python36-32\Scripts\pip.exe" %*

set path=%pathBackup:D:\Users\Scott\AppData\Local\Programs\Python\=D:\Apps\Python\%

"D:\Apps\Python\Python36-32\Scripts\pip.exe" %*

set path=%pathBackup%
rem "D:\techApps\Python\Python36-32\Scripts\pip.exe"
rem "D:\Users\Scott\AppData\Local\Programs\Python\Python36-32\Scripts\pip.exe"
rem "D:\Apps\Python\Python36-32\Scripts\pip.exe"