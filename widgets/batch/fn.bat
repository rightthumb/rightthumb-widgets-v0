@echo off 
call %*
goto:eof 
:one
echo one %*
set fn_one=%*
goto:eof 
:two
echo two %*
set fn_two=%*
goto:eof