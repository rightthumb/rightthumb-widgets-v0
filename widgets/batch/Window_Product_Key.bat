@echo off

rem License

cls
echo.
echo.
echo        Domain: %USERDOMAIN%
echo      Computer: %COMPUTERNAME%

setlocal
set "batchPath=%~dp0"
set "vbsGetKey=%batchPath%getWinKey.vbs"

if not exist "%vbsGetKey%" echo WScript.Echo GetObject("winmgmts:").ExecQuery("select * from SoftwareLicensingService").ItemIndex(0).OA3xOriginalProductKey> "%vbsGetKey%"
if exist "%vbsGetKey%" attrib +h "%vbsGetKey%"

set "licenseFolder=%batchPath%Licenses"
if not exist "%licenseFolder%" mkdir "%licenseFolder%"

set "theFile=%licenseFolder%\%computername%.txt"

rem echo Please wait...
echo ________________________________________ > "%theFile%"
echo        Domain: %USERDOMAIN%  >> "%theFile%"
echo      Computer: %COMPUTERNAME%  >> "%theFile%"
for /f "delims=" %%a in ('cscript.exe //nologo "%vbsGetKey%"') do set "productKey=%%a"


echo %productKey% | find "-" > nul
if errorlevel 1 (
    echo   Product Key: OEM >> "%theFile%"
    echo   Product Key: OEM
) else (
    echo   Product Key: %productKey% >> "%theFile%"
    echo   Product Key: %productKey%
)
echo.
echo.
pause
