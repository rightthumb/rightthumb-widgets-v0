@echo off
if [%1] == [] (
	echo no time given
	goto:eof
)
echo %timestamp_start%
call p. terminal-timer -min %1 > %tmpf%
set /p timestamp_start=<%tmpf%
echo %timestamp_start%
