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
CALL driveLabel %m3ID% MOVIES
if [%foundFolder%] == [True] (

		CALL p. projectTimer -project movieData -start
		CALL p. fileBackup -open -i %m3Data%
		echo.
		CALL p. files --c > %tmpf%
		CALL p. executeEstimate -project movieData -i "dir /s/b /a:a" -prefix "Researching files"
		type %tmpf% | CALL p. dir3 -nopass -save %m3Data% -recursive -stats -skip -prefix "Processing movies" %*
		echo.
		CALL p. projectTimer -project movieData -end -total -prefix "Project"

	) else (
		echo Movie drive not found
	)
CALL b back

goto:eof