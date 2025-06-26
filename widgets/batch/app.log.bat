@echo off


call p. todays-app-logs > "%tmpf%"

set /p todays_app_logs=<"%tmpf%"
echo %todays_app_logs%
if exist "%todays_app_logs%" (
    cd /d "%todays_app_logs%"
) else (
    echo Directory not found: "%todays_app_logs%"
)

call c
call lab logs
echo.
@REM echo p files --c ^| p logs-apps
echo app.logs
echo.

goto:eof

