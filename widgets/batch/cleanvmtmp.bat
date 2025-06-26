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

call m tmp0
call b vmtmp
call m test
set /p test=<%sroot%\script-bookmarks\BM-test.txt
if NOT ["%test%"] == ["%USERPROFILE%\AppData\Local\Temp\vmware-Scott\VMwareDnD"] GOTO ERROR




@attrib -r "%USERPROFILE%\AppData\Local\Temp\vmware-Scott\VMwareDnD\*.*" /s > ~

del ~ /q
del *.* /s/q 

GOTO END
:ERROR
echo ERROR
:END
call b tmp0
 
 
 
 
 
 
 
 
 


 
