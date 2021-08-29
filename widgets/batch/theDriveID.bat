@echo off
SET "theDriveID="
IF EXIST "%stmp%\theDriveID.txt" (
	del "%stmp%\theDriveID.txt"
	)
CALL p findDriveID %* > "%stmp%\theDriveID.txt"
SET /p theDriveID=<"%stmp%\theDriveID.txt"
rem echo '%theDriveID%'
