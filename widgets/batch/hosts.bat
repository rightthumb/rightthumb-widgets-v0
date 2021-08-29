@echo off
if ["%1"] == ["edit"] GOTO EDIT
if ["%1"] == ["e"] GOTO EDIT

type D:\Windows\System32\drivers\etc\hosts

GOTO END

:EDIT
call p fileBackup -i D:\Windows\System32\drivers\etc\hosts
notepad D:\Windows\System32\drivers\etc\hosts

:END
