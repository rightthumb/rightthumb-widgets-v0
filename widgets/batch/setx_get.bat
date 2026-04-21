@echo off
set setx_get_arg=RT_%1
for /f "tokens=2*" %%A in ('reg query "HKCU\Environment" /v %setx_get_arg% ^| findstr /i "%setx_get_arg%"') do set "setx_get=%%B"