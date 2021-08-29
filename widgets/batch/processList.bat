@echo off
call "%userprofile%\c.bat"
echo. > ~relevant.txt
for /F "tokens=*" %%A in  ( ~list.txt ) do  (
   ECHO Processing %%A.... 
   call ff %%A >> ~relevant.txt
)
type ~relevant.txt | sort > relevant.txt 
del ~relevant.txt