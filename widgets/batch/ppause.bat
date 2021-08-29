@echo off
if [%1] == [] (
	ping 127.0.0.1 -n 2 >nul
) else (
	ping 127.0.0.1 -n %1 >nul
)