@echo off
set isinfile=
set tmpFile=%tmp%\isinfile.txt
echo.>"%tmpFile%"
findstr /i /r %1 %2>"%tmpFile%"
set /p checkisinfile=<"%tmpFile%"
IF NOT ["%checkisinfile%"] == [""] (set isinfile=y)
IF ["%checkisinfile%"] == [""] (set isinfile=n)
::echo %isinfile% [%checkisinfile%]

set checkisinfile=
set tmpFile=
