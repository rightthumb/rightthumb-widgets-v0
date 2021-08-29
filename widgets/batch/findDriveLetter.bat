@echo off
SET "theDrive="
IF EXIST "%stmp%\findDriveLetter.txt" (
	del "%stmp%\findDriveLetter.txt"
	)
CALL p findDriveLetter %* > "%stmp%\findDriveLetter.txt"
SET /p theDrive=<"%stmp%\findDriveLetter.txt"
rem echo '%theDrive%'
