@echo off

IF [%1] == [] (
	ping google.com -t
) ELSE (
	CALL p google -q %*
)