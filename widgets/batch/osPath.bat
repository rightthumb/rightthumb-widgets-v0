@echo off
call p. osPath -path %* > %stmp%-osPath
set /p path=<%stmp%-osPath
call cat %stmp%-osPath