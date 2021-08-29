@echo off
:: genealogyMuschko Muschko_MyHeritage_Research.2..txt  | sort > ~dup.txt & dup & del ~dup.txt & del ~fin.txt
:: type obj1.csv > ~out.txt & parse ~out.txt "," 2 > ~dup.txt & dup & del ~dup.txt & del ~out.txt & del ~fin.txt
:: type obj2.csv > ~out.txt & parse ~out.txt "," 1
:: l "Michael Muschko" o
set file=%1
set thisFile=genealogyMuschko.php
%php% %phpFiles%\%thisFile%
echo.
echo.
