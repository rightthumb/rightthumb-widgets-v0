@echo off
rem type d:\tech\MyScripts\photoshop_shortcuts.csv
call p fileBackup -i %*
start "EDIT" %ps% %*
