@echo off
if [%1] == [] goto:eof
call p. recover-backup-log -f %1