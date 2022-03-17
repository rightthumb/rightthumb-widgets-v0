@echo off
rem call p lock-files -w
call uuid -e | p -copy
git commit
git push
