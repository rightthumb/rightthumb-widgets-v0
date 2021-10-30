@echo off

if [%1] == [-kill] (
	taskkill /f /im mongod.exe
) else (
	echo mongod.exe
)