@echo off
call m tmp0
call b vmtmp
call m test
set /p test=<%sroot%\script-bookmarks\BM-test.txt
if NOT ["%test%"] == ["D:\Users\Scott\AppData\Local\Temp\vmware-Scott\VMwareDnD"] GOTO ERROR




@attrib -r "D:\Users\Scott\AppData\Local\Temp\vmware-Scott\VMwareDnD\*.*" /s > ~

del ~ /q
del *.* /s/q 

GOTO END
:ERROR
echo ERROR
:END
call b tmp0
 
 
 
 
 
 
 
 
 
