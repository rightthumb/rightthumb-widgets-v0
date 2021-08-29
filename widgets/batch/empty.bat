@echo off
dir /b /a "%1\*" | >nul findstr "^" && (echo Folder Not Empty) || (echo Folder Empty) 
