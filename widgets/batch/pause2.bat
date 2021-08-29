@echo off
ping google.com > "%stmp%\~"
IF EXIST "%stmp%\~" (del "%stmp%\~")
