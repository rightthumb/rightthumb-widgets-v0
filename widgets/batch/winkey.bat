@echo off
setlocal
set "batchPath=%~dp0"
set "vbsGetKey=%batchPath%getWinKey.vbs"

if not exist "%vbsGetKey%" echo WScript.Echo GetObject("winmgmts:").ExecQuery("select * from SoftwareLicensingService").ItemIndex(0).OA3xOriginalProductKey> "%vbsGetKey%"

echo Please wait...

cscript.exe "%vbsGetKey%"

pause