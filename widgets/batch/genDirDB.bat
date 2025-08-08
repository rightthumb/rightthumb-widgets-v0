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


if [%isAdmin%] == [False] (
	echo Error: Not Admin
) else (
	CALL :GenerateDirDatabase
)
GOTO:EOF

:GenerateDirDatabase

CALL b i

CALL p. 7z -nd -f C_Drive.db
CALL p. 7z -nd -f D_Drive.db

del C_Drive.db
del D_Drive.db

type 01{F8E01519-3977-04B8-3416-1F0048BD97C3} | p. dir -db C_Drive.db -md5
type 01{65E57A88-6471-E426-D878-AD55F117A804} | p. dir -db D_Drive.db -md5

CALL done
GOTO:EOF