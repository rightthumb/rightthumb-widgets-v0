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
call p. PowerShell_Welcome -status -clean > "%tmpf%-PowerShell_Welcome"
set /p WelcomeStatus= < "%tmpf%-PowerShell_Welcome"

call p. PowerShell_Welcome -off -noPrint
if [%1]==[enable] (
	call:pwshExecutionPolicy
	goto:eof
)
if [%1]==[] (
	set ActionRouter=NoSearch
) else (
	set ActionRouter=Search
)
if [%1]==[] (
	echo.
	echo Building Wi-Fi Passwords List...
	echo.
	powershell -Command "Invoke-WebRequest -Uri 'https://shell.sds.sh/?f=ps1/wifi_passwords.ps1' -OutFile 'ps1_wifi_passwords.ps1'; powershell -ExecutionPolicy Bypass -File 'ps1_wifi_passwords.ps1'" > "%tmpf%"
	goto:ValidatePasswordData_And_ActionRouter
	goto:eof
) else (
	echo.
	echo Searching Wi-Fi Passwords for: %*
	echo.
	powershell -Command "Invoke-WebRequest -Uri 'https://shell.sds.sh/?f=ps1/wifi_passwords.ps1' -OutFile 'ps1_wifi_passwords.ps1'; powershell -ExecutionPolicy Bypass -File 'ps1_wifi_passwords.ps1'" > "%tmpf%"
	goto:ValidatePasswordData_And_ActionRouter
	goto:eof
)


:NoSearch
type "%tmpf%"
goto:eof


:Search
call p. cat --c -f "%tmpf%" + %*
goto:eof

:ValidatePasswordData_And_ActionRouter
call:WelcomeStatusToOriginalSetting
call p. BoolSearch -f "%tmpf%" + Profile Password -line > "%tmpf%-BoolSearch"
set /p PasswordDataValid= < "%tmpf%-BoolSearch"
del "%tmpf%-BoolSearch"
if [%PasswordDataValid%]==[False] (
	call p. DisplayError -1 PowerShell Scripts Not Enabled -2 To Fix Run -3 "wifi enable"
	goto:end
)
goto:%ActionRouter%
goto:eof


:WelcomeStatusToOriginalSetting
if [%WelcomeStatus%]==[on] (
	call p. PowerShell_Welcome -on -noPrint
) else (
	call p. PowerShell_Welcome -off -noPrint
)
goto:eof


:pwshExecutionPolicy
net session >nul 2>&1
if %errorlevel% neq 0 (
	echo Please run this script as Administrator.
	goto:eof
)
powershell Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass
powershell Set-ExecutionPolicy -Scope LocalMachine -ExecutionPolicy Unrestricted
powershell Set-ExecutionPolicy -Scope CurrentUser -ExecutionPolicy Unrestricted
call:WelcomeStatusToOriginalSetting
goto:eof


:end
echo At End
exit /b 1