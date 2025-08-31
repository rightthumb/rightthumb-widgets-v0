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

CALL m back

echo.
CALL driveLabel %mID%
rem echo %foundFolder%
if [%foundFolder%] == [True] (

		CALL p. projectTimer -project movieData -start
		CALL p. fileBackup -open -i %mData%
		echo.
		CALL p. executeEstimate -project movieData -i "dir /s/b /a:a" -prefix "Researching files"
		%thisDrive%:
		cd\
		CALL p. dir -save %mData% -recursive >nul
		CALL p. ls -cache %mData% -movietitle -save %mData% >nul
		echo.
		CALL p. projectTimer -project movieData -end -total -prefix "Project"
		
		CALL p. projectTimer -project movieDataIndex -start
		CALL p. indexDB -db %myIndexes%\Movie_Drive.db
		CALL p. projectTimer -project movieDataIndex -end -total -prefix "Project"

	) else (
		echo Movie drive not found
	)
CALL b back

goto:eof