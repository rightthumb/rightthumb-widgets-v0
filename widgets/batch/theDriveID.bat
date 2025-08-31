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

SET "theDriveID="
IF EXIST "%stmp%\theDriveID.txt" (
	del "%stmp%\theDriveID.txt"
	)
CALL p. findDriveID %* > "%stmp%\theDriveID.txt"
SET /p theDriveID=<"%stmp%\theDriveID.txt"
rem echo '%theDriveID%'