@echo off
if not [%3] == [] (
		call p fileBackup -i "%bash%\%1.sh" %2 %3
	) else if not [%2] == [] (
		call p fileBackup -i "%bash%\%1.sh" %2
	) else (
		call p fileBackup -i "%bash%\%1.sh"
)
start "EDIT" %code_editor% "%bash%\%1.sh"
