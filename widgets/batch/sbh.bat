@echo off
set file=D:\Users\Jr\Documents\School\Digestion Project\history
echo =============== >> "%file%"
echo %date% @ %time% >> "%file%"
doskey /history >> "%file%"