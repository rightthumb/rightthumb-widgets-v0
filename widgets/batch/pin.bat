@echo off


:: Backup: fileBackup.json, to the recover folder
call p. fileBackupBackupBackup >nul 2>&1
:: Backup: fileBackup.json, to the recover folder




if [%isPWSH%] == [] (
	call isPWSH
	@REM call isPWSH print
)
@REM echo pin isPWSH = %isPWSH%
if [%isPWSH%] == [yes] (
	echo PowerShell, No Pin Support
	goto :end
)
set asked=0
if "%1" == "-ask" (
	echo ask>"%stmp%/pin_ask"
) else if "%1" == "-noask" (
	call :noask
)

if "%vault_pin%" == "" (
	call :ask
) else (
	call :check
)
goto :end

:noask
if exist "%stmp%/pin_ask" (
	del "%stmp%/pin_ask"
	echo ask setting removed
) else (
	echo no ask setting found
)
goto :end

:ask
set /a asked+=1
if %asked% gtr 3 (
	echo too many attempts
	pause
	call x
	exit
)
call p loginPIN
set /p vault_pin=<"%stmp%/pin"
call rm "%stmp%/pin" --c
if not exist "%rt%\profile\config\.vault.%vault_pin%" (
	call :ask
) else (
	echo pin set
)
goto :end

:check
if not exist "%rt%\profile\config\.vault.%vault_pin%" (
	call :ask
) else (
	echo pin is set
)
goto :end
:end

if [%vault_pin%] == [] (
	prompt └─ 
	set "vpDot="
) else (
	set "vpDot=."
	prompt └─. 
)
@REM TITLE %vpDot%%terminalTitle%