@echo off
set k=outlook.exe
taskkill /F /IM "%k%" /t
set k=spampal.exe
taskkill /F /IM "%k%" /t
set k=wcescomm.exe
taskkill /F /IM "%k%" /t
set k=wcesmgr.exe
taskkill /F /IM "%k%" /t
set k=

exit
taskkill /F /IM "%k%" /t
set k=
taskkill /F /IM "%k%" /t
set k=
taskkill /F /IM "%k%" /t
set k=
taskkill /F /IM "%k%" /t
set k=
taskkill /F /IM "%k%" /t
set k=
taskkill /F /IM "%k%" /t
set k=
taskkill /F /IM "%k%" /t
set k=
taskkill /F /IM "%k%" /t
set k=
taskkill /F /IM "%k%" /t
pause
shutdown -a -m %computername%