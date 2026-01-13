@echo off
if "%~1"=="" (
	echo Usage:
	echo sqlite3 index.db "SELECT name FROM files WHERE content IS NOT NULL AND content LIKE '%%file-open%%'"
	goto :eof
)

C:\ProgramData\chocolatey\bin\sqlite3.exe %*