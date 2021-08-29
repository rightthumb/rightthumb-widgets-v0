@echo off
CALL m back

echo.
CALL driveLabel %m3ID% MOVIES
if [%foundFolder%] == [True] (

		CALL p projectTimer -project movieData -start
		CALL p fileBackup -i %m3Data%
		echo.
		CALL p files --c > %tmpf%
		CALL p executeEstimate -project movieData -i "dir /s/b /a:a" -prefix "Researching files"
		type %tmpf% | CALL p dir3 -nopass -save %m3Data% -recursive -stats -skip -prefix "Processing movies" %*
		echo.
		CALL p projectTimer -project movieData -end -total -prefix "Project"

	) else (
		echo Movie drive not found
	)
CALL b back

goto:eof

