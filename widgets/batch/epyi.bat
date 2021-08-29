@echo off

set rtApp=%1
if [%1] == [base] set rtApp=base%PYTHON_BASE%

set importFolder=%python%\_rightThumb\_%rtApp%
set __init__="%importFolder%\__init__.py"
set initExample="%importFolder%\_%rtApp%_init_example.py"
set child="%importFolder%\_%rtApp%.py"
set childExample="%importFolder%\_%rtApp%_example.py"
set childSample="%importFolder%\_%rtApp%_sample.py"
set childCommands="%importFolder%\_commands.py"


SET template="%myImports%\_base%PYTHON_BASE%\_base%PYTHON_BASE%_init_example.py"

rem echo 1 %1
rem echo 2 %2
rem goto:eof
set fileName=
if [%1] == [?] (
		call :HELP
		goto:eof
	)

if [%1] == [] (
		goto:eof
	)

if [%2] == [] (
		CALL :INIT %*
		goto:eof
	) else if [%2] == [-e] (
		CALL :EXAMPLE %*
		goto:eof

	) else if [%2] == [-c] (
		set rtAppX=%3
		set child="%importFolder%\_%rtAppX%.py"
		CALL :INIT_CHILD %*
		goto:eof
	
	) else if [%2] == [-child] (
		set rtAppX=%3
		set child="%importFolder%\_%rtAppX%.py"
		CALL :INIT_CHILD %*
		goto:eof
	
	) else if [%2] == [-childe] (
		set rtAppX=%3
		set childExample="%importFolder%\_%rtAppX%_example.py"
		CALL :INIT_CHILD_EXAMPLE %*
		goto:eof

	) else if [%2] == [-ce] (
		set rtAppX=%3
		set childExample="%importFolder%\_%rtAppX%_example.py"
		CALL :INIT_CHILD_EXAMPLE %*
		goto:eof


	) else if [%2] == [-build] (
		CALL :BUILD %*
		goto:eof
	) else if [%2] == [-s] (
		CALL :SAMPLE %*
		goto:eof
	) else if ["%2"] == ["-cmd"] (
		CALL :CMDP %*
		goto:eof
	) else if ["%2"] == ["-cmde"] (
		CALL :CMDE %*
		goto:eof
	) else if ["%2"] == ["-file"] (
		CALL :FILE %*
		goto:eof
	) else if ["%2"] == ["-f"] (
		CALL :FILE %*
		goto:eof
	)

goto:eof
:HELP
	echo epyi base                   edit init import
	echo.
	echo epyi base -build newApp     create new app
	echo epyi base -e                edit new app template
	echo.
	echo epyi base -cmd              print list of commands
	echo epyi base -cmde             edit list of commands
	echo.
	echo epyi base -s                edit sample
	echo.
	goto:eof



:INIT_CHILD_EXAMPLE
	if not exist "%childExample%" (
			set /p initOpen=Create new init child example? 
		) else (
			set initOpen=y
		)
	if [%initOpen%] == [y] (

			call p fileBackup -i %childExample% -python
			start "EDIT" %code_editor% %childExample%
			goto:eof

		) else (
			goto:eof
		)

:INIT_CHILD
	if not exist "%child%" (
			set /p initOpen=Create new init? 
			set isNew=Y
		) else (
			set initOpen=y
			set isNew=N
		)
	if [%initOpen%] == [y] (
			if not exist "%importFolder%\" md "%importFolder%\"
			call p fileBackup -i %child% -python
			start "EDIT" %code_editor% %child%
			echo %child%
		) else (
			goto:eof
		)
	goto:eof


:FILE
	if [%3] == [] (
			echo.&set /p fileName=fileName Name: 
		) else (
			set fileName=%3
		)
		rem echo.
		rem set /p fileName=fileName Name: 
		rem echo %fileName%
		if [%fileName%] == [] goto:eof

		call p fileBackup -i "%importFolder%\%fileName%.py" -python
		start "EDIT" %code_editor% "%importFolder%\%fileName%.py"
		rem echo %importFolder%\%fileName%.py

	goto:eof

:BUILD
	if [%3] == [] (
			echo.&set /p fileName=fileName Name: 
		) else (
			set fileName=%3
		)
		rem echo.
		rem set /p fileName=fileName Name: 
		rem echo %fileName%
		if [%fileName%] == [] goto:eof

	if exist "%python%\%fileName%.py" (
			CALL :BUILDFILE_TRUE %*
		) else (
			CALL :BUILDFILE_FALSE %*
		)
	goto:eof
:BUILDFILE_FALSE
	call p fileBackup -i "%python%\%fileName%.py" -python
	type %initExample% > "%python%\%fileName%.py"
	call p fileBackup -i "%python%\%fileName%.py" -python
	start "EDIT" %code_editor% "%python%\%fileName%.py"
	rem echo %python%\%fileName%.py
	goto:eof
:BUILDFILE_TRUE
	echo App already exists
	set /p action=Replace App?: 
	if [%action%] == [y] (
			call p fileBackup -i "%python%\%fileName%.py" -python
			type %initExample% > "%python%\%fileName%.py"
		) else (
			call p fileBackup -i "%python%\%fileName%.py" -python
		)

	start "EDIT" %code_editor% "%python%\%fileName%.py"
	rem echo %python%\%fileName%.py
	goto:eof
:INIT
	if not exist "%__init__%" (
			set /p initOpen=Create new init? 
			set isNew=Y
		) else (
			set initOpen=y
			set isNew=N
		)
	if [%initOpen%] == [y] (
			if not exist "%importFolder%\" md "%importFolder%\"
			call p fileBackup -i %__init__% -python
			if [%isNew%] == [Y] echo %template% %__init__%
			if [%isNew%] == [Y] type %template% > %__init__%
			start "EDIT" %code_editor% %__init__%
			rem echo %__init__%
		) else (
			goto:eof
		)
	goto:eof
:EXAMPLE
	call p fileBackup -i %initExample% -python
	start "EDIT" %code_editor% %initExample%
	rem echo %initExample%
	goto:eof
:SAMPLE
	call p fileBackup -i %childSample% -python
	start "EDIT" %code_editor% %childSample%
	rem echo %childSample%
	goto:eof
:CMDP
	if exist %childCommands% (
			cls
			echo.
			type %childCommands%
		) else (
			call p fileBackup -i %childCommands% -python
			start "EDIT" %code_editor% %childCommands%
			rem echo %childCommands%
		)
	echo.
	echo.
	echo.
	rem echo %childCommands%
	goto:eof
:CMDE
	call p fileBackup -i %childCommands% -python
	start "EDIT" %code_editor% %childCommands%
	rem echo %childCommands%
	echo.
	echo.
	echo.
	rem echo %childCommands%
	goto:eof


goto:eof
rem epyi
rem eeee