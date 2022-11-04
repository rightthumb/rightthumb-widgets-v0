@echo off
call m back --c
call b w > nul
rem call p lock-files -w
call uuid -e | p -copy
git commit
git push
call b back > nul 
