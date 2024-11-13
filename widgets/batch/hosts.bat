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

if ["%1"] == ["edit"] GOTO EDIT
if ["%1"] == ["e"] GOTO EDIT

type D:\Windows\System32\drivers\etc\hosts

GOTO END

:EDIT
call p. fileBackup -open -i D:\Windows\System32\drivers\etc\hosts
notepad D:\Windows\System32\drivers\etc\hosts

:END


 
