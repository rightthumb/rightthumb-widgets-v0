@echo off
CALL p unix


rmdir /s /q %widgets%:\widgets\python\burn\windows
rmdir /s /q %widgets%:\widgets\python\burn\unix
mkdir %widgets%:\widgets\python\burn\windows
mkdir %widgets%:\widgets\python\burn\unix

xcopy /s/d/y/c %widgets%:\widgets\python\src\unix\*.py %widgets%:\widgets\python\burn\unix\
xcopy /s/d/y/c %widgets%:\widgets\python\*.py %widgets%:\widgets\python\burn\windows\

