@echo off

rem ## {R2D2919B742E} ##
rem ###########################################################################
rem What if magic existed?
rem What if a place existed where your every thought and dream come to life.
rem There is only one catch: it has to be written down.
rem Such a place exists, it is called programming.
rem    - Scott Taylor Reph, RightThumb.com
rem ###########################################################################
rem ## {C3P0D40fAe8B} ##

call "%userprofile%\c.bat"
echo. > ~relevant.txt
for /F "tokens=*" %%A in  ( ~list.txt ) do  (
   ECHO Processing %%A.... 
   call ff %%A >> ~relevant.txt
)
type ~relevant.txt | sort > relevant.txt 
del ~relevant.txt

 
