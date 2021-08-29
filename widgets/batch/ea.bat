@echo off

:VAR
set alias=%scriptroot%\script-bookmarks\alias\a.%1.bat
GOTO BAT

notes:
ma  _alias_name
_file

:BAT

start notepad "%alias%"
GOTO END

:END
