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


wmic useraccount where (name='administrator' and domain='%computername%') get name,sid | find /i "admin">"%temp%\getSID.txt"
set /p thisSID=<"%temp%\getSID.txt"
set thisSID=%thisSID:~15,44%
echo %thisSID%>"%temp%\getSID3.txt"
fciv "%temp%\getSID3.txt" | find "getsid">"%temp%\getSID2.txt"
set /p thisSIDMD5=<"%temp%\getSID2.txt"

set thisSIDMD5=%thisSIDMD5:~0,32%
IF EXIST "%temp%\getSID.txt" (del "%temp%\getSID.txt")
IF EXIST "%temp%\getSID2.txt" (del "%temp%\getSID2.txt")
IF EXIST "%temp%\getSID3.txt" (del "%temp%\getSID3.txt")

SET machineID=0ae6aa979971f4d6743dfbc690801822

CALL :UpCase machineID
GOTO:EOF
:UpCase
:: Subroutine to convert a variable VALUE to all UPPER CASE.
:: The argument for this subroutine is the variable NAME.
FOR %%i IN ("a=A" "b=B" "c=C" "d=D" "e=E" "f=F" "g=G" "h=H" "i=I" "j=J" "k=K" "l=L" "m=M" "n=N" "o=O" "p=P" "q=Q" "r=R" "s=S" "t=T" "u=U" "v=V" "w=W" "x=X" "y=Y" "z=Z") DO CALL SET "%1=%%%1:%%~i%%"

set machineID={%machineID:~0,8%-%machineID:~8,4%-%machineID:~12,4%-%machineID:~16,4%-%machineID:~20,12%}
set thisSIDMD5=

 
