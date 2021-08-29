@echo off
if [%1]==[] (
        start .
) ELSE (
        explorer /n, /select,"%~f1"
)
:Same as v.bat
: Just found this: http://ss64.com/nt/syntax-args.html