@echo off
mkdir sample1
mkdir sample2
echo test > sample1\test.txt
call n sample1\test.txt -y
cd sample1
call m 99
call crypt test.txt -y
call o sample1 test.txt
cd ..
call p. pyTimer -start
call mv sample1 sample2 -y 2> %tmpf%-py
call ghost sample2 -y 2> %tmpf%-py
call p. pyTimer -end > %tmpf%
SET /p pyTimer=<%tmpf%
rmdir /s/q sample2
call notify "mvtest %pyTimer%"
goto:eof
set /p sample2=Delete?: 
if [%sample2%] == [y] rmdir /s/q sample2
