@echo off
call %userprofile%\.rt\profile\vars\config.bat
rem call %widgets%\widgets\batch\resetVars.bat
call %widgets%\widgets\batch\c.bat %1 
title python
rem %py%
call base