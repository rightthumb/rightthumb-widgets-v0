@echo off
set to=c:\profile
:mkdir "%to%"
echo.> "%to%\temp"
cls
set "replace= "
netsh wlan show profiles|find "All User Profile" > "%to%\temp"
for /f "tokens=5-10 delims= " %%a in (%to%\temp) do (
    set "line='%%a %%b %%c %%d %%e %%f'"
    setlocal enabledelayedexpansion
    set "line=!line:%replace%%replace%=!"
    set "line=!line:%replace%'='!"
    set "line=!line:'=!"
    netsh wlan export profile name="!line!" folder="%to%"
    endlocal
)
del "%to%\temp"
