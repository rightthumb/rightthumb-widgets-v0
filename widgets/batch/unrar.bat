@echo off
set "rarPath=D:\techApps\WinRAR 3.9\WinRAR\"
set "extractPath=%cd%"

"%rarPath%unrar" x %1 "%extractPath%"

