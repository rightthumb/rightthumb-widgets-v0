@echo off
setlocal enabledelayedexpansion

rem Define default title
set title=SDS

rem Check number of arguments
if "%~1"=="" (
    echo Invalid number of arguments. Expected 1, 2, or 3.
    exit /b 1
)

rem Set message, title and URL based on arguments
set message=%~1
if not "%~2"=="" set title=%~2
if not "%~3"=="" set url=%~3

rem Construct curl command accordingly
if "%~3"=="" (
    if "%~2"=="" (
        rem If only 1 argument, use default title, no URL
        curl -H "Title: !title!" -H "Priority: urgent" -H "Tags: -1" -d "!message!" aleen.m-eta.app:9000/sds-notify
    ) else (
        rem If 2 arguments, use specified title and message, no URL
        curl -H "Title: !title!" -H "Priority: urgent" -H "Tags: -1" -d "!message!" aleen.m-eta.app:9000/sds-notify
    )
) else (
    rem If 3 arguments, use specified title, message, and URL
    curl -H "Title: !title!" -H "Click: !url!" -H "Priority: urgent" -H "Tags: -1" -d "!message!" aleen.m-eta.app:9000/sds-notify
)
