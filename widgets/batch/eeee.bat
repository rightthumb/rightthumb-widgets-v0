@echo off
set importFolder=%pyroot%\_rightThumb\_%1
set __init__="%importFolder%\__init__.py"
set initExample="%importFolder%\_%1_init_example.py"
set child="%importFolder%\_%1.py"
set childExample="%importFolder%\_%1_example.py"
if [%1] == [] (
		goto:eof
	) else (
		if not exist "%importFolder%\" md "%importFolder%\"

	)




if [%2] == [] (
		call p fileBackup -i %__init__%
		start "EDIT" %code_editor% %__init__%
	) else if [%2] == [-e] (
		start "EDIT" %code_editor% %initExample%
	) else if [%2] == [-build] (
		echo.
		set /p file=File Name: 
		if [%file%] == [] goto:eof
		call p fileBackup -i "%pyroot%\%file%.py"
		type %initExample% > "%pyroot%\%file%.py"
		call p fileBackup -i %initExample%
		start "EDIT" %code_editor% "%pyroot%\%file%.py"
	) else if [%3] == [] (
		call p fileBackup -i %child%
		start "EDIT" %code_editor% %child%
	) else if [%3] == [-e] (
		call p fileBackup -i %childExample%
		start "EDIT" %code_editor% %childExample%
	) else if [%3 == [-build] (
		echo.
		set /p file=File Name: 
		if [%file%] == [] goto:eof
		call p fileBackup -i "%pyroot%\%file%.py"
		call p fileBackup -i %childExample%
		type %childExample% > "%pyroot%\%file%.py"
		start "EDIT" %code_editor% "%pyroot%\%file%.py"
		
	)



rem epyi
rem eeee
