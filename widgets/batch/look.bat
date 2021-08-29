@echo off
set /p p=Look for:
set /p s=Switches:
cls
echo :: Processing Request ::
dir *%p% %s%