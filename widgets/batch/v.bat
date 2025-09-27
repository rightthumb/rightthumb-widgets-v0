@echo off
if [%1]==[] (
	explorer .
) else (
	explorer /select, %1
)
@REM explorer /select, %1
@REM call c %*