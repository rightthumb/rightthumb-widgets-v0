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



IF 1%2 NEQ +1%2 ( set gotoLine=0 ) ELSE ( set gotoLine=%2 )

if exist %1 (

	call p. fileBackup -open -i %*
	
	rem taskkill /im sublime_text.exe /f
	start "EDIT" %code_editor% %1:%gotoLine%
	rem echo %*

) else (
	call :shouldcreate %1
)



goto:eof
:shouldcreate
set "create="
			echo File doesn't exist
	set /p "create=-                  Create? "
	if [%create%] == [] (

	call :altlocations %*
	goto:eof

	) else if [%create%] == [n] (
	goto:eof
	) else if [%create%] == [y] (

	echo Create chosen
	call p. fileBackup -open -i %*
	rem taskkill /im sublime_text.exe /f
	start "EDIT" %code_editor% %*:%gotoLine%
	rem echo %*
	goto:eof

	) else if [%create%] == [x] (

	echo exit
	goto:eof

	) else if [%create%] == [n] (

	call :altlocations %*

	) else (

	echo end create
	goto:eof


	)





goto:eof
:altlocations
rem echo Checking other locations...
rem echo.
rem goto:eof

if exist %* (

	call p. fileBackup -open -i %*
	rem taskkill /im sublime_text.exe /f
	start "EDIT" %code_editor% %*:%gotoLine%
	rem echo %*






) else if exist %myTables%\%*.json (

	call p. fileBackup -open -i %myTables%\%*.json
	rem taskkill /im sublime_text.exe /f
	start "EDIT" %code_editor% %myTables%\%*.json:%gotoLine%
	rem echo %myTables%\%*.json


) else if exist %myTables%\%*.txt (

	call p. fileBackup -open -i %myTables%\%*.txt
	rem taskkill /im sublime_text.exe /f
	start "EDIT" %code_editor% %myTables%\%*.txt:%gotoLine%
	rem echo %myTables%\%*.json




) else if exist %python%\%*.py (

	call p. fileBackup -open -i %python%\%*.py
	rem taskkill /im sublime_text.exe /f
	start "EDIT" %code_editor% %python%\%*.py:%gotoLine%
	rem echo %python%\%*.py

) else if exist %phpFiles%\%*.php (

	call p. fileBackup -open -i %phpFiles%\%*.php
	rem taskkill /im sublime_text.exe /f
	start "EDIT" %code_editor% %phpFiles%\%*.php:%gotoLine%
	rem echo %phpFiles%\%*.php

) else if exist %scriptroot%\%*.bat (

	call p. fileBackup -open -i %scriptroot%\%*.bat
	rem taskkill /im sublime_text.exe /f
	start "EDIT" %code_editor% %scriptroot%\%*.bat:%gotoLine%
	rem echo %scriptroot%\%*.bat

) else if exist %powershell%\%*.ps1 (

	call p. fileBackup -open -i %powershell%\%*.ps1
	rem taskkill /im sublime_text.exe /f
	start "EDIT" %code_editor% %powershell%\%*.ps1:%gotoLine%
	rem echo %powershell%\%*.ps1

) else if exist D:\_Scott\S_Documents\Projects\self\Powershell\%*.ps1 (

	call p. fileBackup -open -i D:\_Scott\S_Documents\Projects\self\Powershell\%*.ps1
	rem taskkill /im sublime_text.exe /f
	start "EDIT" %code_editor% D:\_Scott\S_Documents\Projects\self\Powershell\%*.ps1:%gotoLine%
	rem echo D:\_Scott\S_Documents\Projects\self\Powershell\%*.ps1

) else if exist %myPhp%\%*.php (

	call p. fileBackup -open -i %myPhp%\%*.php
	rem taskkill /im sublime_text.exe /f
	start "EDIT" %code_editor% %myPhp%\%*.php:%gotoLine%
	rem echo %myPhp%\%*.php

) else if exist %myPowershell%\%*.ps1 (

	call p. fileBackup -open -i %myPowershell%\%*.ps1
	rem taskkill /im sublime_text.exe /f
	start "EDIT" %code_editor% %myPowershell%\%*.ps1:%gotoLine%
	rem echo %myPowershell%\%*.ps1

) else if exist %myPython%\%*.py (

	call p. fileBackup -open -i %myPython%\%*.py
	rem taskkill /im sublime_text.exe /f
	start "EDIT" %code_editor% %myPython%\%*.py:%gotoLine%
	rem echo %myPython%\%*.py

) else if exist %myTables%\%* (

	call p. fileBackup -open -i %myTables%\%*
	rem taskkill /im sublime_text.exe /f
	start "EDIT" %code_editor% %myTables%\%*:%gotoLine%
	rem echo %myTables%\%*





) else if exist %myDatabases%\%* (

	call p. fileBackup -open -i %myDatabases%\%*
	rem taskkill /im sublime_text.exe /f
	start "EDIT" %code_editor% %myDatabases%\%*:%gotoLine%
	rem echo %myDatabases%\%*

) else if exist %myWebApp%\%* (

	call p. fileBackup -open -i %myWebApp%\%*
	rem taskkill /im sublime_text.exe /f
	start "EDIT" %code_editor% %myWebApp%\%*:%gotoLine%
	rem echo %myWebApp%\%*

) else if exist %USERPROFILE%\Desktop\%* (

	call p. fileBackup -open -i %USERPROFILE%\Desktop\%*
	rem taskkill /im sublime_text.exe /f
	start "EDIT" %code_editor% %USERPROFILE%\Desktop\%*:%gotoLine%
	rem echo %USERPROFILE%\Desktop\%*

) else (
	
	call p. fileBackup -open -i %*
	rem taskkill /im sublime_text.exe /f
	start "EDIT" %code_editor% %*:%gotoLine%
	rem echo %*

)