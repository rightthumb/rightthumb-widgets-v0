@echo off
if not [%3] == [] (
		call p fileBackup -i "%batch%\%1.bat" %2 %3
	) else if not [%2] == [] (
		call p fileBackup -i "%batch%\%1.bat" %2
	) else (
		call p fileBackup -i "%batch%\%1.bat"
)
start "EDIT" %code_editor% "%batch%\%1.bat"
rem echo "%batch%\%1.bat"
