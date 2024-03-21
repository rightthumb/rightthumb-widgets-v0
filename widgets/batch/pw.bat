@echo off 
call p. cat -f C:\Users\Scott\.rt\profile\documents\Chrome_Passwords.csv + %* | p. line -p , 0;2;3
