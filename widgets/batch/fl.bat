@echo off

call m back >nul 2>&1
@REM if not exist "%fileLocks%" mkdir "%fileLocks%"
cd /d "%fileLocks%"

del /q *.lock

call g back >nul 2>&1
