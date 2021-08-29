@echo off
SET /p Drive=<%userprofile%\.tk421
SET widgets=%Drive:~0,1%
CALL %widgets%:\widgets\batch\c.bat
CALL b lynx
SET do=%1
zip appServer.%do% appServer.%do%
SET /p pause=pause: 