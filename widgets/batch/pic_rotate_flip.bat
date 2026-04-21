@echo off
D:\.rightthumb-widgets\widgets\exe\ffmpeg.exe -i "%~1" -vf "transpose=1" -q:v 0 "%~dpn1_temp%~x1"
move /Y "%~dpn1_temp%~x1" "%~1"

D:\.rightthumb-widgets\widgets\exe\ffmpeg.exe -i "%~1" -vf "transpose=1" -q:v 0 "%~dpn1_temp%~x1"
move /Y "%~dpn1_temp%~x1" "%~1"