@echo off

rem ## {R2D2919B742E} ##
rem ###########################################################################
rem What if magic existed?
rem What if a place existed where your every thought and dream come to life.
rem There is only one catch: it has to be written down.
rem Such a place exists, it is called programming.
rem    - Scott Taylor Reph, RightThumb.com
rem ###########################################################################
rem ## {C3P0D40fAe8B} ##


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
@REM echo %*
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
		@REM echo %rtAppX%
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

			rem call p. fileBackup -open -i %childExample% -python
			call p. file-open -app %code_editor% -f %childExample% -backup
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
			rem call p. fileBackup -open -i %child% -python
			call p. file-open -app %code_editor% -f %child% -backup
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

		rem call p. fileBackup -open -i "%importFolder%\%fileName%.py" -python
		call p. file-open -app %code_editor% -f "%importFolder%\%fileName%.py" -backup
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
	rem call p. fileBackup -open -i "%python%\%fileName%.py" -python
	type %initExample% > "%python%\%fileName%.py"
	rem call p. fileBackup -open -i "%python%\%fileName%.py" -python
	call p. file-open -app %code_editor% -f "%python%\%fileName%.py" -backup
	rem echo %python%\%fileName%.py
	goto:eof
:BUILDFILE_TRUE
	echo App already exists
	set /p action=Replace App?: 
	if [%action%] == [y] (
			rem call p. fileBackup -open -i "%python%\%fileName%.py" -python
			type %initExample% > "%python%\%fileName%.py"
		) else (
			rem call p. fileBackup -open -i "%python%\%fileName%.py" -python
		)

	call p. file-open -app %code_editor% -f "%python%\%fileName%.py" -backup
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
			rem call p. fileBackup -open -i %__init__% -python
			if [%isNew%] == [Y] echo %template% %__init__%
			if [%isNew%] == [Y] type %template% > %__init__%
			call p. file-open -app %code_editor% -f %__init__% -backup
			rem echo %__init__%
		) else (
			goto:eof
		)
	goto:eof
:EXAMPLE
	rem call p. fileBackup -open -i %initExample% -python
	call p. file-open -app %code_editor% -f %initExample% -backup
	rem echo %initExample%
	goto:eof
:SAMPLE
	rem call p. fileBackup -open -i %childSample% -python
	call p. file-open -app %code_editor% -f %childSample% -backup
	rem echo %childSample%
	goto:eof
:CMDP
	if exist %childCommands% (
			cls
			echo.
			type %childCommands%
		) else (
			rem call p. fileBackup -open -i %childCommands% -python
			call p. file-open -app %code_editor% -f %childCommands% -backup
			rem echo %childCommands%
		)
	echo.
	echo.
	echo.
	rem echo %childCommands%
	goto:eof
:CMDE
	rem call p. fileBackup -open -i %childCommands% -python
	call p. file-open -app %code_editor% -f %childCommands% -backup
	rem echo %childCommands%
	echo.
	echo.
	echo.
	rem echo %childCommands%
	goto:eof


goto:eof
rem epyi
rem eeee