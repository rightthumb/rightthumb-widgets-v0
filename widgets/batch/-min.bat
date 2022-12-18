@echo off

echo %timestamp_start%
call p terminal-timer -min %1 > %tmpf%
set /p timestamp_start=<%tmpf%
echo %timestamp_start%