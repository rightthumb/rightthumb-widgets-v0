@echo off
set VLC="C:\Program Files (x86)\VideoLAN\VLC\vlc.exe"

if not exist %VLC% (
    echo VLC not found at:
    echo %VLC%
    pause
    exit /b 1
)

start "" %VLC% "%~1"
goto:eof

@REM --loop --fullscreen 
@REM C:\Users\Scott\.rt\profile\documents\vlc-cli.md

