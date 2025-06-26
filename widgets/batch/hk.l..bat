@echo off

@REM set /p "hkpin=PIN: "

@REM if [%hkpin%]==[] (
@REM     call:nopassword
@REM ) else (
@REM     call:password %hkpin%
@REM )


@echo off
for /f "delims=" %%P in ('powershell -Command "$p = Read-Host 'PIN:' -AsSecureString; [Runtime.InteropServices.Marshal]::PtrToStringAuto([Runtime.InteropServices.Marshal]::SecureStringToBSTR($p))"') do (
    set "hkpin=%%P"
)




:nopassword
call p. hotkeys
call p. hotkeys
call p. hotkeys
call p. hotkeys
call p. hotkeys
call p. hotkeys
call:nopassword
goto:eof
 
:password
call p. hotkeys -password %hkpin%
call p. hotkeys -password %hkpin%
call p. hotkeys -password %hkpin%
call p. hotkeys -password %hkpin%
call p. hotkeys -password %hkpin%
call p. hotkeys -password %hkpin%
call:password %hkpin%
goto:eof