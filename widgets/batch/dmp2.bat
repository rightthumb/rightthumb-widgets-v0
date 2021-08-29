@echo off
echo Press Q when done
"D:\Program Files (x86)\Windows Kits\10\Debuggers\x64\kd.exe" -z %1 -y srv*c:\pubsymbols*http://msdl.microsoft.com/download/symbols | find /i "Probably"
