@echo off
if [%1]==[] (
        start .
) ELSE (
        explorer /n, /select,"%~f1"
)
:Same as view.bat
:checkout notes in above script