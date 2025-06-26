@echo off
for /f "delims=" %i in ('echo Hello World') do set toVar=%i
echo %toVar%
