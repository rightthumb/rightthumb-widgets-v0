@echo off
call p fileBackup -i "%powershell%\%1.ps1"
start "EDIT" %code_editor% "%powershell%\%1.ps1"
