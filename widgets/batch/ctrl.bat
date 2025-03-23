@echo off
set count=0
set loop=0
:ctrl
set /a loop+=1
set /a count+=1 & echo %loop%.%count% Start
call p. ctrl %*
set /a count+=1 & echo %loop%.%count% Start
call p. ctrl %*
set /a count+=1 & echo %loop%.%count% Start
call p. ctrl %*
set /a count+=1 & echo %loop%.%count% Start
call p. ctrl %*
set /a count+=1 & echo %loop%.%count% Start
call p. ctrl %*
set /a count+=1 & echo %loop%.%count% Start
call p. ctrl %*
set /a count+=1 & echo %loop%.%count% Start
call p. ctrl %*
set /a count+=1 & echo %loop%.%count% Start
call p. ctrl %*
set /a count+=1 & echo %loop%.%count% Start
call p. ctrl %*
set /a count+=1 & echo %loop%.%count% Start
call p. ctrl %*
goto ctrl