@echo off
IF NOT [%1] == [] (SET b_delay=%1)
IF [%1] == [] (SET b_delay=2)
ping 127.0.0.1 -n %b_delay% -l 10 > "%stmp%\~"
IF EXIST "%stmp%\~" (del "%stmp%\~")