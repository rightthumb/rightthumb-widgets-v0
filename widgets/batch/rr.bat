@echo off
call "%userprofile%\.rt\profile\vars\config.bat"
rem call "%widgets%\widgets\batch\resetVars.bat"
@REM call isPWSH
call "%widgets%\widgets\batch\c.bat" %1 
