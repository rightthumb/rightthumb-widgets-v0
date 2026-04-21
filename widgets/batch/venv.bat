@echo off

if exist ".\.venv\Scripts\activate.bat" (
    call ".\.venv\Scripts\activate.bat"
    goto :eof
)

call "%userprofile%\.venv\Scripts\activate.bat"
