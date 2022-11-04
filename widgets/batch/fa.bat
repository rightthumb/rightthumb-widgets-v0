@echo off
if [%2] == [] (
	call p file-open -backup -alias %*
) else if exist %1  (
	rem echo aa
	SET fi=%1
	shift
	call p file-open -backup -f %fi% -alias %*
	echo p file-open -backup -f %fi% -alias %*
	rem echo aa
) else (
	rem echo bb
	SET alias=%1
	shift
	call p file-open -backup -alias %alias% -f %*
	rem echo bb
) 
