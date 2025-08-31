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

	rem call p. fileBackup -open -i %*
	
	rem taskkill /im sublime_text.exe /f
	start "EDIT" %code_editor% %1
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
	rem call p. fileBackup -open -i %*
	rem taskkill /im sublime_text.exe /f
	start "EDIT" %code_editor% %*
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

	rem call p. fileBackup -open -i %*
	rem taskkill /im sublime_text.exe /f
	start "EDIT" %code_editor% %*
	rem echo %*






) else if exist %myTables%\%*.json (

	rem call p. fileBackup -open -i %myTables%\%*.json
	rem taskkill /im sublime_text.exe /f
	start "EDIT" %code_editor% %myTables%\%*.json
	rem echo %myTables%\%*.json


) else if exist %myTables%\%*.txt (

	rem call p. fileBackup -open -i %myTables%\%*.txt
	rem taskkill /im sublime_text.exe /f
	start "EDIT" %code_editor% %myTables%\%*.txt
	rem echo %myTables%\%*.json




) else if exist %dbTables%\%*.json (

	rem call p. fileBackup -open -i %dbTables%\%*.json
	start "EDIT" %code_editor% %dbTables%\%*.json

) else if exist %dbTables%\%* (

	rem call p. fileBackup -open -i %dbTables%\%*
	start "EDIT" %code_editor% %dbTables%\%*

) else if exist %python%\%*.py (

	rem call p. fileBackup -open -i %python%\%*.py
	rem taskkill /im sublime_text.exe /f
	start "EDIT" %code_editor% %python%\%*.py
	rem echo %python%\%*.py

) else if exist %phpFiles%\%*.php (

	rem call p. fileBackup -open -i %phpFiles%\%*.php
	rem taskkill /im sublime_text.exe /f
	start "EDIT" %code_editor% %phpFiles%\%*.php
	rem echo %phpFiles%\%*.php

) else if exist %scriptroot%\%*.bat (

	rem call p. fileBackup -open -i %scriptroot%\%*.bat
	rem taskkill /im sublime_text.exe /f
	start "EDIT" %code_editor% %scriptroot%\%*.bat
	rem echo %scriptroot%\%*.bat

) else if exist %powershell%\%*.ps1 (

	rem call p. fileBackup -open -i %powershell%\%*.ps1
	rem taskkill /im sublime_text.exe /f
	start "EDIT" %code_editor% %powershell%\%*.ps1
	rem echo %powershell%\%*.ps1

) else if exist D:\_Scott\S_Documents\Projects\self\Powershell\%*.ps1 (

	rem call p. fileBackup -open -i D:\_Scott\S_Documents\Projects\self\Powershell\%*.ps1
	rem taskkill /im sublime_text.exe /f
	start "EDIT" %code_editor% D:\_Scott\S_Documents\Projects\self\Powershell\%*.ps1
	rem echo D:\_Scott\S_Documents\Projects\self\Powershell\%*.ps1

) else if exist %myPhp%\%*.php (

	rem call p. fileBackup -open -i %myPhp%\%*.php
	rem taskkill /im sublime_text.exe /f
	start "EDIT" %code_editor% %myPhp%\%*.php
	rem echo %myPhp%\%*.php

) else if exist %myPowershell%\%*.ps1 (

	rem call p. fileBackup -open -i %myPowershell%\%*.ps1
	rem taskkill /im sublime_text.exe /f
	start "EDIT" %code_editor% %myPowershell%\%*.ps1
	rem echo %myPowershell%\%*.ps1

) else if exist %myPython%\%*.py (

	rem call p. fileBackup -open -i %myPython%\%*.py
	rem taskkill /im sublime_text.exe /f
	start "EDIT" %code_editor% %myPython%\%*.py
	rem echo %myPython%\%*.py

) else if exist %myTables%\%* (

	rem call p. fileBackup -open -i %myTables%\%*
	rem taskkill /im sublime_text.exe /f
	start "EDIT" %code_editor% %myTables%\%*
	rem echo %myTables%\%*





) else if exist %myDatabases%\%* (

	rem call p. fileBackup -open -i %myDatabases%\%*
	rem taskkill /im sublime_text.exe /f
	start "EDIT" %code_editor% %myDatabases%\%*
	rem echo %myDatabases%\%*

) else if exist %myWebApp%\%* (

	rem call p. fileBackup -open -i %myWebApp%\%*
	rem taskkill /im sublime_text.exe /f
	start "EDIT" %code_editor% %myWebApp%\%*
	rem echo %myWebApp%\%*

) else if exist %USERPROFILE%\Desktop\%* (

	rem call p. fileBackup -open -i %USERPROFILE%\Desktop\%*
	rem taskkill /im sublime_text.exe /f
	start "EDIT" %code_editor% %USERPROFILE%\Desktop\%*
	rem echo %USERPROFILE%\Desktop\%*

) else (
	
	rem call p. fileBackup -open -i %*
	rem taskkill /im sublime_text.exe /f
	start "EDIT" %code_editor% %*
	rem echo %*

)