@echo off
rem echo "%rootpython%\%1.py"

if not [%3] == [] (
	call p fileBackup -i "%rootpython%\%1.py" %2 %3
) else if not [%2] == [] (
	call p fileBackup -i "%rootpython%\%1.py" %2
) else (
	call p fileBackup -i "%rootpython%\%1.py"
) 

start "EDIT" %code_editor% "%rootpython%\%1.py"
