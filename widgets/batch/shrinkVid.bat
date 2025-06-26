@echo off

if "%~1" == "" (
    echo Usage: %~nx0 ^<input file^>
    exit /b 1
)

ffmpeg -i "%~1" -vf "scale=500:-2" -c:v libx264 -preset ultrafast -crf 23 -c:a aac -b:a 192k "sm_%~n1.mp4"
