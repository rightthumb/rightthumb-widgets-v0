@echo off
set s=%1
set do=%2
echo :: State: %1 ::
set thisFile=accc-cancer_state.php
%php% %phpFiles%\%thisFile%
echo.
echo.
: copied as g