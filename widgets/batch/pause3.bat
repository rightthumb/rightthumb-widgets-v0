@echo off
ping yahoo.com > "%stmp%\~"
IF EXIST "%stmp%\~" (del "%stmp%\~")