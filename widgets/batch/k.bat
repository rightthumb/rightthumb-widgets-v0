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


set t=quickset.exe
taskkill /F /IM "%t%" /t
set t=Directcd.exe
taskkill /F /IM "%t%" /t
set t=awhost32.exe
taskkill /F /IM "%t%" /t
set t=realsched.exe
taskkill /F /IM "%t%" /t
set t=msmsgs.exe
taskkill /F /IM "%t%" /t
set t=qttask.exe
taskkill /F /IM "%t%" /t
set t=SMSS.EXE
taskkill /F /IM "%t%" /t
set t=mm_tray.exe
taskkill /F /IM "%t%" /t
set t=msmsgs.exe
taskkill /F /IM "%t%" /t
set t=autorunusb.exe
taskkill /F /IM "%t%" /t
exit
set t=
taskkill /F /IM "%t%" /t
set t=
taskkill /F /IM "%t%" /t
shutdown -a -m %computername%