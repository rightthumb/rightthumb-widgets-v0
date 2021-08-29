@echo off
call m current
call b py

echo.
call p f -in *.py + %*
echo.

call b current

