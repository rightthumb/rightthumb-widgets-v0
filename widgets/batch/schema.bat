@echo off

if "%1"=="" (
	sqlite3 index.db .schema
	goto :eof
)
sqlite3 %1 .schema