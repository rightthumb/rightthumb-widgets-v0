@echo off
set app=WinDvr.exe
taskkill /F /IM %app% /t
set app=WinScheduler.exe
taskkill /F /IM %app% /t
set app=WinIEPG.exe
taskkill /F /IM %app% /t
set app=WinCinemaMgr.exe
taskkill /F /IM %app% /t
set app=WCreator.exe
taskkill /F /IM %app% /t
exit
set app=
taskkill /F /IM %app% /t
set app=
taskkill /F /IM %app% /t
set app=
taskkill /F /IM %app% /t