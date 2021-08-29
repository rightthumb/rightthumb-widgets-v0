@echo off
CALL theUSB
if [%theusb%] == [] (
	echo No USB found
) else (
	echo %theusb%
)
