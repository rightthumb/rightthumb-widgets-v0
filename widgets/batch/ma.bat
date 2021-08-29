@echo off
set alias=%myBatch%\a.%1.bat
if not [%3] == [] (
		call p fileBackup -i "%alias%" %2 %3
	) else if not [%2] == [] (
		call p fileBackup -i "%alias%" %2
	) else (
		call p fileBackup -i "%alias%"
)
start "EDIT" %code_editor% "%alias%"
rem echo "%alias%"
