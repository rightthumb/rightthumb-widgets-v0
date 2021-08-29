@echo off
tasklist
set /p t=Enter task::
taskkill /F /IM "%t%" /t