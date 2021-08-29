@echo off
set search=%1 %2 %3 %4 %5 %6 %7 %8 %9
set thisFile=Movie_Names.php

dir /b > ~DIR_LIST.txt

%php% %phpFiles%\%thisFile%
echo.
call ~MOVIE_NAME_RENAME.bat
GOTO END



:END

del ~DIR_LIST.txt
del ~MOVIE_NAME_RENAME.bat