@echo off

call p. blank-file -f %*

rem IF EXIST %1 (
rem     set /p ask=delete file?: 
rem     if [%ask%] == [y] CALL:CREATE %1 yes
rem     if [%ask%] == [] CALL:CREATE %1 yes
rem     if [%ask%] == [n] echo aborted
rem     if [%ask%] == [no] echo aborted
rem ) ELSE (
rem     CALL:CREATE %1 no
rem )

rem :CREATE
rem echo. > %1
rem if [%2] == [yes] echo cleared %1
rem if [%2] == [no] echo created %1
rem call n %1
rem goto:eof 
