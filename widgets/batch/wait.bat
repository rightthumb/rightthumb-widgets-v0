@echo off

if [%1] == [] (
    set lockSubject=x
) else (
    set lockSubject=%1
)

call p. lock-wait -lock %lockSubject%
if errorlevel 1 (
    echo Failed to lock %lockSubject%
    exit /b 1
)  