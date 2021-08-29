@echo off
rem echo "%python%\%1.py"

if not [%3] == [] (
	call p fileBackup -i "%python%\%1.py" %2 %3 -python
) else if not [%2] == [] (
	call p fileBackup -i "%python%\%1.py" %2 -python
) else (
	call p fileBackup -i "%python%\%1.py" -python
) 

start "EDIT" %code_editor% "%python%\%1.py"
