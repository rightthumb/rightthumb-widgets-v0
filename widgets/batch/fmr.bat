@echo off
set out={022D63C9-6556-9BB0-8A71-73659D88BA05}
set bat={84012C6C-5C99-0F37-F788-749098F91A09}.bat
set search=%1
ffn %search% > %out%
set thisFile=fmr.php
ping google.com -n 1 >nul
%php% %phpFiles%\%thisFile%
ping google.com -n 1 >nul
if exist %bat% call %bat%
::if exist %bat% del /q %bat%
::if exist %out% del /q %out%
