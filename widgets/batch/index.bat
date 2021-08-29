@echo off



CALL newindex



GOTO END
call m tmp0
d:
cd\
dir /s/b > d:\index.txt
c:
cd\
dir /s/b >> d:\index.txt
e:
cd\
dir /s/b >> d:\index.txt
g:
cd \backup\D
dir /s/b > i
cd \backup\C
dir /s/b > i
cd \backup\E
dir /s/b > i

call b tmp0
doneBox "index complete"


:END