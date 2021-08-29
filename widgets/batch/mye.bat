@echo off
call p fileBackup -i "%myBatch%\%1.bat"
start "EDIT" %code_editor% "%myBatch%\%1.bat"
