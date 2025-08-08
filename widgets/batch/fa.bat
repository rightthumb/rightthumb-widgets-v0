@echo off
if [%1] == [] (
	call p. file-open -backup secure -alias last
) else (
	call p. file-open -backup secure -alias %*
)
rem if [%2] == [] (
rem 	call p. file-open -backup -alias %*
rem ) else if exist %1  (
rem 	rem echo aa
rem 	SET fi=%1
rem 	shift
rem 	call p. file-open -backup -f %fi% -alias %*
rem 	echo p file-open -backup -f %fi% -alias %*
rem 	rem echo aa
rem ) else (
rem 	rem echo bb
rem 	SET alias=%1
rem 	shift
rem 	call p. file-open -backup -alias %alias% -f %*
rem 	rem echo bb
rem )