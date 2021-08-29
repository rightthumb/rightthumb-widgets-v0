@echo off
::start cmd /c %scriptroot%\dmp2.bat %1
::GOTO END

"D:\Program Files (x86)\Windows Kits\10\Debuggers\x64\kd.exe" -z %1 -y srv*c:\pubsymbols*http://msdl.microsoft.com/download/symbols

:END

:: Press Q to exit