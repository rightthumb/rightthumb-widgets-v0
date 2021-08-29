@echo off
set to=c:\profile
mkdir "%to%"
echo.> "%to%\temp"
cls
netsh wlan show profiles
set /p profile=Profile ? 
set profile_export=Wireless Network Connection-%profile%.xml
set profile_fix=%profile%.xml

:EXPORT
netsh wlan export profile name="%profile%" folder="%to%"

:IMPORT
:netsh wlan add profile filename="%to%\%profile_fix%" user=all

:DELETE
:netsh wlan delete profile %profile%
ping 127.0.0.1 -l 1 -n 1 > "%to%\temp"
rename "%to%\%profile_export%" %profile_fix%
ping 127.0.0.1 -l 1 -n 1 > "%to%\temp"
explorer /select, "%to%\%profile%.xml"
del "%to%\temp"
