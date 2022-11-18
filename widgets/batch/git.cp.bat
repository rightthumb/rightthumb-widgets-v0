@echo off



call m back --c
call b w > nul
rem call p lock-files -w
call uuid -e | p -copy > %tmpf%
SET /p uuid=<%tmpf%
git commit
echo %uuid% >> D:\.rightthumb-widgets\.git\COMMIT_EDITMSG
pause
git push
call b back > nul 
