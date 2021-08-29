@echo off
CALL m back

echo.
CALL driveLabel %mID%
rem echo %foundFolder%
if [%foundFolder%] == [True] (

		CALL p projectTimer -project movieData -start
		CALL p fileBackup -i %mData%
		echo.
		CALL p executeEstimate -project movieData -i "dir /s/b /a:a" -prefix "Researching files"
		%thisDrive%:
		cd\
		 CALL p dir -save %mData% -recursive >nul
		 CALL p ls -cache %mData% -movietitle -save %mData% >nul
		echo.
		CALL p projectTimer -project movieData -end -total -prefix "Project"
		
		CALL p projectTimer -project movieDataIndex -start
		CALL p indexDB -db %myIndexes%\Movie_Drive.db
		CALL p projectTimer -project movieDataIndex -end -total -prefix "Project"

	) else (
		echo Movie drive not found
	)
CALL b back

goto:eof

