@echo off
rem call p lock-files -w
call uuid | p -copy
git commit
git push
