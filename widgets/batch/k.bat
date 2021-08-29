@echo off

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