@echo off
if "%1" == "" (
	call p. PowerShell_Welcome -status
)
call p. PowerShell_Welcome %*