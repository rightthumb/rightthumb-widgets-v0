@echo off
:: genealogyDeath Death_Analysis_for_Scheirer.txt > Death_Analysis_for_Scheirer.csv
set file=%1
set thisFile=genealogyDeath.php
%php% %phpFiles%\%thisFile%
echo.
echo.
