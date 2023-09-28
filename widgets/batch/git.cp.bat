@echo off



call m back --c
call b w > nul
rem call p lock-files -w
rem call uuid -e | p -copy
rem call uuid -e | p -copy > %tmpf%
call uuid -e  > %tmpf%
SET /p uuid=<%tmpf%
git commit -m "%uuid%"
rem echo %uuid% >> D:\.rightthumb-widgets\.git\COMMIT_EDITMSG
rem pause
git push --force
call b back > nul 
 
