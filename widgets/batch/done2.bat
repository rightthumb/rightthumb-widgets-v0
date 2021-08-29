@echo off
set file=PROCESS_IS_DONE.txt
echo done > %file%
start notepad %file%
ping google.com>``
del %file%
del ``