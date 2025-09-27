@echo off
setlocal enabledelayedexpansion

:: Define the years, months, and corresponding folders
set "years=2020 2021 2022 2023"
set "months=01 02 03 04 05 06 07 08 09 10 11 12"

:: Loop through the picture files in the current directory
for %%F in (20??????.*) do (
	set "file=%%~nF"
	set "year=!file:~0,4!"
	set "month=!file:~4,2!"

	:: Check if the year folder exists; if not, create it
	if not exist "!year!" mkdir "!year!"

	:: Check if the month folder exists within the year folder; if not, create it
	if not exist "!year!\!month!" mkdir "!year!\!month!"

	:: Check if a file with the same date already exists in the month folder
	if not exist "!year!\!month!\!file!*" (
		:: Move the picture file to the appropriate year and month folder
		move "%%F" "!year!\!month!\"
	) else (
		:: Handle the case where a file with the same date already exists
		echo A file with the same date already exists in "!year!\!month!\"
		echo Skipping "%%F"
	)
)

:: End of the batch script