@echo off
CALL m back

echo.
CALL driveLabel %pubID% MOVIES
if [%foundFolder%] == [True] (

		CALL p projectTimer -project movieCloudData -start
		CALL p fileBackup -i %mcData%
		echo.
		CALL p executeEstimate -project movieCloudData -i "dir /s/b /a:a" -prefix "Researching files"
		type %tmpf% | CALL p dir3 -save %mcData% -recursive -stats -skip -prefix "Processing movies" %*
		echo.
		CALL p projectTimer -project movieCloudData -end -total -prefix "Project"
		
	) else (
		echo Movie drive not found
	)
CALL b back

goto:eof

